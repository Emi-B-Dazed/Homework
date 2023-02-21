
from random import randrange

class ContactList(): 
    def __init__(self, ls=[]):
        self.__lst = ls
        
        
    """
    prints random hello message. 
    """    
    def Hello(self):
        Hello = ["Hello, it's me.", 
                 "I was wondering if after all these years you'd like to meet.",
                 "Welcome to Contacts R us", "Long time no see"]
        
        print(Hello[randrange(0, len(Hello))])
        
        
    """
    Prints Developer information for Contacts R Us
    """   
    def about(self):
        print("Contacts R Us")
        print("Created by: Emily Bardwell")
        print("Created on: 12/6/16")
        print("For: Python 107")
      
        
    """
    Adds a contact to list of contacts
    """    
    def addcontact(self, n, p, c, e, no):
        # Calls upon contact to make a new contact adds it to list of dics
        dic = Contact(n, p, c, e, no)
        self.__lst.append(dic)
    
    
    def info(self):
        print("Number of contacts:", len(self.__lst))
        
        # goes through all contacts key is company name value is # of contacts
        dic = {}
        for i in range(len(self.__lst)):
            sub = Contact.getcontact(self.__lst[i]) 
            company = sub['company']
            
            # Checks if contact exists in subdic
            if dic.get(company, -1) == -1:
                dic[company] = 1
            
            # Adds 1 to company value if company is already listed   
            else:
                dic[company] = dic[company] + 1
        
        print("Number of contacts per company.") 
        
        # Prints all companies followed by 3 of contacts       
        for k, L in dic.items():
            print("{}: {}".format(k, L))
            
        print("Number of Companies:", len(dic))
    
     
        
    """
    Removes a contact from the list of contacts
    """       
    def remove(self, asp, aspectname):
        # Searches for contact
        i = ContactList().search(asp, aspectname)
        
        # Checks if there is a contact
        if i.isdigit() == True:
            # Removes contact
            self.__lst.pop(int(i))
            print("Contacts have been updated")
        
        # Prints error no contact    
        else:
            print(i)
   
              
    """
    Searches for a specific contact based on the search name ie name phone number
    and then searches for the actual contact like Emily or 231-432-3454
    """    
    
                    
                    
    """
    Lists all the contacts by name and gets phone company email
    """                 
    def list(self):
        print("{}\t:{}\t\t{}\t{}".format("Name", "Phone", "Company", "Email"))
        print("------------------------------------------------------------------------")
        
        # For loop goes through all contacts and prints them in the given order
        for i in range(len(self.__lst)):
            d = Contact.getcontact(self.__lst[i])
            print("{}\t:{}\t{}\t{}".format(d["name"], d["phone"], d["company"], d["email"]))
         
         
         
    """
    edits the aspec like name phone ect
    searchname is name phone email company or note
    search word is the contact value
    editee is what aspect they want to edit name phone email company or note
    and edit is the actual edit
    """        
    def editaspect(self, asp, asp_name, editee, mode, edit="-"):
        # gets the return from search function
        i = ContactList().search(asp, asp_name)
        tf = Contact.getcontact(self.__lst[0]).get(asp.lower(), -1)
        tf2 = Contact.getcontact(self.__lst[0]).get(editee.lower(), -1)
        
        # checks if i is a digit
        if i.isdigit() == True and tf != -1 and tf2 != -1:
            i = int(i)
            # Prints the aspect that it is currently and name of contact
            print(editee, "for contact", Contact.getcontact(self.__lst[i])["name"],
                      "is:", Contact.getcontact(self.__lst[i])[editee])
                      
            # gets the mode  edits if edited         
            if mode.lower() == "edit":
                self.__lst[i].editnote(editee, edit)
                print(editee, "has been updated to:", 
                      Contact.getcontact(self.__lst[i])[editee])
                          
            # If mode isn't a mode choice  
            elif mode.lower() != "see":
                print("Mode not available.")
                      
        # If i isn't a digit               
        elif tf != -1:
            print("Error improper input.")
            
        else:
            print("You chose to edit", editee, " and this is not an aspect of your contacts.")
        
    
    """
    Searches specific asp name and asp of contact
    """    
    def search(self, asp, asp_name):
    
        count = 0
        
        # lowercase of how user wants to look up
        asp = asp.lower()
        # lowercase of value of what user is looking up
        asp_name = asp_name.lower()
        
        # CHecks if user is looking up something that can be searched
        if Contact.getcontact(self.__lst[0]).get(asp, -1) == -1:
            return str(asp) + "is not a searchable object in your contact list."
                        
        else:
            # For loop checks if it exists in any contacts returns error message if not there
            for i in range(len(self.__lst)):
                if Contact.getcontact(self.__lst[i])[asp].lower() == asp_name:
               
                    return str(i)
            
                else:
                    count = count + 1
                    if count == len(self.__lst):
                        return "Error. Contact doesn't exist."
                    
        
                
    """
    prints random goodbye message
    """
    def Goodbye(self):
        Bye = ["Peace", "Bye", "Good riddence to ya", "Buggar off", "Fuck off",
               "I DIDN'T WANNA TALK TO YOU JUST ANYWAYS"]
        
        print(Bye[randrange(0, len(Bye))])
        
        
    """
    saves contacts to file
    """    
    def save(self, file_name):
        # opens new file with file name
        f = open(file_name, "w")
        
        # for loop goes through and writes all contacts in file
        for i in range(len(self.__lst)):
            dic = Contact.getcontact(self.__lst[i])
            
            # Special format
            f.write("{} {} {} {} {} \n".format(dic["name"], dic["phone"], 
            dic["company"],  dic["email"], dic["note"]))

        f.close()
 
    """
    Reads a file and carries out commands
    """
    def commands(self, f_n):
        # Opens file reads lines
        with open(f_n, "r") as f:
            lst = f.readlines()
        
        # Gets the contact list
        clst = ContactList()

        # For loop goes through each and every command
        for i in range(len(lst)):
            sublst = lst[i].split()
            
            # Checks first if sublst is long enough for following commands
            if len(sublst) > 1:
                
                # Add command
                if sublst[0].lower() == "add" or sublst[0].lower() == "add:":
                
                    # while loop
                    k = 1
                    holder = "-"
                    # name phone company email and note
                    n = sublst[1]
                    p = holder
                    c = holder
                    e = holder
                    no = holder
                    
                    # While loop reads lines to see ifany commands give more info on cont.
                    while k != 'end':
                        try:
                            # sub2 is a list of the next line
                            sub2 = lst[i+k].split()
                       
                            # Checks for phone
                            if len(sub2) > 1 and (sub2[0].lower() == "phone:" or 
                            sub2[0].lower() == "phone"):
                                # resets the variable
                                p = sub2[1] 
                                # This gets the next line               
                                k = k + 1
                            
                            # Checks for company    
                            elif len(sub2) > 1 and (sub2[0].lower() == "company:" or 
                            sub2[0].lower() == "company"):
                                c = sub2[1]                
                                k = k + 1
                            
                            # Checks for email    
                            elif len(sub2) > 1 and (sub2[0].lower() == "email:" or 
                            sub2[0].lower() == "email"):
                                e = sub2[1]
                                k = k + 1
                            
                            # Checks for note    
                            elif len(sub2) > 1 and (sub2[0].lower() == "note:" or 
                            sub2[0].lower() == "note"):
                                no = sub2[1]
                                k = k + 1
                            
                            elif sub2 == [] or (len(sub2)>0 and (sub2[0].lower() == "note:" or 
                            sub2[0].lower() == "note" or sub2[0].lower() == "email:" or 
                            sub2[0].lower() == "email" or sub2[0].lower() == "company:" or
                            sub2[0].lower() == "company" or sub2[0].lower() == "phone:" or 
                            sub2[0].lower() == "phone")):
                                k = k + 1
                                
                            else:
                                i = i + k - 1
                                clst.addcontact(n, p, c, e, no)
                                k = 'end'
                        # CHecks if k makes it go into a line that doesn't exist
                        except IndexError:
                            clst.addcontact(n, p, c, e, no)
                            k = 'end'

                
                # Remove
                elif sublst[0].lower() == "remove:" or sublst[0].lower() == "remove":
                    clst.remove("name", sublst[1])
                 
                # Save   
                elif sublst[0].lower() == "save":
                    clst.save(sublst[1])
                 
                # Commands    
                elif sublst[0].lower() == 'commands:' or sublst[0].lower() == 'commands':
                    clst.commands(sublst[1])
                
                # Note    
                elif len(sublst) > 2 and (sublst[0].lower() == 'note:' or 
                         sublst[0].lower() == 'note'):
                    clst.note("name", sublst[1], "note", "edit", sublst[2]) 
            
            # if len is only 1 or less
            elif len(sublst) > 0:     
                # List   
                if sublst[0].lower() == "list":
                    clst.list()
                    
                # about    
                elif sublst[0].lower() == "about":
                    clst.about()
                    
                # Info    
                elif sublst[0].lower() == "info":
                    clst.info()
                
                # Load
                elif sublst[0].lower() == "load":
                    lst.commands("lol.txt")
                    
                    
                    
     
   
"""
Contact class creates the individual contacts can get the contact and can edit the contact
"""        
class Contact(): 
    def __init__(self, name="-", phone="-", company="-", email="-", note="-"):
        self.__dic = {}
        self.__dic["name"] = name
        self.__dic["phone"] = phone
        self.__dic["company"] = company
        self.__dic["email"] = email
        self.__dic["note"] = note

        
        
        
    def getcontact(self):
        dic = self.__dic
        return dic
        
   
   
         
    def editnote(self, editee, edit):
        self.__dic[editee] = edit
            
 
   






    
