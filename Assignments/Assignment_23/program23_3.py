# 3. Write a Python program to implement a class named Numbers with the following specifications:
#   -> The class should contain one instance variable 
#       -> Value
#   -> Define a constructor init that accepts a number from the user and initializes Value.
#   -> Implement the following instance methods
#       -> ChkPrime()returns True if the number is prime, otherwise returns False
#       -> ChkPerfect()returns True if the number is perfect, otherwise returns False
#       -> Factors()-displaya all factors of the number
#       -> SumFactors()returns the sum of all factors
#       (You may use this method as a helper in ChkPerfect() if required)
#   -> Create multiple objects and call all methods

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter the number : "))

    def ChkPrime(self):
        Flag = True
        NoHalf = int(self.Value/2)

        for i in range(2, NoHalf+1):
            if(self.Value % i == 0):
                Flag = False
                break

        return Flag
        
    def Factors(self):
        NoHalf = int(self.Value/2)

        for i in range(1, NoHalf+1):
            if(self.Value % i == 0):
                print(i)

    def SumFactors(self):
        Sum = 0
        NoHalf = int(self.Value/2)

        for i in range(1, NoHalf+1):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum

    def ChkPerfect(self):
        if(self.SumFactors() == self.Value):
            return True
        else:
            return False
        
def main():

    print("Initialized Constructor for obj1 :-")
    obj1 = Numbers()
    if(obj1.ChkPrime()):
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")

    print("Factors of the numbers are : ")
    obj1.Factors()

    print("Addition of factors are :", obj1.SumFactors())

    if(obj1.ChkPerfect()):
        print("It is perfect Number")
    else:
        print("It is not a perfect Number")

    print()

    print("Initialized Constructor for obj2 :-")
    obj2 = Numbers()
    if(obj2.ChkPrime()):
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")

    print("Factors of the numbers are : ")
    obj2.Factors()

    print("Addition of factors are :", obj2.SumFactors())

    if(obj2.ChkPerfect()):
        print("It is perfect Number")
    else:
        print("It is not a perfect Number")

    print()

        
    print("Initialized Constructor for obj3 :-")
    obj3 = Numbers()
    if(obj3.ChkPrime()):
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")

    print("Factors of the numbers are : ")
    obj3.Factors()

    print("Addition of factors are :", obj3.SumFactors())

    if(obj3.ChkPerfect()):
        print("It is perfect Number")
    else:
        print("It is not a perfect Number")

    print()

if __name__ == "__main__":
    main()
        


