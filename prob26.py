#date an dick and balls
from datetime import datetime
from time import time

import time
def datediffinseconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds
  
def D(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days)
    
def H(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return (hours)
    
def M(seconds):
	minutes, seconds = divmod(seconds, 60)
	return (minutes)
    
def S(seconds):
	return (seconds)
    
def DHMS(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)
    
def HMS(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return (hours, minutes, seconds)
    
def MS(seconds):
	minutes, seconds = divmod(seconds, 60)
	return (minutes, seconds)
    
def DH(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours)
    
def DM(seconds):
	minutes = seconds // 60
	days, minutes = divmod(minutes, 1440)
	return (days, minutes)
    
def DS(seconds):
	days, seconds = divmod(seconds, 86400)
	return (days, seconds)
    
def HM(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return (hours, minutes)
    
def HS(seconds):
	hours, seconds = divmod(seconds, 3600)
	return (hours, seconds)
    
data = []
loopbreak = time.time() + 1
try:
    while loopbreak > time.time():
        data.append(input())
        loopbreak = time.time() + 1
except EOFError:
    for i in range(0, len(data)):
        startdate, starttime, enddate, endtime, form = data[i].split()
        start = startdate + ' ' + starttime
        end = enddate + ' ' + endtime
        
        start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        
        if form == 'D':
            print("there are %d days remaining until" % D(datediffinseconds(start, end)), end)
        elif form == 'H':
            print("there are %d hours remaining until" % H(datediffinseconds(start, end)), end)
        elif form == 'M':
            print("there are %d minutes remaining until" % M(datediffinseconds(start, end)), end)
        elif form == 'S':
            print("there are %d seconds remaining until" % S(datediffinseconds(start, end)), end)
        elif form == 'DHMS':
            print("there are %d days %d hours %d minutes %d seconds remaining until" % DHMS(datediffinseconds(start, end)), end)
        elif form == 'HMS':
            print("there are %d hours %d minutes %d seconds remaining until" % HMS(datediffinseconds(start, end)), end)
        elif form == 'MS':
            print("there are %d minutes %d seconds remaining until" % MS(datediffinseconds(start, end)), end)
        elif form == 'DH':
            print("there are %d days %d hours remaining until" % DH(datediffinseconds(start, end)), end)
        elif form == 'DM':
            print("there are %d days %d minutes remaining until" % DM(datediffinseconds(start, end)), end)
        elif form == 'DS':
            print("there are %d days %d seconds remaining until" % DS(datediffinseconds(start, end)), end)
        elif form == 'HM':
            print("there are %d hours %d minutes remaining until" % HM(datediffinseconds(start, end)), end)
        elif form == 'HS':
            print("there are %d hours %d seconds remaining until" % HS(datediffinseconds(start, end)), end)
            