import sys
import json
import doses
from doses import usage
def main():
    args = sys.argv
    if len(sys.argv) > 1 and sys.argv[1] == 'dose':
        dmg = '150'
        dstr = '1'
        if len(sys.argv) > 2:
            dmg = sys.argv[2]
        if len(sys.argv) > 3:
            dstr = sys.argv[3]
        doses.use(dmg,dstr)
    if len(sys.argv) > 1 and sys.argv[1] == 'last':
        dos=doses.get_last_time()
        ts = dos
        print(str(ts))
    if len(sys.argv) > 1 and sys.argv[1] == 'dump':
        print (doses.dump())
    if len(sys.argv) > 1 and sys.argv[1] == 'level':
        if len(sys.argv) > 2:
            ts = float (sys.argv[2])
            print (doses.get_level_at(ts))
            return
        print (doses.get_cur_lev())
    if len(sys.argv) > 2 and sys.argv[1] == 'graph':
        doses.graphpng("graph.png")
    print ("Herion Cherubim: One Dose At a Time: ")
    print ("--You can get help with 'hc.py help' or just 'hc.py'--\n")
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
   # help()

def help():
    print ("The following commands are avilable \n")
    print ("Help [command] shows this or can be used to get more help on a command (ex Help Dose)\n")
    print ("Dose (mg): Adds a dose at current time with (options) or default if unset")

def help_dose():
    print ("    -mg n (Size of dose in milligrams)")
    print ("    -analgesia n (How strong the opioid used was")
    print ("        (This is done using standard Equianalgesic values) For Reference:")
    print ("        Codeine=0.1")
    print ("        Tramadol=0.1")
    print ("        Oxycoone=1.5")
    print ("        Morphine(IV)=3.0")
    print ("        Pharm Grade Heroin=5.0")
    print ("        Fentanyl=50.0")
    print ("        Street Grade Heroin varies wildly. 'Fire' Black Tar can be around 1.0 (IV)")

main()

