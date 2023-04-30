#************************************************************************
# * Name: Elvis Vranishti                                       
# * Ask for name
# * ready to crack the code?
# * if yes, run. if no, terminate.
# * takes 3 integers, first==3, second number==1 || 33 - 100. third % 3 or 7 == 0.    
# * if all three pass, code cracked
# *************************************************************************
num1 = 0
num2 = 0
num3 = 0
name = input("Welcome. What is your name?""\n")
decision = input("Hello " + name + ". Are you ready to crack the code?""\n")
decision = decision.lower()
if decision == 'yes':
   print("\n")
   print("PHASE 1")
   num1 = int(input("Enter a number: ""\n"))
   if num1 == 3:
      print("Correct!")
      print("\n")
   
      print("PHASE 2")
      num2 = int(input("Enter a number: ""\n"))
         
   if (num2 == 1) or (num2 >= 33) and (num2 <= 100):
      print("Correct!")
      print("\n")
      print("PHASE 3")
      num3 = int(input("Enter a number: ""\n"))
              
      if (num3 > 0) and (num3 % 3 == 0):
         print("Correct!")
         print("You have cracked the code!")
      elif (num3 > 0) and (num3 % 7 == 0):
         print("Correct!")
         print("You have cracked the code!")
               
      else:
         print("Sorry, that was incorrect!")
         print("Better luck next time!")
           
   else:
      print("Sorry, that was incorrect!")
      print("Better luck next time!")
         

if decision == 'no':
   print("Come back when you are ready to crack the code")
   
