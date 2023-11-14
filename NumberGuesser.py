
# coding: utf-8

# In[2]:


## Number Guesser
import random
import math


# In[3]:


class Number_guesser:
    rightnum = random.randint(1,100) ## class attribute
 
    def __init__(self,uinp): #, hintyesno
        self.uinp =uinp
        #self.rightnum = rightnum
        
    def factors(self):
        factors = [fact for fact in range(1, Number_guesser.rightnum + 1) if  Number_guesser.rightnum % fact == 0]
        rand_factor = random.choice(factors)
        if rand_factor > 0:
            return rand_factor
        else: return False
                
    def multiples(self):
        multiples = [multi*Number_guesser.rightnum for multi in range(5+1)] ## first 10 multiples
        #multiples = [multi*Number_guesser.rightnum for multi in range(100) if Number_guesser.rightnum * multi <= 100] ## multiples in range 1,100
        rand_multiple = random.choice(multiples)
        if rand_multiple > 0:
            return rand_multiple
        else: return False
    
    def larger(self):
        larger = random.randint(Number_guesser.rightnum, 100)
        if larger <= 100:
            return larger
        else: return False
        
    def smaller(self):
        smaller = random.randint(1, Number_guesser.rightnum)
        if smaller > 0:
            return smaller
        else: return False
        
    def parity(self):
        if(Number_guesser.rightnum%2) == 0:
            return "even"
        else:
            return "odd"
            


# In[32]:


rightnum = Number_guesser.rightnum
hints =3
for i in range(4, 0, -1):
    uinp = int(input(f"\n Please guess a number! You have {i} guesses to make"))
    print(f"your input is {uinp}")
    if uinp == Number_guesser.rightnum:
        print ("congratulations! you guessed right")
        break
    elif i-1 == 0:
        break 
    else:
        print (f"\n Wrong Guess; you now have {i-1} guesses left; You can request upto {hints} hints")
        hintip = input("Type 'hint' to request")
        if hintip == "hint":
            chosen_hint_cat = random.choice(["a", "b", "c"])
            hint_op = Number_guesser(uinp)

            if chosen_hint_cat == "a":
                choice_a = random.choice(["factors", "multiples"])
                notchoice_a = [item for item in ["factors", "multiples"] if item != choice_a]
                if getattr(hint_op, choice_a)() > 0:                        ##  getattr Python method, to call methods by name
                    print(f"{getattr(hint_op, choice_a)()}, is one of the {choice_a} of the number")
                elif getattr(hint_op, notchoice_a[0])() > 0:
                        print(f"{getattr(hint_op, notchoice_a[0])()}, is one of the {notchoice_a[0]} of the number")
                else: print("number has no factor or multiple")
                
            elif chosen_hint_cat == 'b':
                choice_b = random.choice(["larger", "smaller"])
                notchoice_b = [item for item in ["larger", "smaller"] if item != choice_b]
                if getattr(hint_op, choice_b)() > 0:
                    print(f"{getattr(hint_op, choice_b)()}, is {choice_b} then the number")
                elif getattr(hint_op, notchoice_b[0])() > 0:
                    print(f"{getattr(hint_op, notchoice_b[0])()}, is {notchoice_b[0]} then the number")

            else: print(f"The number is {hint_op.parity()}") 
            hints -= 1
           

if i ==1:
    print (f"End Of Game; the number was {Number_guesser.rightnum}!")

