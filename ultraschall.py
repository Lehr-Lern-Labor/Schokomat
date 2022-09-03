#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 12
GPIO_ECHO = 6
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance(times: float = 0.000005):
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(times)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
    diff = StartZeit
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0 and StartZeit-diff < 2:
        StartZeit = time.time()
        if StartZeit-diff >= 2:
            return 2000
        #print("while1")
        
 
    # speichere Ankunftszeit :
    while GPIO.input(GPIO_ECHO) == 1 and StopZeit-diff < 4:
        StopZeit = time.time()
        if StopZeit-diff >= 4:
            return 4000
        #print("while2")
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
 
    return distanz

def test_sensor(sleepd: float, sleepm: float, dist: int):
    counter = 0
    doubled = 0
    repeated = 0
    for i in range(10000):
        abstand = distance(sleepd)
        if abstand < dist:
            counter += 1
            repeated +=1
            if repeated == 2:
                doubled +=1
                repeated = 0
        else:
            repeated = 0
        time.sleep(sleepm)
    return counter, doubled
        
def test_messung():
    pd = .000005
    values = [(pd,0.003,20),(pd,0.004,20),(pd,0.005,20),
              (pd,0.006,20),(pd,0.007,20)]
    datei = open('messwerte.txt','a')
    datei2 = open('messreihe.txt','a')
    datei2.write(str(len(values)) + ", Mini Messbereich Abstand Sensor größer \n")
    datei2.close()
    for i in values:
        result = test_sensor(i[0],i[1],i[2])
        d_list = [*i, *result]
        print("Messung (Werte" + str(i) + "), Fehler: " + str(result[0]) + " Doppelte: " + str(result[1]))
        datei.write(", ".join(map(str, d_list)) + "\n")
    datei.close()
def item_dropped():
    abstand = distance()
    print(abstand)
    count = 0
    while count < 2:
        if abstand < 12:
            count += 1
            print(count, round(abstand,2))
        else:
            count = 0
        abstand = distance()
        time.sleep(0.005)
    print(abstand)
    
def sensor_blocked():
    abstand = distance()
    print(abstand)
    count = 0
    while count < 20:
        if abstand > 12:
            count += 1
            print(count, round(abstand,2))
        else:
            count = 0
        abstand = distance()
        time.sleep(0.05)
    print(abstand)
    
if __name__ == '__main__':
    try:
        '''
        test_messung()
        '''
        counter = 0
        while True:
            abstand = distance()
            if counter%20 == 0:
                print ("Gemessene Entfernung = %.1f cm" % abstand)
            if abstand < 8:
                print ("Gemessene Entfernung = %.1f cm" % abstand)
            counter += 1
            time.sleep(0.01)
        ''''''
        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
