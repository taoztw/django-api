from rest_framework.throttling import SimpleRateThrottle


class SendMessageRate(SimpleRateThrottle):
    scope = "anon"

    # 只对包含手机号的请求做验证
    def get_cache_key(self, request, view):
        phone = request.query_params.get("phone")

        if not phone:
            return None

        # 返回数据 根据手机号动态展示返回的值
        return phone
