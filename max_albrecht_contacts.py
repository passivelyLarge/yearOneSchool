#   Max Albrecht
#   11/30/2022
#   PROG108 9606

# Contacts manager: a program that is used to manage the primary email
# address and phone number for a contact.

def selection(names):
    numb=(input('Contact Number:'))
    limit=int(len(names))+1
    #print(limit)
    while numb.isdigit()==False or int(numb) not in range(1,limit):
        print('invalid Selection')
        numb=(input('Contact Number:'))
    numb=int(numb)
    numb-=1
    return numb

def display(names):
    print()
    numb=(len(names))
    for n in range(numb):
        print (n+1,'-',names[n])
    print()
        
def add(names, emails, numbers):
    name=str(input('Name: '))
    email=str(input('Email: '))
    number=str(input('Number: '))
    names.append(name)
    emails.append(email)
    numbers.append(number)
    print(name, 'has been added')
    return(names,emails,numbers)

def view(names, emails, numbers):
    numb = selection(names)
    print('Name:',names[numb])
    print('Email:',emails[numb])
    print('Number:',numbers[numb])
    
def delete(names, emails, numbers):
    numb = selection(names)
    dname=str(names[numb])
    demail=str(emails[numb])
    dnumber=str(numbers[numb])
    print('Removing',dname)
    names.remove(dname)
    emails.remove(demail)
    numbers.remove(dnumber)
    return(names,emails,numbers)

def edit_phone(names, emails, numbers):
    numb = selection(names)
    name=names[numb]
    print(name,end="'s ")
    new_numb=str(input('new Number:'))
    numbers[numb]=new_numb
      
def show_title():
    print("Contact Manager")
    print()

def show_menu():
    print("COMMAND MENU")
    print("list - Show all contacts", end = "\t")
    print("view - View a contact")
    print("edit - Edit phone number",end = "\t")
    print("add  - Add a contact")
    print("del  - Delete a contact",end = " \t")
    print("exit - Exit program")
    print()    

def main():
    contacts_names = ["Harry Potter","Ron Weasley"]
    contacts_emails = ["hpotter@hogwarts.edu","rweasley@hogwarts.edu"]
    contacts_numbers = ["+44 20 6789 0022", "+44 20 2345 0958"]

    show_title()
    show_menu()
    
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts_names)
        elif command == "view":
            view(contacts_names, contacts_emails, contacts_numbers)
        elif command == "add":
            add(contacts_names, contacts_emails, contacts_numbers)
        elif command == "del":
            delete(contacts_names, contacts_emails, contacts_numbers)
        elif command == "edit":
            edit_phone(contacts_names, contacts_emails, contacts_numbers)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
