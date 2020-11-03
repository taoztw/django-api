"""
Created bt tz on 2020/11/2 
"""

__author__ = 'tz'


class A:   # APIView
    def __init__(self):
        pass
    def p(self):
        print('我是A')
class B(A):
    def __init__(self):
        pass

    def p(self):
        print('B重写A')
class C(A):
    def __init__(self):
        pass
    def p(self):
        print('C重写A')

class D(C,B):
    # def __init__(self):
    #     pass
    def __init__(self):
        super().__init__()

D().p()