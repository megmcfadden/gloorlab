for fasta in $(ls /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna); do
output=$(python3 hmer_filenames.py $fasta)
echo $fasta
echo $output
done

cat /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna |\
awk '/^>/ {if(N>0) printf("\n"); printf("%s\n",$0);++N;next;} { printf("%s",$0);} END {printf("\n");}' | \
split -l 2 -$output




#for /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna |\
#  awk '/^>/ {if(N>0) printf("\n"); printf("%s\n",$0);++N;next;} { printf("%s",$0);} END {printf("\n");}' |\
#  split -l 2 --additional-suffix=single.fna -
