import json;
import time;
from use import dose;
import math;

class usage:
    doses=[]
    def add_dose(self,d):
        # todo: check for type
        self.doses.append(d)
    def get_num_doses(self):
        return self.doses.count()
    def get_dose_num(self,num):
        return self.doses[num]
    def get_from_json_file(self):
       with open("usage.json") as inf:
        lines = inf.readlines();
        for dline in lines:
            dstr = str(dline)
            dobj=json.loads(str(dstr))
            d = dose(dobj['mg'],dobj['analgesic'],dobj['halflife'],dobj['time'])
            self.add_dose(d)
    def get_last_dose(self):
        self.get_from_json_file()
        dos = self.doses[0]
        return dos
    def get_current_level(self):
        sum=0
        for dos in self.doses:
            fac =  2**(((time.time()-float(dos.time))/3600)/dos.halflife)
            print (str(dos.mg) + " - " + str(fac) + " = = " + str(float(dos.mg)/fac))
            sum += float(dos.mg)/fac
            return sum
    def dump(self):
        self.get_from_json_file()
        ret=""
        for d in self.doses:
            ret += "\"" + str(d.mg) + "\",\"" + str(d.time) +"\"\n"
        return ret
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


def get_cur_lev():
    my_usage=usage()
    my_usage.get_from_json_file()
    return my_usage.get_current_level()

def dump():
    my_usage=usage()
    my_usage.get_from_json_file()
    return my_usage.dump()

def get_last_time():
    my_usage=usage()
    my_usage.get_from_json_file()
    dos = my_usage.get_last_dose()
    difsecs = (float(time.time()-float(dos.time)))
    difsecs = math.floor(difsecs)
    deltasecs = difsecs % 60
    deltamin = math.floor(difsecs/60) % 60
    deltahours = math.floor(difsecs/3600)
    print (str(deltahours) + ":" + str(deltamin) + ":" + str(deltasecs))


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

