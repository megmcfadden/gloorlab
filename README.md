# hmer.overlap

Workflow to find all homopolymers in a FASTA file over x length and determine if each homopolymer falls within an open reading frame. 

1. Use hmer.py to find all hmers in fasta file, this will output each hmer with its sequence id, length, position, and specifc base.
2. Use prodigal or other to determine open reading frames in fasta file - must be gff format 
3. Use overlap.py to determine if each homopolymer falls inside or outside an open reading frame. 
