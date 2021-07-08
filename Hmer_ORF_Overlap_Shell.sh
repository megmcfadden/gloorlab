
#Run prodigal to get the open reading frames
for fasta in $(ls /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna); do
output=$(python3 prodigal_filenames.py $fasta)
echo $fasta
echo $output
prodigal -i $fasta -o $output -a protein-translations.faa -f gff -g 4
done

#Execute HMER_Finder script
#path=/Volumes/ubdata/mmcfad/NCBI_Genomes
#path=/home/meg/Documents/project
#python3 Hmer-finder.py $path

#Execute Overlap-finder
#outputname="Output_files/July_2_ALL.txt"
#python3 Overlap-finder2.py $path $outputname
