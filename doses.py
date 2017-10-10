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
            return (fi.read().splitlines())
            fi.close()
    def get_last_time(self):
        dos = self.get_from_json_file("usage.json")
        do = dose(dos[0])
        print (do)
        return dos[0]
    def save_to_json(self, filename):
        with open(filename,'w') as wf:
         for use in self.doses:
          d= dose(use.mg,use.analgesic,use.halflife,use.time)
          print(d)
          wf.write(d.to_json())
          wf.write("\n")
    def __init__(self,fn="usage.json"):
        self.doses = []
        self.filename = fn

def get_last_time():
    my_usage=usage()
    my_usage.get_last_dose()
def use(d_mg='150', d_str='1'):
    my_usage=usage()
    d=(dose(d_mg,d_str,'1',str(time.time())))
    my_usage.add_dose(d)
    dos = json.dumps(d.__dict__)
    with open("usage.json") as inf:
        lines = inf.readlines();
        for dline in lines:
            dstr = str(dline)
            dobj=json.loads(str(dstr))
            d = dose(dobj['mg'],dobj['analgesic'],dobj['halflife'],dobj['time'])
            my_usage.add_dose(d)
    my_usage.save_to_json("usage.json")
