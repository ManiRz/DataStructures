# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:43:14 2019

@author: subramaniam.sethu
"""


def RemoveDuplicatedRows(InputDF):
       InputDF['Duplicated'] = InputDF.duplicated()
       InputDF = InputDF[InputDF['Duplicated']==False]
       del InputDF['Duplicated']
       return InputDF


def RemoveAllNullColumns(InputDF):
       All_Null_Columns = []
       for col_name in InputDF.columns.tolist():
              if InputDF[str(col_name)].isnull().all()==True:
                    All_Null_Columns.append(col_name)
       print("Number of Columns Containing 100% Null : "+str(len(All_Null_Columns)))             
       InputDF = InputDF.drop(All_Null_Columns,axis=1)
       print("Removed Null Columns...")
       return InputDF


def RemoveMaxNullColumns(InputDF,Percentage=50):
       Maximum_Null_Columns = []
       for col_name in InputDF.columns.tolist():
              if ((InputDF[col_name].isna().sum()/len(InputDF))*100)>Percentage:
                     print(((InputDF[col_name].isna().sum()/len(InputDF))*100)) 
                     Maximum_Null_Columns.append(col_name)
       print("Number of Columns Having null greater than "+str(Percentage)+" percent : "+str(len(Maximum_Null_Columns)))              
       InputDF =  InputDF.drop(Maximum_Null_Columns,axis=1)
       return InputDF
       print("Removed Null Columns.....")
