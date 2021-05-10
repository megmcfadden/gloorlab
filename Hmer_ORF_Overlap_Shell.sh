

#Run prodigal to get the open reading frames
'''
for fasta in $(ls /home/meg/Documents/project/*.fna); do
output=$(python3 prodigal_filenames.py $fasta)
echo $fasta
echo $output
prodigal -i $fasta -o $output -a protein-translations.faa -f gff
done
'''
#Execute HMER_Finder script
path=/home/mmcfad/NCBI_Genomes
python3 Hmer-finder.py $path

#Execute Overlap-finder
outputname="May_10th_2021.txt"
python3 Overlap-finder.py $path $outputname
