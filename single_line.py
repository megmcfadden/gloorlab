fasta_ext=['*single.fna']
files_fasta= [f for f_ext in fasta_ext for f in glob.glob(os.path.join(input_location,f_ext))]

input_split=input.split('.fna')
organism_name= input_split[0]
output= organism_name + '_single.fna'

input2=files_fasta.tolist()
output2=output.tolist()
pairs=[]

for file in input2:
    print(file)
    file_split = file.split('.fna')
    print(file_split[1])
    match= [file for file in output2 if file_split[1] in file]
    pairs.append([file, match[0]])

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
