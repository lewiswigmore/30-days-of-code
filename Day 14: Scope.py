class Difference:
    def __init__(self, a):
        # Initialize the elements with the input list 'a'.
        self.__elements = a

    def computeDifference(self):
        # Calculate the maximum difference between elements.
        self.maximumDifference = max(self.__elements) - min(self.__elements)
        return self.maximumDifference

_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
