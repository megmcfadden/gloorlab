import pandas as pd

tene= pd.read_table("/home/meg/Documents/Tenericutes_GFC_num.txt")

filenames=pd.read_table("/home/meg/Documents/project/filenames.txt")

fnames=filenames.iloc[:,0].tolist()

tene_list=tene.iloc[:,0].tolist()

tene_name=[]

for t in range(len(tene_list)):

    name=[f for f in fnames if tene_list[t] in f]
    tene_name.append(name[0])

    t+=1

print(tene_name)
print(len(tene_name))

txt = open("tene_file_names.txt", "w")
for element in tene_name:
    txt.write(element + "\n")
    txt.close
