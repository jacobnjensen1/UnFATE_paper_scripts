#used to make the numLoci figure, replace samples with the accessions you want
#FcC_supermatrix.fas couldn't be included in this repository due to size, even when xzipped
#Use FASconCAT-G to concatenate the nucleotide database, save the partition file with -l

from Bio import SeqIO


#Colletotrichum fructicola
#Colletotrichum siamense

samples = ["GCA_000319635.2", "GCA_002314275.2", "GCA_002887685.1", "GCA_009771025.1", \
           "GCA_012932255.1", "GCA_013201875.1", "GCA_013201905.1", "GCA_013201925.1", \
           "GCA_008520285.1", "GCA_011426375.1", "GCA_011426385.1", "GCA_011428095.1", \
           "GCA_011428115.1", "GCA_011445115.1", "GCA_011947465.1", "GCA_013201745.1"]

with open("FcC_supermatrix.fas") as inFile, open("Coll_f_s_supermatrix.fas", 'w') as outFile:
  for record in SeqIO.parse(inFile, "fasta"):
    if record.id in samples:
      SeqIO.write(record, outFile, "fasta-2line")


"""
AFO_samples = ['GCA_001576635.1', 'GCA_001576645.1', 'GCA_001576655.1', 'GCA_001576715.1', \
        'GCA_001576725.1', 'GCA_001576735.1', 'GCA_001576745.1', 'GCA_001576795.1', \
        'GCA_001695535.1', 'GCA_002217615.1', 'GCA_002007945.1', 'GCA_002214955.1', \
        'GCA_002214965.1', 'GCA_004353305.1', 'GCA_009684795.1', 'GCA_009684815.1', \
        'GCA_009684835.1', 'GCA_009684855.1', 'GCA_009684875.1', 'GCA_009684895.1']"""

"""ATN_samples = ["GCA_001630395.1", "GCA_002749855.1", "GCA_002930435.1", "GCA_009014675.1", \
        "GCA_009834425.1", "GCA_009932835.1", "GCA_015266375.1", "GCA_015333565.1", \
        "GCA_000166915.1", "GCA_000149615.1", "GCA_000002855.2", "GCA_001515345.1", \
        "GCA_001715265.1", "GCA_001741885.1", "GCA_001741905.1", "GCA_001741915.1", \
        "GCA_001931795.1", "GCA_002211485.2", "GCA_002740505.1", "GCA_004634315.1"]"""

"""CFS_samples = ["GCA_000319635.2", "GCA_002314275.2", "GCA_002887685.1", "GCA_009771025.1", \
           "GCA_012932255.1", "GCA_013201875.1", "GCA_013201905.1", "GCA_013201925.1", \
           "GCA_008520285.1", "GCA_011426375.1", "GCA_011426385.1", "GCA_011428095.1", \
           "GCA_011428115.1", "GCA_011445115.1", "GCA_011947465.1", "GCA_013201745.1"]"""

#CKS_samples = ["GCA_005356855.1", "GCA_009193115.1", "GCA_002217505.1", "GCA_005356805.1"]
