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
    #converting hours to minutes (24 hour clock)

    return int((time.hours() * 60) + time.minutes())

def minutesToTime(minutes):
#converts given minutes to a time

    extraMinutes = minutes % 60
    hours = int((minutes - extraMinutes) / 60)

    return time(hours, extraMinutes)

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

    #finding the hours of the time for subtraction
    hours1 = timeOne.hour
    hours2 = timeTwo.hour

    #finding the minutes of the time for subtraction
    minutes1 = timeOne.minute
    minutes2 = timeTwo.minute

    #subtracting the final hours and minutes
    finalHours = (hours1 - hours2) % 24
    finalMinutes = (minutes1 - minutes2) % 60

    #returning the new time class
    return time(finalHours, finalMinutes)