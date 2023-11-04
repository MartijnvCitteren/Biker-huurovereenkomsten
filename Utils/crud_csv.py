# all functionalities to Create, Read, Update and delte
import csv
import Utils.valid_input_check as valid

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
               "verzekeringsnummer",
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
                  "verzekeringsnummer": valid.entry_field_is_number(self.insurance_entry.get()),
                  "Medewerkersnummer": valid.entry_field_is_number(self.employee_entry.get()),
                  "Start-datum huur": self.start_rent_entry.get(),
                  "Eind-datum huur": self.end_rent_entry.get(),
                  "Reserveringsdatum": self.reservation_date_entry.get()
                  }
    invalid_entry_return_value = valid.invalid_entry_return_value
    if invalid_entry_return_value in input_dict.values():
        return 0

    else:
        csv_file = "Database_biker.csv"

        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow(input_dict)
            file.close()


