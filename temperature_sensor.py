import mraa
import time
import math

def getTemperature():
    B = 3975
    ain = mraa.Aio(0)
    a = ain.read() 
    resistance = (1023-a)*10000.0/a
    temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15 #1raOp
    #temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-263.15
    return str(temp)
