menu = "=" * 30 + \
"\nWelcome to our Phonebook App\n\n" + \
"1. Create a new contact\n" + \
"2. Edit a contact\n" + \
"3. View all contacts\n" + \
"4. Search for a contact\n" + \
"0. Quit\n" + \
"=" * 30
data = []

while True:
    print(menu)
    command = input(">>>")


    if command == "1":
        name = input("Enter name of contact:")
        phone = input("Enter phone number:")
        contact = {"name": name, "phone": phone}
        data.append(contact)
        print("Contact added successfully")
        print(data)
    elif command == "2":
        name = input("Enter the name of the contact you wish to edit:")
        print(data)
        for i, contact in enumerate(data):
            print(f"i = {i}, contact = {contact}")
    elif command == "0":
        print("Program ended. Have a nice day!")
        break

