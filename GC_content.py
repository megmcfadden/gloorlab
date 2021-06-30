#GC content of all genomes

import pandas as pd
import gffpandas.gffpandas as gffpd
import numpy as np
import glob
import os, os.path
import csv
from csv import writer

path= '/Volumes/ubdata/mmcfad/NCBI_Genomes'

orf_ext = ['*.gff']
files_orf = [o for o_ext in orf_ext for o in glob.glob(os.path.join(path, o_ext))]

overlap=pd.read_table("/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/June_1st_2021.txt", sep='\t')

expect_combined=[]

table_df=pd.DataFrame(columns=["Sequence","Length","BP_inside","Expected","Hmer_inside(BP)", "Hmer_outside(BP)", "Observed"])

with open("/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/GC_content.txt", "w+") as w:

    for i in range(len(files_orf)):
        print(files_orf[i])
        #Determining the expected amounts inside vs outside open reading frames
        orf=gffpd.read_gff3(files_orf[i])

        df_orfLarge = pd.DataFrame(orf.df)
        selected_columns= df_orfLarge[["seq_id","start","end"]]
        ORF = selected_columns.copy()
        scaffolds=ORF['seq_id'].nunique()

        if scaffolds == 1:
            #Length of the genome from the header of the gff file
            header = orf.header

            split = header.split(" ")
            select_split=split[15].replace(";","=").split("=")
            GC=select_split[2]

            seq=ORF["seq_id"].unique()
            sequence=seq[0]

            data_expt={'Sequence':[sequence],'GC':[GC]}

            df_expt=pd.DataFrame(data=data_expt)

            expect_combined.append(df_expt)


            i+1

        else:
            print("skip")
            i+1

    #convert expect_combined from list to a data frame
    expect_combined_df=pd.concat(expect_combined)



    expect_combined_df.to_csv(w, sep="\t", index=False)
