'''
for fasta in $(ls /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna);
do
while read line
do
  if [[ ${line:0:1} == '>']]
  then
    outfile=${line #>}.fna
    echo $line > $outfile
  else
    echo $line >> $outfile
  fi
done
done
'''
