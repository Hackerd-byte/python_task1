class calculator:
    def getnum(self):
        self.x=float(input("Enter a number1:"))
        self.y=float(input("Enter a number2:"))
    def add(self):
        ans=self.x+self.y
        print(f"Addition of {self.x} and {self.y} is {ans}")
    def sub(self):
        ans=self.x-self.y
        print(f"Subraction of {self.x} and {self.y} is {ans}")
    def multiply(self):
        ans=self.x*self.y
        print(f"Multiplication of {self.x} and {self.y} is {ans}")
    def div(self):
        ans=self.x/self.y
        print(f"Division of {self.x} and {self.y} is {ans}")
calc=calculator()
ch=0
try:
    while ch!=5:
        print("1.Addition\n2.Subraction\n3.Multipication\n4.Division\n5.Exit")
        ch=int(input("Enter your choice:"))
        if (ch==1):
            calc.getnum()
            calc.add()
        elif (ch==2):
            calc.getnum()
            calc.sub()
        elif (ch==3):
            calc.getnum()
            calc.multiply()
        elif (ch==4):
            calc.getnum()
            calc.div()
        elif ch not in (1,2,3,4,5):
            print("Choose 1 to 5")
except ValueError as e:
    print(f"ERROR:{e}")
else:
    print("<<<  Thank you  >>>")