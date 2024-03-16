# class f15:
#     def light(self,color):
#         print("The color of light",color)
#     def fan(self,speed):
#         self.s=speed
#         print("The regulator speed is",speed)
#     def ac(self,tempin,tempout):
#         self.tin=tempin
#         self.tout=tempout
#         print("The inside temparature",tempin)
#         print("The outside temparature",tempout)
#     def diff(self):
#         difference=self.tout-self.tin
#         print(difference)
#         print(self.s)
# obj=f15()
# obj.light("blue")
# obj.fan(4)
# obj.ac(16,32)
# obj.diff()

# class f15:
#     ##constructor
#     def __init__(self):
#         print("The number of placements this year is 659 and still counting.......")
#         a=10
#         b=12.3
#         print(a*b)
#     def light(mani,color):
#         print("The color of light",color)
#     def fan(mani,speed):
#         mani.s=speed
#         print("The regulator speed is",speed)
#     def ac(mani,tempin,tempout):
#         mani.tin=tempin
#         mani.tout=tempout
#         print("The inside temparature",tempin)
#         print("The outside temparature",tempout)
#     def diff(mani):
#         difference=mani.tout-mani.tin
#         print(difference)
#         print(mani.s)
# obj=f15()
# obj.light("blue")
# obj.fan(4)
# obj.ac(16,32)
# obj.diff()

# ##parameterized constructor
# class project:
#     def __init__(self,a,b):
#         print("The number of placements this year is 659 and still counting.......")
#         print(a*b)
# obj=project(4,5)


# class f15:
# #     ##constructor
#     def __init__(mani,a,b,st,endt):
#         print("The number of placements this year is 659 and still counting.......")
#         print(a*b)
#         print("The start time is :",st)
#         print("The ending time is :",endt)
#     def light(mani,color):
#         print("The color of light",color)
#     def fan(mani,speed):
#         mani.s=speed
#         print("The regulator speed is",speed)
#     def ac(mani,tempin,tempout):
#         mani.tin=tempin
#         mani.tout=tempout
#         print("The inside temparature",tempin)
#         print("The outside temparature",tempout)
#     def diff(mani):
#         difference=mani.tout-mani.tin
#         print(difference)
#         print(mani.s)
# obj=f15(4,5,9,4)
# obj.light("blue")
# obj.fan(4)
# obj.ac(16,32)
# obj.diff()

# class showroom:
#     def ask(self,Tayota,Mercides,Mahindra):
#         print("Available car companies :")
#         print("Tayota")
#         print("Mercides")
#         print("Mahindra")
#         a=input("Enter which car company do you want :")
#         if(a==Tayota):
#             print(".....WELCOME TO TAYOTA FAMILY....")
#         elif(a==Mercides):
#             print(".....WELCOME TO MERCIDES FAMILY.....")
#         elif(a==Mahindra):
#             print(".....WELCOME TO MAHINDRA FAMILY....")
#     def varient(self):
        
# obj=showroom()
# obj.ask('Tayota','Mercides','Mahindra')


# class faculty:
#     def __init__(self,f_name,department,f_id):
#         self.f_name=f_name
#         self.department=department
#         self.f_id=f_id
#     def print_info(self):
#         print("faculty information=",self.f_name,self.department,self.f_id)
# obj=faculty("ashish","CSE",10001)
# obj.print_info()
# class cse(faculty):
#     pass
# obj=cse("Jyothi","CSE",10002)
# obj.print_info()


##create a class of name placements which has a function info which displays we have 623 selects and still counting.
##create another class name department when function display which  will display the names of departments present in the college.
##create a class pragati with a function welcome which displays the message welcome to pragati eengineering .pragati class should also display  the details about departments and placements


##Multiple Inheritence
# class placemnts:
#     def info(self):
#         print("We have 623 selects in placements and still counting.....")
# class department():
#     def display(self):
#         print("The departments present in our college are...")
#         print( "CSE\nIT\nCIVIL\nEEE\nECE\nMECHANICAL")
# class pragati(department,placemnts):
#     def welcome(self):
#         print("Welcome to pragati engineering college..")
# obj=pragati()
# obj.welcome()
# obj.display()
# obj.info()

##multi level inheritance
# class placemnts:
#     def info(self):
#         print("We have 623 selects in placements and still counting.....")
# class department(placemnts):
#     def display(self):
#         print("The departments present in our college are...")
#         print( "CSE\nIT\nCIVIL\nEEE\nECE\nMECHANICAL")
# class pragati(department):
#     def welcome(self):
#         print("Welcome to pragati engineering college..")
# obj=pragati()
# obj.welcome()
# obj.display()
# obj.info()

##FUNCTION OVERLOADING  IS NOT ALLOWED IN PYTHON ,IF HAVE MULTIPLE SAME FUNCTIONS THE LAST FUNCTION ONLY EXECUTED
##FUNCTION OVERLOADING EXAMPLE

# class Arthemetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Arthemetic()
# # obj.add(10)
# # obj.add(10,20)
# obj.add(1,2,3)

##function overriding
# class Father:
#     def bike(self):
#         print("HARLY DAVIDSON")
#     def laptop(self):
#         print("Laptop with 2GB ram and 500GB processor")
# class Mani(Father):
#     def laptop(self):
#         print("As per my programming software required the laptop so...")
#         print("laptop with 8GB RAM and 1TB HDD I7 also needed")
# obj=Mani()
# obj.bike()
# obj.laptop()

##create a class ticket which will be the abstract class inside that create a function bookticket which will be the abstract method and has nothing in it.
##create a class makemytrip which will use the book ticket function from ticket class to take the details such as name,phone no,email id,journey date and displays a mesage safe thank you for bokking from makemytrip.
##create a class irctc which uses the book ticket of ticket class and takes the same datails as makemytrip but in the end it will give an option to user to selsect wheather it is one way or round trip.if the user option is round trip it again asks the user to enter the return date as well and then prints a message thank you for choosing else print thankyou for choosing irctc
##create a class indigo which takes all the datails like irctc and just asks which mode of transport you want want to go train or bus or flight.and displays thank you for choosing indigo

# from abc import ABC,abstractmethod
# class Ticket(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass
# class Makemytrip(Ticket):
#     def bookticket(self):
#         name=input("Enter passenger name :")
#         phone=input("Enter phone number :")
#         email=input("Enter Email Id :")
#         journeydate=input("Enter journey Date :")
#         print("HAVE A SAFE JOURNEY \n THANKYOU FOR BOOKING MAKE MY TRIP")
# class Irctc(Makemytrip):
#     def bookticket(self):
#     # name=input("Enter passenger name :")
#     # phone=input("Enter phone number :")
#     # email=input("Enter Email Id :")
#     # journeydate=input("Enter journey Date :")
#         a=input("Enter wheather you want oneway service or roundway service :")
#         if(a=="roundway"):
#             b=input("Enter Return date journey :")
#             print("Thankyou for choosing us")
#         else:
#             print("Thankyoou for choosing IRCTC")
# class Indigo(Irctc):
#     def bookticket(self):
#         # name=input("Enter passenger name :")
#         # phone=input("Enter phone number :")
#         # email=input("Enter Email Id :")
#         # journeydate=input("Enter journey Date :")
#         c=input("Enter which type of transport do you want Train or Bus or Flight :")
#         print("Thank you for choosing Indigo")
# obj=Indigo()
# obj.bookticket()

##create an atm system
##1.display the remaining amount in the atm
##2.authentication of user.authenticate using username and password.if the user is authenticated then give him the following options to choose 1.check balance2.cash withdrawl 3.cash deposit
##3.Mini statement of the last three transactions
##4.card renewal provide an


import csv
f=open("Student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentID","Rollno","Name","phonenumber"])
StudentID=input("Enter student ID :")
Rollno=int(input("Enter Roll No :"))
Name=input("Enter Student Name :")
Phonenumber=int(input("Enter Phone Number :"))
a.writerow([StudentID,Rollno,Name,Phonenumber])
