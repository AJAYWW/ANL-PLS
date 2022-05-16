import json
class members:

    def __init__(self, fname, lname, password):
        self.fname = fname
        self.lname = lname
        self.password = password



f = open("memberlist.json", "r")
beter = json.load(f)
Username = "admin"
Password = "admin123"

pik = members("penis", "hond", "kanker")
print(beter.keys())