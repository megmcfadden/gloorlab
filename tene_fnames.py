import pandas as pd

tene= pd.read_table("/home/meg/Documents/Tenericutes_GFC_num.txt")

filenames=pd.read_table("/home/meg/Documents/project/filenames.txt")

fnames=filenames.iloc[:,0].tolist()

tene_list=tene.iloc[:,0].tolist()

names=[]
tene_name_in=[]
tene_name_out=[]


for t in range(len(tene_list)):

    name=[f for f in fnames if tene_list[t] in f]
    names.append('/Volumes/ubdata/mmcfad/NCBI_Genomes/'+name[0])
    name2=name[0].split('.fna')
    organism_name= name2[0]
    output= organism_name + '_4orf.gff'
    tene_name_in.append('/Volumes/ubdata/mmcfad/NCBI_Genomes/'+"Hmer_"+name2[0]+".txt")
    tene_name_out.append('/Volumes/ubdata/mmcfad/NCBI_Genomes/'+output)

    t+=1
print(names)



fna = open("tene_ALL_Filenames_fna.txt","w")
for element_fna in names:
    fna.write(element_fna + '\n')
    fna.close
txt = open("tene_ALL_filenames_in.txt", "w")
for element in tene_name_in:
    txt.write(element + "\n")
    txt.close
txt_out = open("tene_ALL_filenames_out.txt", "w")
for element_out in tene_name_out:
    txt_out.write(element_out+"\n")
    txt_out.close
