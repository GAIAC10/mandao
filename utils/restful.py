#encoding: utf-8
from django.http import JsonResponse

# 获取表单错误信息
# form.errors：获取的错误信息是一个包含html标签
# form.errors.get_json_data()：获取到的是一个字典类型的错误信息：将某个字段的名字作为key, 错误信息作为value
# form.as_json(): 将.get_json_data()返回的字典dump成json格式的字符串，方便进行传输
class FormMixin(object):
    # 相当于是除去了code
    def get_errors(self):
        # 判断class中是否有该属性(self中是否有errors属性)
        if hasattr(self,'errors'):
            errors = self.errors.get_json_data()
            # !!! {'username': [{'message': 'Enter a valid URL.', 'code': 'invalid'}]}
            # !!! items->['username',[{'message': 'Enter a valid URL.', 'code': 'invalid'}]]
            # !!! key->'username'
            # !!! message_dicts->[{'message': 'Enter a valid URL.', 'code': 'invalid'}]
            # !!! message->{'message': 'Enter a valid URL.', 'code': 'invalid'}
            # !!! messages->['Enter a valid URL.']
            # !!! {'username':['Enter a valid URL.']}

            # .get_json_data()之后
            # errors={'message':message,'code':code}
            new_errors = {}
            # errors.items=[('message',message),('code',code)]
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            # new_errors={'key':'messages'}
            return new_errors
        else:
            return {}

class HttpCode(object):
    ok = 200
    paramserror = 400
    unauth = 401
    methoderror = 405
    servererror = 500

# {"code":400,"message":"","data":{}}
def result(code=HttpCode.ok,message="",data=None,kwargs=None):
    json_dict = {"code":code,"message":message,"data":data}
    if kwargs and isinstance(kwargs,dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)

def ok(data=None):
    return result(data=data)

def params_error(message="",data=None):
    return result(code=HttpCode.paramserror,message=message,data=data)

def unauth(message="",data=None):
    return result(code=HttpCode.unauth,message=message,data=data)

def method_error(message='',data=None):
    return result(code=HttpCode.methoderror,message=message,data=data)

def server_error(message='',data=None):
    return result(code=HttpCode.servererror,message=message,data=data)

