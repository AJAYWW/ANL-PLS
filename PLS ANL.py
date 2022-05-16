import json
Username = "admin"
Password = "admin123"

with open("memberlist.json", "r") as f:
    memberDict = json.load(f)

class member:
    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password

def login():
    print("\npress 1 to login to admin\n")
    print("press 2 to login to member\n")
    temp = input()
    if temp == "1":
        adminSeq()
    elif temp == "2":
        memberSeq()
    else:
        print("try again \n\n")
        login()
    

def adminSeq():
    print("please enter admin pass\n\n")
    if input() == Password:
        adminPage()
    
    else:
        print("WRONG PASS TRY AGAIN \n \n")
        adminSeq()
    
def adminPage():
    print("To see member list, press 1 \n")
    input()
    print(list(memberDict.keys()))

login()
