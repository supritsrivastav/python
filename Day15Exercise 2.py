# Creating a Greeting for the teacher using Time Modules for theDifferent Different Time Zones.
# ismehmm import time se time module import kiya time module built in hota hai
# isseliye ye aaram se import ho jata hai hme PIP(Pacakge Manager for python) ki
# jarurat nhi padti hai function aaram se import ho jaati hai ...
# strf ek function hai ho hme hour hand and minute hand provide karta hai


# ACTUAL SOLUTION 
import time    
name=input("Enter Your Name:")
recenttime = time.strftime('%H:%M:%S') 
Recenttime = int(time.strftime('%H'))       
c= name.capitalize()                                
if(4<=Recenttime<12):                        
    print('GOOD MORNING' ,c,'its',recenttime)                           
elif(12>=Recenttime<17):                                             
    print('GOOD EVENING',c,'its',recenttime)        
else:                                              
      print('GOOD NIGHT',c,'its',recenttime)   
                                             
# print('Hii',name,'its',recenttime)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59


                        