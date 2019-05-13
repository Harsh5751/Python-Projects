"""
A program that stores this book information
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry 
Update entry
Delete
Close

"""

from tkinter import *
import backendDatabase

#gets special event parameter cause its binded to a widget
def get_selected_row(event):
    #we get an error when clicking the listbox when empty. This try/except block fixes the issue
    try:
        #have a global variable so we don't need a return type. Having return type causes issues cause of event parameter when calling function which can't be removed.
        global selected_tuple
        #grab index 
        index = list1.curselection()[0]
        #get tuple at index 
        selected_tuple = list1.get(index)
    
        #click on the row in listbox and values of entry box will be filled with those
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    #delete previous item from list box before you press viewall again
    list1.delete(0, END)
    for row in backendDatabase.view():
        #END to put next element at last line
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    #Note: have to use .get() to get string from the object itself
    for row in backendDatabase.search(titleText.get(), authorText.get(), yearText.get(), ISBN_Text.get()):
        list1.insert(END, row)

def insert_command():
    backendDatabase.insert(titleText.get(), authorText.get(), yearText.get(), ISBN_Text.get())
    list1.delete(0, END)
    list1.insert(END, (titleText.get(), authorText.get(), yearText.get(), ISBN_Text.get()))

def delete_command():
    #grab the id of the selected tuple at index 0 of the tuple
    backendDatabase.delete(selected_tuple[0])

def update_command():
    backendDatabase.update(selected_tuple[0], titleText.get(), authorText.get(), yearText.get(), ISBN_Text.get())


#open tkinter GUI
window = Tk()

window.title("Library DataBase System")

#label and position for title
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

#label and position for author
l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

#label and position for year
l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

#label and position for ISBN
l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

#Textbox to enter title
titleText = StringVar()
e1 = Entry(window, textvariable = titleText)
e1.grid(row = 0, column = 1)

#Textbox to enter author
authorText = StringVar()
e2 = Entry(window, textvariable = authorText)
e2.grid(row = 0, column = 3)

#Textbox to enter year
yearText = StringVar()
e3 = Entry(window, textvariable = yearText)
e3.grid(row = 1, column = 1)

#Textbox to enter ISBN
ISBN_Text = StringVar()
e4 = Entry(window, textvariable = ISBN_Text)
e4.grid(row = 1, column = 3)

#Listbox to view stored books fetched 
list1 = Listbox(window, height = 6 , width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

#scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

#add scroll bar to list
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#bind function to widget element so this code activates when clicking listbox and points to get_selected_row function
list1.bind("<<ListboxSelect>>", get_selected_row)

#Adding button widgets to GUI; Remember don't pass brackets in command cause its not a function call but rather a pointer to the function
b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add Entry", width = 12, command = insert_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update Selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete Selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
