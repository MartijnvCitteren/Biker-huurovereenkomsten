import tkinter as tk
from tkinter import ttk
import Utils.crud_functionalities as crud
import csv


# setting size colors and fonts
window_width = 750
window_height = 750
window_bar_color = "546A7B"
button_color = "#C5D9E2"
button_font_large = "bold"
pad_y = 10
icon = "C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico"


# Create a function to center at the middel of your screen
def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

#create function to delete widgets
def delete_widgets(self):
    for widget in self.winfo_children():
        widget.destroy()

class StartWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(icon)
        center_window(window_width, window_height)

        new_reservation_button = tk.Button(self, text="Nieuwe Reservering", font=button_font_large, width=15, padx=30,
                                           pady=30, bg=button_color, command=self.go_to_new_reservation_window)
        new_reservation_button.grid(row=0, column=0, padx=35, pady=150)

        update_reservation_button = tk.Button(self, text="Wijzig reservering", font=button_font_large, width=15,
                                              padx=30, pady=30, bg=button_color,
                                              command=self.go_to_update_reservation_window)
        update_reservation_button.grid(row=0, column=2, padx=30, pady=150)

        overview_reservations_button = tk.Button(self, text="Overzicht reserveringen", font=button_font_large, width=15,
                                                 padx=30, pady=30, bg=button_color, command=self.go_to_overview_window)
        overview_reservations_button.grid(row=2, column=1, pady=25)
        self.grid()

    def go_to_new_reservation_window(self):
        delete_widgets(self)
        self.destroy()
        NewReservationWindow(self.root)

    def go_to_update_reservation_window(self):
        delete_widgets(self)
        self.destroy()
        UpdateReservationWindow(self.root)

    def go_to_overview_window(self):
        delete_widgets(self)
        self.destroy()
        ViewAllReservationsWindow(self.root)


class NewReservationWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("NEW Reservation -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(icon)
        center_window(window_width, window_height)
        self.to_home_button = tk.Button(self, text="Home", font=button_font_large, width=10, padx=5, pady=5, bg=button_color, command=self.to_home)
        self.to_home_button.grid(row=0, column=3, padx=10, pady=10, sticky="we")

        rows_above = 0
        self.create_reservation_fields(rows_above)

        self.make_reservation_button = tk.Button(self, text="Reserveer", font=button_font_large, width=10, padx=5,
                                                 pady=5, bg='#AEE4A0', command=self.save_to_csv)
        self.make_reservation_button.grid(row=10, column=3, padx=10, pady=10, sticky="we")
        self.grid()

    def create_reservation_fields(self, rows_above):
        # define grid
        self.root.columnconfigure((0, 1, 2, 3), weight=15)

        email_label = tk.Label(self, text="E-mail", width=25)
        email_label.grid(row=1+rows_above, column=0, sticky="w")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1+rows_above, column=1, sticky="we", pady=pad_y, columnspan=3)

        first_name_label = tk.Label(self, text="Voornaam", width=25)
        first_name_label.grid(row=2+rows_above, column=0)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=2+rows_above, column=1, sticky="we", pady=pad_y)

        family_name_label = tk.Label(self, text="Achternaam", width=25)
        family_name_label.grid(row=2+rows_above, column=2)
        self.family_name_entry = tk.Entry(self)
        self.family_name_entry.grid(row=2+rows_above, column=3, sticky="we", pady=pad_y)

        street_name_label = tk.Label(self, text="Straatnaam", width=25)
        street_name_label.grid(row=3+rows_above, column=0)
        self.street_name_entry = tk.Entry(self)
        self.street_name_entry.grid(row=3+rows_above, column=1, sticky="we", pady=pad_y)

        adress_num_label = tk.Label(self, text="Huisnummer", width=25)
        adress_num_label.grid(row=3+rows_above, column=2)
        self.adress_num_entry = tk.Entry(self)
        self.adress_num_entry.grid(row=3+rows_above, column=3, sticky="we", pady=pad_y)

        zip_code_label = tk.Label(self, text="Postcode", width=25)
        zip_code_label.grid(row=4+rows_above, column=0)
        self.zip_code_entry = tk.Entry(self)
        self.zip_code_entry.grid(row=4+rows_above, column=1, sticky="we", pady=pad_y)

        city_label = tk.Label(self, text="Stad", width=25)
        city_label.grid(row=4+rows_above, column=2)
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=4+rows_above, column=3, sticky="we", pady=pad_y)

        man_bike_label = tk.Label(self, text="Aantal herenfietsen", width=25)
        man_bike_label.grid(row=5+rows_above, column=0, columnspan=2, sticky='w')
        self.num_man_bikes_entry = tk.Entry(self)
        self.num_man_bikes_entry.grid(row=5+rows_above, column=1, columnspan=2, sticky='w', pady=pad_y)

        woman_bike_label = tk.Label(self, text="Aantal vrouwenfietsen", width=25)
        woman_bike_label.grid(row=5+rows_above, column=2, columnspan=2, sticky='w')
        self.num_woman_bikes_entry = tk.Entry(self)
        self.num_woman_bikes_entry.grid(row=5+rows_above, column=3, columnspan=2, sticky='w', pady=pad_y)

        E_bike_label = tk.Label(self, text="Aantal Elektrische fietsen", width=25)
        E_bike_label.grid(row=6+rows_above, column=0, columnspan=2, sticky='w')
        self.num_E_bikes_entry = tk.Entry(self)
        self.num_E_bikes_entry.grid(row=6+rows_above, column=1, columnspan=2, sticky='w', pady=pad_y)

        child_bicycle_seat_label = tk.Label(self, text="Aantal kinderzitjes", width=25)
        child_bicycle_seat_label.grid(row=7+rows_above, column=0, columnspan=2, sticky='w')
        self.num_child_seat_entry = tk.Entry(self)
        self.num_child_seat_entry.grid(row=7+rows_above, column=1, columnspan=2, sticky='w', pady=pad_y)

        helmet_label = tk.Label(self, text="Aantal helmen", width=25)
        helmet_label.grid(row=7+rows_above, column=2, columnspan=2, sticky='w')
        self.num_helmets_entry = tk.Entry(self)
        self.num_helmets_entry.grid(row=7+rows_above, column=3, columnspan=2, sticky='w', pady=pad_y)

        insurance_label = tk.Label(self, text="Verzekeringsnummer", width=25)
        insurance_label.grid(row=8+rows_above, column=0)
        self.insurance_entry = tk.Entry(self)
        self.insurance_entry.grid(row=8+rows_above, column=1, sticky="we", pady=pad_y)

        employee_label = tk.Label(self, text="Medeweker nr.", width=25)
        employee_label.grid(row=8+rows_above, column=2)
        self.employee_entry = tk.Entry(self)
        self.employee_entry.grid(row=8+rows_above, column=3, sticky="we")

        start_rent_label = tk.Label(self, text="Startdatum huur (dd-mm-jjjj)", width=25)
        start_rent_label.grid(row=9+rows_above, column=0, stick="w")
        self.start_rent_entry = tk.Entry(self)
        self.start_rent_entry.grid(row=9+rows_above, column=1, sticky="we", pady=pad_y)

        end_rent_label = tk.Label(self, text="einddatum huur (dd-mm-jjjj)", width=25)
        end_rent_label.grid(row=9+rows_above, column=2)
        self.end_rent_entry = tk.Entry(self)
        self.end_rent_entry.grid(row=9+rows_above, column=3, sticky="we", pady=pad_y)

        reservation_date_label = tk.Label(self, text="Reserveringsdatum (dd-mm-jjjj)", width=25)
        reservation_date_label.grid(row=10+rows_above, column=0)
        self.reservation_date_entry = tk.Entry(self)
        self.reservation_date_entry.grid(row=10+rows_above, column=1, sticky="we", pady=pad_y)

        self.grid()

    def to_home(self):
        delete_widgets(self)
        self.destroy()
        StartWindow(self.root)

    def save_to_csv(self):
        crud.write_to_csv(self)

class UpdateReservationWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("UPDATE Reservation -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(icon)
        center_window(window_width, window_height)

        self.to_home_button = tk.Button(self, text="Home", font=button_font_large, width=10, padx=5, pady=5, bg=button_color, command=self.to_home)
        self.to_home_button.grid(row=0, column=3, padx=10, pady=10, sticky="we")

        search_email_label = tk.Label(self, text="Zoek email-adres", width=25)
        search_email_label.grid(row=1, column=0, sticky="we")
        self.search_email_entry = tk.Entry(self)
        self.search_email_entry.grid(row=1, column=1, sticky="we", pady=pad_y, columnspan=2)
        search_email_button = tk.Button(self, text="zoek", font=button_font_large, width=10, padx=5, pady=5, command=self.search_and_fil)
        search_email_button.grid(row=1, column=3, padx= 10, pady=25, sticky="we")

        rows_above = 1
        NewReservationWindow.create_reservation_fields(self,rows_above)

        self.delete_button = tk.Button(self, text="Verwijder", font=button_font_large, width=10, padx=5, pady=5,
                                                 bg='#B06D74', command=self.delete_data)
        self.delete_button.grid(row=11, column=2, padx=10, pady=10)
        self.make_reservation_button = tk.Button(self, text="Wijzig", font=button_font_large, width=10, padx=5, pady=5,
                                                 bg='#AEE4A0', command=self.update_data)
        self.make_reservation_button.grid(row=11, column=3, padx=10, pady=10)
        self.grid()


    def search_and_fil(self):
        crud.fill_update_fields(self)

    def delete_data(self):
        crud.delete_row(self)
        self.to_home()

    def update_data(self):
        crud.update(self)

    def to_home(self):
        delete_widgets(self)
        self.destroy()
        StartWindow(self.root)

class ViewAllReservationsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("VIEW Reservations -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(icon)
        center_window(window_width, window_height)
        root.columnconfigure(3, weight=1)
        root.rowconfigure(30, weight=1)

        self.to_home_button = tk.Button(self, text="Home", font=button_font_large, width=10, padx=5, pady=5, bg=button_color, command=self.to_home)
        self.to_home_button.grid(row=0, padx=10, pady=10, sticky="we")

        self.tree = ttk.Treeview(root, show="headings", )
        self.tree.grid(row=2, column=0, padx=20, pady=20, columnspan=4, sticky="nsew")

        self.y_scroll = ttk.Scrollbar(root, orient="vertical")
        self.y_scroll.grid(row=2, column=3, sticky="nse")
        self.y_scroll.configure(command=self.tree.yview)

        self.x_scroll = ttk.Scrollbar(root, orient="horizontal")
        self.x_scroll.grid(column=0, columnspan=25, sticky="esw")
        self.x_scroll.configure(command=self.tree.xview)

        self.tree.configure(yscrollcommand=self.y_scroll.set, xscrollcommand=self.x_scroll.set)

        csv_file = "Database_biker.csv"

        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)

            self.tree["columns"] = headers
            for col in headers:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=150)

            for row in reader:
                self.tree.insert("", "end", values=row)

        file.close()
        self.grid()

    def to_home(self):
        delete_widgets(self)
        self.tree.destroy()
        self.x_scroll.destroy()
        self.y_scroll.destroy()
        self.destroy()
        StartWindow(self.root)

root = tk.Tk()
StartWindow(root)
root.mainloop()
