'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
n=int(input("Enter the date: " ))
n1=int(input("Enter the year: " ))
n4=input("Enter Month: " )
lst=n1%100
qu=lst//4 
if(n4=="jan"):
    mcode=1 
elif(n4=="feb"):
    mcode=4 
elif(n4=="march"):
    mcode=4 
elif(n4=="april"):
    mcode=0 
elif(n4=="may"):
    mode=2 
elif(n4=="jun"):
    mcode=5
elif(n4=="jul"):
    mcode=0 
elif(n4=="aug"):
    mcode=3 
elif(n4=="sept"):
    mcode=6 
elif(n4=="oct"):
    mcode=1 
elif(n4=="nov"):
    mcode=4 
elif(n4=="dec"):
    mcode=6 
else:
    pass
if n1 in range(1500,1599+1):
    ycode=0
elif n1 in range(1600,1699+1):
    ycode=6 
elif n1 in range(1700,1799+1):
    ycode=4 
elif n1 in range(1800,1899+1):
    ycode=2  
elif n1 in range(1900,1999+1):
    ycode=0 
elif n1 in range(2000,2099+1):
    ycode=6 
else:
    pass

res=n+lst+qu+mcode+ycode
fires=res%7 
if fires==1:
    print("sunday")
elif(fires==2):
    print("monday")
elif(fires==3):
    print("tues")
elif(fires==4):
    print("wednesday")
elif(fires==5):
    print("thus")
elif(fires==6):
    print("fri")
elif(fires==7 or fires==0):
    print("sat")
else:
    pass


