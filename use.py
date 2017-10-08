import json
import time

class dose:
    def val_dose(self):
        if isinstance(self.mg,int):
            print ("Good, milligrams is an integer")
        if isinstance(self.analgesic, float):
            print ("Good, Analgesic is a float")
        if isinstance(self.halflife, float):
            print ("Good, Half-life is a float (of hours)")
        if isinstance(self.time, int):
            print ("Good, time is a DateTime")
    def to_json(self):
       return (json.dumps(self.__dict__))
    def __init__(self, mg, analgesic, halflife, time):
        self.mg=mg
        self.analgesic=float(analgesic)
        self.halflife=float(halflife)
        self.time=time

