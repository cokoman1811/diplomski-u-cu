"""Didakticki primjer: stablo s 8 listova na 20 uzoraka iz Jena podataka.

Replicira logiku iz src/gap_features.c i src/decision_tree.c, ali s
min_leaf = 2 i dubinom 3 kako bi stablo imalo tocno 8 listova i moglo se
nacrtati u dokumentaciji. Pravi kod koristi min_leaf = 4 i dubinu 8.
"""

import csv
import math
from pathlib import Path

CSV = Path(__file__).resolve().parents[1] / "data/processed/jena_windows/window_01.csv"
N = 20
STEP = 6          # 6 * 10 min = 1 h
GAPS = [3, 4, 11, 16]
MIN_LEAF = 2
MAX_DEPTH = 6

FEATURE_NAMES = [
    "prev_val", "next_val", "alpha", "d_prev", "d_next",
    "lin_base", "position_norm", "hour_sin", "hour_cos",
]


def load():
    rows = []
    with CSV.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            rows.append((row["timestamp"], float(row["temperature"])))
    return [rows[i * STEP] for i in range(N)]


def gap_features(temp):
    """Isto kao gap_features_compute: susjedi se traze bez same tocke."""
    n = len(temp)
    prev_idx, next_idx = [], []

    last = -1
    for i in range(n):
        prev_idx.append(last)
        if temp[i] is not None:
            last = i

    nxt = -1
    tail = [0] * n
    for i in range(n - 1, -1, -1):
        tail[i] = nxt
        if temp[i] is not None:
            nxt = i
    next_idx = tail

    out = []
    for i in range(n):
        pi, ni = prev_idx[i], next_idx[i]
        if pi >= 0 and ni >= 0:
            pv, nv = temp[pi], temp[ni]
            alpha = (i - pi) / (ni - pi)
            dp, dn = i - pi, ni - i
        elif pi >= 0:
            pv = nv = temp[pi]
            alpha, dp, dn = 1.0, i - pi, 1e4
        elif ni >= 0:
            pv = nv = temp[ni]
            alpha, dp, dn = 0.0, 1e4, ni - i
        else:
            pv = nv = 0.0
            alpha, dp, dn = 0.5, 1e4, 1e4
        out.append({
            "prev_val": pv, "next_val": nv, "alpha": alpha,
            "d_prev": dp, "d_next": dn,
            "lin_base": pv + alpha * (nv - pv),
        })
    return out


def build_features(stamps, temp):
    gaps = gap_features(temp)
    rows = []
    for i, (stamp, g) in enumerate(zip(stamps, gaps)):
        hour = int(stamp[11:13])
        ang = 2 * math.pi * hour / 24.0
        rows.append({
            **g,
            "position_norm": i / (N - 1),
            "hour_sin": math.sin(ang),
            "hour_cos": math.cos(ang),
        })
    return rows


def sse(vals):
    if not vals:
        return 0.0
    m = sum(vals) / len(vals)
    return sum((v - m) ** 2 for v in vals)


def best_split(rows, resid, idx):
    best = None
    for f in FEATURE_NAMES:
        order = sorted(idx, key=lambda i: rows[i][f])
        for k in range(len(order) - 1):
            a, b = order[k], order[k + 1]
            if rows[a][f] == rows[b][f]:
                continue
            left, right = order[:k + 1], order[k + 1:]
            if len(left) < MIN_LEAF or len(right) < MIN_LEAF:
                continue
            score = sse([resid[i] for i in left]) + sse([resid[i] for i in right])
            thr = 0.5 * (rows[a][f] + rows[b][f])
            if best is None or score < best[0]:
                best = (score, f, thr, left, right)
    return best


def build(rows, resid, idx, depth, path, leaves):
    if depth >= MAX_DEPTH or len(idx) < MIN_LEAF * 2:
        val = sum(resid[i] for i in idx) / len(idx)
        leaves.append((path, val, idx))
        return {"leaf": True, "value": val, "n": len(idx), "path": path}
    sp = best_split(rows, resid, idx)
    if sp is None:
        val = sum(resid[i] for i in idx) / len(idx)
        leaves.append((path, val, idx))
        return {"leaf": True, "value": val, "n": len(idx), "path": path}
    _, f, thr, left, right = sp
    return {
        "leaf": False, "feature": f, "threshold": thr,
        "left": build(rows, resid, left, depth + 1, path + ["DA"], leaves),
        "right": build(rows, resid, right, depth + 1, path + ["NE"], leaves),
    }


def walk(node, row):
    steps = []
    while not node["leaf"]:
        v = row[node["feature"]]
        yes = v <= node["threshold"]
        steps.append((node["feature"], node["threshold"], v, "DA" if yes else "NE"))
        node = node["left"] if yes else node["right"]
    return steps, node


def show(node, indent=0, label="korijen"):
    pad = "  " * indent
    if node["leaf"]:
        print(f"{pad}{label}: LIST  {node['value']:+.3f}  (n={node['n']})")
    else:
        print(f"{pad}{label}: {node['feature']} <= {node['threshold']:.4f} ?")
        show(node["left"], indent + 1, "DA ")
        show(node["right"], indent + 1, "NE ")


def main():
    data = load()
    stamps = [d[0] for d in data]
    truth = [d[1] for d in data]

    damaged = list(truth)
    for g in GAPS:
        damaged[g] = None

    rows = build_features(stamps, damaged)
    known = [i for i in range(N) if damaged[i] is not None]
    resid = {i: truth[i] - rows[i]["lin_base"] for i in known}

    print("=== NIZ (20 uzoraka, svaki 1 h) ===")
    for i in range(N):
        mark = "RUPA" if damaged[i] is None else "    "
        print(f"{i:3d}  {stamps[i][11:16]}  istina={truth[i]:7.2f}  {mark}")

    print("\n=== TABLICA GRESAKA (samo poznate) ===")
    print(f"{'i':>3} {'sat':>6} {'T':>7} {'crta':>8} {'greska':>8} {'alpha':>6} {'d_prev':>7} {'d_next':>7}")
    for i in known:
        r = rows[i]
        print(f"{i:3d} {stamps[i][11:16]:>6} {truth[i]:7.2f} {r['lin_base']:8.2f} "
              f"{resid[i]:+8.3f} {r['alpha']:6.2f} {r['d_prev']:7.0f} {r['d_next']:7.0f}")

    leaves = []
    tree = build(rows, resid, known, 0, [], leaves)

    print(f"\n=== STABLO ({len(leaves)} listova) ===")
    show(tree)

    print("\n=== LISTOVI ===")
    for k, (path, val, idx) in enumerate(leaves, 1):
        greske = ", ".join(f"{resid[i]:+.3f}" for i in idx)
        print(f"list {k}  put={'-'.join(path):12s}  value={val:+.3f}  "
              f"tocke={idx}  greske=[{greske}]")

    print("\n=== HOD SVAKE RUPE ===")
    for g in GAPS:
        r = rows[g]
        steps, leaf = walk(tree, r)
        print(f"\nrupa i={g} ({stamps[g][11:16]})  crta={r['lin_base']:.2f}  "
              f"alpha={r['alpha']:.2f}  d_prev={r['d_prev']:.0f}  d_next={r['d_next']:.0f}")
        for f, thr, v, ans in steps:
            print(f"   {f} = {v:.4f}  <= {thr:.4f} ?  -> {ans}")
        pred = r["lin_base"] + leaf["value"]
        print(f"   LIST {leaf['value']:+.3f}  (put {'-'.join(leaf['path'])})")
        print(f"   {r['lin_base']:.2f} {leaf['value']:+.3f} = {pred:.2f}   "
              f"(istina {truth[g]:.2f}, crta bi dala {r['lin_base']:.2f})")


if __name__ == "__main__":
    main()
