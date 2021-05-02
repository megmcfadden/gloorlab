from overlap import find_overlap

import glob
import os, os.path

hmer_ext = ['*.txt']
orf_ext = ['*.gff']






path = '/Volumes/ubdata/mmcfad/NCBI_Genomes'

files_hmer = [h for h_ext in hmer_ext for h in glob.glob(os.path.join(path, h_ext))]
files_orf = [o for o_ext in orf_ext for o in glob.glob(os.path.join(path, o_ext))]
#"{}_overlap.txt".format(files_hmer) #this is a guess - not sure if it will work
pairs = []

for file in files_hmer:
    file_split = file.replace('Hmer_', '.txt').split('.txt')
    match= [file for file in files_orf if file_split[1] in file]
    pairs.append([file, match[0]])


find_overlap(pairs,'NCBI_04_21_2021.txt')
