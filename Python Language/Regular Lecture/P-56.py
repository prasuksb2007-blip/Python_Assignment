class EvenOdd:
    def IsEvenOdd(self,num):
        if(num % 2 ==0):
            print("Number is Even")
        else:
            print("Number is Odd")
obj=EvenOdd()
num1 = int(input("Enter Number:"))
obj.IsEvenOdd(num1)