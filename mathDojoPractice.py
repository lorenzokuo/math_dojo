# first attempt
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0

#     def add(self, *num):
#         for i in num:
#             self.result += i
#             print("+"+ str(i))
#         return self

#     def subtract(self, *num):
#         for i in num:
#             self.result -= i
#             print("-"+ str(i))
#         return self

# md = MathDojo()
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)

# second attempt
# creat checking if the number is tuple or list
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *num):
        for i in num:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result += j
            else:
                self.result += i
        return self

    def subtract(self, *num):
        for i in num:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result -= i
            else:
                self.result -= i
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)