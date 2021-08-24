#! /usrs/bin/env python3

# TODO: ADD FEATURES LIST
# Record date checked out
# Record date return, If book past 14 days it'll give PAST DUE Notice and AMOUNT OWED
# Search Engine, and tell location
# read excerpt from book
# Donate books


# count how many days between checkout date and return day
return_days = 0

# Library books

# mystery = dict(
#   I1001={'TITLE': "The Last Thing He Told Me ", 'AUTHOR': 'Laura Dave'},
#   I1002={'TITLE': "Sweet Water ", 'AUTHOR': 'Cara Reinard'},
#  I1003={'TITLE': "Local Woman missing ", 'AUTHOR': 'Mary Kubica'},
# I1004={'TITLE': "The Maidens", 'AUTHOR': 'Alex Micaelides '}
# )

mystery = {
    'I1001': {'TITLE': "The Last Thing He Told Me ", 'AUTHOR': 'Laura Dave'},
    'I1002': {'TITLE': "Sweet Water ", 'AUTHOR': 'Cara Reinard'},
    'I1003': {'TITLE': "Local Woman missing ", 'AUTHOR': 'Mary Kubica'},
    'I1004': {'TITLE': "The Maidens", 'AUTHOR': 'Alex Micaelides '}
}

fantasy = {
    "2007": "The Queens's Weapons -Anne Bishop",
    "2008": "The Last Druid -Terry Brooks",
    "2009": "A Deadly Education -Naomi Novik",
    "2010": "Spy,Spy Again - Mercedes Lackey"
}

romance = {
    "3002": "Pride and Prejudice -Jane Austen",
    "3004": "Jane Eyre -Charlotte Bronte",
    "3006": "Gone with the Wind -Margaret Mitchell",
    "3008": "The Notebook -Nicholas Sparks"
}

textbook = {
    "4003": "Python Crash Course - Eric Matthews",
    "4004": "Automate the Boring Stuff with Python -Al Sweigart",
    "4005": "Learning Python -Mark Lutz",
    "4006": "Head-First Python -Paul Barry",
}

user_books = []
test_book = {}
# test_book = dict({})
# count how many book checked out
book_checkout_count = 0


# Computer Lab


# TODO: CREATE options list for books
def book_options():
    print(" \n Would you like to....[Please enter a Numeric Value]")
    print("1.Checkout Books")
    print("2.Return Books to Shelf")
    print("3.Return to Genre Menu")
    print("4.Return to Main Menu")
    print("5.Show Books in your Cart")

    while True:
        user_option = int(input("> "))
        if user_option == 1:
            checkout()
            continue
        elif user_option == 2:
            return_book()
            continue
        elif user_option == 3:
            library()
            continue
        elif user_option == 4:
            main_menu()
            continue
        elif user_option == 5:
            show_book()
            continue
        else:
            print("You entered Wrong input, Try Again...")
            continue


# TODO: CREATE LIBRARY FUNCTION
def library():
    print("Welcome to Library Department,type in your Genre OR" " SHOW " "to view Cart")
    print("1.Mystery")
    print("2.Fantasy")
    print("3.Romance")
    print("4.Textbook")
    print("5.SHOW")

    while True:
        genre_choice = str(input("> "))
        if genre_choice.lower() == ("mystery" and "fantasy") or ("romance" and "textbook"):
            access_book(genre_choice)
        elif genre_choice.lower() == "show":
            show_book()


# TODO: CREATE ACCESS TO BOOK GENRE
def access_book(book):
    genre_choice = book
    user_book = []
    if genre_choice.lower() == "mystery":
        print("{} Bookshelf".format(genre_choice).upper())
        for key, value in mystery.items():
            print("ISBN : {} , {}".format(key, value))

        book_checkout = input(" \n Please type in ISBN to add to cart...>>")

        # add isbn to new dictionary
        print(" \n Added to Cart: {}".format(mystery["{}".format(book_checkout)]))

        # user_books.append(mystery["{}".format(book_checkout)])
        test_book.update(mystery["{}".format(book_checkout)])

        # remove book from library and list remaining books on bookshelf
        mystery.pop('{}'.format(book_checkout), 'Key Not Found')
        print("\n Mystery Bookshelf: ")
        for key, value in mystery.items():
            print("ISBN : {} , {}".format(key, value))
        # print(mystery)

        book_options()
    elif genre_choice.lower() == "fantasy":
        print("{} Books".format(genre_choice))
        for key, value in fantasy.items():
            print("ISBN : {} , TITLE : {}".format(key, value))
        book_options()
    elif genre_choice.lower() == "romance":
        print("{} Books".format(genre_choice))
        for key, value in romance.items():
            print("ISBN : {} , TITLE : {}".format(key, value))
        book_options()
    elif genre_choice.lower() == "textbook":
        print("{} Books".format(genre_choice))
        for key, value in textbook.items():
            print("ISBN : {} , TITLE : {}".format(key, value))
        book_options()
    else:
        print("Wrong Input, Please type your Genre Correctly...")


# TODO: CREATE BOOK CHECKOUT
def checkout():
    book_checkout = input("Would you like to check out these books in your cart...\n>> [Y/N]   ")
    if book_checkout == "Y" or "y":
        for key, value in test_book.items():
            print("{}: {}".format(key, value))
        print("Thank you and Happy Reading!")
    elif book_checkout == "N" or "n":
        book_options()
    else:
        print("Invalid..Try Again")
        checkout()
    # add isbn to new dictionary
    # counter for how many books user has
    # delete isbn from old dictionary


# TODO: CREATE BOOK return
def return_book():
    print("Cart: ")
    for key, value in test_book.items():
        print("{}: {}".format(key, value))

    book_return = input("Please type in ISBN to return Item to Shelf...>>")
    if mystery[book_return] in mystery:
        mystery.update(book_return)
        # mystery['{}'.format(book_return)] = user_books[0]
    for key, value in mystery.items():
        print("ISBN : {} , {}".format(key, value))
        mystery['{}'.format(book_return)] = {'TITLE': '{}', 'AUTHOR': '{}'.format(key, value)}
    print(mystery)
    book_options()


# TODO: CREATE BOOK SHOW
def show_book():
    print("Cart: ")
    for key, value in test_book.items():
        print("{}: {}".format(key, value))
    print("Cart Total: {} items.".format(len(test_book)))
    return library()


# TODO: CREATE COMPUTER FUNCTION
def computer():
    print("Welcome to the Computer Lab")


# TODO: Create Menu to enter library or Computer lab
def main_menu():
    print("Welcome to the Public Library and Computer Lab")
    print("1.Enter the Library")
    print("2.Enter the Computer Lab")
    print("3.Quit")

    while True:
        # try:
        user_choice = str(input(">> "))
        # except TypeError as Argument:
        # print("Invalid Input, Please use numeric Number"), Argument
        # else:
        if user_choice == "1":
            print("You have Entered the Library....")
            library()
        elif user_choice == "2":
            print("You have entered the Computer Lab...")
            computer()
        elif user_choice == "3":
            break
        else:
            print("Wrong Input, Please try Again...")
            main_menu()
            continue
    print("Thank you...You have Exited the Menu")


print(main_menu())
