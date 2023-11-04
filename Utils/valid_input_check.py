from tkinter import messagebox
import re

#value that get returned to prevent data get's added to the database.
invalid_entry_return_value: str = "error99999999999"

def entry_field_is_number(get_entry):
    try:
        integer_result =int(get_entry)
    except ValueError:
        messagebox.showinfo("Error - geen nummer","Error- bij huisnummer, medewerker- of verzekeringsnummer"
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
    #e-mail validating seems challenging because the is not an international standard in email formatting
    # "regular-expressions-cookbook - O'reilly". Therefore only decided to check if there is
    # at least an "@" and 1 "." in the entry.
    if (re.search(("@"), get_entry)) and (re.search(("\."),get_entry)):
        return get_entry.strip()

    else:
        messagebox.showinfo("Error - geen email", "Geldig email adres ontbreekt")
        return invalid_entry_return_value


def entry_field_is_zipcode(get_entry):
    #build regex expression via Pythex cheatsheat: https://pythex.org/
    if re.search("\A[1-9][0-9]{3}\s{0,4}[a-zA-Z]{2}\s{0,4}\Z", get_entry):
        return get_entry.replace(" ","")

    else:
        messagebox.showinfo("Error - Postcode", "Geldige postcode ontbreekt. Controleer of postcode dit format heeft: 1234AB")
        return invalid_entry_return_value


def entry_is_date(get_entry):
    pass