from overlap2 import find_overlap

import glob
import os, os.path
import sys
import pandas as pd

hmer= pd.read_table('tene_sub_filenames_in.txt',names=['hmer'])
gff=pd.read_table('tene_sub_filenames_out.txt')

hmer['gff']=gff


pairs=hmer[['hmer','gff']].apply(tuple,axis=1).tolist()


print(pairs)


#find_hmer(pairs,'/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_2_sub.txt')
