#The final step in making the numLoci figure
#previous steps: 1. extractSamples.py, 2. sampleSupermatrix.py, 3. calcDistances.py
#If you do all of these steps yourself, results will be slightly different due to random seeds,
#but should be quite similar. Results should be identical if the included results.csv files are used.

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-paper")

dataC = pd.read_csv("C_more_results.csv")
dataCFS = pd.read_csv("C_fruc_siam_results.csv")
dataAFO = pd.read_csv("A_f_o_results.csv")
dataATN = pd.read_csv("A_t_n_results.csv")

dataC_filtered = dataC[dataC["score"] < .02]
#The data from Cercospora had one randomly sampled 3-loci group that had
#large differences (~0.03) between all individuals.
#These data points were removed because they substantially reduced the readability
#of the figure.
#This removal was deemed justifiable because they were randomly selected from a very large set,
#and the points were not critical to the trends in the data.

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=2, sharex=True, \
                                           sharey=False, figsize=(8,8))
f.tight_layout()

ax1 = sns.stripplot(data=dataC, x="numGenes", y="score", hue="type", ax=ax1, dodge=True)
ax1.set(xlabel = " ", ylabel = "Distance")
ax1.get_legend().remove()
ax1.title.set_text("Cercospora kikuchii & C. cf. sigesbeckiae")
ax2 = sns.stripplot(data=dataCFS, x="numGenes", y="score", hue="type", ax=ax2, dodge=True)
ax2.legend(title="Relation", labels=["Interspecific", "Intraspecific"])
ax2.set(ylabel=" ", xlabel=" ")
ax2.title.set_text("Colletotrichum fructicola & C. siamense")
ax3 = sns.stripplot(data=dataAFO, x="numGenes", y="score", hue="type", ax=ax3, dodge=True)
ax3.set(xlabel="Number of loci", ylabel="Distance")
ax3.get_legend().remove()
ax3.title.set_text("Aspergillus flavus & A. oryzae")
ax4 = sns.stripplot(data=dataATN, x="numGenes", y="score", hue="type", ax=ax4, dodge=True)
ax4.set(xlabel="Number of loci", ylabel=" ")
ax4.get_legend().remove()
ax4.title.set_text("Aspergillus terreus & A. niger")


f.savefig("inter_intra_variation.svg", bbox_inches="tight")
