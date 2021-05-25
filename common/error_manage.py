
#This file stores the error information to generate for error in code
def errorManagement(httpcode,apim_error_code,errormsg):
    
    error = {
        'errormanagements': {
            'errorcode': str(apim_error_code),
            'error_description': str(errormsg)
        }
        }
    
    return  error  
     
 


