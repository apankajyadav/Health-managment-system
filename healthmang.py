import datetime
def gettime():
    return datetime.datetime.now()

print("Health Managment System")
def take(k):
    if(k==1):
        c=int(input("Enter 1 for Exercise and 2 for Food of pankaj"))
        if (c==1):
            value=input("Hey pankaj plz Enter our Exeercise deatails\n")
            with open("pankaj_exe.txt","a")as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("successfull writen pankaj  exercise detail int file")
        elif(c==2):
            value = input("hey pankaj plz Enter our food deatails")
            with open("pankaj_food.txt", "a")as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("successfull writen pankaj food detail int file")

    elif (k == 2):
            c = int(input("Enter 1 for Exercise and 2 for Food of Anjali"))
            if (c == 1):
                value = input("Hey Anjali plz Enter our Exeercise deatails\n")
                with open("anjali_exe.txt", "a")as op:
                    op.write(str([str(gettime())])+":"+value+"\n")
                    print("successfull writen anjali  exercise detail int file")
            elif (c == 2):
                    value = input("hey anjali plz Enter our food deatails\n")
                    with open("anjali_food.txt", "a")as op:
                        op.write(str([str(gettime())])+":"+value+"\n")
                        print("successfull writen anjali food detail int file")
    elif(k == 3):
        c=int(input("Enter 1 for Exercise and 2 for Food of ashok\n"))
        if (c==1):
            value=input("Hey ashok plz Enter our Exeercise deatails")
            with open("ashok_exe.txt","a")as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("successfull writen ashok  exercise detail into the file")
        elif(c==2):
            value = input("hey ashok plz Enter our food deatails\n")
            with open("ashok_food.txt", "a")as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("successfull writen ashok food detail int file")

    else:
        print("plz enter valid key")

def retrive(k):
        if (k == 1):
            c = int(input("Enter 1 for Exercise and 2 for Food of pankaj data retrive"))

            if (c == 1):
                with open("pankaj_exe.txt") as op:
                    for i in op:
                        print(i,end=" ")
            elif (c == 2):
                with open("pankaj_food.txt") as op:
                    for i in op:
                        print(i,end=" ")


        elif(k == 2):
            c = int(input("Enter 1 for Exercise and 2 for Food of Anjali data retrive"))

            if (c == 1):
                with open("Anjali_exe.txt") as op:
                    for i in op:
                        print(i, end=" ")
            elif (c == 2):
                with open("Anjali_food.txt") as op:
                    for i in op:
                        print(i, end=" ")
        elif (k == 3):
            c = int(input("Enter 1 for Exercise and 2 for Food of ashok data retrive"))

            if (c == 1):
                with open("ashok_exe.txt") as op:
                    for i in op:
                        print(i, end=" ")
            elif (c == 2):
                with open("ashok_food.txt") as op:
                    for i in op:
                        print(i, end=" ")
        else:
         print("enter valid key")

a=int(input("press 1 for data enter and 2 for retrive of data"))
if(a==1):
     b=int(input("press 1 for pankaj 2 for anjali 3 for ashok"))
     take(b)
elif(a==2):
    b = int(input("press 1 for pankaj 2 for anjali 3 for ashok"))
    retrive(b)
else:
    print("plz enter valid key")


