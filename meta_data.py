import pandas as pd
import gffpandas.gffpandas as gffpd
import numpy as np
import glob
import os, os.path
import csv
from csv import writer


gff=pd.read_table('tene_sub_filenames_out.txt', names=['gff'])
gff2=gff['gff'].tolist()


overlap=pd.read_table("/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/July_2_sub.txt", sep='\t')

expect_combined=[]

table_df=pd.DataFrame(columns=["Sequence","Length","BP_inside","Expected","Hmer_inside(BP)", "Hmer_outside(BP)", "Observed"])

with open("/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/Observed_expected_tene.txt", "w+") as w:

    for i in range(len(gff2)):
        print(gff2[i])
        #Determining the expected amounts inside vs outside open reading frames
        orf=gffpd.read_gff3((gff2)[i])

        df_orfLarge = pd.DataFrame(orf.df)
        selected_columns= df_orfLarge[["seq_id","start","end"]]
        ORF = selected_columns.copy()
        scaffolds=ORF['seq_id'].nunique()

        if scaffolds == 1:
            #Length of the genome from the header of the gff file
            header = orf.header

            split = header.split(" ")
            select_split=split[5].replace(";","=").split("=")
            length=int(select_split[3])

            seq=ORF["seq_id"].unique()
            sequence=seq[0]

            c_split=split[-1].replace(";","=").split("=")
            code=c_split[4]


            gc_split=split[-1].replace(";","=").split("=")
            print(gc_split)
            GC=select_split[2]
            print(GC)
            #determine the expected ratio of inside vs outside the open reading frame

            sum_expt=sum(ORF["end"]-ORF['start'])

            expected=(length-sum_expt)/sum_expt

            data_expt={'Sequence':[sequence],'Length':[length],'ORF(BP)': [sum_expt], "Expected": [expected], 'Genetic_code':[code], 'GC_Content':[GC]}

            df_expt=pd.DataFrame(data=data_expt)

            expect_combined.append(df_expt)


            i+1

        else:
            print("skip")
            i+1


    #determine the Observed
    overlap["BasePairs"]=overlap["Length"]*overlap["Counts"]
    copy=overlap[["Sequence", "InORF(T/F)", "BasePairs"]]
    overlap_clean=copy.copy()
    overlap_sum=overlap_clean.groupby(["Sequence","InORF(T/F)"]).sum(["BasePairs"])
    observed1=overlap_sum.pivot_table(index="Sequence", columns="InORF(T/F)")
    observed=observed1.reset_index()
    observed.columns=["Sequence","HmerOut(BP)","HmerIn(BP)"]
    observed["Observed"]=observed["HmerOut(BP)"]/observed["HmerIn(BP)"]

    #convert expect_combined from list to a data frame
    expect_combined_df=pd.concat(expect_combined)

    combined=pd.merge(observed,expect_combined_df, left_on=['Sequence'], right_on=["Sequence"], how='left')
    print(combined)

    combined.to_csv(w, sep="\t", index=False)
