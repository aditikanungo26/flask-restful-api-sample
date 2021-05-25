from .azure_conn.synapse_connector import *
import requests
import json
import os
import pandas as pd
import sys
from datetime import date,datetime
import io
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


def key_vault_intialise():
        credentials = DefaultAzureCredential()
        key_vault_uri = os.environ.get("KEY_VAULT_URI")
        env_Name = os.environ.get("ENVIRONMENT_NAME")
        secret_client = SecretClient(key_vault_uri,credentials)
        return secret_client,env_Name


def saveRuleSets(versionName,ruleBookName,ruleSetJson,userName,baseVersion):
    try:
        secret_client,env_Name = key_vault_intialise() 
        driver = secret_client.get_secret("driver").value
        server = secret_client.get_secret("synapse-server").value
        database = secret_client.get_secret("synapse-database").value
        table = secret_client.get_secret("tablename").value
        schema = secret_client.get_secret("dbname").value

        status,Result = saverules(driver,server,database,schema,table,versionName,ruleBookName,ruleSetJson,userName,baseVersion,env_Name)
        return status,Result
    except Exception as e:
        return False,str(e)


def getAllRulesetWithVersionDetails():
    try:
        secret_client,env_Name = key_vault_intialise() 
        driver = secret_client.get_secret("driver").value
        server = secret_client.get_secret("synapse-server").value
        database = secret_client.get_secret("synapse-database").value
        table = secret_client.get_secret("tablename").value
        schema = secret_client.get_secret("dbname").value

        status,Result = getallrulewithversion(driver,server,database,schema,table,env_Name)
        return status,Result
    except Exception as e:
        return False,str(e)



