
ls *.fna>tene_sub_filenames.txt
#Run prodigal to get the open reading frames
for fasta in $(cat 'tene_sub_filenames.txt'); do
output=$(python3 prodigal_filenames.py $fasta)
echo $fasta
echo $output
prodigal -i $fasta -o $output -a protein-translations.faa -f gff -g 4
#done

#Execute HMER_Finder script
#path=/Volumes/ubdata/mmcfad/NCBI_Genomes
#path=/home/meg/Documents/project
#python3 Hmer-finder.py $path

#Execute Overlap-finder
#outputname="Output_files/June_30th_2021.txt"
#python3 Overlap-finder.py $path $outputname
