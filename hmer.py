# Finding homopolymers in FASTA file


#num must be one smaller then desired - if looking for lengths of 4 and above imput 3
def find_hmer(file, output, num):
    with open(file, "r") as infile, open(output, "w+") as w:
        contig = base = start = end = -1

        for line in infile:
            if line[0] == '>':
                if end - start > 1:
                    w.write('\t'.join(map(str,[contig,start,end,end-start,base]))+'\n')
                contig = line.strip().split()[0][1:]
                base = -1
                start = end = 1
            else:
                for b in line.strip():
                    if b !=base:
                        if end - start > num:
                            w.write('\t'.join(map(str,[contig,start,end,end-start,base]))+'\n')
                        start = end
                        base = b
                    end +=1
            if end - start > num:
                w.write('\t'.join(map(str,[contig,start,end,end-start,base]))+'\n')
