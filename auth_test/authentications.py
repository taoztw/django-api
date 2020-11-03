from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from api.models import User

"""
1. 继承BaseAuthentication类
2. 重写authenticate方法
3. 自定义认证规则
    没有认证信息返回None (游客)
    有认证信息但不符合要求 (非法)
    有认证信息且认证成功  返回认证用户与信息 返回的格式一定是元祖 (合法用户)
"""


class MyAuth(BaseAuthentication):
    """
    前端发送请求必须携带 认证信息  需要按照一定的格式来
    默认使用Authorization来携带认证信息
    认证信息都包含在 request.META中
    """

    def authenticate(self, request):
        # 获取认证信息
        auth = request.META.get('HTTP_AUTHORIZATION', None)

        if auth is None:
            # 代表游客
            return None

        # 设置认证信息的校验规则  "auth 认证信息"
        auth_split = auth.split()

        # 校验规则
        if not (len(auth_split) == 2 and auth_split[0].lower() == "auth"):
            raise exceptions.AuthenticationFailed("认证信息有误，认证失败")

        # 如果认证成功，开始解析用户  规定用户信息必须是 abc.admin.123
        if auth_split[1] != "abc.admin.123":
            raise exceptions.AuthenticationFailed("用户信息认证失败")

        # 校验数据库是否存在此用户
        user = User.objects.filter(username="admin").first()

        if not user:
            raise exceptions.AuthenticationFailed("用户不存在或者已删除")

        return user, None
