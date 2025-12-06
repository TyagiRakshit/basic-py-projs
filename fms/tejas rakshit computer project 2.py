import mysql.connector as mc
mdb=mc.connect(host='localhost',user='root',passwd='1234',database='fms')
mcur=mdb.cursor()
if mdb.is_connected():
    print("Connected")
else:
 print("nc")
def createtable():
 q1 = create table if not exists passengers(Name varchar(20),Age int, Seat _ no int PRIMARY KEY,Destination varchar(20),No_bag char(l ),Wt_lug char(2))
 mcur.execute(ql)
 q2 ="create table if not exists flights (Starting _from varchar(20),Going_to varchar(20),Takeoffdate datetime,Land_date datetime,Type varchar(13))"
 mcur.execute(q2)
 q3="create table if not exists Cake (Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))"
 mcur.execute(q3)
 q4="create table if not exists Mocktail(Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))"
 mcur.execute(q4)
 q5="create table if not exists Coffee(Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))"
 mcur.execute(q5)
 q6="create table if not exists Tea(Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))"
 mcur.execute(q6)
 q7="create table if not exists Meal(Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))"
 mcur.execute(q7)
 q8="create table if not exists Snacks(Srno int(2) PRIMARY KEY, Type varchar(15), Price varchar(3))" mcur.execute(q8) q13="create table if not exists forder(Srno int(2) PRIMARY KEY, Name varchar(20), Item varchar(15))" mcur.execute(q13) print("Tables created sucessfully")
def addpassenger():
 name=input("Enter passenger's name :: :") 
 age=input("Enter age :: ")
 seat_no=int(input("Enter alloted seat number :: ")) 
 destination=input("Enter destination :: ")
 wtallowed=5
  nobag=int(input("Enter number of bags :: ")) 
 wtbag=int(input("Enter weight of luggage (kg) :: ")) 
 if wtbag<wtallowed:
                 print("Passed")
 else:
  print("Your luggage is over weight")
  q9="insert into passengers value('{}',{},{})".format(name,age,seat_no,destination,n obag,wtbag)
  mcur.execute(q9)
  mdb.commit()
  print("executed")
  def food():
  print("l .Cake")
  print("2.Mocktail")
  print("3.Coffee")
  print("4.Tea")
  print("5.Meal")
  print("6.Snacks")
  choice=int(input("Enter your choice :: ")) 
if choice==l :
  q 10="Select * from cake"
  mcu r.execute(q 10) dl
  print(dl)
elif choice==2:
  q11 ="Select * from Mocktail"
  mcur.execute(ql1)
  d2=mcur.fetchall()
  print(d2)
elif choice==3:
  q12="Select * from Coffee"
  mcu r.execute(q12)
  d3=mcur.fetchall()
  print(d3)
  elif choice==4:
      q * from Tea"
      mcur.execute(q13)
      d4=mcur.fetchall()
      print(d4)
elif choice==5:
  q14="Select * from Meal" mcu r.execute(q 14) d5=mcur.fetchall() print(d5) elif choice==3:
  q12="Select * from Snacks" mcu r.execute(q 1 2) d6=mcur.fetchall() print(d6) else:
  print("You entered invalid choice
#noitem=input("Enter no of food items : :
while True:
#name=input("Enter your name : :  srno=int(input("Enter srno : : ")) name=input("Enter your name : : ") item=input("Enter order : :  q 15="insert into forder value({},'{}','{}')".format(srno,name,item) mcu r.execute(q 1 5) mdb.commit() print("Ordered") c=input("Do you want to order more (y/
if  continue else:
break
def avail_flights():
 q16="select Starting _ from, Going _ to from flights"
 mcur.execute(q16)
 d7=mcur.fetchall()
 print("From ---> To")
 print(d7)
def display _ passengers():
 q17="select * from passengers"
 mcur.execute(q17)
 d8=mcur.fetchall()
 print(d8)
def passengers_goingto():
 q18=" select Name, Destination from passengers order by Destination"
 mcur.execute(q18)
 d9=mcur.fetchall()
 print(d9)
 
createtable()
while True:
 print("l .add passenger")
 print("2.flights available")
 print("3.To display all passengers")
 print("4.passengers going to common place")
 print("5.food ordering")
 print("6.Exit")
 print("")
 ch=int(input("Enter your choice :: ")) 
 if ch==l :
   addpassenger()
 elif ch==2:
     avail_flights()
 elif ch==3:
  display _ passengers()
 elif ch==4:
  passengers_goingto()
 elif ch==5:
     food()
 elif ch==6:
  c=input("Do you want to exit (y/n)::")
 if c=='y':
  print("Thanks for visting..")
        break
  else:
   continue
else:
 print("lnvalid Choice")
 break
#create table flight(From varchar(20),To varchar(20));
#insert into passengers  
