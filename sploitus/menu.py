class MenuItem:
    def __init__(self, index, title, description, function):
        # add validation
        self.index = index 
        self.title = title
        self.description = description
        self.call = function

    def __str__(self):
        buf = ""
        buf += f"[{self.index}] - {self.title}:\n"
        buf += f"\t[*] - {self.description}\n"
        return buf

    def call(self):
        pass


class Menu:
    def __init__(self, title, items=[]):
        self.title = title
        self.items = items
    
    def add_item_raw(self, item):
        if not isinstance(item, MenuItem):
            raise TypeError("Provided Item is not of type 'MenuItem'")

        # add validation for indexing
        self.items.append(item)

    def add_item(self, index, title, description, function):
        item = MenuItem(index, title, description, function)
        self.add_item_raw(item)

    def print(self):
        print(f"[*] - {self.title} - [*]")
        for item in self.items:
            print(item)

    def input_choice(self):
        self.print()
        while True:
            choice = input("[?] - SELECT AN OPTION FROM ABOVE > ")
            if self.handle_choice(choice):
                self.print()
            else:
                print("[!] - NOT A VALID CHOICE, PLEASE TRY AGAIN - [!]")

    def handle_choice(self, choice):
        valid_choice = False

        try:
            choice = int(choice)
        except ValueError:
            return valid_choice

        for i in self.items:
            if i.index == choice:
                valid_choice = True
                i.call()
                input("[*] - PRESS ENTER TO RETURN TO THE MENU - [*]")
                break

        return valid_choice
