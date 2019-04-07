from peewee import datetime
import csv
import models
 
def csv_reader(file_obj):
    """
    Read a csv file and put values to DB
    """
    reader = csv.reader(file_obj, delimiter=";")
    for row in reader:
        models.add_license_parser(software_name=row[0], key=row[2], version=row[1], start_date=row[3], end_date=row[4], user=row[5], folder=row[6], comment=row[7])
 
if __name__ == "__main__":
    csv_path = "licenses.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)