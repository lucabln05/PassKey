import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk
import webbrowser

#local import

import handler.databasehandler as db

class gui():
    def login_gui():

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        gui.login_gui.frame = ctk.CTk()
        gui.login_gui.frame.geometry("400x400")
        gui.login_gui.frame.title("PassKey")

        # Set the label
        label = ctk.CTkLabel(gui.login_gui.frame,text="PassKey")
        
        label.pack(pady=20)
        
        # Create a frame
        frame = ctk.CTkFrame(master=gui.login_gui.frame)
        frame.pack(pady=20,padx=40,
                fill='both',expand=True)
        
        # Set the label inside the frame
        label = ctk.CTkLabel(master=frame,
                            text='Vault Login')
        label.pack(pady=12,padx=10)
        
        # Create the text box for taking
        # username input from user
        gui.login_gui.salt_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Salt")
        gui.login_gui.salt_entry.pack(pady=12,padx=10)
        
        # Create a text box for taking 
        # password input from user
        gui.login_gui.password_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Password",
                                show="*")
        gui.login_gui.password_entry.pack(pady=12,padx=10)
        
        # Create a login button to login
        button = ctk.CTkButton(master=frame,
                            text='Login', command=command.login)
        button.pack(pady=12,padx=10)
        
        # Create a create button to login
        button = ctk.CTkButton(master=frame,
                            text='Create', command=gui.create_gui)
        button.pack(pady=12,padx=10)
        
        gui.login_gui.frame.mainloop()

    def create_gui():
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        gui.create_gui.frame = ctk.CTk()
        gui.create_gui.frame.geometry("400x400")
        gui.create_gui.frame.title("PassKey")

        # Set the label
        label = ctk.CTkLabel(gui.create_gui.frame,text="PassKey Create")
        
        label.pack(pady=20)
        
        # Create a frame
        frame = ctk.CTkFrame(master=gui.create_gui.frame)
        frame.pack(pady=20,padx=40,
                fill='both',expand=True)
        
        # Set the label inside the frame
        label = ctk.CTkLabel(master=frame,
                            text='Create Vault')
        label.pack(pady=12,padx=10)
        
        # Create the text box for taking
        # username input from user
        gui.create_gui.password_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Password", show="*")
        gui.create_gui.password_entry.pack(pady=12,padx=10)
        
        # Create a text box for taking 
        # password input from user
        gui.create_gui.confirm_password_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Confirm Password",
                                show="*")
        gui.create_gui.confirm_password_entry.pack(pady=12,padx=10)
        
        # Create a create button to create vault
        button = ctk.CTkButton(master=frame,
                            text='Login', command=command.create)
        button.pack(pady=12,padx=10)

        
        gui.create_gui.frame.mainloop()
        
    def safe_gui():     
        # Create the main window
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        
        gui.safe_gui.safe = ctk.CTk()
        gui.safe_gui.safe.title("PassKey")
        gui.safe_gui.safe.geometry("800x500")
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
             
            #search bar above the treeview
            search_bar = tk.Entry(gui.safe_gui.safe, width=30)
            search_bar.pack(side=tk.TOP, fill=tk.X)
            search_bar.bind("<KeyRelease>", lambda e: search_tree(e, tree, data, 0))

    
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
            
            # Create a search box
            search_frame = tk.Frame(gui.safe_gui.safe, pady=10)
            search_frame.pack(side=tk.TOP)

            search_label = tk.Label(search_frame, text="Search:")
            search_label.pack
            
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

                #display password in **** if the user clicks on the password entry reveal the password and kopie it to the clipboard
                password_entry = tk.Entry(frame, width=30, show="*")
                password_entry.grid(row=2, column=1, padx=10, pady=5)
                

               
                password_entry.bind("<Button-1>", lambda e: on_copy_password(e))
                def on_copy_password(event):
                    #zeige nun dem nutzer das das password kopiert wurde rechts neben dem password entry mit einem label
                    password_copied_label = tk.Label(frame, text="Password copied to clipboard", fg="green")
                    password_copied_label.grid(row=2, column=2, padx=10, pady=5)
                    password_copied_label.after(1000, lambda: password_copied_label.grid_forget())
                    on_double_click(event)

                
                # make clickable url
                url_entry = tk.Label(frame, text=url, fg="#282c34", cursor="hand2")
                url_entry.grid(row=3, column=1, padx=10, pady=5)
                url_entry.bind("<Button-1>", lambda e: webbrowser.open(url))
                
                notes_entry = tk.Entry(frame, width=30)
                notes_entry.grid(row=4, column=1, padx=10, pady=5)
                # insert the values
                service_name_entry.insert(0, service_name)
                username_entry.insert(0, username)
                password_entry.insert(0, password)
                notes_entry.insert(0, notes)

            def search_tree(event, tree, data, col):
                 
                search_term = search_bar.get()
                tree.delete(*tree.get_children())
                for item in data:
                    if search_term.lower() in item[col].lower():
                        tree.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4]))
            
            def delete_row(event):
                item = tree.selection()[0]
                service_name = tree.item(item, "values")[0]
                username = tree.item(item, "values")[1]
                print(service_name, username)
                # delete the row from the database
                if db.delete_object(service_name, username, safe_password, safe_salt):
                    tree.delete(item)
                else:
                    print("Error deleting row")


            tree.bind("<<TreeviewSelect>>", on_one_click)            
            tree.bind("<Double-1>", on_double_click)
            tree.bind("<Button-3>", delete_row)

            tree.pack()

        except Exception as e:
            print(e)
            
        # Create a frame to hold the login form
        frame = tk.Frame(gui.safe_gui.safe, pady=20)
        frame.pack()
        gui.safe_gui.safe.mainloop()

    def add_gui():
        gui.safe_gui.safe.destroy()
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        
        gui.add_gui.frame = ctk.CTk()
        gui.add_gui.frame.geometry("400x600")
        gui.add_gui.frame.title("PassKey")

        # Set the label
        label = ctk.CTkLabel(gui.add_gui.frame,text="PassKey Add")
        
        label.pack(pady=20)
        
        # Create a frame
        frame = ctk.CTkFrame(master=gui.add_gui.frame)
        frame.pack(pady=20,padx=40,
                fill='both',expand=True)
        
        # Set the label inside the frame
        label = ctk.CTkLabel(master=frame,
                                text='Add Service')
        label.pack(pady=12,padx=10)
        service_name_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Service Name")
        service_name_entry.pack(pady=12,padx=10)
        username_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Username")
        username_entry.pack(pady=12,padx=10)
        password_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Password")
        password_entry.pack(pady=12,padx=10)
        url_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="URL")
        url_entry.pack(pady=12,padx=10)
        notes_entry= ctk.CTkEntry(master=frame,
                                placeholder_text="Notes")
        notes_entry.pack(pady=12,padx=10)
        

        def addhandler():
                objectname = service_name_entry.get()
                username = username_entry.get()
                password = password_entry.get()
                url = url_entry.get()
                notes = notes_entry.get()

                content = [objectname, username, password, url, notes]

                if db.encrypt_object(content, safe_password, safe_salt) == True:
                    print("Object encrypted and added to the database")
                    gui.add_gui.frame.destroy()
                    gui.safe_gui()
                else:
                    print("Error adding object to the database")
        
        # Create a create button to create vault
        button = ctk.CTkButton(master=frame,
                                text='Add', command=addhandler)
        button.pack(pady=12,padx=10)

        
        gui.add_gui.frame.mainloop()

class command():
    def login():
        # Get the values entered by the user
        global safe_salt 
        global safe_password
        safe_salt = gui.login_gui.salt_entry.get()
        safe_password = gui.login_gui.password_entry.get()
        db.check.check_password(safe_password, safe_salt)
        if db.check.check_password(safe_password, safe_salt) == True:
            gui.login_gui.frame.destroy()
            gui.safe_gui()
    
    def create():
            
            if gui.create_gui.password_entry.get() == gui.create_gui.confirm_password_entry.get():
                try: 
                    data = db.create_db(gui.create_gui.password_entry.get())
                    if data != False:
                        
                        for widget in gui.create_gui.frame.winfo_children():
                            widget.destroy()

                        labelueb = ctk.CTkLabel(master=gui.create_gui.frame,
                                        text=f'Vault created successfully!')
                        labelueb.pack(pady=12,padx=10)

                        label1 = ctk.CTkLabel(master=gui.create_gui.frame,
                                        text=f'''
Salt:  {data[1]} 
Password:  {data[0]}''')
                        label1.pack(pady=12,padx=10)

                        label2 = ctk.CTkLabel(master=gui.create_gui.frame,
                                        text=f'Please save this information in a safe place.')
                        label2.pack(pady=12,padx=10)
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
                        label1 = ctk.CTkLabel(master=gui.create_gui.frame,
                            text=f'Password to short, or Vault already exists.')
                        label1.pack(pady=12,padx=10)

                except:
                                            # clear row 3
                    for widget in gui.create_gui.frame.grid_slaves(row=3):
                            widget.destroy()
                    label1 = ctk.CTkLabel(master=gui.create_gui.frame,
                            text=f'Error creating vault.')
                    label1.pack(pady=12,padx=10)
            else:
                                        # clear row 3
                for widget in gui.create_gui.frame.grid_slaves(row=3):
                            widget.destroy()
                label1 = ctk.CTkLabel(master=gui.create_gui.frame,
                            text=f'Passwords do not match.')
                label1.pack(pady=12,padx=10)
gui.login_gui()