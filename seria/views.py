from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
from rest_framework.views import APIView
from seria.models import Teacher
from rest_framework.response import Response
from seria.serializers import TeacherSerializer,TeacherDeSerializer


@method_decorator(csrf_exempt, name="dispatch")
class TercherView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询 单个/多个 用户接口
        """
        user_id = kwargs.get("id")
        # print(user_id)
        # print(request.data) QueryDict
        if user_id:
            user = Teacher.objects.get(pk=user_id,user_flag=1)
            # print('无序列化测试',user)
            teacher_serializer = TeacherSerializer(user).data

            return Response({ # json dumps
                "code":200,
                "message":"查询单个用户成功",
                "result":teacher_serializer
            })
        else:
            # 如果用户id不存在，查询所有用户
            # users = Teacher.objects.all().values("username","gender")
            users = Teacher.objects.all()
            teachers_serializer = TeacherSerializer(users, many=True).data
            if users:
                return Response({
                    "code":200,
                    "message":"查询所有用户成功",
                    "result": teachers_serializer
                })

        return Response({
            "code":400,
            "message":"查询用户失败",
        })

    def post(self, request, *args, **kwargs):

        request_data = request.data
        # 判断参数格式是否合法
        if not isinstance(request_data, dict) or request_data=={}:
            return Response({
            "code":400,
            "message":"参数有误",
            })
        # 使用反序列化器完成数据库的反序列化
        print(request_data.get('username'))
        s = TeacherDeSerializer(data=request_data)
        if not Teacher.objects.filter(username=request_data.get('username'), user_flag=1).first() and s.is_valid():
            teacher = s.save()
            print(teacher)
            return Response({
                "code": 200,
                "message": "新增成功",
                "result": TeacherSerializer(teacher).data
            })
        else:
            return Response({
                "code": 400,
                "message": "新增失败",
            })


    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = Teacher.objects.filter(pk=user_id).first()
        if user_id:
            Teacher.objects.filter(pk=user_id).update(user_flag=0)
            return Response({
                "code":200,
                "message":"删除成功"
            })
        else:
            return Response({
                "code":400,
                "message":"删除失败"
            })