state_list_for_DL=('AP','AR','AS','BR','CG','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LD','MP',\
                   'MH','MN','ML','MZ','NL','OD','PY','PB','RJ','SK','TN','TS','TR','UP','UK','WB',\
                   'AN','CH','DN','DD','LA')

bike_list={'std_bike':['hero splendor','honda shine','pulsar 125','pulsar 150'],\
           'premium_bike':['pulsar ns 200','RE classic 350','himalaya 350','jawa 42','ktm duke'],\
           'scooters':['honda activa','hero pleasure','tvs jupiter','honda dio']}

stocks={"bike":{'std_bike':100,'premium_bike':70,'scooters':150},\
        "car":{'hatchback':50,'sedan':30,'suv':20},\
        'bus':{'seater':{'ac':10,'non_ac':10},'sleeper':{'ac':10,'non_ac':10}}}    

car_list={'hatchback':['ms swift','tata tiago','renault kwid','hyundai i20','ms baleno'],\
           'sedan':['ms dezire','tata tigor','honda city','hyundai verna'],\
           'suv':['hyundai creta','tata nexon','ms brezza','mahindra xuv300']}

bus_list={'seater':['ac','non-ac'],'sleeper':['ac','non-ac']} 
  
stocks={"bike":{'std_bike':100,'premium_bike':70,'scooters':150},\
        "car":{'hatchback':50,'sedan':30,'suv':20},\
        'bus':{'seater':{'ac':10,'non_ac':10},'sleeper':{'ac':10,'non_ac':10}}} 

pricing_list={"bike":{'std_bike':{'hourly': 100, 'daily': 500},'premium_bike':{'hourly': 200, 'daily': 1200},\
                      "scooters":{'hourly': 150, 'daily': 800}},\
              "car":{'hatchback':{'hourly': 300, 'daily': 1500},'sedan':{'hourly': 500, 'daily': 2500},\
                     'suv':{'hourly': 800, 'daily': 5000}},
              "bus":{'seater': {'ac':750, 'non-ac':500},'sleeper': {'ac':1500, 'non-ac':1000}}}


class  VRS_VG01():
    shop_name="VRS Velocity"
    """
    This is the function for rent the vehicles 
    input-customer details
    output-providing the vehicle for customer for the period time"""

    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
        
    def license(self):
        '''
        It checks the driving license entered by the user whether it is valid or not.
        input=It takes only one input as license
        returns=Returns the result either as a valid license or invalid license
        '''
        while True:
            try:
                license=input('enter your driving license: ').upper()
                if (license[0]+license[1]) in state_list_for_DL:
                    print("license is valid")
                    break
            
                else:
                    print("enter a valid driving license")
                    
            except Exception as ex:
                print(f"Error occured because; {ex}.")
               
    
    
    def mobile_no(self):
        '''
        It checks the mobile number entered by the user whether it is valid or not.
        input=It takes only one input as mobile number
        returns=Returns the result either as a correct number or not.
        '''
        while True:
            try:
                mobile=int(input("Enter your number :  +91"))
                
                if len(str(mobile))!=10 or str(mobile).isdigit()==False:
                    print("enter a correct phone number")
                else:
                    
                    break
    
            except ValueError as ve:
                print(f"enter only numbers:{ve}")
            except Exception as ex:
                print(f"something is wrong.please enter the details correctly.{ex}")
            
   
    def email_id(self):
        '''
        It checks the  email id entered by the user whether it is valid or not.
        input=It takes only one input as gmail id
        returns=Returns the result either as a correct gmail id 
        '''
        while True:
            try:
                email=input("enter your mail id: ")
                if email.find('@')==-1:
                    print("Enter a correct email id")
                elif email.endswith("gmail.com")==False:
                    print("Only gmail id will be accepted.Please enter gmail id")
                else:
                    break
            except Exception as ex:
                print(f"Error occured because {ex}.")
        
        
        
    def bike(self):
            option=int(input(":: Select Bike Type ::\n            \n1 --->  std_bike    \n2 --->  premium_bike  \n3 --->  scooters  \n   \n"))
            
            
            if option == 1:
                print("::           Standard Bikes           ::")
                print("**The list of Standard Bikes we have is as follows**")
                print(bike_list['std_bike'])
                click=int(input(f" Enter the following number to select standard bikes\n1 --->  {bike_list['std_bike'][0]}\n2 --->  {bike_list['std_bike'][1]}\n3 --->  {bike_list['std_bike'][2]}\n4 --->  {bike_list['std_bike'][3]}\n \n"))
    
                if click == 1:
                    print(f"Hello {name} the {bike_list['std_bike'][click-1]} is available for you,please follow the process ")
                    
                elif click == 2:
                    print(f"Hello {name} the {bike_list['std_bike'][click-1]} is available for you,please follow the process ")
        
                elif click == 3:
                    print(f"Hello {name} the {bike_list['std_bike'][click-1]} is available for you,please follow the process ")
        
                elif click == 4:
                    print(f"Hello {name} the {bike_list['std_bike'][click-1]} is available for you,please follow the process ")
                else:
                    print("enter a valid option")
                    
                customer.vehicle_charge(1)
            
            if option == 2:
                print("::            Premium Bikes          ::")
                print("**The list of Premium Bikes  we have is as follows**")
                print(bike_list['premium_bike'])
                click=int(input(f" Enter the following number to select premium bikes\n1 --->  {bike_list['premium_bike'][0]}\n2 ---> {bike_list['premium_bike'][1]}\n3 --->  {bike_list['premium_bike'][2]}\n4 --->  {bike_list['premium_bike'][3]}\n5 --->  {bike_list['premium_bike'][4]}\n \n"))
    
                if click == 1:
                    print(f"Hello {name} the  {bike_list['premium_bike'][click-1]} is available for you,please follow the process ")
    
                elif click == 2:
                    print(f"Hello {name} the {bike_list['premium_bike'][click-1]} is available for you,please follow the process ")
        
                elif click == 3:
                    print(f"Hello {name} the {bike_list['premium_bike'][click-1]} is available for you,please follow the process ")
        
                elif click == 4:
                    print(f"Hello {name} the {bike_list['premium_bike'][click-1]} is available for you,please follow the process ")
        
                elif click == 5:
                    print(f"Hello {name} the {bike_list['premium_bike'][click-1]} is available for you,please follow the process ")
                else:
                    print("enter a valid option")
                    
                customer.vehicle_charge(3)
            
        
    
            if option == 3:
                print("::            Scooters            ::")
                print("**The list of Scooters  we have is as follows**")
                print(bike_list['scooters'])
                click=int(input(f" Enter the following number to select scooters\n1 ---> {bike_list['scooters'][0]}\n2 --->  {bike_list['scooters'][1]}\n3 --->  {bike_list['scooters'][2]}\n4 --->  {bike_list['scooters'][3]}\n \n"))
    
            
                if click == 1:
                    print(f"Hello {name} the  {bike_list['scooters'][click-1]} is available for you,please follow the process ")
        
                elif click == 2:
                    print(f"Hello {name} the {bike_list['scooters'][click-1]} is available for you,please follow the process ")
        
                elif click == 3:
                    print(f"Hello {name} the {bike_list['scooters'][click-1]} is available for you,please follow the process ")
        
                elif click == 4:
                    print(f"Hello {name} the {bike_list['scooters'][click-1]} is available for you,please follow the process ")
                else:
                    print("enter a valid option")
                    
                customer.vehicle_charge(2)
            
           
    def last(self,bb):
        if bb == 1:
            print(f" You need to pay 50% in advance \nThe Bike is granted for you & all the best for your trip hope you enjoy it")
        
        if bb == 2:
            print(f" You need to pay 50% in advance \nThe Car is granted for you & all the best for your trip hope you enjoy it")
        
        if bb == 3:
            print(f" You need to pay 50% in advance \nThe Bus is granted for you & all the best for your trip hope you enjoy it")




                    
    def vehicle_charge(self,aa):
        if aa==1:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours bike required"))
                print(f"Charges for this trip is",hour*(pricing_list ["bike"]['std_bike']['hourly']))
                customer.last(1)
                
            elif sellect==2:
                day=int(input(" number of days bike required"))
                print("Charges for this trip is",day*pricing_list["bike"]['std_bike']['daily'])
                customer.last(1) 
            else:
                print("enter a valid option")
                
        if aa==2:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours bike required"))
                print(f"Charges for this trip is",hour*pricing_list ["bike"]['premium_bike']['hourly'])
                customer.last(1)
                
            elif sellect==2:
                day=int(input(" number of days bike required"))
                print("Charges for this trip is",day*pricing_list["bike"]['premium_bike']['daily'])
                customer.last(1) 
            else:
                print("enter a valid option")
                
        if aa==3:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours bike required"))
                print(f"Charges for this trip is",hour*pricing_list ["bike"]["scooters"]['hourly'])
                customer.last(1)
                
            elif sellect==2:
                day=int(input(" number of days bike required"))
                print("Charges for this trip is",day*pricing_list["bike"]["scooters"]['daily'])
                customer.last(1) 
            else:
                print("enter a valid option")
    
        if aa == 4:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours car required"))
                print(f"Charges for this trip is",hour*pricing_list ["car"]['hatchback']['hourly'])
                customer.last(2)
                
            elif sellect==2:
                day=int(input(" number of days car required"))
                print("Charges for this trip is",day*pricing_list["car"]['hatchback']['daily'])
                customer.last(2) 
            else:
                print("enter a valid option")
                
        if aa == 5:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours car required"))
                print(f"Charges for this trip is",hour*pricing_list ["car"]['sedan']['hourly'])
                customer.last(2)
                
            elif sellect==2:
                day=int(input(" number of days  car required"))
                print("Charges for this trip is",day*pricing_list["car"]['sedan']['daily'])
                customer.last(2) 
            else:
                print("enter a valid option")
                
        if aa == 6:
            sellect=int(input("    \n1 ---> for Hourly basis \n2 ---> for Daily basis\n"))
            if sellect==1:
                hour=int(input(" number of hours SUV required"))
                print(f"Charges for this trip is",hour*pricing_list ["car"]['suv']['hourly'])
                customer.last(2)
                
            elif sellect==2:
                day=int(input(" number of days SUV required"))
                print("Charges for this trip is",day*pricing_list["car"]["suv"]['daily'])
                customer.last(2) 
            else:
                print("enter a valid option")
                
        if aa == 7:
            day=int(input(" number of hours Non-Ac Seater Bus required"))
            print("Charges for this trip is",day*pricing_list["bus"]["seater"]['non-ac'])
            customer.last(3)
                
        if aa == 8:
            day=int(input(" number of days Non-Ac Sleeper Bus required"))
            print("Charges for this trip is",day*pricing_list["bus"]["sleeper"]['non-ac'])
            customer.last(3) 

                
        if aa == 9:
            day=int(input(" number of hours Ac Seater Bus required"))
            print("Charges for this trip is",day*pricing_list["bus"]["seater"]['ac'])
            customer.last(3)
                
        if aa == 10:
            day=int(input(" number of days Ac Sleeper Bus required"))
            print("Charges for this trip is",day*pricing_list["bus"]["sleeper"]['ac'])
            customer.last(3)
            
        

                
   
# car_list={'hatchback':['ms swift','tata tiago','renault kwid','hyundai i20','ms baleno'],\
           #'sedan':['ms dezire','tata tigor','honda city','hyundai verna'],\
           #'suv':['hyundai creta','tata nexon','ms brezza','mahindra xuv300']}
        
        
    def car(self):
        option=int(input(":: Sellect Car Type ::\n            \n1 --->  Hatchback    \n2 --->  Sedan  \n3 --->  SUV's  \n   \n"))

        if option == 1:
            print("::           Hatchback           ::")
            print("**The list of Hatchbacks we have is as follows**")
            print(car_list['hatchback'])
            click=int(input(f" Enter the following number to select hatchback cars\n1 --->  {car_list['hatchback'][0]}\n2 --->  {car_list['hatchback'][1]}\n3 --->  {car_list['hatchback'][2]}\n4 --->  {car_list['hatchback'][3]}\n5 --->  {car_list['hatchback'][4]}\n"))
    
            if click == 1:
                print(f"Hello {name}, the {car_list['hatchback'][click-1]} is available for you,please follow the process ")
    
            elif click == 2:
                print(f"Hello {name}, the {car_list['hatchback'][click-1]} is available for you,please follow the process ")
        
            elif click == 3:
                print(f"Hello {name}, the {car_list['hatchback'][click-1]} is available for you,please follow the process ")
        
            elif click == 4:
                print(f"Hello {name}, the {car_list['hatchback'][click-1]} is available for you,please follow the process ")
            elif click == 5:
                print(f"Hello {name}, the {car_list['hatchback'][click-1]} is available for you,please follow the process ")
            else:
                print("enter a valid option")
            customer.vehicle_charge(4)
    
    
    
        if option == 2:
            print("::            Sedan          ::")
            print("**The list of Sedans  we have is as follows**")
            print(car_list['sedan'])
            click=int(input(f" Enter the following number to select sedan cars\n1 --->  {car_list['sedan'][0]}\n2 --->  {car_list['sedan'][1]}\n3 --->  {car_list['sedan'][2]}\n4 --->  {car_list['sedan'][3]}\n  "))
            if click == 1:
                print(f"Hello {name} the  {car_list['sedan'][click-1]} is available for you,please follow the process ")
    
            elif click == 2:
                print(f"Hello {name} the {car_list['sedan'][click-1]} is available for you,please follow the process ")
        
            elif click == 3:
                print(f"Hello {name} the {car_list['sedan'][click-1]} is available for you,please follow the process ")
        
            elif click == 4:
                print(f"Hello {name} the {car_list['sedan'][click-1]} is available for you,please follow the process ")
        
            else:
                print("enter a valid option")
            customer.vehicle_charge(5)
        
    
        if option == 3:
            print("::            SUV            ::")
            print("**The list of SUVs  we have is as follows**")
            print(car_list['suv'])
            click=int(input(f" Enter the following number to select SUVs\n1 --->  {car_list['suv'][0]} \n2 --->  {car_list['suv'][1]}\n3 --->  {car_list['suv'][2]}\n4 --->  {car_list['suv'][3]}\n "))
    
            
            if click == 1:
                print(f"Hello {name} the  {car_list['suv'][click-1]} is available for you,please follow the process ")
    
            elif click == 2:
                print(f"Hello {name} the {car_list['suv'][click-1]} is available for you,please follow the process ")
        
            elif click == 3:
                print(f"Hello {name} the {car_list['suv'][click-1]} is available for you,please follow the process ")
        
            elif click == 4:
                print(f"Hello {name} the {car_list['suv'][click-1]} is available for you,please follow the process ")
            else:
                print(" ")
            customer.vehicle_charge(6)
                
#bus_list={'seater':['ac','non-ac'],'sleeper':['ac','non-ac']}         
    def bus(self):
        
        print("::            BUS            ::")
        print("**The list of BUSs  we have is as follows**")
        print(bus_list)
        option=int(input(" Enter the following number to select buses\n1 --->'Seater Bus' \n2 ---> 'Sleeper Bus'\n"))
        
        if option == 1:
            click=int(input(f" Enter the following number to select Buses\n1 --->  {bus_list['seater'][0]} \n2 --->{bus_list['seater'][1]}\n")) 
            
            if click==1:
                print(f"Hello {name} the  {bus_list['seater'][click-1]} seater bus is available for you,\please follow the process ")
                customer.vehicle_charge(9)
                
            if click==2:
                print(f"Hello {name} the  {bus_list['seater'][click-1]}seater bus is available for you,\please follow the process ")
                customer.vehicle_charge(7)           
                            
        if option == 2:
            click=int(input(f" Enter the following number to select Buses\n1 --->  {bus_list['sleeper'][0]} \n2 --->{bus_list['sleeper'][1]}\n"))
            
            if click==1:
                print(f"Hello {name} the  {bus_list['sleeper'][click-1]} sleeper bus is available for you,\please follow the process ")
                customer.vehicle_charge(10)
                
            if click==2:
                print(f"Hello {name} the  {bus_list['sleeper'][click-1]} sleeper bus is available for you,\please follow the process ")
                customer.vehicle_charge(8)
    
 
            
            
            
    def bill(self):
        pass
        
            
        
   

print("****Welcome to Velocity Vehicle Rental System****")

#user_type=input("Are you a new user ? press 'y' for YES and 'n' for NO: ").lower()
#if user_type=="y":
print("**Please enter the following details**")
name=input('enter your name: ').title()

while True:
    age=int(input('enter your age: '))
    if age<18  :
        print("Sorry sir you cannot avail our services as you are below 18.")
    elif age > 60:
        print("Sorry sir, you cannot avai our services as you are above 60")
    else:
        break
customer=VRS_VG01(name,age)    
customer.mobile_no()    
customer.email_id()
customer.license()
        
choice=int(input(":: Select Vehicle Type ::\n1 --->  BIKE    \n2 --->  CAR  \n3 --->  BUS  \n   \n"))
if choice==1:
    customer.bike()
    
        
elif choice==2:
    customer.car()
    
    
elif choice==3:
    customer.bus()
    
else:
    print("**Please enter a correct choice**")
    