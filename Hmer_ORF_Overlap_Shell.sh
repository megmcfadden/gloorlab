

#Run prodigal to get the open reading frames

for fasta in $(ls /home/mmcfad/NCBI_Genomes/*.fna); do
output=$(python3 prodigal_filenames.py $fasta)
echo $fasta
echo $output
prodigal -i $fasta -o $output -a protein-translations.faa -f gff
done

#Execute HMER_Finder script
python3 Hmer-finder.py

#Execute Overlap-finder
python3 Overlap-finder.py
