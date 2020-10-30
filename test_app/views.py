from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from test_app.models import User
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):

    def get(self, request, *args, **kwargs):
        """
        查询 单个/多个 用户接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        user_id = request.GET.get('id')
        print(user_id)
        if user_id:
            user = User.objects.filter(pk=user_id,user_flag=1).values("username","gender").first()
            print(user)
            if user:
                return JsonResponse({ # json dumps
                    "code":200,
                    "message":"查询单个用户成功",
                    "result":user
                })
        else:
            # 如果用户id不存在，查询所有用户
            users = User.objects.all().values("username","gender")
            if users:
                return JsonResponse({
                    "code":200,
                    "message":"查询所有用户成功",
                    "result": list(users)
                })

        return JsonResponse({
            "code":400,
            "message":"查询用户失败",
            "result":""
        })

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        gender = request.POST.get("gender",1)
        print(username, pwd,gender)
        if User.objects.filter(username=username, user_flag=1).first():
            return JsonResponse({
                "code": 400,
                "message": "新增失败"
            })
        else:
            try:
                user = User.objects.create(username=username,
                                           password=pwd, gender=gender)
                return JsonResponse({
                    "code":200,
                    "message":"新增单个用户成功",
                    "result":{"usernmae":user.username, "gender":user.gender}
                })
            except Exception as e:
                print(e)
                return JsonResponse({
                    "code":400,
                    "message":"新增失败"
                })


    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.filter(pk=user_id).first()
        if user_id:
            User.objects.filter(pk=user_id).update(user_flag=0)
            return JsonResponse({
                "code":200,
                "message":"删除成功"
            })
        else:
            return JsonResponse({
                "code":400,
                "message":"删除失败"
            })


