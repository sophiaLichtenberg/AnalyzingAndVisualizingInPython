from ziegen import *
import gc
import traceback
import sys

door_number = 5
test_no = 1

try:
    doors = MontyHall(door_number)
except:
    print "Fehler: Monty_Hall-Klasse konnte nicht instanziiert werden:"
    traceback.print_exc()
    sys.exit()
print "Test {} OK: Monty_Hall-Klasse wurde instanziiert.".format(test_no)

test_no+=1    
all_doors = set()
#print gc.get_objects()
for collected_objects in gc.get_objects():
    if isinstance(collected_objects, Door):
        all_doors.add(collected_objects)
if len(all_doors) != door_number:
    print "Fehler: {} Tueren sollten erzeugt werden, allerdings wurden {} Tueren angelegt.".format(door_number, len(all_doors))
    sys.exit()
else:
    print "Test {} OK: {} Tueren wurden angelegt.".format(test_no, door_number)

test_no+=1
try:
    car_doors = [i for i in all_doors if i.car]
except:
    print '"car"-Attribut konnte nicht gelesen werden:'
    traceback.print_exc()
    sys.exit()
if len(car_doors) == 0:
    print "Fehler: Hinter keiner Tuer ist ein Auto versteckt (es existiert kein Door-Objekt mit car==True)"
if len(car_doors) > 1:
    print "Fehler: Hinter mehr als einer Tuer ist ein Auto versteckt (es existieren mehrere Door-Objekt mit car==True)"
print "Test {} OK: Hinter genau einer Tuer ist ein Auto versteckt.".format(test_no)

test_no+=1
try:
    door_ids = sorted([i.id for i in all_doors])
except:
    print '"id"-Attribut konnte nicht gelesen werden:'
    traceback.print_exc()
    sys.exit()
correct_door_ids = [str(i) for i in range(1,door_number+1)]
if door_ids != correct_door_ids:
    print "Fehler: Die IDs der Tueren sind {}, sollten aber {} sein.".format(door_ids, correct_door_ids)
    sys.exit()
print "Test {} OK: IDs der Tueren sind korrekt.".format(test_no)

test_no+=1
try:
    doors.choose(str(door_number))
except:
    print 'Fehler: Aufruf der choose()-Methode gescheitert.'
    traceback.print_exc()
    sys.exit()
try:
    chosen_door_ids = [i.id for i in all_doors if i.chosen]
except:
    print 'Fehler: "chosen"-Attribut konnte nicht gelesen werden:'
    traceback.print_exc()
    sys.exit()
if len(chosen_door_ids) == 0:
    print "Fehler: Nach Aufruf von choose({}) gibt es kein einziges Door-Objekt mit chosen == True.".format(door_number)
    sys.exit()
if len(chosen_door_ids) > 1:
    print "Fehler: Nach Aufruf von choose({}) gibt es mehr als ein Door-Objekt mit chosen == True.".format(door_number)
    sys.exit()
if chosen_door_ids[0] != str(door_number):
    print "Fehler: Nach Aufruf von choose({}) ist {} die id des Door-Objektes mit chosen == True.".format(door_number, chosen_door_ids[0])
    sys.exit()
print "Test {0} OK: Nach Aufruf von choose({1}) ist das chosen-Attribut der Tuere mit id {1} == True.".format(test_no, door_number)

test_no+=1
try:
    opened_doors = doors.open_empty_doors()
except:
    print 'Fehler: Aufruf der open_empty_doors()-Methode gescheitert.'
    traceback.print_exc()
    sys.exit()
if not isinstance(opened_doors, set):
    print "Fehler: open_empty_doors() liefert kein Set der geoeffneten Tueren als Rueckgabeargument."
    sys.exit()
if not all([isinstance(i, str) for i in opened_doors]):
    print "Fehler: Der Rueckgabewert von open_empty_doors() ist zwar ein Set, besteht aber nicht aus Strings."
    sys.exit()
if any([i.chosen for i in all_doors if i.id in opened_doors]):
    print "Fehler: open_empty_doors() hat eine Tuer mit chosen == True zurueckgegeben."
    sys.exit()
if any([i.car for i in all_doors if i.id in opened_doors]):
    print "Fehler: open_empty_doors() hat eine Tuer mit car == True zurueckgegeben."
    sys.exit()
if len(set([i.id for i in all_doors]).difference(opened_doors)) < 2:
    print "Fehler: Zu wenige Tueren wurden von der Funktion open_empty_doors() geoeffnet. Es sollen alle bis auf zwei Tueren geoeffnet werden."
    sys.exit()
if len(set([i.id for i in all_doors]).difference(opened_doors)) > 2:
    print "Fehler: Zu viele Tueren wurden von der Funktion open_empty_doors() geoeffnet. Es sollen alle bis auf zwei Tueren geoeffnet werden."
    sys.exit()
print "Test {0} OK: open_empty_doors() hat alle bis auf zwei Tueren als Liste zurueckgegeben. Dabei wurde keine Tuere mit car==True oder chosen==True zurueckgeliefert.".format(test_no)
