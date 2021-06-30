#Prokka open reading frames
file=/home/meg/Documents/GitHub/hmer.overlap/tene_file_names.txt
filenames= 'cat $file'

for fasta in $(/home/meg/Documents/GitHub/hmer.overlap/tene_file_names.txt); do
output=$(python3 prokka_filenames.py $fasta)
echo $output
#prodigal -i $fasta -o $output -a protein-translations.faa -f gff
done
