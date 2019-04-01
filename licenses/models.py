from peewee import SqliteDatabase, Model, PrimaryKeyField, TextField, DateField, DateTimeField, datetime
from config import DB_NAME

db = SqliteDatabase(DB_NAME)

class XLicenses(Model):
    class Meta:
        database = db
        db_table = "licenses"
    key_id = PrimaryKeyField()
    software_name = TextField()
    key = TextField(null=True)
    folder = TextField(null=True)
    version = TextField(null=True)
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    user = TextField(null=True)
    comment = TextField(null=True)
    updated = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "XLicenses(software name): %s" % self.software_name

def init_db():
    #db.drop_tables(XLicenses)
    XLicenses.create_table()
    XLicenses.create(
        software_name="KES",
        key="g45y45hwtthj4",
        folder="z:\\license\\123",
        version="23b",
        start_date=datetime.date(2014, 5, 1),
        end_date=datetime.date(2015, 4, 2),
        user="skuchinskiy"
    )
    print("db Licenses is created with test string KES")

def add_license(software_name, key, folder="", version="", start_date=None, end_date=None, user="", comment=""):
    XLicenses.create(
        software_name=software_name,
        key=key,
        folder=folder,
        version=version,
        start_date=start_date,
        end_date=end_date,
        user=user
    )
    print("New license added - %s" % software_name)

def del_license(key_id):
    '''
    delte license by key_id
    '''
    try:
        license = XLicenses.get(XLicenses.key_id == key_id)
        #license.delete_instance()
        print("License with id %s and name %s - deleted" % (key_id, license.software_name))
    except:
        print("License with id %s - not found" % key_id)

def change_license(key_id,software_name="", key="", folder="", version="", start_date="", end_date=datetime.date(2050, 12, 12), user="", comment=""):
    '''
    change license by key_id
    '''
    try:
        license = XLicenses.get(XLicenses.key_id == key_id)
        if software_name:
            license.software_name = software_name
        if key:
            license.key = key
        if folder:
            license.folder = folder
        if version:
            license.version = version
        if start_date:
            license.version = version
        if start_date:
            license.start_date = start_date
        if end_date:
            license.end_date = end_date
        if user:
            license.user = user
        if comment:
            license.comment = comment
        license.save()
        print("License with id %s and name %s - changed" % (key_id, license.software_name))
    except:
        print("License with id %s - not found" % key_id)

def create_table():
    XLicenses.create_table()

def get_all_licenses():
    selected_licenses = []
    for row in XLicenses.select():
        try:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key + " | End=" + row.end_date.strftime("%d.%m.%Y"))
        except AttributeError:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name)
    return(selected_licenses)

def get_license_by_name(software_name):
    selected_licenses = []
    for row in XLicenses.select().where(XLicenses.software_name == software_name):
        try:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key + " | End=" + row.end_date.strftime("%d.%m.%Y"))
        except AttributeError:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name)
    return(selected_licenses)

def get_license_by_end_date(end_date):
    selected_licenses = []
    for row in XLicenses.select().where(XLicenses.end_date <= end_date):
        try:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key + " | End=" + row.end_date.strftime("%d.%m.%Y"))
        except AttributeError:
            selected_licenses.append(row)
            print("Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name)
    return(selected_licenses)

if __name__ == '__main__':
    software_name = "PRTG"
    key = "gg54hth46h245y245y54"
    folder = "z:\\license\\PRTG"
    start_date = datetime.date(2019, 3, 28)
    end_date = datetime.date(2020, 3, 25)
    
    print("-"*10 + "Show all"+"-"*50)
    a = get_all_licenses()
    #print("-"*10 + "Show KES"+"-"*50)
    #get_license_by_name("KES")
    #print("-"*10 + "Show PRTG"+"-"*50)
    #get_license_by_name("PRTG")
    #print("-"*10 + "Show EMPTY output"+"-"*50)
    #get_license_by_name("EMPTY output")
    print("-"*10 + "Show by date"+"-"*50)
    #get_license_by_end_date(datetime.date(2020, 12, 29))
    #init_db()
    #add_license(software_name=software_name, key=key, folder=folder, start_date=start_date, end_date=end_date)
    #del_license(key_id=3)
    #change_license(key_id=4,key="22222")
    for row in a:
        print(row.key_id)
    print("main - OK")
