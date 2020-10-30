"""
Created bt tz on 2020/10/29 
"""

__author__ = 'tz'

from rest_framework import serializers

from model_s.models import Book, Press


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


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields应该写哪些字段  应该填写序列化与反序列化所需字段的并集
        fields = ("book_name", "price", "publish", "authors", "pic")

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
        return attrs

    def validate_book_name(self, obj):
        # print(obj)
        return obj

    # def update(self, instance, validated_data):
    #     book_name = validated_data.get("book_name")
    #     instance.book_name = book_name
    #     instance.save()
    #     return instance