import random

def elements(a):
    a=[]
    while True:
        element = input()
        if element == "":
            break
        a.append(element)
    return  a   

when=[]
print("Enter time one by one. Press Enter without typing anything to stop.")
when=elements(when)
where=[]
print("Enter places one by one. Press Enter without typing anything to stop.")
where=elements(where)
who=[]
print("Enter persons one by one. Press Enter without typing anything to stop.")
who=elements(who)
did=[]
print("Enter what they did one by one. Press Enter without typing anything to stop.")
did=elements(did)
drinks=[]
print("Enter food one by one. Press Enter without typing anything to stop.")
drinks=elements(drinks)
print(random.choice(when)+" "+random.choice(where)+" "+random.choice(who)+" "+random.choice(did)+" "+random.choice(drinks))