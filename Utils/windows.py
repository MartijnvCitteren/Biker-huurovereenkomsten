import csv
import tkinter as tk
from tkinter import messagebox

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

def delete_widgets(self):
    for widget in self.winfo_children():
        widget.destroy()

class StartWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.root.title("Home of Biker -- Rent your Bike")
        self.root.resizable(False, False)
        self.root.iconbitmap('C:\\Users\marti\OneDrive\\1. Documenten\\4. Studie\Haagse Hogeschool\ICT - deeltijd\Semester 1\Introduction Python\Eindopdracht - Biker - Huurovereenkomst\Biker-huurovereenkomsten\Icons\\biker_logo.ico')
        center_window(window_width, window_height)

        new_reservation_button = tk.Button(self, text="Nieuwe Reservering",font=button_font_large, width=15, padx=30, pady=30, bg=button_color, command=self.go_to_new_reservation_window)
        new_reservation_button.grid(row=0,column=0, padx=10, pady=150 )

        adjust_reservation_button = tk.Button(self, text="Wijzig reservering", font=button_font_large, width=15, padx=30, pady=30, bg=button_color)
        adjust_reservation_button.grid(row=0, column=2, pady=150)

        overview_reservations_button = tk.Button(self, text="Overzicht reserveringen",font=button_font_large, width=15, padx=30, pady=30, bg=button_color)
        overview_reservations_button.grid(row=2, column=1, pady=25)
        self.grid()


    def go_to_new_reservation_window(self):
        delete_widgets(self)
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


        #define grid
        self.root.columnconfigure((0,1,2,3), weight=15)
        #spacing between rows
        pad_y = 10

        to_home_button = tk.Button(self, text="Home",font=button_font_large, width=5, padx=5, pady=5, bg=button_color, command=self.go_to_home)
        to_home_button.grid(row=0, column=3, padx=10, pady=10)

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
        self.street_name_label = tk.Entry(self)
        self.street_name_label.grid(row=3, column=1, sticky="we" , pady=pad_y)

        adress_num_label = tk.Label(self, text="Huisnummer", width=25)
        adress_num_label.grid(row=3, column=2)
        self.adress_num_label = tk.Entry(self)
        self.adress_num_label.grid(row=3, column=3, sticky="we", pady=pad_y)

        zip_code_label = tk.Label(self, text="Postcode", width=25)
        zip_code_label.grid(row=4, column=0)
        self.zip_code_label = tk.Entry(self)
        self.zip_code_label.grid(row=4, column=1, sticky="we", pady=pad_y)

        city_label = tk.Label(self, text="Stad", width=25)
        city_label.grid(row=4, column=2)
        self.city_label = tk.Entry(self)
        self.city_label.grid(row=4, column=3, sticky="we", pady=pad_y)

        #TO DO: Welke fiets wil je huren + aantallen dropdown
        what_bike_label = tk.Label(self, text="Welke fiets wil je huren?", width=25, font=14)
        what_bike_label.grid(row=5, column=0, columnspan=3, sticky='w')

        #TO DO: Welke accesoires wil je huren + aantallen dropdown
        what_accessories_label = tk.Label(self, text="Welke fiets wil je huren?", width=25, font=14)
        what_accessories_label.grid(row=7, column=0, columnspan=3, sticky='w')


        insurance_label = tk.Label(self, text="verzekeringsnummer", width=25)
        insurance_label.grid(row=8, column=0)
        self.insurance_label = tk.Entry(self)
        self.insurance_label.grid(row=8, column=1, sticky="we", pady=pad_y)

        employee_label = tk.Label(self, text="Medeweker nr.", width=25)
        employee_label.grid(row=8, column=2)
        self.employee_label = tk.Entry(self)
        self.employee_label.grid(row=8, column=3, sticky="we")

        start_rent_label = tk.Label(self, text="Startdatum huur", width=25)
        start_rent_label.grid(row=9, column=0, stick="w")
        self.start_rent_label = tk.Entry(self)
        self.start_rent_label.grid(row=9, column=1, sticky="we", pady=pad_y)

        end_rent_label = tk.Label(self, text="einddatum huur", width=25)
        end_rent_label.grid(row=9, column=2)
        self.end_rent_label = tk.Entry(self)
        self.end_rent_label.grid(row=9, column=3, sticky="we", pady=pad_y)

        reservation_date_label = tk.Label(self, text="Reserveringsdatum", width=25)
        reservation_date_label.grid(row=10, column=0)
        self.reservation_date_label = tk.Entry(self)
        self.reservation_date_label.grid(row=10, column=1, sticky="we", pady=pad_y)

        make_reservation_button = tk.Button(self, text="Reserveer",font=button_font_large, width=10, padx=5, pady=5, bg='#AEE4A0')
        make_reservation_button.grid(row=10, column=3, padx=10, pady=10, sticky="we")

        self.grid()

    def go_to_home(self):
        delete_widgets(self)
        self.destroy()
        StartWindow(self.root)

    def go_to_thanks_page(self):
        delete_widgets(self)
        self.destroy()

    def save_data_to_list(self,db_list):
        pass


    def write_to_csv(self,db_list):
        lista =[self.email_entry.get(),
                self.first_name_entry.get(),
                self.family_name_entry.get()
               ]
        db_list.append(lista)
        print(db_list)
        with open("Database_biker.csv","w") as file:
            writer = csv.writer(file)
            writer.writerow(["e-mail", "Voornaam", "Achternaam"])
            writer.writerows(db_list)
            messagebox.showinfo("Nieuwe reservering is succesvol opgeslagen")



root = tk.Tk()
StartWindow(root)
#NewReservationWindow(root)
root.mainloop()
