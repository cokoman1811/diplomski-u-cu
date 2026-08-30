#!/usr/bin/env python3
"""
Racuna sve brojke potrebne za azuriranje diplomskog rada.

Izvor su results/experiment_results.csv (agregat po 20 ponavljanja) i
results/experiment_runs.csv (pojedinacna izvodenja). Rezultat se sprema u
results/_brojke_za_rad.json, odakle ih preuzima azuriraj_word.py.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
IZLAZ = ROOT / "results" / "_brojke_za_rad.json"

# Redoslijed i kratki nazivi kakvi se koriste u tablicama rada.
# adaptive_imputation se namjerno izostavlja iz tablica jer je rijec o oracle
# postupku koji bira metodu prema stvarnim vrijednostima; obraduje se u tekstu.
METODE = [
    ("forward_fill", "forward_fill"),
    ("linear_interpolation", "linear"),
    ("time_interpolation", "time"),
    ("cubic_interpolation", "cubic"),
    ("spline_interpolation", "spline"),
    ("moving_average", "moving_average"),
    ("knn", "knn"),
    ("knn_upgraded", "knn_upgraded"),
    ("decision_tree", "decision_tree"),
    ("random_forest", "random_forest"),
    ("neural_net", "neural_net"),
]
PUNO = [p for p, _ in METODE]
KRATKO = dict(METODE)
SCEN = [("random", "none"), ("block", "none"), ("block_start", "start"),
        ("block_middle", "middle"), ("block_end", "end")]
RATES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
EPS = 1e-9


def hr(x: float, d: int = 4) -> str:
    """Broj u hrvatskom zapisu s decimalnim zarezom."""
    return f"{x:.{d}f}".replace(".", ",")


def main() -> None:
    res = pd.read_csv(ROOT / "results" / "experiment_results.csv")
    runs = pd.read_csv(ROOT / "results" / "experiment_runs.csv")
    res["missing_rate"] = res.missing_rate.round(2)
    runs["missing_rate"] = runs.missing_rate.round(2)
    tab = res[res.method.isin(PUNO)]

    out: dict = {}
    out["n_ponavljanja"] = int(runs.repeat.nunique())
    out["n_metoda"] = len(PUNO)
    out["n_kombinacija"] = len(SCEN) * len(RATES)
    out["n_agregat"] = len(tab)
    out["n_izvodenja"] = int(len(runs[runs.method.isin(PUNO)]))
    out["n_uzoraka"] = 1008

    # ---- Tablica 5-1: najbolja metoda po scenariju i rateu -------------------
    t1 = []
    for scen, poz in SCEN:
        for rate in RATES:
            d = tab[(tab.scenario == scen) & (tab.missing_rate == rate)]
            m = d.mae.min()
            pob = d[d.mae <= m + EPS]
            imena = " / ".join(KRATKO[x] for x in PUNO if x in set(pob.method))
            r = pob.iloc[0]
            t1.append([scen, poz, f"{int(rate * 100)} %", imena,
                       hr(m), hr(float(r.rmse)), hr(float(r.r2))])
    out["tablica_najbolja"] = t1

    # ---- Tablice 5-2 do 5-6: MAE po metodi i rateu ---------------------------
    out["tablice_mae"] = {}
    for scen, _ in SCEN:
        redovi = []
        for puno in PUNO:
            d = tab[(tab.scenario == scen) & (tab.method == puno)].set_index("missing_rate")
            redovi.append([KRATKO[puno]] + [hr(float(d.loc[r, "mae"])) for r in RATES])
        out["tablice_mae"][scen] = redovi

    # ---- Tablica 5-7: sazetak po metodi --------------------------------------
    pob_broj = {p: 0 for p in PUNO}
    for scen, _ in SCEN:
        for rate in RATES:
            d = tab[(tab.scenario == scen) & (tab.missing_rate == rate)]
            m = d.mae.min()
            for x in d[d.mae <= m + EPS].method:
                pob_broj[x] += 1
    saz = []
    for puno in PUNO:
        d = tab[tab.method == puno]
        saz.append((float(d.mae.mean()), [KRATKO[puno], hr(float(d.mae.mean())),
                                          hr(float(d.rmse.mean())), hr(float(d.r2.mean())),
                                          hr(float(d.mae.std(ddof=0))), str(pob_broj[puno])]))
    saz.sort(key=lambda t: t[0])
    out["tablica_sazetak"] = [r for _, r in saz]

    # ---- Brojke u tekstu, po scenariju ---------------------------------------
    out["scenariji"] = {}
    for scen, _ in SCEN:
        s = tab[tab.scenario == scen]
        lin = s[s.method == "linear_interpolation"].set_index("missing_rate")
        po_rateu = {}
        for rate in RATES:
            d = s[s.missing_rate == rate]
            m = d.mae.min()
            po_rateu[f"{int(rate * 100)}"] = {
                "prosjek_mae": hr(float(d.mae.mean())),
                "prosjek_rmse": hr(float(d.rmse.mean())),
                "prosjek_r2": hr(float(d.r2.mean())),
                "najbolji": " / ".join(KRATKO[x] for x in PUNO
                                       if x in set(d[d.mae <= m + EPS].method)),
                "najbolji_mae": hr(m),
            }
        out["scenariji"][scen] = {
            "po_rateu": po_rateu,
            "lin_80_mae": hr(float(lin.loc[0.8, "mae"])),
            "lin_80_rmse": hr(float(lin.loc[0.8, "rmse"])),
            "lin_80_r2": hr(float(lin.loc[0.8, "r2"])),
            "lin_prosjek_mae": hr(float(s[s.method == "linear_interpolation"].mae.mean())),
        }

    # ---- Rekonstrukcije: prvi prozor, linear, 20 % ---------------------------
    r0 = runs[(runs.repeat == 0) & (runs.method == "linear_interpolation")
              & (runs.missing_rate == 0.2)]
    out["rekonstrukcije"] = {
        row.scenario: {"mae": hr(float(row.mae)), "rmse": hr(float(row.rmse)),
                       "r2": hr(float(row.r2))}
        for row in r0.itertuples()
    }

    # ---- Globalne brojke ------------------------------------------------------
    out["globalno"] = {
        "mae_10": hr(float(tab[tab.missing_rate == 0.1].mae.mean())),
        "mae_80": hr(float(tab[tab.missing_rate == 0.8].mae.mean())),
        "rmse_10": hr(float(tab[tab.missing_rate == 0.1].rmse.mean())),
        "rmse_80": hr(float(tab[tab.missing_rate == 0.8].rmse.mean())),
        "r2_negativnih": int((tab.r2 < 0).sum()),
        "r2_ukupno": int(len(tab)),
        "adaptive_mae": hr(float(res[res.method == "adaptive_imputation"].mae.mean())),
    }

    IZLAZ.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- Ispis za pisanje teksta ---------------------------------------------
    print("=" * 92)
    print("SAZETAK PO METODI (tablica 5-7)")
    print("=" * 92)
    print(f"{'metoda':<18}{'MAE':>9}{'RMSE':>9}{'R2':>11}{'std MAE':>9}{'pobjede':>9}")
    for r in out["tablica_sazetak"]:
        print(f"{r[0]:<18}{r[1]:>9}{r[2]:>9}{r[3]:>11}{r[4]:>9}{r[5]:>9}")

    print()
    print("=" * 92)
    print("NAJBOLJA METODA PO SCENARIJU I RATEU")
    print("=" * 92)
    for scen, _ in SCEN:
        d = out["scenariji"][scen]["po_rateu"]
        print(f"\n{scen}:")
        for k, v in d.items():
            print(f"   {k:>3} %  {v['najbolji']:<26} MAE {v['najbolji_mae']:>9}"
                  f"   prosjek svih {v['prosjek_mae']:>9}  R2 {v['prosjek_r2']:>12}")

    print()
    print("=" * 92)
    print("LINEAR NA 80 % I REKONSTRUKCIJE (prvi prozor, 20 %)")
    print("=" * 92)
    for scen, _ in SCEN:
        s = out["scenariji"][scen]
        rk = out["rekonstrukcije"].get(scen, {})
        print(f"  {scen:<14} 80%: MAE {s['lin_80_mae']:>8} RMSE {s['lin_80_rmse']:>8} "
              f"R2 {s['lin_80_r2']:>10}   |  rekonstrukcija 20%: MAE {rk.get('mae'):>7} "
              f"RMSE {rk.get('rmse'):>7} R2 {rk.get('r2'):>9}")

    print()
    print("globalno:", out["globalno"])
    print(f"\nzapisano u {IZLAZ.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
