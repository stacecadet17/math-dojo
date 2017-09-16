class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self, *amounts):
        for amount in amounts:
            if isinstance(amount, list):
                for smallamount in amount:
                    self.result += smallamount
            else:
                self.result += amount
        return self

    def subtract(self, *numbers):
        for number in numbers:
            if isinstance(number, list):
                for num in number:
                    self.result -= num
            else:
                self.result -= number
        return self

md = MathDojo()

print (md.add(0,2).add(2,5).add(3,2).subtract(2,2).result)
print(md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result)
