mystery = {
    'I1001': {'TITLE': "The Last Thing He Told Me ", 'AUTHOR': 'Laura Dave'},
    'I1002': {'TITTLE': "Sweet Water ", 'AUTHOR': 'Cara Reinard'},
    'I1003': {'TITTLE': "Local Woman missing ", 'AUTHOR': 'Mary Kubica'},
    'I1004': {'TITTLE': "The Maidens", 'AUTHOR': 'Alex Micaelides '}
}

fantasy = {
    "2007": {'TITLE': 'The Queens Weapons', 'AUTHOR': 'Anne Bisho'},
    "2008": {'TITLE': 'The Last Druid', 'AUTHOR': 'Terry Brooks'},
    "2009": {'TITLE': 'A Deadly Education', 'AUTHOR': 'Naomi Novik'},
    "2010": {'TITLE': 'Spy,Spy Again', 'AUTHOR': 'Mercedes Lackey'}
}

romance = {
    "3002": {'TITLE': 'Pride and Prejudice', 'AUTHOR': 'Jane Austen'},
    "3004": {'TITLE': 'Jane Eyre', 'AUTHOR': 'Charlotte Bronte'},
    "3006": {'TITLE': 'Gone with the Wind', 'AUTHOR': 'Margaret Mitchell'},
    "3008": {'TITLE': 'The Notebook', 'AUTHOR': 'Nicholas Sparks'}
}

textbook = {
    "4003": {'TITLE': 'Python Crash Course', 'AUTHOR': 'Eric Matthews'},
    "4004": {'TITLE': 'Automate the Boring Stuff with Python', 'AUTHOR': 'Al Sweigart'},
    "4005": {'TITLE': 'Learning Python', 'AUTHOR': 'Mark Lutz'},
    "4006": {'TITLE': 'Head-First Python', 'AUTHOR': 'Paul Barry'},
}

# TODO: Create empty dictionary to add and return books
return_add_books = {}


# TODO: CREATE COMPUTER FUNCTION
def computer():
    print("Welcome to the Computer Lab")


# TODO: CREATE ACCESS TO BOOK GENRE
def access_book(book):
    genre_choice = book

    if genre_choice.lower() == "mystery":
        print("{} Bookshelf".format(genre_choice).upper())
        for key, value in mystery.items():
            print("ISBN : {} , {}".format(key, value))

        book_checkout = input(" \n Please type in ISBN to add to cart...>>").upper()
        print(mystery[book_checkout])

        # add isbn to new dictionary
        return_add_books.update({book_checkout: mystery[book_checkout]})
        print(" \n Added to Cart:ISBN: {}".format(mystery[book_checkout]))

        # Remove book from Mystery bookshelf
        mystery.pop(book_checkout, 'Key Not Found')

        # print updated bookshelf with book removed
        print("\n Mystery Bookshelf: ")
        for key, value in mystery.items():
            print("ISBN : {} , {}".format(key, value))

        print('book cart test')
        print(return_add_books)
        book_options()
    elif genre_choice.lower() == "fantasy":
        print("{} Books".format(genre_choice))
        for key, value in fantasy.items():
            print("ISBN : {} , TITLE : {}".format(key, value))

        book_checkout = input(" \n Please type in ISBN to add to cart...>>").upper()
        print(fantasy[book_checkout])

        # add isbn to new dictionary
        return_add_books.update({book_checkout: fantasy[book_checkout]})
        print(" \n Added to Cart:ISBN: {}".format(fantasy[book_checkout]))

        # Remove book from Mystery bookshelf
        fantasy.pop(book_checkout, 'Key Not Found')

        # print updated bookshelf with book removed
        print("\n Fantasy Bookshelf: ")
        for key, value in fantasy.items():
            print("ISBN : {} , {}".format(key, value))
        book_options()
    elif genre_choice.lower() == "romance":
        print("{} Books".format(genre_choice))
        for key, value in romance.items():
            print("ISBN : {} , TITLE : {}".format(key, value))

        book_checkout = input(" \n Please type in ISBN to add to cart...>>").upper()
        print(romance[book_checkout])

        # add isbn to new dictionary
        return_add_books.update({book_checkout: romance[book_checkout]})
        print(" \n Added to Cart:ISBN: {}".format(romance[book_checkout]))

        # Remove book from Mystery bookshelf
        romance.pop(book_checkout, 'Key Not Found')

        # print updated bookshelf with book removed
        print("\n Romance Bookshelf: ")
        for key, value in romance.items():
            print("ISBN : {} , {}".format(key, value))
        book_options()
    elif genre_choice.lower() == "textbook":
        print("{} Books".format(genre_choice))
        for key, value in textbook.items():
            print("ISBN : {} , TITLE : {}".format(key, value))

        book_checkout = input(" \n Please type in ISBN to add to cart...>>").upper()
        print(textbook[book_checkout])

        # add isbn to new dictionary
        return_add_books.update({book_checkout: textbook[book_checkout]})
        print(" \n Added to Cart:ISBN: {}".format(textbook[book_checkout]))

        # Remove book from Mystery bookshelf
        textbook.pop(book_checkout, 'Key Not Found')

        # print updated bookshelf with book removed
        print("\n Textbook Bookshelf: ")
        for key, value in textbook.items():
            print("ISBN : {} , {}".format(key, value))
        book_options()
    else:
        print("Wrong Input, Please type your Genre Correctly...")


# TODO: CREATE BOOK CHECKOUT
def checkout():
    book_checkout = input("Would you like to check out these books in your cart...\n>> [Y/N]   ")
    if book_checkout == "Y" or "y":
        for key, value in return_add_books.items():
            # Prints out all books in cart
            print("ISBN: {}: {}".format(key, value))
            # counter for how many books user has
            print('Total Books: {}'.format(len(return_add_books)))
        print("Thank you and Happy Reading!")
    elif book_checkout == "N" or "n":
        book_options()
    else:
        print("Invalid..Try Again")
        checkout()


# TODO: CREATE BOOK return
def return_book():
    print("Cart: ")
    for key, value in return_add_books.items():
        print("{}: {}".format(key, value))

    book_return = input("Please type in ISBN to return Item to Shelf...>>")



    book_options()


# TODO: CREATE BOOK SHOW
def show_book():
    print("Cart: ")
    for key, value in return_add_books.items():
        print("{}: {}".format(key, value))
    print("Cart Total: {} items.".format(len(return_add_books)))
    return library()


# TODO: CREATE options for book functions
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
