"""
Created bt tz on 2020/10/29 
"""

__author__ = 'tz'

from rest_framework import serializers

from model_s.models import Book, Press, User


class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ("press_name", "pic", "address")





class BookDeModelSerializer(serializers.ModelSerializer):
    """反序列化器"""

    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors")

        # 添加DRF提供的默认校验规则
        extra_kwargs = {
            "book_name": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                "error_messages": {
                    "required": "图书名必须提供",
                    "min_length": "图书名不能少于两个字符",
                }
            },
        }

    def validate(self, attrs):
        print(attrs)
        return attrs

    def validate_book_name(self, obj):
        print(obj)
        return obj


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")

        # 添加DRF提供的默认校验规则
        extra_kwargs = {
            "username": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名不能少于两个字符",
                }
            },
            "password": {
                "required": True,  # 必填字段
                "min_length": 8,  # 最小长度
                "error_messages": {
                    "required": "密码不能为空",
                    "min_length": "密码不能少于八个字符",
                }
            },
        }

    def validate(self, attrs):
        print(attrs)
        return attrs


class BookListSerializer(serializers.ListSerializer):
    """
    使用此序列化器完成更新多个对象
    """

    # 重写update方法完成更新
    def update(self, instance, validated_data):
        print(instance)  # 要修改的实例
        print(validated_data)  # 要修改的实例的值
        print(self.child)  # 调用逻辑的序列化器类-->BookModelSerializerV2

        # TODO 将修改多个  改变成循环中每次修改一个
        for index, obj in enumerate(instance):
            # 每遍历一次  就修改一个对象的数据
            print(self.child)
            self.child.update(obj, validated_data[index])

        return instance


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields应该写哪些字段  应该填写序列化与反序列化所需字段的并集
        fields = ("book_name", "price", "publish", "authors", "pic")
        list_serializer_class = BookListSerializer
        extra_kwargs = {
            "book_name": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                "error_messages": {
                    "required": "图书名必须提供",
                    "min_length": "图书名不能少于两个字符",
                }
            },
            # 指定某个字段只参与序列化
            "pic": {
                "read_only": True
            },
            # 指定某个字段只参与反序列化
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
        }

    def validate(self, attrs):
        # print(attrs)
        # print('validate',attrs)
        return attrs

    def validate_book_name(self, obj):
        # print(obj)
        # print('validate book name',obj)
        return obj
