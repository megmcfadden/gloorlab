import glob
import os, os.path

input_location= "/Volumes/ubdata/mmcfad/NCBI_Genomes"
fasta_ext=['*.fna']
files_fasta= [f for f_ext in fasta_ext for f in glob.glob(os.path.join(input_location,f_ext))]

outputlist=[]
for x in files_fasta:
    input_split=x.split('.fna')
    organism_name= input_split[0]
    output= input_location + organism_name + '_single.fna'
    outputlist.append(output)

print(outputlist)
pairs=[]

for file in files_fasta:
    file_split = file.replace("NCBI_Genomes",".fna").split('.fna')
    match=[file for file in outputlist if file_split[1] in file]
    pairs.append([file, match[0]])

print(pairs)


for i in range(len(pairs)):
    with open(pairs[i][0]) as f_input, open(pairs[i][1], 'w') as f_output:
        block = []

        for line in f_input:
            if line.startswith('>header'):
                if block:
                    f_output.write(''.join(block) + '\n')
                    block = []
                f_output.write(line)
            else:
                block.append(line.strip())

    if block:
        f_output.write(''.join(block) + '\n')
