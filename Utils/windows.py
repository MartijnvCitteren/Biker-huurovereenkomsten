import tkinter as tk

#setting size colors and fonts
window_width = 750
window_height = 750
window_bar_color = "546A7B"
button_color = "#C5D9E2"
button_font_large = "bold"

# Create a function to center a the middel of your screen
def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

def destroy_widgets(self):
    for widget in self.winfo_childeren():
        widget.destroy()

class StartWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap('C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)

        #define grid
        self.root.columnconfigure((0,1,2,3,4,5,6), weight=4)
        self.root.rowconfigure((0,1,2,3,4,5,6), weight=4)

        new_reservation_button = tk.Button(self, text="Nieuwe Reservering",font=button_font_large, padx=30, pady=30, bg=button_color, command=self.go_to_new_reservation_window)
        new_reservation_button.grid(row=2, column=2)

        adjust_reservation_button = tk.Button(self, text="Wijzig reservering", font=button_font_large, padx=30, pady=30, bg=button_color)
        adjust_reservation_button.grid(row=2, column=5)

        overview_reservations_button = tk.Button(self, text="Overzicht reserveringen",font=button_font_large, padx=30, pady=30, bg=button_color)
        overview_reservations_button.grid(row=4, column=3)
        self.grid()


    def go_to_new_reservation_window(self):
        self.destroy()
        NewReservationWindow(self.root)

    def go_to_change_reservation_window(self):
        pass

    def go_to_overview_window(self):
        pass

class NewReservationWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("NEW Reservation -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap('C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)

        email_entry = tk.Label(text="E-mail", width=10)
        email_entry.place(x="250", y="400")

root = tk.Tk()
StartWindow(root)
#NewReservationWindow(root)
root.mainloop()
