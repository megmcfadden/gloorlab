#determining overlap between open reading frames and hmers
import pandas as pd
import numpy as np
import gffpandas.gffpandas as gffpd
import csv
from csv import writer

def find_overlap(pairs, file_output):
    with open(file_output, "w+") as w:
        Hmer_total=[]
        df_Counts_Total=pd.DataFrame(columns=['Sequence','Length','Base','InORF(T/F)'])

        for i in range(len(pairs)):
            print(pairs[i][0])
            print(pairs[i][1])
            #create data frames from  txt - hmer.py output and gff prodigal output files
            dfH = pd.read_table(pairs[i][0], names=["Sequence","Acession_ID","Start","End","Length","Base","Info"], sep='\t')

            ORFLarge = gffpd.read_gff3(pairs[i][1])
            #read gff makes a strange data frame structure - convert to standard Pandas data frame
            dfORFLarge = pd.DataFrame(ORFLarge.df)


            #remove excess info from gff data frame
            selected_columns= dfORFLarge[["seq_id","start","end"]]
            dfORF = selected_columns.copy()
            print(type(dfH))
            print(type(dfORF))
            #retain only the hmers from genomes that are complete
            hmer_rows=dfH[dfH["Info"].str.contains("completegenome")]
            print(hmer_rows)
            #retain the open reading frames that contain the same accession ID that is saved in the hmer rows
            sequence_complete=hmer_rows.iloc[0,0]
            print(sequence_complete)
            orf_rows=dfORF[dfORF["seq_id"].str.contains(sequence_complete)]

            print(hmer_rows)
            print(orf_rows)
            #using numpy array to combine the subtraction of Hmer from ORF for both start and end

            arrayH=np.array(hmer_rows[['Start','End']])

            arrayORF=np.array(orf_rows[['start','end']])

            #create a 3D array which is sets=numbers of hmers, rows=#open reading frames columns=2 (start,end)
            combined=(arrayORF - arrayH[:,np.newaxis]).reshape(-1,arrayORF.shape[0],2)
            #Find and denote true or false for when True = (negative -Start), (positive -end)

            T_F=np.where((combined[:,:,0] <0)&(combined[:,:,1]>0),True,False).reshape(-1,1,combined.shape[1])

            #if set contains True = True if not = False, reduce to one value per set
            T_F_clean = np.any((T_F[:,0,:]==True),axis=1).reshape(-1,1)

            T_F_dataframe=pd.DataFrame(data=T_F_clean,columns=['In_ORF'])

            #add the in ORF column to the hmer data frames
            hmer_rows['InORF(T/F)']=T_F_dataframe

            dfCounts=hmer_rows[['Sequence','Acession_ID','Length','Base','InORF(T/F)','Info']].value_counts().sort_index().reset_index(name="Counts")

            Hmer_total.append(dfCounts)

            i+=1

        Counts=pd.concat(Hmer_total)

        Counts.to_csv(w, sep="\t", index=False)
