import pandas as pd

tene= pd.read_table("/home/meg/Documents/Mycoplasma_Spiroplasma_GFC_num.txt")

filenames=pd.read_table("/home/meg/Documents/project/filenames.txt")

fnames=filenames.iloc[:,0].tolist()

tene_list=tene.iloc[:,0].tolist()

tene_name=[]

for t in range(len(tene_list)):

    name=[f for f in fnames if tene_list[t] in f]
    name2=name[0].split('.fna')
    organism_name= name2[0]
    output= organism_name + '_4orf.gff'
    tene_name.append('/Volumes/ubdata/mmcfad/NCBI_Genomes/'+name[0]+"*"+output)

    t+=1

print(tene_name)
print(len(tene_name))



txt = open("tene_sub_filenames.txt", "w")
for element in tene_name:
    txt.write(element + "\n")
    txt.close
