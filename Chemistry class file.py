import random
a={"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8,"F":9,"Ne":10,"Na":11,"Mg":12,"Al":13,"Si":14,"P":15,"S":16,"Cl":17,"Ar":18,"K":19,"Ca":20}
f=int(input("How many rounds do u wanna play"))
rights=0
wrongs=0
for x in range(f):
    c=random.choice(list(a))
    b=input(f"Enter the number of {c}:")
    if b==a[c]:
        print("ur good!")
        rights+=1
    else:
        print("Wrong!")
        wrongs+=1
print(f"You got {rights} rights and {wrongs} wrong asnwers")



