from tkinter import messagebox
from datetime import date, datetime
import re

# value that get returned to prevent data get's added to the database.
invalid_entry_return_value: str = "error99999999999"

# define today's date
today_date = date.today()
# create ordinal to check if a date is in the past or in the future
today_ordinal = today_date.toordinal()


def entry_field_is_number(get_entry):
    try:
        integer_result = int(get_entry)
    except ValueError:
        messagebox.showinfo("Error - geen nummer", "Error- bij huisnummer, medewerker- of verzekeringsnummer"
                                                   " is een onjuiste waarde ingevuld. Laat huisnummer toevoegingen weg.")
        return invalid_entry_return_value

    else:
        return integer_result


def entry_field_is_not_empty(get_entry):
    if len(get_entry.strip()) == 0:
        messagebox.showinfo("Error - leeg veld", "Error-veld niet ingevuld.")
        return invalid_entry_return_value

    else:
        return get_entry


def entry_field_is_email(get_entry):
    # e-mail validating seems challenging because the is not an international standard in email formatting
    # "regular-expressions-cookbook - O'reilly". Therefore only decided to check if there is
    # at least an "@" and 1 "." in the entry.
    if (re.search(("@"), get_entry)) and (re.search(("\."), get_entry)):
        return get_entry.strip()

    else:
        messagebox.showinfo("Error - geen email", "Geldig email adres ontbreekt")
        return invalid_entry_return_value


def entry_field_is_zipcode(get_entry):
    # build regex expression via Pythex cheatsheat: https://pythex.org/
    if re.search("\A[1-9][0-9]{3}\s{0,4}[a-zA-Z]{2}\s{0,4}\Z", get_entry):
        return get_entry.replace(" ", "")

    else:
        messagebox.showinfo("Error - Postcode", "Ongeldige postcode. Controleer of postcode dit format heeft: 1234AB")
        return invalid_entry_return_value


def entry_is_date(get_entry):
    if re.search("\A[0-9]{1,2}[\/\-][0-9]{1,2}[\/\-][2][0-9]{3}\Z", get_entry):
        get_entry = get_entry.replace("/", "-")

        try:
            get_entry_date = datetime.strptime(get_entry, "%d-%m-%Y")
            get_entry_ordinal = get_entry_date.toordinal()

            if get_entry_ordinal >= today_ordinal:
                return get_entry

            else:
                messagebox.showinfo("Error - datum in het verleden",
                                    "De door u gekozen datum ligt in het verleden. Controleer de datum")
                return invalid_entry_return_value

        except:
            return invalid_entry_return_value

    else:
        messagebox.showinfo("Error - datum ",
                            "De door u gekozen datum is ongeldig")
        return invalid_entry_return_value

def entry_bike_rent_is_number(get_entry):
    if get_entry == "":
        get_entry = 0
        return get_entry

    else:
        return entry_field_is_number(get_entry)

def bike_is_rented(get_entry_1, get_entry_2, get_entry_3):
    if (entry_bike_rent_is_number(get_entry_1) == 0) and (entry_bike_rent_is_number(get_entry_2) == 0) and (entry_bike_rent_is_number(get_entry_3) == 0):
        messagebox.showinfo("Geen fiets gereserveerd",
                        "U kunt alleen accesoires huren als u hierbij ook een fiets huurt. Controleer uw reserevering.")
        return 0

    else:
        return 1