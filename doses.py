import json;
import time;
from use import dose;
class usage:
    doses=[]
    def add_dose(self,d):
        # todo: check for type
        self.doses.append(d)
    def get_num_doses(self):
        return self.doses.count()
    def get_dose_num(self,num):
        return self.doses[num]
    def get_from_json_file(self, filename):
        with open(filename, 'r') as fi:
            print(fi.read().splitlines())
            fi.close()
    def add_dose_to_json(self, filename, dose):
        open(filename,'w')
    def __init__(self,fn="usage.json"):
        self.doses = []
        self.filename = fn

my_use=usage()

now = int(time.time())
f = dose(100,0.8,8.0,now)
my_use.add_dose(f)
print(f.to_json())
my_use.get_from_json_file(my_use.filename)
