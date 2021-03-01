#determining overlap between open reading frames and hmers
import pandas as pd
import numpy as np
import gffpandas.gffpandas as gffpd
import csv

def find_overlap(file_hmer, file_orf, file_output):
    with open(file_hmer, "r") as fileH, open(file_orf, "r") as infileO, open(file_output, "w+") as w:
            infileH = csv.reader(fileH, delimiter="\t")

        #create data frames from  txt - hmer.py output and gff prodigal output files
            dfH = pd.DataFrame(infileH, columns=["Sequence","Start","End","Length","Base"])
            ORFLarge = gffpd.read_gff3(file_orf)
            #read gff makes a strange data frame structure - convert to standard Pandas data frame
            dfORFLarge = pd.DataFrame(ORFLarge.df)


            #remove excess info from gff data frame
            selected_columns= dfORFLarge[["seq_id","start","end"]]
            dfORF = selected_columns.copy()
            dfORF = pd.to_numeric(dfORF[['start','end']])

            #THIS IS WHERE THE GOOD SHIT STARTS
            #using numpy array to combine the subtraction of Hmer from ORF for both start and end
            arrayH=np.array(dfH[['Start','End']])

            arrayORF=np.array(dfORF[['start','end']])

            print(arrayH)
            print(arrayORF)

            #create a 3D array which is sets=numbers of hmers, rows=#open reading frames columns=2 (start,end)
            combined=(arrayORF - arrayH[:,np.newaxis]).reshape(-1,arrayORF.shape[0],2)
            #Find and denote true or false for when True = (negative -Start), (positive -end)
            T_F=np.where((combined[:,:,0] <0)&(combined[:,:,1]>0),True,False).reshape(-1,combined.shape[1],1)

            #if set contains True = True if not = False, reduce to one value per set
            T_F_clean = np.any((T_F[:,0,:]==True),axis=1).reshape(-1,1)

            T_F_dataframe=pd.DataFrame(data=T_F_clean,columns=['In_ORF'])

            #add the in ORF column to the hmer data frames
            dfH['InORF(T/F)']=T_F_dataframe

            dfH.to_csv('file_output', sep="\t")
