from overlap2 import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

hmer= pd.read_table('tene_sub_filenames_in.txt')
gff=pd.read_table('tene_sub_filenames_out.txt')
pairs=[]

for i in range(len(hmer)):
    pairs.append((hmer[i],gff[i]))

    
print(pairs)


#find_hmer(pairs,'/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_2_sub.txt')
