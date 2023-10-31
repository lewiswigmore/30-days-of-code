# Define a class for a Person.
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

# Define a class for a Student, which inherits from Person.
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        # Calculate the average score.
        score = sum(self.scores) / len(self.scores)
        
        # Determine the grade based on the score.
        if score >= 90:
            return "O"  # Outstanding
        elif score >= 80:
            return "E"  # Excellent
        elif score >= 70:
            return "A"  # Acceptable
        elif score >= 55:
            return "P"  # Poor
        elif score >= 40:
            return "D"  # Dismal
        else:
            return "T"  # Troll

# Read input for the student.
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # The number of scores (not needed for Python)
scores = list(map(int, input().split()))

# Create a Student object and calculate the grade.
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
