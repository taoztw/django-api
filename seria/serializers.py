"""
Created bt tz on 2020/10/28 
"""

__author__ = 'tz'

from rest_framework import serializers
from seria.models import Teacher

class TeacherSerializer(serializers.Serializer):

    username = serializers.CharField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()

    # 自定义序列化器
    phone = serializers.SerializerMethodField()
    def get_phone(self, obj):
        print('自定义序列化器输出')
        return obj.phone

class TeacherDeSerializer(serializers.Serializer):
    # 对前端参数进行校验
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=64)
    # phone = models.CharField(max_length=11, null=True, blank=True)


    username = serializers.CharField(
        max_length=10,
        min_length=1,
        error_messages={
            "max_length":"长度太短了",
            "min_length":"长度太长了"
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()

    # 重写create方法
    def create(self, validated_data):
        print(self)
        print(validated_data)
        return Teacher.objects.create(**validated_data)