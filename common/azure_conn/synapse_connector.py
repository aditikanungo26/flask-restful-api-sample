import pandas as pd
import pyodbc
import os 
import json
from common.log import log
from datetime import date,datetime
from common.response_manager import generate_response,generate_error_response
import sys
import requests 

        
def getConnectionString(driver,server,database,env_Name):
        cnxnstr =''
        userName= 'username'
        if env_Name == 'local':
            cnxnstr='Driver='+driver+';Server='+server+';PORT=1433;Database='+database+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;UID='+userName+';Authentication=ActiveDirectoryInteractive'
        elif env_Name == 'Dev':
            cnxnstr='Driver='+driver+';Server='+server+';PORT=1433;Database='+database+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=180;Authentication=ActiveDirectoryMsi'
            
        cnxn = pyodbc.connect(cnxnstr, autocommit=True)
        return cnxn
        

def saverules(driver,server,database,schema,table,versionName,ruleBookName,ruleSetJson,userName,baseVersion,env_Name):
    try:
        cnxn = getConnectionString(driver,server,database,env_Name)
        query = "declare @dateval datetime=GetDate() insert into "+schema+"."+table+" values ('"+str(versionName)+"','"+ruleBookName+"',@dateval,'"+ruleSetJson+"','"+userName+"','"+baseVersion+"')"
        cursor = cnxn.cursor()
        cursor.execute(query) 
        output= {"Output" :"Record has been added successfully"}
        return True,output 
    except Exception as e:
        return False,str(e)
            


def getallrulewithversion(driver,server,database,schema,table,env_Name):
    try:
        cnxn = getConnectionString(driver,server,database,env_Name)
        query = "select ruleBookName,VersionName as versions from ["+ schema+"].["+ table+"]"  
        df = pd.read_sql(query,cnxn)
        if len(df.index)!=0:
            df = df.groupby('ruleBookName')['versions'].apply(list)
            df = df.to_frame()
            df = df.reset_index()
            dfdict = df.to_dict('record') 
        else:
            dfdict= {}
        return True,dfdict 
    except Exception as e:
        return False,str(e)
