from overlap import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

hmer= pd.read_table('tene_ALL_filenames_in.txt',names=['hmer'])
gff=pd.read_table('tene_ALL_filenames_out.txt', names=['gff'])


hmer2=hmer['hmer'].tolist()
gff2=gff['gff'].tolist()
print(type(hmer2))
pairs=[]

for file in hmer2:
    print(file)
    file_split = file.replace('Hmer_', '.txt').split('.txt')
    print(file_split[1])
    match= [file for file in gff2 if file_split[1] in file]
    pairs.append([file, match[0]])

print(pairs)


find_overlap(pairs,'/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_6_ALL.txt')
