# Finding homopolymers in FASTA file
#

#num must be one smaller then desired - if looking for lengths of 4 and above imput 3
def find_hmer(pair, num):
    for i in range(len(pair[0])):
        with open(pair[0][i], "r") as infile, open(pair[1][i], "w+") as w:
            contig = ident = base = start = end = info=-1
            for line in infile:
                if line[0] == '>':
                    if end - start > 1:
                        w.write('\t'.join(map(str,[contig,ident,start,end,end-start,base,info]))+'\n')
                    contig = line.strip().split()[0][1:]
                    ident = pair[2][i]
                    info_split = line.split(" ")
                    info_space=info_split[-2]+info_split[-1]
                    info=info_space.rstrip("\n")
                    base = -1
                    start = end = 1
                else:
                    for b in line.strip():
                        if b !=base:
                            if end - start > num:
                                w.write('\t'.join(map(str,[contig,ident,start,end,end-start,base,info]))+'\n')
                            start = end
                            base = b
                        end +=1
                if end - start > num:
                    w.write('\t'.join(map(str,[contig,ident,start,end,end-start,base,info]))+'\n')
        ++i
