from peewee import datetime
import csv
import models
 
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj, delimiter=";")
    for row in reader:
        #print(row[0]) # software_name
        #print(row[1]) # version
        #print(row[2]) # key
        #print(row[3]) # start_date
        #print(row[4]) # end_date
        #print(row[5]) # username
        #print(row[6]) # folder
        #print(row[7]) # comment
        models.add_license_parser(software_name=row[0], key=row[2], version=row[1], start_date=row[3], end_date=row[4], user=row[5], folder=row[6], comment=row[7])
 
if __name__ == "__main__":
    csv_path = "licenses.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)