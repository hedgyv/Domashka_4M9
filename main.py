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

def main():
    while True:
        do_requirement = input(f'Write your command: ')
        do_requirement_parts = do_requirement.split()

        split_command = ''
        for char in do_requirement:
            if char != ' ':
                split_command += char.lower()
            else:
                break
        #print(do_requirement_parts)
        if split_command == 'hello':
            print("How can I help you? \n")

        elif split_command == 'add':
            if len(do_requirement_parts) < 3:
                print("Error: Tap an existed name and new phone")
            else:
                print(add_contact(do_requirement_parts[1], do_requirement_parts[2]))

        elif split_command == 'change':
            if len(do_requirement_parts) < 3:
                print("Error: Tap an existed name and new phone")
            else:
                print(change_contact(do_requirement_parts[1], do_requirement_parts[2]))

        elif split_command == 'phone':
            if len(do_requirement_parts) < 2:
                print("Error: Tap an existed name")
            else:
                print(find_contact(do_requirement_parts[1]))
            
        elif do_requirement == 'show all':
            print(show_contacts())

        elif do_requirement.lower() in ('good bye', 'close', 'exit'):
            print("Good bye")
            break

        else:
            print("Use command only: 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")
if __name__ == '__main__':
    main()