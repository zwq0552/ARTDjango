from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt
import json
from loguru import logger
# 自定义封装类
from .apiResponse import *

@csrf_exempt
def testApiResponse(request):

    '''
    json.dumps(): 对数据进行编码。将字典转成json
    json.loads(): 对数据进行解码。将json转成字典
    :desc: 测试封装类以及post数据读取
    :param request:
    :return: apiResponse
    '''
    
    if request.method != "POST":
        return apiResponse.fail(400)


    requestInfo = json.loads(request.body)
    if len(requestInfo) == 0:
        logger.error("请求数据为空")
        return apiResponse.fail(405)

    username = requestInfo['username']
    if username != None or username != "":

        logger.info(username + "开始登录。。")
        if username == 'admin':
            data = {"username":"admin"}
            return apiResponse.success(200,data)
        else:
            return apiResponse.fail(201)
    else:
        return apiResponse.fail(405)
