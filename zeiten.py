'''
Created on 24.04.2012

@author: andreasrettig
'''

etat = 1e8
costperasic = 100
opsPerSecond = 5e8
bits = 128

asics = etat / costperasic

timeInS = 2**bits / opsPerSecond / asics
timeInH = timeInS/3600
timeInD = timeInH/24
timeInY = timeInD/365

print "ASICS = "+str(asics)
print "TIME [s]= "+str(timeInS)
print "TIME [h]= "+str(timeInH)
print "TIME [y]= "+str(timeInY)

mooreUnits = 0
mooreMonths= 18
hoursNeededMax = 48

while (timeInH > hoursNeededMax):
    timeInH /= 2
    mooreUnits += 1

years = mooreUnits * mooreMonths/12
print "Time to break "+str(bits)+" bits in "+str(hoursNeededMax)+" hours = "+str(years)+" years"