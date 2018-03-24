class A:
    def __init__(self):
        print('Constructing A')

    @staticmethod
    def myA():
        print("I'm Aay")


class B:
    def __init__(self):
        print('Constructing B')

    @staticmethod
    def myB():
        print("I'm Bee")


class C (B, A):
    def __init__(self):
        super().__init__()
        print('Constructing C')

    def myAB(self):
        A.myA()  # can use self.myA()
        B.myB()

# Sample Run

c = C()
c.myAB()

# Method Resolution Order:

print(C.__mro__)



