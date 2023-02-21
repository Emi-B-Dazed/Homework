"""
User interface.
Fuck yeah
"""
from OO import Contact
from OO import ContactList


def main():
    lst = ContactList()
    lst.Hello()
    
    usr = "null"
    
    # While loop exits after user exits
    while usr != "exit":
        usr = input(str("Please enter a command: "))
        
        # Add
        if usr == "add":
            n = input("Enter name: ")
            p = input("Enter phone number: ")
            c = input("Enter Company: ")
            e = input("Enter email: ")
            no = input("Enter a note: ")
            
            
            print(n, p, c, e, no, "has been added to your contacts.")
            
            lst.addcontact(n, p, c, e, no)
            
        # List    
        elif usr == "list":
            lst.list()
            
        # Note    
        elif usr == "note":
        
            asp = input(str("How do you want to look up the contact? "))
            asp_name = input(str("What is the value of the aspect? "))
            mode = input(str("Enter a mode see/edit: "))
            newnote = ""
            
            if mode == "edit":
                newnote = input(str("Enter a new note: "))
            
            lst.editaspect(asp, asp_name, "note", mode, newnote)
        
        # Edit
        elif usr == "edit":
            asp = input(str("How do you want to look up the contact? "))
            asp_name = input(str("What is the value of the aspect? "))
            editee = input(str("What part of the contact do you want to edit? "))
            newnote = input(str("Enter new value "))
            
            lst.editaspect(asp, asp_name, editee, "edit", newnote) 
            
        # Exit    
        elif usr == "exit":
            lst.Goodbye()
         
        # Info   
        elif usr == "info":
            lst.info()
        
        # Save    
        elif usr == "save":
            save_file = input(str("Enter a file name: "))            
            lst.save(save_file)
        
        # Commands    
        elif usr == "commands":
            commands_file =  input(str("Enter file name: "))
            lst.commands(commands_file)
        
        # Load    
        elif usr == "load":
            lst.commands("lol.txt")
            
            
        elif usr == "remove":
            asp = input(str("How would you like to look up contact? "))
            asp_name = input(str("What is the value of this lookup? "))
            
            lst.remove(asp, asp_name)
            
            
        elif usr == "about":
            lst.about()
        
        # If no proper command given    
        else: 
            print("Command not Available")
            
            
     


















































if __name__ == '__main__':
    main()
