

#Run prodigal to get the open reading frames
for fasta in $(ls /Volumes/ubdata/mmcfad/NCBI_Genomes*.fna); do
output=$(python3 prodigal_filenames.py $fasta)
#echo $fasta
#echo $output
#prodigal -i $fasta -o $output -a protein-translations.faa -f gff
#done

#Execute HMER_Finder script
path=/Volumes/ubdata/mmcfad/NCBI_Genomes
#path=/home/meg/Documents/project
#python3 Hmer-finder.py $path

#Execute Overlap-finder
outputname="Output_files/June_30th_2021.txt"
python3 Overlap-finder.py $path $outputname
