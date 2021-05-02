import glob
import os, os.path


input_location = '/home/mmcfad/NCBI_Genomes'

from hmer import find_hmer


fasta_ext=['*.fna']
files_fasta= [f for f_ext in fasta_ext for f in glob.glob(os.path.join(input_location,f_ext))]

file_new=[]
pairs=[]


for i in files_fasta:
    split=i.replace(input_location,'.fna').replace('/','.fna').split('.fna')
    name="Hmer_"+split[2]+'.txt'
    file_new.append(name)

pairs=[files_fasta,file_new]

find_hmer(pairs,3)
