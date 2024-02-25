from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    # def __str__(self):
    #      return str(self.value)  

class Name(Field):
   def __init__(self, name):
     self.name = name
                

class Phone(Field):
    # реалізація класу
     def __init__(self, number):
          if number.isdigit() and len(number)==10:
               self.number = number
          else:
               raise ValueError
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def edit_phone(self, old_phone, new_phone):
         pass
    
    def find_phone(self, phone):
         return [p.number for p in self.phones if p.number == phone]

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass

nm = Name('Karnok')
ph = Phone('0667961915')

print(nm.name)
print(ph.number)
#print(f.name)
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

print(john_record)

'''
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not exist"
        except IndexError:
            return "Contact not found"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name]=phone
    return "Contact added successfully"

@input_error
def change_contact(args, contacts):
    if args[0] in contacts.keys():
        add_contact(args, contacts)
    else:
        raise(KeyError)
    return "Contact successfully changed"

@input_error
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]
    else:
        raise(IndexError)

def show_all(contacts):
    all_contacts = ''
    for name, phone in contacts.items():
        all_contacts+=name+' '+phone+'\n'
    return all_contacts

def main():
    print("Welcome to the assistant bot!")
    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ['close','exit']:
            print('Good by!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            if contacts:
                print(show_phone(args[0], contacts))
            else:
                print('Contacts is empty')

        elif command == 'all':
            if contacts:
                print(show_all(contacts))
            else:
                print('Contacts is empty')
        else:
            print('Invalid command.')


if __name__=="__main__":
    main()
'''