import json
import time

class dose extends object:
    def val_dose(self):
        if isinstance(self.mg,int):
            print ("Good, milligrams is an integer")
        if isinstance(self.analgesic, float):
            print ("Good, Analgesic is a float")
        if isinstance(self.halflife, float):
            print ("Good, Half-life is a float (of hours)")
        if isinstance(self.time, int):
            print ("Good, time is a DateTime")
    def __init__(self, mg, analgesic, halflife, time):
        self.mg=mg
        self.analgesic=float(analgesic)
        self.halflife=float(halflife)
        self.time=time
    def toJSON(self):
        return self.__dict__

now = int(time.time())
d = dose(150,1,6.0,now)
print dose.toJSON();
val = d.val_dose()

print (json.dumps(d.__dict__))
