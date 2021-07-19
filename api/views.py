from rest_framework.views import APIView
import json
from rest_framework import status

# 注册登录
from TestServer.base.JsonResponse import JsonResponse
from TestServer.base.constant import miss_required_para, user_already, user_create_success, success_msg
from api.models import Banner, User
from api.serializers import BannerSerializer, UserSerializer


class LoingRegister(APIView):
    def post(self, request):
        try:
            req = json.loads(request.body)
        except:
            req = json.dumps(request.POST)
            req = json.loads(req)

        try:
            secret = req["secret"]
            username = req["username"]
            avatar = req["avatar"]
        except:
            return JsonResponse(code=status.HTTP_404_NOT_FOUND, msg=miss_required_para, data={})
        else:
            user = User.objects.filter(secret=secret)
            if user.exists():  # 用户已存在
                msg = user_already
                user = User.objects.get(secret=secret)
            else:  # 创建用户
                msg = user_create_success
                user = User.objects.create(secret=secret, username=username, avatar=avatar)
            u = UserSerializer(instance=user)
            return JsonResponse(code=status.HTTP_200_OK, msg=msg, data=u.data)


# banner列表数据，数据较少不需要分页
class BannerList(APIView):

    def get(self, request):
        queryset = Banner.objects.all()
        b = BannerSerializer(instance=queryset, many=True)
        return JsonResponse(code=status.HTTP_200_OK, msg=success_msg, data=b.data)
