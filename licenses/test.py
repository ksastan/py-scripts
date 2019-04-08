import unittest
import models
from peewee import datetime

software_name = "test-software"
key = "test-key"
folder = "z:\\test\\folder"
start_date = datetime.date(2018, 1, 30)
end_date = datetime.date(2030, 12, 1)

class Test(unittest.TestCase):    
    '''
    Test add_license and get_license
    '''  
    def test_add_get(self):
        models.add_license(software_name=software_name, key=key, folder=folder, start_date=start_date, end_date=end_date)
        get_lic = models.get_license(software_name=software_name)
        for i in get_lic:
            self.assertEqual(i.key, "test-key")
    
    def test_del(self):
        '''
        Test del_license function
        '''
        get_lic = models.get_license(software_name=software_name)
        for i in get_lic: 
            self.assertEqual(models.del_license(key_id=i.key_id), True)

if __name__ == '__main__':
    unittest.main()
