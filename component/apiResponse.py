# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/21 14:43
@Auth ： magician
@Desc ：封装响应数据
"""

from django.http import JsonResponse
from ARTDjango.settings import  CODE_MESSAGE

class apiResponse():

    @staticmethod
    # 前面参数有默认值，后面也要有
    def success(code=200,data=None):
        # data为空时
        if not data:
            data = dict()
        returnData = dict()
        returnData['code'] = 200
        returnData['message'] = CODE_MESSAGE[str(code)]
        returnData['data'] = data
        return JsonResponse(returnData)

    @staticmethod
    def fail(code):
        returnData = dict()
        if code == 201 or code == 404 or code ==500 or code == 400:
            returnData['code'] = code
            returnData['message'] = CODE_MESSAGE[str(code)]
            returnData['data'] = {}
            return JsonResponse(returnData)
        else:
            returnData['code'] = "unknow"
            returnData['message'] = "bad request"
            returnData['data'] = {}
            return JsonResponse(returnData)

