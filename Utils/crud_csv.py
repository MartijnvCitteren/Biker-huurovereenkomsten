# all functionalities to Create, Read, Update and delte
import csv
import Utils.valid_input_check as valid
import Utils.windows as windows
import pandas as pd
from tkinter import messagebox
import Utils.row_id as id

# CSV file
csv_file = "Database_biker.csv"

# headers
headers = ["ID",
           "e-mail",
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


# Create - write to the CSV file
def write_to_csv(self):
    input_dict = {"ID": id.create_id(csv_file),
                  "e-mail": valid.entry_field_is_email(self.email_entry.get()),
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
        return 0

    elif valid.bike_is_rented(self.num_man_bikes_entry.get(), self.num_woman_bikes_entry.get(),
                              self.num_E_bikes_entry.get()) == 0:
        return 0

    else:

        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(input_dict)
            file.close()
            windows.NewReservationWindow.go_to_home(self)
            messagebox.showinfo("Reservering toegevoegd", "Uw reservering is succesvol verwerkt")
            return 1


def search_reservation(self):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        e_mail_search_entry = valid.entry_field_is_email(self.search_email_entry.get())

        for dict in reader:
            found = False
            for value in dict.values():
                if value == e_mail_search_entry.lower():
                    found = True

            if found:
                messagebox.showinfo("Reservering gevonden", "De gegevens worden geladen")
                return dict

    file.close()
    messagebox.showinfo("Geen reservering", "Er is geen reservering met dit emailadres.")
    return 0


def fill_update_fields(self):
    dict = search_reservation(self)

    if dict == 0:
        return 0

    self.email_entry.insert(0, dict.get(headers[1]))
    self.first_name_entry.insert(0, dict.get(headers[2]))
    self.family_name_entry.insert(0, dict.get(headers[3]))
    self.street_name_entry.insert(0, dict.get(headers[4]))
    self.adress_num_entry.insert(0, dict.get(headers[5]))
    self.zip_code_entry.insert(0, dict.get(headers[6]))
    self.city_entry.insert(0, dict.get(headers[7]))
    self.num_man_bikes_entry.insert(0, dict.get(headers[8]))
    self.num_woman_bikes_entry.insert(0, dict.get(headers[9]))
    self.num_E_bikes_entry.insert(0, dict.get(headers[10]))
    self.num_child_seat_entry.insert(0, dict.get(headers[11]))
    self.num_helmets_entry.insert(0, dict.get(headers[12]))
    self.insurance_entry.insert(0, (dict.get(headers[13])))
    self.employee_entry.insert(0, str(dict.get(headers[14])))
    self.start_rent_entry.insert(0, dict.get(headers[15]))
    self.end_rent_entry.insert(0, dict.get(headers[16]))
    self.reservation_date_entry.insert(0, dict.get(headers[17]))

    return 1


def indentify_similar_row_in_csv(self):
    """Loop door file heen. Voor elke row check of (2 * 3 'unieke' waarders gelijk zijn
    als dat zo is verwijder dan de rij."""

    # haal unieke waardes uit formulier
    check_email = valid.entry_field_is_email(self.email_entry.get())
    check_postcode = valid.entry_field_is_zipcode(self.zip_code_entry.get())
    check_achternaam = valid.entry_field_is_not_empty(self.family_name_entry.get())
    check_voornaam = valid.entry_field_is_not_empty(self.first_name_entry.get())
    check_verzekeringsnummer = valid.entry_field_is_number(self.insurance_entry.get())
    check_straatnaam = valid.entry_is_date(self.reservation_date_entry.get())

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for dict in reader:
            for value in dict.values():
                if ((value == check_email and check_postcode and check_verzekeringsnummer) or
                        (value == check_email and check_verzekeringsnummer and check_voornaam) or
                        (value == check_achternaam and check_straatnaam and check_postcode)):
                    file.close()
                    return dict['ID']
        print("niks gevonden!")
        file.close()


def delete_row(self):
    id_to_delete = int((indentify_similar_row_in_csv(self)))
    df = pd.read_csv(csv_file)
    df = df.drop(df[df.ID == id_to_delete].index)
    df.to_csv(csv_file, index=False)

    messagebox.showinfo("Gegevens verwijdert", "Reservering is succesvol verwijdert")


def update(self):
    id_to_update = int((indentify_similar_row_in_csv(self)))
    df = pd.read_csv(csv_file)
    df.update(df[df.ID == id_to_update].index)
    print(df)
    df.to_csv(csv_file, index=False)

    messagebox.showinfo("Gegevens Ge-update", "Reservering is succesvol aangepast")
