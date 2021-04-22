from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import User
import json
from django.http import JsonResponse
import hashlib
import requests
from django_redis import get_redis_connection
from idea_community_back_ends import settings

def login(request):
    appid='1'
    secret='1'
    request.params = json.loads(request.body)
    if not request.params['code'] or not request.params['nickname']:
        return JsonResponse({'ret':1,
                             'msg':'缺少参数'})
    js_code=request.params['code']
    nickname=request.params['nickname']
    print(js_code)
    url='https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid + '&secret=' + secret + '&js_code=' + js_code + '&grant_type=authorization_code'
    response=json.loads(requests.get(url).content)
    if 'errcode' in response:
        return JsonResponse({'ret':1,
                             'msg':response['errmsg']})
    open= response['openid']
    session_key=response['session_key']

    '''
    open='???????'
    session_key='session_key'
    '''
    user,created=User.objects.get_or_create(openid=open)
    sha=hashlib.sha1()
    sha.update(open.encode())
    sha.update(session_key.encode())
    digset = sha.hexdigest();
    settings.r.set(digset,nickname,ex=2*60*60)
    print(settings.r.get(digset))
    return JsonResponse({'ret':0,
                         'msg':'ok',
                         'data':digset
                         })


