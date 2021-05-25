from flask import Flask,jsonify,make_response,request
from .log import log
import json
import os
import sys
from .error_manage import errorManagement
        
def generate_response(headers,output,out_msg,API_name):
    try:
        resp = make_response(jsonify(out_msg))
        log(headers,"INFO",API_name,"Response",json.dumps(output))
        return resp
    except Exception as e:
        return False,str(e) 
        
def generate_error_response(httpcode,apim_error_code,errormsg,headers,API_name):
    try:
       error = errorManagement(httpcode,apim_error_code,errormsg)
       resp = make_response(jsonify(error),httpcode)
       log(headers,"ERROR",API_name,"Response",str(errormsg))
       return resp
    except Exception as e:
        return False,str(e)
    


    
     
