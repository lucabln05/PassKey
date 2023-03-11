import tkinter as tk 

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
        frame = tk.Frame(gui.login_gui.login, pady=20)
        frame.pack()

        # Create the login form labels and entries
        username_label = tk.Label(frame, text="Salt:")
        username_label.grid(row=0, column=0, padx=10, pady=5)

        gui.login_gui.salt_entry = tk.Entry(frame, width=30)
        gui.login_gui.salt_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)

        gui.login_gui.password_entry = tk.Entry(frame, show="*", width=30)
        gui.login_gui.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create the login button

        login_button = tk.Button(frame, text="Login", bg="blue", fg="white", width=15, command=command.login)
        login_button.grid(row=2, column=1, pady=10)

        # Add padding to the frame
        frame.configure(pady=10)
        gui.login_gui.login.mainloop()

    def safe_gui():
        # Create the main window
        safe = tk.Tk()
        safe.title("Safe")

        # Set the window size and position
        window_width = 800
        window_height = 500
        screen_width = safe.winfo_screenwidth()
        screen_height = safe.winfo_screenheight()
        x_coordinate = (screen_width/2) - (window_width/2)
        y_coordinate = (screen_height/2) - (window_height/2)
        safe.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

        # Create a frame to hold the login form
        frame = tk.Frame(safe, pady=20)
        frame.pack()
        safe.mainloop()




class command():
    def login():
        # Get the values entered by the user
        global safe_salt 
        global safe_password
        safe_salt = gui.login_gui.salt_entry.get()
        safe_password = gui.login_gui.password_entry.get()
        db.check.check_password(safe_password, safe_salt)
        if db.check.check_password(safe_password, safe_salt) == True:
            print("Login successful")
            gui.login_gui.login.destroy()
            gui.safe_gui()
        else:
            print("Login failed")


gui.login_gui()