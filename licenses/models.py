from peewee import SqliteDatabase, Model, PrimaryKeyField, TextField, DateField, DateTimeField, datetime, fn
from config import DB_NAME, log

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

def add_license(software_name, key, folder="", version="", start_date=None, end_date=None, user="", comment="", count=1):
    i = 0
    while i < count:
        XLicenses.create(
            software_name=software_name,
            key=key,
            folder=folder,
            version=version,
            start_date=start_date,
            end_date=end_date,
            user=user,
            comment = comment
        )
        i = i + 1
        log.info("License added - %s" % software_name)

def add_license_parser(software_name, key, folder="", version="", start_date=None, end_date=None, user="", comment=""):
    '''
    Add license for dbparser. Include date format changing
    '''
    if start_date:
        start_date = datetime.datetime.strptime(start_date, "%d.%m.%Y")
    if end_date:
        end_date = datetime.datetime.strptime(end_date, "%d.%m.%Y")
    XLicenses.create(
        software_name=software_name,
        key=key,
        folder=folder,
        version=version,
        start_date=start_date,
        end_date=end_date,
        user=user,
        comment = comment
    )
    log.info("New license added - %s" % software_name)

def del_license(key_id):
    '''
    delete license by key_id
    '''
    try:
        license = XLicenses.get(XLicenses.key_id == key_id)
        license.delete_instance()
        log.info("License with id %s and name %s - deleted" % (key_id, license.software_name))
        return(True)
    except:
        log.info("License with id %s - not found" % key_id)
        return(False)

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
        else:
            license.key = ""
        if folder:
            license.folder = folder
        else:
            license.folder = ""
        if version:
            license.version = version
        else:
            license.version = ""
        if start_date:
            license.start_date = start_date
        if end_date:
            license.end_date = end_date
        else:
            license.end_date = None
        if user:
            license.user = user
        else:
            license.user = ""
        if comment:
            license.comment = comment
        else:
            license.comment = ""
        license.save()
        log.info("License with id %s and name %s - changed" % (key_id, license.software_name))
    except:
        log.info("License with id %s - not found" % key_id)

def create_table():
    XLicenses.create_table()

def get_license(key_id=None, software_name="", end_date=None):
    '''
    get licenses by key_id, software_name or end_date
    '''
    selected_licenses = []
    if key_id:
        for row in XLicenses.select().where(XLicenses.key_id == key_id):
            selected_licenses.append(row)
            log.debug("By key_id Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key)
    elif software_name and end_date: 
        for row in XLicenses.select().where(fn.Lower(XLicenses.software_name.contains(software_name.lower())), XLicenses.end_date <= end_date, XLicenses.end_date >= datetime.datetime(2010, 1, 1)):
            selected_licenses.append(row)
            log.debug("By software_name and Date Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key)
    elif software_name:
        for row in XLicenses.select().where(fn.Lower(XLicenses.software_name.contains(software_name.lower()))):
            selected_licenses.append(row)
            log.debug("By software name Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key)
    elif end_date:
        for row in XLicenses.select().where(XLicenses.end_date <= end_date, XLicenses.end_date >= datetime.datetime(2010, 1, 1)):
            if row.end_date:
                selected_licenses.append(row)
                log.debug("By end_date Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key)
    else:
        for row in XLicenses.select():
            selected_licenses.append(row)
            log.debug("All licenses Key_id=" + str(row.key_id) + " | Software_name=" + row.software_name + " | Key=" + row.key)
    return(selected_licenses)

if __name__ == '__main__':
    print("main - OK")
