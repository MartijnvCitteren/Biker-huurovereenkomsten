import csv
import Utils.generate_values_functionalities as generate
import Utils.valid_input_functionalities as valid

csv_file = "Database_biker.csv"
class Reservation:
    def __init__(self, client_id, email, first_name, last_name, street, adresnummer,zipcode, city, man_bike_num,
                 woman_bike_num, e_bike_num, child_seat_num, helmets_num, insurance_number, employee_number, start_rent,
                 end_rent, rental_period, reservation_date):
        self.client_id = client_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.adresnummer = adresnummer
        self.zipcode = zipcode
        self.city = city
        self.man_bike_num = man_bike_num
        self.woman_bike_num = woman_bike_num
        self.e_bike_num = e_bike_num
        self.child_seat_num = child_seat_num
        self.helmet_num = helmets_num
        self.insurance_number = insurance_number
        self.employee_number = employee_number
        self.start_rent = start_rent
        self.end_rent = end_rent
        self.rental_period = rental_period
        self.reservation_date = reservation_date

    def set_new_reservation(self):
        self.client_id = generate.create_id(csv_file)
        self.email = valid.entry_field_is_email(self.email_entry.get())
        self.first_name = valid.entry_field_is_not_empty(self.first_name_entry.get())
        self.last_name = valid.entry_field_is_not_empty(self.family_name_entry.get())
        self.street = valid.entry_field_is_not_empty(self.street_name_entry.get())
        self.adresnummer = valid.entry_field_is_number(self.adress_num_entry.get())
        self.zipcode = valid.entry_field_is_zipcode(self.zip_code_entry.get())
        self.city = valid.entry_field_is_not_empty(self.city_entry.get())
        self.man_bike_num = valid.entry_bike_rent_is_number(self.num_man_bikes_entry.get())
        self.woman_bike_num = valid.entry_bike_rent_is_number(self.num_woman_bikes_entry.get())
        self.e_bike_num = valid.entry_bike_rent_is_number(self.num_E_bikes_entry.get())
        self.child_seat_num = valid.entry_bike_rent_is_number(self.num_child_seat_entry.get())
        self.helmet_num = valid.entry_bike_rent_is_number(self.num_helmets_entry.get())
        self.insurance_number = valid.entry_field_is_number(self.insurance_entry.get())
        self.employee_number = valid.entry_field_is_number(self.employee_entry.get())
        self.start_rent = valid.entry_is_date(self.start_rent_entry.get())
        self.end_rent = valid.entry_is_date(self.end_rent_entry.get())
        self.rental_period = generate.rental_periode_in_days(self)
        self.reservation_date = valid.entry_is_date(self.reservation_date_entry.get())

    def get_reservation_dict_with_out_validation(self):
        input_dict = {"Klantnummer": self.client_id,
                      "e-mail": self.email,
                      "Voornaam": self.first_name,
                      "Achternaam": self.last_name,
                      "Straat": self.street,
                      "Huisnummer": self.adresnummer,
                      "Postcode": self.zipcode,
                      "Woonplaats": self.city,
                      "Herenfiets aantal": self.man_bike_num,
                      "Vrouwenfiets aantal": self.woman_bike_num,
                      "E-bike aantal": self.e_bike_num,
                      "Kinderzitjes aantal": self.child_seat_num,
                      "Helmen aantal": self.helmet_num,
                      "Verzekeringsnummer": self.insurance_number,
                      "Medewerkersnummer": self.employee_number,
                      "Start-datum huur": self.start_rent,
                      "Eind-datum huur": self.end_rent,
                      "Aantal huur dagen": self.rental_period,
                      "Reserveringsdatum": self.reservation_date
                      }
        return input_dict


