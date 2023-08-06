def var():
    global b_dic
    global books

def add():
    var()
    
    bk = input("Enter the Book: ")
    a_name = input("Enter the Book Author name: ")
    num = input("Enter the ISBN num: ")

    book_id = len(b_dic) + 1
    b_dic[bk] = {"id": book_id, "Author": a_name, "ISBN": num}
    books.append(bk)

def remove():
    var()
    r = input("Enter the Book to remove: ")
    if r in b_dic:
        del b_dic[r]
        books.remove(r)
        print(f"{r} has been removed from the library.")
    else:
        print(f"{r} not found in the library.")

def show():
    var()
    print("List of Books:")
    for book in books:
        print(f"{book} - Author: {b_dic[book]['Author']}, ISBN: {b_dic[book]['ISBN']}, ID: {b_dic[book]['id']}")
    print("End of Book List")

def update():
    var()
    book_to_update = input("Enter the Book to update: ")
    if book_to_update in b_dic:
        print("Enter new details:")
        new_author = input("New Author Name: ")
        new_isbn = input("New ISBN: ")

        b_dic[book_to_update]["Author"] = new_author
        b_dic[book_to_update]["ISBN"] = new_isbn

        print(f"{book_to_update} has been updated with new details.")
    else:
        print(f"{book_to_update} not found in the library.")

# Example of usage:
print("Welcome to my Library Management Program")
b_dic = {
    "Rich Dad Poor Dad": {"id": 1, "Author": "Robert T. Kiyosaki", "ISBN": "978-1612680194"},
    "The Millionaire Next Door": {"id": 2, "Author": "Thomas J. Stanley", "ISBN": "978-1589795471"},
    "The Psychology of Money": {"id": 3, "Author": "Morgan Housel", "ISBN": " 978-0857197689"},
    "Thinking, Fast and Slow": {"id": 4, "Author": "Daniel Kahneman", "ISBN": "978-0374533557"},
    "The Intelligent Investor": {"id": 5, "Author": "Benjamin Graham", "ISBN": "978-0060555665"},
    "A Random Walk Down Wall Street": {"id": 6, "Author": "Burton G. Malkiel", "ISBN": "978-0393352245"},
    "How to Win Friends and Influence People": {"id": 7, "Author": "Dale Carnegie", "ISBN": "978-0671027032"},
    "Atomic Habits": {"id": 8, "Author": "James Clear", "ISBN": "978-0735211292"},
    "Grit: The Power of Passion and Perseverance": {"id": 9, "Author": "Angela Duckworth", "ISBN": "978-1501111112"},
    "Mindset: The New Psychology of Success": {"id": 10, "Author": "Carol S. Dweck", "ISBN": "978-0345472328"},
    "You Are a Badass": {"id": 11, "Author": "Jen Sincero", "ISBN": "978-0762447695"},
    "The 7 Habits of Highly Effective People": {"id": 12, "Author": "Stephen R. Covey", "ISBN": "978-0743269513"},
    "The Four Hour Work Week": {"id": 13, "Author": "Timothy Ferriss", "ISBN": "978-0307465351"},
    "Emotional Intelligence": {"id": 14, "Author": "Daniel Goleman", "ISBN": "978-0553383713"}
}

books = list(b_dic.keys())  

while True:
    print("\nOptions:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Update Book Details")
    print("4. Show All Books")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add()
    elif choice == "2":
        remove()
    elif choice == "3":
        update()
    elif choice == "4":
        show()
    elif choice == "5":
        print("Goodbye! Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
