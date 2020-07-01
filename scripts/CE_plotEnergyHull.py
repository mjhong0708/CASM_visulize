#!/usr/bin/env python
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import ConvexHull, convex_hull_plot_2d


energyHull = pd.read_csv('energyHull.csv')

comp = np.array(energyHull['comp'])
E_DFT = np.array(energyHull['formationE_DFT(eV)'])
E_CE = np.array(energyHull['formationE_CE(eV)'])

hull_DFT = ConvexHull(list(zip(comp, E_DFT)))
hull_CE = ConvexHull(list(zip(comp, E_CE)))

plt.figure(figsize=(6,4.5))
# plt.style.use(['grayscale'])
plt.title('Energy convex hull',fontsize=16)
plt.xlabel('Composition(coverage)',fontsize=16)
plt.ylabel('Formation Energy(eV)',fontsize=16)
plt.xticks(np.arange(0,1.1,0.1))
plt.minorticks_on()


plt.scatter(
            comp,
            E_DFT,
            marker='s',
            s=20,
            facecolor="k",
            edgecolor="k",
            label="DFT"
                )
for simplex in hull_DFT.simplices[1:]:
    plt.plot(
                comp[simplex],
                E_DFT[simplex],
                'k-'
                )

plt.scatter(
                comp,
                E_CE,
                marker="o",
                s=45,
                facecolor="none",
                edgecolor="b",
                label="CE"
                )
for simplex in hull_CE.simplices[1:]:
    plt.plot(
                comp[simplex],
                E_CE[simplex],
                "b--"
                )

plt.legend(loc = 'lower right', fontsize=14, edgecolor='k')
plt.tight_layout()
plt.savefig('energyHull.png',dpi=1200)
plt.show()


# %%
