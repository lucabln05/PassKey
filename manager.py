import tkinter as tk 
from tkinter import ttk

#local import

import handler.databasehandler as db

class gui():
    def login_gui():

        # Create the main window
        gui.login_gui.login = tk.Tk()
        gui.login_gui.login.title("Login Page")

        # Set the window size and position
        window_width = 400
        window_height = 250
        screen_width = gui.login_gui.login.winfo_screenwidth()
        screen_height = gui.login_gui.login.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        gui.login_gui.login.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

        # Create a frame to hold the login form
        gui.login_gui.frame = tk.Frame(gui.login_gui.login, pady=20)
        gui.login_gui.frame.pack()


        # Create the login form labels and entries
        username_label = tk.Label(gui.login_gui.frame, text="Salt:")
        username_label.grid(row=0, column=0, padx=10, pady=5)

        gui.login_gui.salt_entry = tk.Entry(gui.login_gui.frame, width=30)
        gui.login_gui.salt_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(gui.login_gui.frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)

        gui.login_gui.password_entry = tk.Entry(gui.login_gui.frame, show="*", width=30)
        gui.login_gui.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create the login button
        create_button = tk.Button(gui.login_gui.frame, text="Create", bg="grey", fg="white", width=15, command=gui.create_gui)
        create_button.grid(row=2, column=0, pady=10)

        login_button = tk.Button(gui.login_gui.frame, text="Login", bg="#84d1eb", fg="white", width=15, command=command.login)
        login_button.grid(row=2, column=1, pady=10)


        # Add padding to the frame
        gui.login_gui.frame.configure(pady=10)
        gui.login_gui.login.mainloop()

    def create_gui():
       #create window for create the database with have input password and return the password and salt when the user click on create button or False if there is an error
        gui.create_gui.create = tk.Tk()
        gui.create_gui.create.title("Create Page")
        gui.create_gui.frame = tk.Frame(gui.create_gui.create, pady=20)
        gui.create_gui.frame.pack()

        # Set the window size and position
        window_width = 400
        window_height = 250
        screen_width = gui.create_gui.create.winfo_screenwidth()
        screen_height = gui.create_gui.create.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        gui.create_gui.create.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))


        # Create the login form labels and entries
        password_label = tk.Label(gui.create_gui.frame, text="Password:")
        password_label.grid(row=0, column=0, padx=10, pady=5)

        gui.create_gui.password_entry = tk.Entry(gui.create_gui.frame, show="*", width=30)
        gui.create_gui.password_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(gui.create_gui.frame, text="Confirm Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)

        gui.create_gui.confirm_password_entry = tk.Entry(gui.create_gui.frame, show="*", width=30)
        gui.create_gui.confirm_password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create the login button
        create_button = tk.Button(gui.create_gui.frame, text="Create", bg="#84d1eb", fg="white", width=15, command=command.create)
        create_button.grid(row=2, column=1, pady=10)

            

        # Add padding to the frame
        gui.create_gui.frame.configure(pady=10)
        gui.create_gui.create.mainloop()
        
    def safe_gui():
        # Create the main window
        gui.safe_gui.safe = tk.Tk()
        gui.safe_gui.safe.title("Safe")

        # Set the window size and position
        window_width = 800
        window_height = 500
        screen_width = gui.safe_gui.safe.winfo_screenwidth()
        screen_height = gui.safe_gui.safe.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        gui.safe_gui.safe.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
        # ADD THE MENU BAR
        menu_bar = tk.Menu(gui.safe_gui.safe)
        gui.safe_gui.safe.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Add", command=gui.add_gui)
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        menu_bar.add_cascade(label="File", menu=file_menu)


        try:
            data = db.decrypt_db(safe_password, safe_salt)

            tree = tk.ttk.Treeview(gui.safe_gui.safe, columns=("Service Name", "Username"))
           
            tree.pack(side=tk.LEFT, fill=tk.Y)
            
            vsb = tk.ttk.Scrollbar(gui.safe_gui.safe, orient="vertical", command=tree.yview)
            vsb.pack(side=tk.RIGHT, fill=tk.Y)
            tree.configure(yscrollcommand=vsb.set)
           
            tree.column("#0", width=0, stretch=tk.NO)
            
            tree.column("Service Name", width=100, stretch=tk.NO)
            tree.column("Username", width=100, stretch=tk.NO)
            
            tree.heading("Service Name", text="Service Name")
            tree.heading("Username", text="Username")

            for i, item in enumerate(data):
                tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4]))
            
            def on_double_click(event):
                item = tree.selection()[0]
                password = tree.item(item, "values")[2]
                gui.safe_gui.safe.clipboard_clear()
                gui.safe_gui.safe.clipboard_append(password)
            
            def on_one_click(event):
                # diplay the content of the selected row on the right side with a label
                item = tree.selection()[0]
                service_name = tree.item(item, "values")[0]
                username = tree.item(item, "values")[1]
                password = tree.item(item, "values")[2]
                url = tree.item(item, "values")[3]
                notes = tree.item(item, "values")[4]
                # create the labels
                service_name_label = tk.Label(frame, text="Service Name:")
                service_name_label.grid(row=0, column=0, padx=10, pady=5)
                username_label = tk.Label(frame, text="Username:")
                username_label.grid(row=1, column=0, padx=10, pady=5)
                password_label = tk.Label(frame, text="Password:")
                password_label.grid(row=2, column=0, padx=10, pady=5)
                url_label = tk.Label(frame, text="URL:")
                url_label.grid(row=3, column=0, padx=10, pady=5)
                notes_label = tk.Label(frame, text="Notes:")
                notes_label.grid(row=4, column=0, padx=10, pady=5)
                # create the entries
                service_name_entry = tk.Entry(frame, width=30)
                service_name_entry.grid(row=0, column=1, padx=10, pady=5)
                username_entry = tk.Entry(frame, width=30)

                username_entry.grid(row=1, column=1, padx=10, pady=5)
                password_entry = tk.Entry(frame, width=30)
                password_entry.grid(row=2, column=1, padx=10, pady=5)
                url_entry = tk.Entry(frame, width=30)

                url_entry.grid(row=3, column=1, padx=10, pady=5)
                notes_entry = tk.Entry(frame, width=30)
                notes_entry.grid(row=4, column=1, padx=10, pady=5)
                # insert the values
                service_name_entry.insert(0, service_name)
                username_entry.insert(0, username)
                password_entry.insert(0, password)
                url_entry.insert(0, url)
                notes_entry.insert(0, notes)

            

            tree.bind("<<TreeviewSelect>>", on_one_click)            
            tree.bind("<Double-1>", on_double_click)
            tree.pack()

        except Exception as e:
            print(e)
            
        # Create a frame to hold the login form
        frame = tk.Frame(gui.safe_gui.safe, pady=20)
        frame.pack()
        gui.safe_gui.safe.mainloop()

    def add_gui():
                gui.safe_gui.safe.destroy()
                add = tk.Tk()
                add.title("Add")
                add.geometry("300x300")
                # create the labels and entries
                service_name_label = tk.Label(add, text="Service Name:")
                service_name_label.grid(row=0, column=0, padx=10, pady=5)
                service_name_entry = tk.Entry(add, width=30)
                service_name_entry.grid(row=0, column=1, padx=10, pady=5)
                username_label = tk.Label(add, text="Username:")
                username_label.grid(row=1, column=0, padx=10, pady=5)
                username_entry = tk.Entry(add, width=30)
                username_entry.grid(row=1, column=1, padx=10, pady=5)
                password_label = tk.Label(add, text="Password:")
                password_label.grid(row=2, column=0, padx=10, pady=5)
                password_entry = tk.Entry(add, width=30)
                password_entry.grid(row=2, column=1, padx=10, pady=5)
                url_label = tk.Label(add, text="URL:")
                url_label.grid(row=3, column=0, padx=10, pady=5)
                url_entry = tk.Entry(add, width=30)
                url_entry.grid(row=3, column=1, padx=10, pady=5)
                notes_label = tk.Label(add, text="Notes:")
                notes_label.grid(row=4, column=0, padx=10, pady=5)
                notes_entry = tk.Entry(add, width=30)
                notes_entry.grid(row=4, column=1, padx=10, pady=5)
                # create the add button
                def addhandler():
                    objectname = service_name_entry.get()
                    username = username_entry.get()
                    password = password_entry.get()
                    url = url_entry.get()
                    notes = notes_entry.get()

                    content = [objectname, username, password, url, notes]

                    if db.encrypt_object(content, safe_password, safe_salt) == True:
                        print("Object encrypted and added to the database")
                        add.destroy()
                        gui.safe_gui()
                    else:
                        print("Error adding object to the database")

                add_button = tk.Button(add, text="Add", bg="blue", fg="white", width=15, command=addhandler)
                add_button.grid(row=5, column=1, pady=10)

                


                add.mainloop()

class command():
    def login():
        # Get the values entered by the user
        global safe_salt 
        global safe_password
        safe_salt = gui.login_gui.salt_entry.get()
        safe_password = gui.login_gui.password_entry.get()
        db.check.check_password(safe_password, safe_salt)
        if db.check.check_password(safe_password, safe_salt) == True:
            gui.login_gui.login.destroy()
            gui.safe_gui()
        else:
            tk.Label(gui.login_gui.frame, text="Wrong password or salt").grid(row=3, column=0, padx=0, pady=0)
            gui.login_gui.salt_entry.delete(0, tk.END)
            gui.login_gui.password_entry.delete(0, tk.END)
    
    def create():
            
            if gui.create_gui.password_entry.get() == gui.create_gui.confirm_password_entry.get():
                try: 
                    data = db.create_db(gui.create_gui.password_entry.get())
                    if data != False:
                        
                        for widget in gui.create_gui.frame.winfo_children():
                            widget.destroy()

                        tk.Label(gui.create_gui.frame, text="Please save following Password and Salt.").grid(row=1, column=0, padx=0, pady=0)

                        tk.Label(gui.create_gui.frame, text=f"Salt: {data[1]}").grid(row=2, column=0, padx=0, pady=0)
                        tk.Label(gui.create_gui.frame, text=f"Password: {data[0]}").grid(row=3, column=0, padx=0, pady=0)

                        tk.Label(gui.create_gui.frame, text="IF YOU FORGOT YOUR PASSWORD OR SALT OF YOUR DATABASE,", bg="red").grid(row=4, column=0, padx=0, pady=0)
                        tk.Label(gui.create_gui.frame, text="YOU WILL NOT BE ABLE TO ACCESS YOUR PASSWORDS.", bg="red").grid(row=5, column=0, padx=0, pady=0)
                        tk.Label(gui.create_gui.frame, text="PLEASE SAVE YOUR PASSWORD AND SALT IN A SAFE PLACE.", bg="red").grid(row=5, column=0, padx=0, pady=0)

                        tk.Label(gui.create_gui.frame, text="Database Created", bg="green", width=20).grid(row=7, column=0, padx=0, pady=0)
                        tk.Label(gui.create_gui.frame, text="Salt and Password was copied in clipboard,", bg="green", width=20).grid(row=8, column=0, padx=0, pady=0)
                        tk.Label(gui.create_gui.frame, text="PLEASE SAVE IT.", bg="green", width=20).grid(row=9, column=0, padx=0, pady=0)
                        # copies the password and salt to the clipboard
                        gui.create_gui.frame.clipboard_clear()
                        gui.create_gui.frame.clipboard_append(f"Salt: {data[1]} Password: {data[0]}")

                        recovery_file = open("recovery.txt", "w")
                        recovery_file.write(f"Salt: {data[1]} Password: {data[0]}")
                        recovery_file.close()

                    else:
                        # clear row 3
                        for widget in gui.create_gui.frame.grid_slaves(row=3):
                            widget.destroy()
                        tk.Label(gui.create_gui.frame, text="Password is to short.").grid(row=3, column=1, padx=0, pady=0)

                except:
                                            # clear row 3
                    for widget in gui.create_gui.frame.grid_slaves(row=3):
                            widget.destroy()
                    tk.Label(gui.create_gui.frame, text="Error").grid(row=3, column=0, padx=1, pady=0)
            else:
                                        # clear row 3
                for widget in gui.create_gui.frame.grid_slaves(row=3):
                            widget.destroy()
                tk.Label(gui.create_gui.frame, text="Password and Confirm Password does not match.").grid(row=3, column=1, padx=0, pady=0)

gui.login_gui()