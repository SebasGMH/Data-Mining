from numpy import NaN
import pandas as pd
from pandas.core.frame import DataFrame

original_df = pd.read_csv("diabetesData.csv",names=['preg','PG_Conc','bld_prs','skin','insulin','mass',
'pedigree','age','class'])

#remove skin and insulin
dropped_df= original_df.drop(columns=['skin','insulin'])
# print(dropped_df)
#remove rows with empty values, cant use dropna instead use 0 value
#exclude preg as a 0 for preg is not null
#first take preg col away
preg= dropped_df['preg'].to_frame()
dropped_df= dropped_df.drop(columns='preg')
dropped_df= dropped_df.replace(0,NaN)
#add back preg col
dropped_df.insert(0,'preg',preg)
dropped_df=dropped_df.dropna()
#now have a more accurate data set with 0s for preg and dropped col for other values

#make dropped df to csv
# dropped_df.to_csv('diabettesDropped.csv',index=False)

#get accurate means/meds for 'PG_Conc','bld_prs','mass'
mean_1= dropped_df['PG_Conc'].mean()
mean_2= dropped_df['bld_prs'].mean()
mean_3= dropped_df['mass'].mean()
mean_6= dropped_df['pedigree'].mean()
mean_7= dropped_df['age'].mean()
med_1=dropped_df['PG_Conc'].median()
med_2=dropped_df['bld_prs'].median()
med_3=dropped_df['mass'].median()
med_6=dropped_df['pedigree'].median()
med_7=dropped_df['age'].median()


#get mean /med of skin and insulin with original data set
mean_4=original_df['skin'].mean()
mean_5=original_df['insulin'].mean()
med_4=original_df['skin'].median()
med_5=original_df['insulin'].median()

#define functions for med /mean filled dataset
def medDf():
    med_df= original_df
    #replace 0s with corresponding med value
    med_df['PG_Conc']= med_df['PG_Conc'].replace(0,med_1)
    med_df['bld_prs']= med_df['bld_prs'].replace(0,med_2)
    med_df['skin']= med_df['skin'].replace(0,med_4)
    med_df['insulin']= med_df['insulin'].replace(0,med_5)
    med_df['mass']= med_df['mass'].replace(0,med_3)
    med_df['pedigree']= med_df['pedigree'].replace(0,med_6)
    med_df['age']= med_df['age'].replace(0,med_7)
    #save medDf into csv
    med_df.to_csv('DiabetesMediums.csv',index=False)
    return med_df

def meanDf():
    mean_df= original_df
    #replace 0s with corresponding mean value
    mean_df['PG_Conc']= mean_df['PG_Conc'].replace(0,mean_1)
    mean_df['bld_prs']= mean_df['bld_prs'].replace(0,mean_2)
    mean_df['skin']= mean_df['skin'].replace(0,mean_4)
    mean_df['insulin']= mean_df['insulin'].replace(0,mean_5)
    mean_df['mass']= mean_df['mass'].replace(0,mean_3)
    mean_df['pedigree']= mean_df['pedigree'].replace(0,mean_6)
    mean_df['age']= mean_df['age'].replace(0,mean_7)
    #save medDf into csv
    mean_df.to_csv('DiabetesMeans.csv',index=False)
    return mean_df
