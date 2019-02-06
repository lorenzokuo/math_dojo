class MathDojo(object):
    # Attribute
    def __init__(self):
        self.result = 0
    # Methods
    def add(self, *num):
        for i in num:
            self.result += i
            print("+"+ str(i))
        return self
    def subtract(self, *num):
        for i in num:
            self.result -= i
            print("-"+ str(i))
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)