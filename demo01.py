class demo():
    a=1

    @classmethod
    def clsdemo(cls):
        print("我是cls，a的值是:",demo.a)

    def __init__(self,b):
        self.b=b

    def demo01(self):
        print(demo.a)
        demo.clsdemo()
        self.clsdemo()  #实例方法中可以直接调用类方法


de=demo("3")
de.demo01()