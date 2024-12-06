#import libaries
import time
import adafruit_dht
import board
import Adafruit_ADS1x15
from gpiozero import LightSensor, Buzzer
#initalize sensors
dht_device = adafruit_dht.DHT11(board.D4)
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
fields = []
rows = []
def main()
    #collect temp and humidity
    while True:
	    try:
		    temp_c = dht_device.temperature
		    temp_f = temp_f * (9/5)+32
		    humidity = dht_device.humidity
		    temp_humid = ("temp:{:1f} c / {:.1f} F Humidity: {} %".format(temp_c, temp_f, humidity))
		    except RuntimeError as err:
		    print(err.args[0])
	    time.sleep(5)
    #collect moisture
    try:
	    while True:
		    raw_value = adc.read_adc(3, gain=GAIN)
		    raw = ("Raw Value: {}".format(raw_value))
		    time.sleep(5)
    #collect light
    ldr = LightSensor(4)
    while True:
	    light = (ldr.value)
    #add time
    t = time.strftime("%Y %d %b %H.%M.%S"))
    time.sleep(5)
    #output to csv
    with open ("planter.csv","w") as f:
        f.write(','.join(str(value for value in header) + "\n")
        output = ",".jpin(str(value) for value in data)
        batch_data.append(output)
        sense_data=[]
        sense_data.append(t)
        sense_data.append(temp_humid)
        sense_data.append(raw)
        sense_data.append(light)    
#schedule repeat every hour
time.sleep(6)
main()
