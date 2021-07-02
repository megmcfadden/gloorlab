from overlap2 import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

hmer= pd.read_table('tene_sub_filenames_in.txt')
gff=pd.read_table('tene')
pairs=list(zip(hmer,gff))
print(pairs)


#find_hmer(pairs,'/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_2_sub.txt')
