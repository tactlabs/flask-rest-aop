'''
    Source:
        
'''

from flask import request
from functools import wraps
from rest_api.response_utils import JSON_MIME_TYPE, success_, success_json

'''
    
'''
def pre_log(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        
        print('trap 1.1')        
        
        # finally call f. f() now haves access to g.user
        return f(*args, **kwargs)
   
    return wrap


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        
        # if user is not logged in, redirect to login page      
        #if not request.headers["authorization"]:
        #    return redirect("login page")
        
        # get user via some ORM system
        #user = User.get(request.headers["authorization"])
        
        # make user available down the pipeline via flask.g
        #g.user = user
        
        # finally call f. f() now haves access to g.user
        return f(*args, **kwargs)
   
    return wrap


def apikey_required(f):
    
    @wraps(f)
    def wrap(*args, **kwargs):
        
        if not request.args.get("apikey"):
            result_json = {
                'api_error': 2001,
                'api_error_messae' : 'apikey required'
            }
    
            return success_json(result_json)
        
        # get user via some ORM system
        #user = User.get(request.headers["authorization"])
        
        # make user available down the pipeline via flask.g
        #g.user = user
        
        # finally call f. f() now haves access to g.user
        return f(*args, **kwargs)
   
    return wrap