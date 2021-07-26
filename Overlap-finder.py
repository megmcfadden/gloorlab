from overlap import find_overlap

import glob
import os, os.path
import sys

hmer_ext = ['*single.txt']
orf_ext = ['*orf.gff']


path = sys.argv[1]
outname= sys.argv[2]

files_hmer = [h for h_ext in hmer_ext for h in glob.glob(os.path.join(path, h_ext))]
files_orf = [o for o_ext in orf_ext for o in glob.glob(os.path.join(path, o_ext))]
#"{}_overlap.txt".format(files_hmer) #this is a guess - not sure if it will work
pairs = []

for file in files_hmer:
    file_split = file.replace('HmerSingle_', '.txt').replace('single.txt','.txt').split('.txt')
    match= [file for file in files_orf if file_split[1] in file]
    pairs.append([file, match[0]])

output= path + "/" + outname
find_overlap(pairs,output)
