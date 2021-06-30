import sys
input= sys.argv[1]
input_split=input.split('.fna')
organism_name= input_split[0]
output= organism_name + '_orf.gff'
print(output)
