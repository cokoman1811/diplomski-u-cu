#ifndef KNN_UPGRADED_H
#define KNN_UPGRADED_H

#include "series.h"

/*
 * Napredna KNN imputacija — KNN u prostoru znacajki praznine, na rezidualu.
 *
 * Prva verzija je bila obican KNN s ciklickim znacajkama i pokazala se losijom
 * od osnovnog KNN-a na svih pet scenarija. Uzrok: uz weight_hour = 2,0 i
 * position_norm u rasponu 0..1, tocka udaljena CIJELI DAN s istim satom bila je
 * blize (d^2 = 0,021) od tocke udaljene samo SAT VREMENA (d^2 = 0,273). Metoda
 * je gradila dnevnu klimatologiju umjesto da prati lokalni trend, sto je na
 * sedmodnevnom nizu s rasponom od 22 C stetno.
 *
 * Nova zamisao je drugacija po vrsti, a ne po ugadanju:
 *
 *   Umjesto "koje su tocke vremenski blizu", pita "koje su poznate tocke bile u
 *   SLICNOJ SITUACIJI unutar praznine" — slican relativni polozaj (alpha),
 *   slicne udaljenosti do susjeda i slicno doba dana. Od tih tocaka uci koliko
 *   je linearna baza tamo grijesila, i tu korekciju primjenjuje na rupu.
 *
 * Predikcija je lin_base + tezinski prosjek reziduala susjeda. Ako slicnih
 * situacija nema, reziduali su blizu nule i metoda se svede na linearnu bazu,
 * pa ne moze biti bitno losija od nje.
 */
typedef struct {
    int n_neighbors;         /* broj susjednih "situacija" (zadano 12) */
    double weight_alpha;     /* tezina relativnog polozaja u praznini */
    double weight_gap;       /* tezina log-udaljenosti do susjeda */
    double weight_hour;      /* tezina ciklickog sata */
    double distance_epsilon; /* stabilizacija pri 1/(d+eps) */
} KnnUpgradedConfig;

KnnUpgradedConfig knn_upgraded_default(void);

int knn_imputation_upgraded(const Series *series, const double *temp,
                            const KnnUpgradedConfig *cfg, double *out);

#endif /* KNN_UPGRADED_H */
