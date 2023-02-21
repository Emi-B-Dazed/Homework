
from random import randrange
from OO import ContactList

with open("lol.txt", "r") as f:
    lst = f.readlines()

clst = ContactList()


for i in range(len(lst)):
    sublst = lst[i].split()
    if len(sublst) > 1:
        if sublst[0].lower() == "add" or sublst[0].lower() == "add:":
            n = sublst[1]
            k = 1
            holder = "-"
            p = holder
            c = holder
            e = holder
            no = holder
            while k != 'end':
                sub2 = lst[i+k].split()
                if len(sub2) > 1 and (sub2[0].lower() == "phone:" or 
                sub2[0].lower() == "phone"):
                    p = sub2[1]                
                    k = k + 1
                    
                elif len(sub2) > 1 and (sub2[0].lower() == "company:" or 
                sub2[0].lower() == "company"):
                    c = sub2[1]                
                    k = k + 1
                    
                elif len(sub2) > 1 and (sub2[0].lower() == "email:" or 
                sub2[0].lower() == "email"):
                    e = sub2[1]
                    k = k + 1
                    
                elif len(sub2) > 1 and (sub2[0].lower() == "note:" or 
                sub2[0].lower() == "note"):
                    no = sub2[1]
                    k = k + 1
                    
                elif sub2 == [] or (len(sub2) > 0 and (sub2[0].lower() == "note:" or 
                      sub2[0].lower() == "note" or sub2[0].lower() == "email:" or 
                      sub2[0].lower() == "email" or sub2[0].lower() == "company:" or
                      sub2[0].lower() == "company" or sub2[0].lower() == "phone:" or 
                      sub2[0].lower() == "phone")):
                    k = k + 1
                    
                else:
                    i = i + k - 1
                    clst.addcontact(n, p, c, e, no)
                    k = 'end'
                    

        elif sublst[0].lower() == "remove:" or sublst[0].lower() == "remove":
            clst.remove("name", sublst[1])
            
        elif sublst[0].lower() == "save":
            clst.save(sublst[1])
    
    
    elif len(sublst) > 0:        
        if sublst[0].lower() == "list":
            clst.list()
            
        elif sublst[0].lower() == "about":
            clst.about()
            
        elif sublst[0].lower() == "info":
            clst.info()
            
    
          


clst.list()
   






























































"""
def usr_nm(usr_name, passwrd):
    file_name = "." + usr_name + ".txt"
    
    try:
        with open(file_name, "r") as f:
            password = f.readline()
            return Pass_Word(passwrd, password, file_name)
        
    except FileNotFoundError:
        return ["Login Failed"]
    
    
    
    
    
    
def Pass_Word(usr_pass, password, file_name): 
    
    if password == (usr_pass + ):
        return ["Succesful longin welcome.", file_name]
        
    else:
        return ["Login Failed"]
    
def Good_Bye():
    Bye = ["Peace", "Bye", "Good riddence to ya", "Buggar off", "Fuck off",
           "I DIDN'T WANNA TALK TO YOU JUST ANYWAYS"]
    
    print(Bye[randrange(0, len(Bye))])
    
       
    
#def Commands(file_name)    
"""   
"""
def contacts(file_name):
    lst = []
    with open(file_name, 'r') as f:
        for i in f:
            if i == "add":
                
                
                
            else:
                print(i) 
                print("Fail")


def main():
    contacts(".em.txt")

   

    
 
if __name__ == '__main__':
    main()   
    
"""






























"""
con = [{"Name":"Emily", "Phone":"505-333-2343", "Company":"Bitchhouse", 
        "Email":"datbitch@gmail.com", "Note":"I hate this bitch"}, 
       {"Name":"Jessie", "Phone":"444-333-2222", "Company":"Goobop", 
        "Email":"JJ@gmail.com", "Note":"No idea who it is"}, 
       {"Name":"Drew", "Phone":"234-456-9494", "Company":"TBOT", 
        "Email":"Drewboo@gmail.com", "Note":"Love dis bitch"}, 
       {"Name":"Jacob", "Phone":"000-111-2345", "Company":"Crycry", 
        "Email":"Cub@gmail.com", "Note":"dis bitch makes me laugh"}]

"""













































































































