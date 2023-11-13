import csv
def create_id(csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        # go to last row
        last_row_dict = int(file.readlines()[-1].split(',')[0])
        new_id = last_row_dict + 1
        return new_id
