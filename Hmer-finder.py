import glob
import os, os.path
import sys

input_location = sys.argv[1]

from hmer import find_hmer


fasta_ext=['*.fna']
files_fasta= [f for f_ext in fasta_ext for f in glob.glob(os.path.join(input_location,f_ext))]

file_new=[]
acc=[]
pairs=[]


for i in files_fasta:
    split=i.replace(input_location,'.fna').replace('/','.fna').split('.fna')
    name=input_location+"/"+"Hmer_"+split[2]+'.txt'
    file_new.append(name)
    ident=split[2].split('_')
    accID=ident[0]+'_'+ident[1]
    acc.append(accID)


pairs=[files_fasta,file_new,acc]

find_hmer(pairs,3)
