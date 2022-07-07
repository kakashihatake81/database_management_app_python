from tkinter import*
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("database management system")
root.iconbitmap("pixel_move.ico")
#root.geometry("400×400") #alt+0215 for multiply sign still not usable???
root.geometry("400x400")

#database

#create a database or connect one 

conn = sqlite3.connect("address_book.db")

#create cursor 

c = conn.cursor()

#create Tables for our database
#c.execute("""CREATE TABLE addresses(
#    first_name text,
 #  last_name text,
#    address text,
 #   city text,
 #   state text,
#    zipcode integer
 #   )""")

#create update function for our edit btn work
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
	# Create cursor
    c = conn.cursor()
    
    record_id= delete_box.get()
    
    c.execute(""" UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""",
              
              #here we are creating python dictionary to show our sql code what are the value of first,last etc
              {
                  "first": f_name_editor.get(),
                  "last": l_name_editor.get(),
                  "address": address_editor.get(),
                  "city": city_editor.get(),
                  "state": state_editor.get(),
                  "zipcode": zipcode_editor.get(),
                  
                  "oid": record_id      
                  }
              )
    
    #commit changes to our databases
    conn.commit()
    #close connection
    conn.close()
    
    #clear text boxes
    f_name_editor.delete(0,END)
    l_name_editor.delete(0,END)
    address_editor.delete(0,END)
    city_editor.delete(0,END)
    state_editor.delete(0,END)
    zipcode_editor.delete(0,END)

#create a function to edit existing record in database
def edit():
    editor = Tk()
    editor.title("edit record")
    editor.iconbitmap("pixel_move.ico")
    editor.geometry("400x250")
    
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
	# Create cursor
    c = conn.cursor()
    
    record_id = delete_box.get()
    
	# Query the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()
    
    #create global variable for text box so it can used by other function
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0,column=1,padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1,column=1,padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2,column=1,padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3,column=1,padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4,column=1,padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5,column=1, padx=30)
    

    #create labels of our text boxes

    f_name_label=Label(editor, text="first name")
    f_name_label.grid(row=0,column=0, pady=(10, 0))
    l_name_label=Label(editor, text="last name")
    l_name_label.grid(row=1,column=0)
    address_label=Label(editor, text="address")
    address_label.grid(row=2,column=0)
    city_label=Label(editor, text="city")
    city_label.grid(row=3,column=0)
    state_label=Label(editor, text="state")
    state_label.grid(row=4,column=0)
    zipcode_label=Label(editor, text="zipcode")
    zipcode_label.grid(row=5,column=0)
    
    #loop thru results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
    
    #create a save button to save edited record
    edit_btn=Button(editor, text="edit record", command=update)
    edit_btn.grid(row=11,column=0, columnspan=2, padx=10,pady=1 ,ipadx=145)
    
    


#create a function to delete a record in our database

def delete():
    #create a database or connect one 
    conn = sqlite3.connect("address_book.db")
    #create cursor 
    c = conn.cursor()
    
    #delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    
    
    
    #commit changes to our databases
    conn.commit()
    #close connection
    conn.close()



#create submit function for submit_btn
def submit():
    
    #create a database or connect one 
    conn = sqlite3.connect("address_book.db")
    #create cursor 
    c = conn.cursor()
    
    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get(),
			})
    
    
    #commit changes to our databases
    conn.commit()
    #close connection
    conn.close()
    
    
    #clear text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

def query():
	# Create a database or connect to one
	conn = sqlite3.connect('address_book.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM addresses")
	records = c.fetchall()
	# print(records)

	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[6]) + "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()



#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root, width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root, width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root, width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1, padx=30)

delete_box = Entry(root, width=30)
delete_box.grid(row=9,column=1, pady=5)

#create labels of our text boxes

f_name_label=Label(root, text="first name")
f_name_label.grid(row=0,column=0, pady=(10, 0))
l_name_label=Label(root, text="last name")
l_name_label.grid(row=1,column=0)
address_label=Label(root, text="address")
address_label.grid(row=2,column=0)
city_label=Label(root, text="city")
city_label.grid(row=3,column=0)
state_label=Label(root, text="state")
state_label.grid(row=4,column=0)
zipcode_label=Label(root, text="zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root, text="select id")
delete_box_label.grid(row=9,column=0, pady=5)

#create submite buttons
submit_btn=Button(root, text="submite record in database", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2, padx=10,pady=10, ipadx=100)

#create query button
query_btn=Button(root, text="show records", command=query)
query_btn.grid(row=7,column=0, columnspan=2, padx=10,pady=1 ,ipadx=137)

#create delete button
delete_btn=Button(root, text="delete record", command=delete)
delete_btn.grid(row=10,column=0, columnspan=2, padx=10,pady=1 ,ipadx=136)

#create update button
edit_btn=Button(root, text="edit record", command=edit)
edit_btn.grid(row=11,column=0, columnspan=2, padx=10,pady=1 ,ipadx=145)

#commit changes to our databases

conn.commit()

#close connection
conn.close()


root.mainloop()