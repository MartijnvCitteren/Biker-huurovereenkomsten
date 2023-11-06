import tkinter as tk
import Utils.crud_csv as crud

# setting size colors and fonts
window_width = 750
window_height = 750
window_bar_color = "546A7B"
button_color = "#C5D9E2"
button_font_large = "bold"


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
        self.root.iconbitmap(
            'C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)

        new_reservation_button = tk.Button(self, text="Nieuwe Reservering", font=button_font_large, width=15, padx=30,
                                           pady=30, bg=button_color, command=self.go_to_new_reservation_window)
        new_reservation_button.grid(row=0, column=0, padx=10, pady=150)

        update_reservation_button = tk.Button(self, text="Wijzig reservering", font=button_font_large, width=15,
                                              padx=30, pady=30, bg=button_color,
                                              command=self.go_to_update_reservation_window)
        update_reservation_button.grid(row=0, column=2, pady=150)

        overview_reservations_button = tk.Button(self, text="Overzicht reserveringen", font=button_font_large, width=15,
                                                 padx=30, pady=30, bg=button_color)
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
        pass


class NewReservationWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("NEW Reservation -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(
            'C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)
        self.to_home_button = tk.Button(self, text="Home", font=button_font_large, width=5, padx=5, pady=5, bg=button_color,
                                   command=self.go_to_home)
        self.to_home_button.grid(row=0, column=3, padx=10, pady=10)

        self.create_reservation_fields()

        self.make_reservation_button = tk.Button(self, text="Reserveer", font=button_font_large, width=10, padx=5,
                                                 pady=5, bg='#AEE4A0', command=self.save_to_csv)
        self.make_reservation_button.grid(row=10, column=3, padx=10, pady=10, sticky="we")
        self.grid()

    def create_reservation_fields(self):
        # define grid
        self.root.columnconfigure((0, 1, 2, 3), weight=15)
        # spacing between rows
        pad_y = 10



        email_label = tk.Label(self, text="E-mail", width=25)
        email_label.grid(row=1, column=0, sticky="w")
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=1, column=1, sticky="we", pady=pad_y, columnspan=3)

        first_name_label = tk.Label(self, text="Voornaam", width=25)
        first_name_label.grid(row=2, column=0)
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(row=2, column=1, sticky="we", pady=pad_y)

        family_name_label = tk.Label(self, text="Achternaam", width=25)
        family_name_label.grid(row=2, column=2)
        self.family_name_entry = tk.Entry(self)
        self.family_name_entry.grid(row=2, column=3, sticky="we", pady=pad_y)

        street_name_label = tk.Label(self, text="Straatnaam", width=25)
        street_name_label.grid(row=3, column=0)
        self.street_name_entry = tk.Entry(self)
        self.street_name_entry.grid(row=3, column=1, sticky="we", pady=pad_y)

        adress_num_label = tk.Label(self, text="Huisnummer", width=25)
        adress_num_label.grid(row=3, column=2)
        self.adress_num_entry = tk.Entry(self)
        self.adress_num_entry.grid(row=3, column=3, sticky="we", pady=pad_y)

        zip_code_label = tk.Label(self, text="Postcode", width=25)
        zip_code_label.grid(row=4, column=0)
        self.zip_code_entry = tk.Entry(self)
        self.zip_code_entry.grid(row=4, column=1, sticky="we", pady=pad_y)

        city_label = tk.Label(self, text="Stad", width=25)
        city_label.grid(row=4, column=2)
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=4, column=3, sticky="we", pady=pad_y)

        man_bike_label = tk.Label(self, text="Aantal herenfietsen", width=25)
        man_bike_label.grid(row=5, column=0, columnspan=2, sticky='w')
        self.num_man_bikes_entry = tk.Entry(self)
        self.num_man_bikes_entry.grid(row=5, column=1, columnspan=2, sticky='w', pady=pad_y)

        woman_bike_label = tk.Label(self, text="Aantal vrouwenfietsen", width=25)
        woman_bike_label.grid(row=5, column=2, columnspan=2, sticky='w')
        self.num_woman_bikes_entry = tk.Entry(self)
        self.num_woman_bikes_entry.grid(row=5, column=3, columnspan=2, sticky='w', pady=pad_y)

        E_bike_label = tk.Label(self, text="Aantal Elektrische fietsen", width=25)
        E_bike_label.grid(row=6, column=0, columnspan=2, sticky='w')
        self.num_E_bikes_entry = tk.Entry(self)
        self.num_E_bikes_entry.grid(row=6, column=1, columnspan=2, sticky='w', pady=pad_y)

        child_bicycle_seat_label = tk.Label(self, text="Aantal kinderzitjes", width=25)
        child_bicycle_seat_label.grid(row=7, column=0, columnspan=2, sticky='w')
        self.num_child_seat_entry = tk.Entry(self)
        self.num_child_seat_entry.grid(row=7, column=1, columnspan=2, sticky='w', pady=pad_y)

        helmet_label = tk.Label(self, text="Aantal helmen", width=25)
        helmet_label.grid(row=7, column=2, columnspan=2, sticky='w')
        self.num_helmets_entry = tk.Entry(self)
        self.num_helmets_entry.grid(row=7, column=3, columnspan=2, sticky='w', pady=pad_y)

        insurance_label = tk.Label(self, text="verzekeringsnummer", width=25)
        insurance_label.grid(row=8, column=0)
        self.insurance_entry = tk.Entry(self)
        self.insurance_entry.grid(row=8, column=1, sticky="we", pady=pad_y)

        employee_label = tk.Label(self, text="Medeweker nr.", width=25)
        employee_label.grid(row=8, column=2)
        self.employee_entry = tk.Entry(self)
        self.employee_entry.grid(row=8, column=3, sticky="we")

        start_rent_label = tk.Label(self, text="Startdatum huur (dd-mm-jjjj)", width=25)
        start_rent_label.grid(row=9, column=0, stick="w")
        self.start_rent_entry = tk.Entry(self)
        self.start_rent_entry.grid(row=9, column=1, sticky="we", pady=pad_y)

        end_rent_label = tk.Label(self, text="einddatum huur (dd-mm-jjjj)", width=25)
        end_rent_label.grid(row=9, column=2)
        self.end_rent_entry = tk.Entry(self)
        self.end_rent_entry.grid(row=9, column=3, sticky="we", pady=pad_y)

        reservation_date_label = tk.Label(self, text="Reserveringsdatum (dd-mm-jjjj)", width=25)
        reservation_date_label.grid(row=10, column=0)
        self.reservation_date_entry = tk.Entry(self)
        self.reservation_date_entry.grid(row=10, column=1, sticky="we", pady=pad_y)

        self.grid()

    def go_to_home(self):
        delete_widgets(self)
        self.destroy()
        StartWindow(self.root)


    def save_to_csv(self):
        #dict = get_data(self)
        #dict = [{"e-mail": "Arie@gmail.com", "Voornaam": "Arie", "Achternaam": "de Boer"}]
        crud.write_to_csv(self)

class UpdateReservationWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("UPDATE Reservation -- Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap(
            'C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)

        #search_email_label = tk.Label(self, text="Zoek email-adres", width=25)
        #search_email_label.grid(row=0, column=0)
        #search_email_entry = tk.Entry(self)
        #self.reservation_date_entry.grid(row=0, column=1, sticky="we", pady= NewReservationWindow.pad_y)



        NewReservationWindow.create_reservation_fields(self)
        self.make_reservation_button = tk.Button(self, text="Wijzig", font=button_font_large, width=10, padx=5, pady=5,
                                                 bg='#AEE4A0')
        self.make_reservation_button.grid(row=10, column=3, padx=10, pady=10, sticky="we")
        self.grid()


root = tk.Tk()
StartWindow(root)
root.mainloop()
