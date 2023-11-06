# all functionalities to Create, Read, Update and delte
import csv
import Utils.valid_input_check as valid
import Utils.windows as windows
from tkinter import messagebox


# create function for

# Create - write to the CSV file
def write_to_csv(self):
    headers = ["e-mail",
               "Voornaam",
               "Achternaam",
               "Straat",
               "Huisnummer",
               "Postcode",
               "Woonplaats",
               "Herenfiets aantal",
               "Vrouwenfiets aantal",
               "E-bike aantal",
               "Kinderzitjes aantal",
               "Helmen aantal",
               "Verzekeringsnummer",
               "Medewerkersnummer",
               "Start-datum huur",
               "Eind-datum huur",
               "Reserveringsdatum"
               ]

    input_dict = {"e-mail": valid.entry_field_is_email(self.email_entry.get()),
                  "Voornaam": valid.entry_field_is_not_empty(self.first_name_entry.get()),
                  "Achternaam": valid.entry_field_is_not_empty(self.family_name_entry.get()),
                  "Straat": valid.entry_field_is_not_empty(self.street_name_entry.get()),
                  "Huisnummer": valid.entry_field_is_number(self.adress_num_entry.get()),
                  "Postcode": valid.entry_field_is_zipcode(self.zip_code_entry.get()),
                  "Woonplaats": valid.entry_field_is_not_empty(self.city_entry.get()),
                  "Herenfiets aantal": valid.entry_bike_rent_is_number(self.num_man_bikes_entry.get()),
                  "Vrouwenfiets aantal": valid.entry_bike_rent_is_number(self.num_woman_bikes_entry.get()),
                  "E-bike aantal": valid.entry_bike_rent_is_number(self.num_E_bikes_entry.get()),
                  "Kinderzitjes aantal": valid.entry_bike_rent_is_number(self.num_child_seat_entry.get()),
                  "Helmen aantal": valid.entry_bike_rent_is_number(self.num_helmets_entry.get()),
                  "Verzekeringsnummer": valid.entry_field_is_number(self.insurance_entry.get()),
                  "Medewerkersnummer": valid.entry_field_is_number(self.employee_entry.get()),
                  "Start-datum huur": valid.entry_is_date(self.start_rent_entry.get()),
                  "Eind-datum huur": valid.entry_is_date(self.end_rent_entry.get()),
                  "Reserveringsdatum": valid.entry_is_date(self.reservation_date_entry.get())
                  }

    invalid_entry_return_value = valid.invalid_entry_return_value
    if invalid_entry_return_value in input_dict.values():
        print("herkent dat er een invalid value in dict zit")
        return 0

    elif valid.bike_is_rented(self.num_man_bikes_entry.get(), self.num_woman_bikes_entry.get(), self.num_E_bikes_entry.get()) == 0:
        print("herkent dat er geen fiets gehuurd wordt")
        return 0

    else:
        csv_file = "Database_biker.csv"

        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(input_dict)
            file.close()
            windows.NewReservationWindow.go_to_home(self)
            messagebox.showinfo("Reservering toegevoegd", "Uw reservering is succesvol verwerkt")
