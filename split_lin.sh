for fasta in $(ls /Volumes/ubdata/mmcfad/NCBI_Genomes/*.fna);do
  awk '/^>/ {if(N>0) printf("\n"); printf("%s\n",$0);++N;next;} {printf("%s",$0):} END {printif("\n");}' |\
  split -l 2 --additional-suffix=single.fna - seq_
done


#for file in OUT*
#do
#  mv "$file" "$file.fna"
#done
#
#for i in *.fna; do
#mv $i $(head -1 $i | cut -f1 -d ' ' | tr -d '>').fna
#done
