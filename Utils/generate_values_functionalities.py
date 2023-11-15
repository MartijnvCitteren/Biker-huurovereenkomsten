import csv
from Utils import valid_input_functionalities as valid
from datetime import datetime


def create_id(csv_path):
    with open(csv_path, 'r') as file:
        last_row_dict = int(file.readlines()[-1].split(',')[0])
        new_id = last_row_dict + 1
        file.close()
        return new_id


def rental_periode_in_days(self):
    start_rent = valid.entry_is_date(self.start_rent_entry.get())
    start_rent = datetime.strptime(start_rent, "%d-%m-%Y")
    start_ordinal = start_rent.toordinal()

    end_rent = valid.entry_is_date(self.end_rent_entry.get())
    end_rent = datetime.strptime(end_rent, "%d-%m-%Y")
    end_ordinal = end_rent.toordinal()

    days = end_ordinal - start_ordinal
    return int(days)
