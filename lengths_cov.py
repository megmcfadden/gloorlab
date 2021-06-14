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

with open("/Volumes/ubdata/mmcfad/NCBI_Genomes/Output_files/Observed_expected_test.txt", "w+") as w:

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
            select_split=split[5].replace(";","=").split("=")
            length=int(select_split[3])

            seq=ORF["seq_id"].unique()
            sequence=seq[0]

            #determine the expected ratio of inside vs outside the open reading frame

            sum_expt=sum(ORF["end"]-ORF['start'])

            expected=(length-sum_expt)/sum_expt

            data_expt={'Sequence':[sequence],'Length':[length],'ORF(BP)': [sum_expt], "Expected": [expected]}

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
