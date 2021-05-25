from common.response_manager import generate_response,generate_error_response
from common.adapter import *
from common.log import log
from common.error_manage import errorManagement
from flask_restful import Resource
from flask import Response, request
import json

class saveresult(Resource):

    def post(self): 
        try:
            record = request.get_json()[0]
            versionName = record["versionName"] 
            ruleBookName = record["ruleBookName"] 
            ruleSetJson =json.dumps(record["ruleSetsJson"])
            userName =record["userName"] if(record["userName"] is not None) else "" 
            baseVersion =record["baseVersion"] if(record["baseVersion"] is not None) else ""
            q1,output_msg=saveRuleSets(versionName,ruleBookName,ruleSetJson,userName,baseVersion)
            
            if q1==True:           
                resp = generate_response(request.headers,None,output_msg,"saveruleset")
                return resp

            else:
                error_resp = generate_error_response(500,"error_code","Internal Server Error",request.headers,"saveruleset")
                log(request.headers,"ERROR","saveruleset","Main",str(output_msg))
                return error_resp
        except Exception as e:
            log(request.headers,"ERROR","saveruleset","Main",str(e))
            errormsg = generate_error_response(500,"error_code","Internal Server Error",request.headers,"saveruleset")
            return errormsg


class getallRulesetWithVersion(Resource):
    def get(self):
        try: 
            q1,output_msg=getAllRulesetWithVersionDetails()
            if q1==True:           
                if not output_msg:  
                    error_resp= generate_error_response(400,"error_code","No record found",request.headers,"getallRulesetWithVersion")
                    return error_resp
                else:        
                    resp = generate_response(request.headers,None,output_msg,"getallRulesetWithVersion")
                    return resp

            else:
                log(request.headers,"ERROR","getallRulesetWithVersion","rulesmaster",str(output_msg))
                error_resp = generate_error_response(500,"error_code","Internal Server Error",request.headers,"getallRulesetWithVersion")
                return error_resp            
                
        except Exception as e:
            log(request.headers,"ERROR","getallRulesetWithVersion","Main",str(e))
            errormsg = generate_error_response(500,"error_code","Internal Server Error",request.headers,"getallRulesetWithVersion")
            return errormsg

