#modules for use in smartSleep.py
from datetime import time

def isKid(age):
    #checks if a user is a child
    return 10 <= age and age <= 18

def isAdult(age):
    #checks if a user is an adult
    return 18 <= age and age <= 64

def isSenior(age):
    #checks if a user is a senior
    return 65 <= age

def isFemale(gender):
    #checks if a user is female
    return gender == 'f' or gender == 'F'

def timeToMinutes(time):
    #converts given time to minutes

    return (time.hour * 60) + time.minute

def minutesToTime(minutes):
    #converts given minutes to a time

    extraMinutes = minutes % 60
    hours = int((minutes - extraMinutes) / 60)

    newtime = time(hours, extraMinutes)

    return newtime

def strTimeToTime(strtime):
    #converts a given time in string and converts it to a time object

    #finds the hours
    if len(strtime) == 4:
        hours = int(strtime[0])
    else:
        hours = int(strtime[0:2])
    
    #finds the minutes
    minutes = int(strtime[-2:len(strtime)])

    return time(hours, minutes)

def addTime(timeOne, timeTwo):
    #adds 2 given times in datetime.time() datatype

    #finding the hours of the time for addition
    hours1 = timeOne.hour
    hours2 = timeTwo.hour

    #finding the minutes of the time for addition
    minutes1 = timeOne.minute
    minutes2 = timeTwo.minute

    #adding the final hours and minutes
    finalHours = (hours1 + hours2) % 24
    finalMinutes = (minutes1 + minutes2) % 60

    #returning the final time
    return time(finalHours, finalMinutes)

def subTime(timeOne, timeTwo):
    #subtracts 2 given times in datetime.time() datatype
    """
    #finding the hours of the time for subtraction
    hours1 = timeOne.hour
    hours2 = timeTwo.hour

    #finding the minutes of the time for subtraction
    minutes1 = timeOne.minute
    minutes2 = timeTwo.minute

    print("Hours: ", hours1, " ", hours2)
    print("Minutes: ", minutes1, " ", minutes2)

    #subtracting the final hours and minutes
    finalHours = (hours1 - hours2) % 24
    finalMinutes = (minutes1 - minutes2) % 60

    print("Final hours: ", finalHours)
    print("Final minutes: ", finalMinutes)

    #returning the new time class
    return time(finalHours, finalMinutes)
    """
    #converting times to minutes
    minutes1 = timeToMinutes(timeOne)
    minutes2 = timeToMinutes(timeTwo)

    #converting minutes to decimals in relation to times
    decimal1 = minutes1 / 60
    decimal2 = minutes2 / 60

    #subtracting decimals to be converted back to minutes, then time
    decimalDif = decimal1 - decimal2

    #checking if the time will be in the previous day, or in the same day
    if decimalDif < 0:
        decimalDif = 24 + decimalDif

    #converting decimalDif back to minutes
    minutesDif = int(decimalDif * 60)

    #converting minutesDif back to time
    timeDif = minutesToTime(minutesDif)

    #returning the time
    return timeDif
    