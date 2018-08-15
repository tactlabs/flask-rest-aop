from . import api
from flask import current_app as app
from flask import request
from .response_utils import JSON_MIME_TYPE, success_, success_json
from aop.log_aop import *

'''
    /math/add?a=2&b=2
    http://127.0.0.1:5000/math/add?a=2&b=2
'''
@api.route('/math/add')
@pre_log
@apikey_required
def add():   
    
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)    
    
    '''
    a = request.form.get('a', type=int)
    b = request.form.get('b', type=int)
    '''
    
    c = a + b

    result_json = {
        'result': c,
        
        'api_error': 0
    }
    
    return success_json(result_json)


'''
    /math/add/post?a=2&b=2
    http://127.0.0.1:5000/math/add/post?a=2&b=2
'''
@api.route('/math/add/post', methods=['POST'])
def add_post():   
   
    ''' 
        this can be used as well
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    '''
    
    a = request.form.get('a', type=int)
    b = request.form.get('b', type=int)
    
    
    c = a + b

    result_json = {
        'result': c,
        
        'api_error': 0
    }
    
    return success_json(result_json)


'''
    /math/subtract?a=2&b=2
    http://127.0.0.1:5000/math/subtract?a=2&b=44
'''
@api.route('/math/subtract')
def subtract():
    
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
   
    c = a - b

    result_json = {
            'result': c,
            
            'api_error': 0
        }
    
    return success_json(result_json)





'''
App Config:
    https://stackoverflow.com/questions/18214612/how-to-access-app-config-in-a-blueprint
    
Decorators
    https://medium.com/@nguyenkims/python-decorator-and-flask-3954dd186cda    
'''