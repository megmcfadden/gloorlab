#file output name for prodigal run
import sys
input= sys.argv[1]
input_split=input.split('.fna')
organism_name= input_split[0]
output= organism_name + '_4orf.gff'
print(output)
