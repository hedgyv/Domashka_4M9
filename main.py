phone_book = {}

def input_error(func):
    pass
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input. Please enter name and phone number."
        except IndexError:
            return "Error: You don't have any contacts yet."
    return inner

    
@input_error
def add_contact(name, phone):
    if name in phone_book:
        raise ValueError
    phone_book[name] = phone
    return f"Contact {name} with phone {phone} has been added."

@input_error
def find_contact(name):
    if name not in phone_book:
        raise KeyError
    return (f"{name}'s phone number is {phone_book[name]}.")


@input_error
def change_contact(name, phone):
    if name not in phone_book:
        raise KeyError
    else:
        phone_book[name] = phone
        return f"Phone number for {name} has been changed to {phone}."

@input_error
def show_contacts():
    if not phone_book:
        raise IndexError
    for name, phone in phone_book.items():
        return f"{name}: {phone}\n"
    
def handle_requirement(req):
    split_command = ''
    for char in req:
        if char != ' ':
            split_command += char.lower()
        else:
            break
    return split_command

def split_req(req):
    return req.split()


def main():


    def hello_func():
        print("How can I help you? \n")

    def add_func():
        if len(do_requirement_parts) < 3:
            print("Error: Tap an existed name and new phone")
        else:
            print(add_contact(do_requirement_parts[1], do_requirement_parts[2]))
    
    def change_func():
        if len(do_requirement_parts) < 3:
            print("Error: Tap an existed name and new phone")
        else:
            print(change_contact(do_requirement_parts[1], do_requirement_parts[2]))

    def phone_func():
        if len(do_requirement_parts) < 2:
            print("Error: Tap an existed name")
        else:
            print(find_contact(do_requirement_parts[1]))
    
    def show_all_func():
        print(show_contacts())


    while True:
        do_requirement = input(f'Write your command: ')

        do_requirement_parts = split_req(do_requirement)

        split_command = handle_requirement(do_requirement)
        
        all_commands = {
            'hello': hello_func,
            'add': add_func,
            'change': change_func,
            'phone': phone_func,
            'show all': show_all_func,
            'good bye': lambda: print("Good bye!"),
            'close': lambda: print("Good bye!"),
            'exit': lambda: print("Good bye!")
        }


        if do_requirement in all_commands:
            all_commands[do_requirement]()
            if do_requirement.lower() in ('good bye', 'close', 'exit'):
                break
        
        elif split_command in all_commands:
            all_commands[split_command]()


        else:
            print("Use command only: 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")
if __name__ == '__main__':
    main()



         ###COMMENTS
        # if split_command == 'hello':
        #     print("How can I help you? \n")

        # elif split_command == 'add':
        #     if len(do_requirement_parts) < 3:
        #         print("Error: Tap an existed name and new phone")
        #     else:
        #         print(add_contact(do_requirement_parts[1], do_requirement_parts[2]))

        # elif split_command == 'change':
        #     if len(do_requirement_parts) < 3:
        #         print("Error: Tap an existed name and new phone")
        #     else:
        #         print(change_contact(do_requirement_parts[1], do_requirement_parts[2]))

        # elif split_command == 'phone':
        #     if len(do_requirement_parts) < 2:
        #         print("Error: Tap an existed name")
        #     else:
        #         print(find_contact(do_requirement_parts[1]))
            
        # elif do_requirement == 'show all':
        #     print(show_contacts())

        # elif do_requirement.lower() in ('good bye', 'close', 'exit'):
        #     print("Good bye")
        #     break   