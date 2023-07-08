import random
def gamewin(comp,you):
      if comp==you:
        return None
      elif comp=='s':
       if you=='w':
        return False
      elif you=='g':
         return True
      elif comp=='w':
        if you=='g':
         return False
      elif you=='s':
        return True
      if you=='s':
          return False
      elif you=='w':
        return True
      

print("comp turn :snake(s) water(w) gun(g)")
randno=random.randint(1,3)
if randno==1:
      comp='s'
elif randno==2:
      comp='w'
elif randno==3:
         comp='g'


you =input("its your turn")
a=gamewin(comp,you)
print(f"computer chooses {comp}")
if a==None:
   print("this is a tie")
elif a:
   print("you win")
else:
   print("you loose")


      