from datetime import datetime, timedelta

class Birthday:
    def __init__(self, date_str):
        self.date = self.validate_date(date_str)

    def validate_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            return date_obj
        except ValueError:
            raise ValueError("Invalid date format. Please use DD.MM.YYYY.")

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = self.validate_phone(phone)
        self.birthday = birthday

    def validate_phone(self, phone):
        if len(phone) == 10 and phone.isdigit():
            return phone
        else:
            raise ValueError("Invalid phone number. Please provide a 10-digit number.")

    def add_birthday(self, date_str):
        self.birthday = Birthday(date_str)

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, birthday=None):
        if name not in self.contacts:
            self.contacts[name] = Record(name, phone, birthday)
            return 'Contact added.'
        else:
            return 'Contact already exists.'

    def change_contact(self, name, phone):
        if name in self.contacts:
            self.contacts[name].phone = phone
            return 'Contact updated.'
        else:
            return 'Contact not found.'

    def show_phone(self, name):
        if name in self.contacts:
            return self.contacts[name].phone
        else:
            return 'Contact not found.'

    def show_all(self):
        if not self.contacts:
            return 'No contacts found.'
        else:
            return '\n'.join([f"{record.name}: {record.phone}" for record in self.contacts.values()])

    def add_birthday(self, name, date_str):
        if name in self.contacts:
            self.contacts[name].add_birthday(date_str)
            return 'Birthday added.'
        else:
            return 'Contact not found.'

    def show_birthday(self, name):
        if name in self.contacts and self.contacts[name].birthday:
            return self.contacts[name].birthday.date.strftime("%d.%m.%Y")
        else:
            return 'Birthday not found.'

    def get_birthdays_per_week(self):
        today = datetime.now()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = []

        for record in self.contacts.values():
            if record.birthday:
                birthday_date = record.birthday.date.replace(year=today.year)
                if today <= birthday_date < next_week:
                    upcoming_birthdays.append(f"{record.name}'s birthday on {birthday_date.strftime('%A')}.")

        return upcoming_birthdays


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    book = AddressBook()
    print('Welcome to the assistant bot!')
    
    while True:
        user_input = input('Enter a command: ')
        command, args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(book.add_contact(*args))
        elif command == 'change':
            print(book.change_contact(*args))
        elif command == 'phone':
            print(book.show_phone(*args))
        elif command == 'all':
            print(book.show_all())
        elif command == 'add-birthday':
            print(book.add_birthday(*args))
        elif command == 'show-birthday':
            print(book.show_birthday(*args))
        elif command == 'birthdays':
            print('\n'.join(book.get_birthdays_per_week()))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
