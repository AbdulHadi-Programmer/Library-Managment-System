# Library-Managment-System
# Overview
The provided code implements a simple Library Management Program. The program allows users to add, remove, update, and display books in the library. The library data is represented using two global variables: b_dic (a dictionary) and books (a list).

# Function Descriptions
1. var()
This function is defined but not utilized in the code. It declares two global variables, b_dic and books, which should be used throughout the program.

2. add()
The add() function allows the user to add a new book to the library. It prompts the user to input the book title, author's name, and ISBN number. The book is then added to the b_dic dictionary with a unique book ID, and the book title is also appended to the books list.

3. remove()
The remove() function allows the user to remove a book from the library. It prompts the user to enter the title of the book they wish to remove. If the book exists in the b_dic dictionary, it will be removed from both the dictionary and the books list. Otherwise, an appropriate message is displayed.

4. show()
The show() function displays a list of all books in the library along with their respective authors, ISBN numbers, and unique IDs. It iterates through the books list and retrieves the book details from the b_dic dictionary.

5. update()
The update() function allows the user to update the details of an existing book. The user is prompted to enter the title of the book they want to update. If the book exists in the b_dic dictionary, the function then asks the user to provide new details (author name and ISBN number) for the book. The provided information is then updated in the b_dic dictionary.

# Example Library Data
The example library data is provided as a dictionary named b_dic, where each book title serves as a key, and the associated value is another dictionary containing the book's author, ISBN number, and a unique ID.

# User Interaction Loop
The program includes a while loop that repeatedly presents the user with a menu of options:

1) Add a Book
2) Remove a Book
3) Update Book Details
4) Show All Books
5) Exit
The user can input the corresponding number to execute the desired operation. The loop continues until the user chooses to exit (option 5).
