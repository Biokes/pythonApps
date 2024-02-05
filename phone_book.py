class phone_book:
    def __int__(self):
        self.numbers = []
        self.names = []

    def save_contact(self, name_gotten, number_gotten):
        while not number_gotten.isnumeric():
            number_gotten = input('Enter a valid number: ')
        self.numbers.append(number_gotten)
        self.names.append(name_gotten)
        return "contact saved successfully"

    def delete_contact(self, name_given):
        if name_given in self.names:
            index_of_name = self.names.index(name_given)
            del self.numbers[index_of_name]
            del self.names[index_of_name]
        else:
            return "contact not found"
        return "contact deleted successfully"

    def exit(self):
        return "Exiting..........."

    def display_contacts(self):
        if self.numbers:
            for number in range(len(self.numbers)):
                print(self.names[number], ' ---------->', self.numbers[number])
        else:
            return "no contacts available."
        return ''

    def phone_menu(self):
        print('''
        1. Add Contact.
        2. Delete number.
        3. display contact.contact
        4. Exit.
        ''')
        condition = True
        while condition:
            menu = int(input('Enter the nenu number of your choice: '))
            match menu:
                case 1:
                    name = input('Enter the contact name: ')
                    number_given = input('Enter phone number:  ')
                    print(self.save_contact(name, number_given))
                case 2:
                    name = input('Enter the contact name to be deleted: ')
                    print(self.delete_contact(name))
                case 3:
                    self.display_contacts()
                case 4:
                    self.exit()
                    condition = False
                case _:
                    print("Invalid number.")
