#3rd step in making numLoci figure, after sampleSupermatrix.py, before makeNumLociFigure.py
#run each resampled file through this (bash for loops are your friend)

from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from glob import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)
parser.add_argument("--num", required=True)
args = parser.parse_args()

accsCf = ["GCA_000319635.2", "GCA_002314275.2", "GCA_002887685.1", "GCA_009771025.1", \
           "GCA_012932255.1", "GCA_013201875.1", "GCA_013201905.1", "GCA_013201925.1"]

accsCs = ["GCA_008520285.1", "GCA_011426375.1", "GCA_011426385.1", "GCA_011428095.1", \
           "GCA_011428115.1", "GCA_011445115.1", "GCA_011947465.1", "GCA_013201745.1"]

aln = AlignIO.read(open(args.file), "fasta")
for record in aln:
    record.seq = record.seq.upper()

calc = DistanceCalculator("trans", ["N", "-", "W", "S", "M", "K", "R", "Y", "B", "D", "H", "V"])
dm = calc.get_distance(aln)
#print(dm)

intraScoresF = []
intraScoresS = []
interScores = []

with open("results.csv", 'a') as resFile:
  for i, scoreList in enumerate(dm.matrix):
    #print(dm.names[i])
    names = dm.names
    for j, score in enumerate(scoreList):
      print("{} and {}: {}".format(names[i], names[j], score))
      if names[i] == names[j]:
        continue #same sample, we don't care
      elif names[i] in accsCf and names[j] in accsCf:
        intraScoresF.append(score)
        resFile.write("{},{},{}\n".format(args.num, "intra", score))
      elif names[i] in accsCs and names[j] in accsCs:
        intraScoresS.append(score)
        resFile.write("{},{},{}\n".format(args.num, "intra", score))
      else:
        interScores.append(score)
        resFile.write("{},{},{}\n".format(args.num, "inter", score))

print(len(intraScoresS))
print(sum(intraScoresS) / len(intraScoresS))
print(len(intraScoresF))
print(sum(intraScoresF) / len(intraScoresF))
print(len(interScores))
print(sum(interScores) / len(interScores))

"""ATN:
accsAter = ["GCA_001630395.1", "GCA_002749855.1", "GCA_002930435.1", "GCA_009014675.1", \
        "GCA_009834425.1", "GCA_009932835.1", "GCA_015266375.1", "GCA_015333565.1", \
        "GCA_000166915.1", "GCA_000149615.1"]

accsAnig = ["GCA_000002855.2", "GCA_001515345.1", "GCA_001715265.1", "GCA_001741885.1", \
        "GCA_001741905.1", "GCA_001741915.1", "GCA_001931795.1", "GCA_002211485.2", \
        "GCA_002740505.1", "GCA_004634315.1"]
"""

"""AFO:
accsAfla = ['GCA_001576635.1', 'GCA_001576645.1', 'GCA_001576655.1', 'GCA_001576715.1', \
        'GCA_001576725.1', 'GCA_001576735.1', 'GCA_001576745.1', 'GCA_001576795.1', \
        'GCA_001695535.1', 'GCA_002217615.1']

accsAory = ['GCA_002007945.1', 'GCA_002214955.1', 'GCA_002214965.1', 'GCA_004353305.1', \
        'GCA_009684795.1', 'GCA_009684815.1', 'GCA_009684835.1', 'GCA_009684855.1', \
        'GCA_009684875.1', 'GCA_009684895.1']
"""

"""CFS:
accsCf = ["GCA_000319635.2", "GCA_002314275.2", "GCA_002887685.1", "GCA_009771025.1", \
           "GCA_012932255.1", "GCA_013201875.1", "GCA_013201905.1", "GCA_013201925.1"]

accsCs = ["GCA_008520285.1", "GCA_011426375.1", "GCA_011426385.1", "GCA_011428095.1", \
           "GCA_011428115.1", "GCA_011445115.1", "GCA_011947465.1", "GCA_013201745.1"]
"""


"""CKS:
accsCkik = ["GCA_005356855.1", "GCA_009193115.1"]

accsCsig = ["GCA_002217505.1", "GCA_005356805.1"]
"""


