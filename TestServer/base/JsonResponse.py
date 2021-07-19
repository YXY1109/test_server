# -*-coding:utf-8-*-
__author__ = 'YXY'
__date__ = '2020/12/19 16:58'

from rest_framework.response import Response


class JsonResponse(Response):
    def __init__(self, code=1, msg="Success", data="", status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super(JsonResponse, self).__init__(data, status, template_name, headers,
                                           exception, content_type)

        self.data = {"code": code, "msg": msg, "data": data}
