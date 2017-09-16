class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self, *amounts):
        for amount in amounts:
            self.result += amount
            return self

    # def subtract(self, amount2):
    #     self.result -= amount2
    #     return self

md = MathDojo()

print (md.add(0,2).add(2,5).add(3,2).result)
