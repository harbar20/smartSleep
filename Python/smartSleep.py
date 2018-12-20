#Smart Sleep
#takes in gender, age, ideal wakeup time, & happiness level and decides the optimal bedtime for the user

from datetime import time
from modules import *
from errors import *

#parameters to decide optimal sleep
#gender of user. we can't handle non-binary yet
gender = input("Gender (M or F): ")

#age of user. we can't handle children yet
age = int(input("Age: "))
#catching errors for age. if less than 10, age is not valid.
if age < 10 and age > 0:
    print("Age is too young.")
    raise ageError(age)
elif age < 0:
    print("Invalid age. Reload the page and try again.")
    raise ageError(age)

#optimal wake-up time of user. if invalid, return an error
wakeTime = input("What time do you want to wake up? ")
wakeTime = strTimeToTime(wakeTime)

sleepTimesList = []

#different sleep amounts for different ages

print("Here are your options for your bedtime: ")
#for kids
if isKid(age):
    kidWakeTime = subTime(wakeTime, time(3))

    for i in range(6):
        kidMinutes = minutesToTime(90 * (i + 1))
        kidSleep = subTime(kidWakeTime, kidMinutes)

        if isFemale(gender):
            kidSleep = subTime(kidSleep, time(0, 20))

        print("Choice ", i+1,  ": ", kidSleep)
        sleepTimesList.append(kidSleep)

#for adults
elif isAdult(age):
    for i in range(6):
        adultMinutes = minutesToTime(90 * (i + 1))
        adultSleep = subTime(wakeTime, adultMinutes)

        if isFemale(gender):
            adultSleep = subTime(adultSleep, time(0, 20))

        print("Choice ", i+1, ": ", adultSleep)
        sleepTimesList.append(adultSleep)

#for seniors
elif isSenior(age):
    seniorWakeTime = addTime(wakeTime, time(0, 30))

    for i in range(6):
        seniorMinutes = minutesToTime(90 * (i + 1))
        seniorSleep = subTime(wakeTime, seniorMinutes)

        if isFemale(gender):
            seniorSleep = subTime(seniorSleep, time(0, 20))
        
        print("Choice ", i+1, ":", seniorSleep)
        sleepTimesList.append(seniorSleep)

#person's choice for bedtime
sleepTimeChoiceInt = int(input("What time would you like to sleep (select a choice from the above choices)? "))
sleepTimeChoiceTime = sleepTimesList[sleepTimeChoiceInt - 1]

#happiness level
happiness = int(input("How are you feeling today (scale of 1-5)? "))

#actually adjusts sleep based on happiness level. Target happiness is 3
if happiness < 3:
    sleepTimeMultiplier = 3 - happiness
    multiplierTime = minutesToTime(sleepTimeMultiplier * 44)
    realSleepTime = subTime(sleepTimeChoiceTime, multiplierTime)
else:
    realSleepTime = sleepTimeChoiceTime

#accounting for studies that say people take 7 minutes to go to sleep on average
realSleepTime = subTime(realSleepTime, time(0, 7))
#accounting for studies that say people shouldn't look at screens before bedtime
realsleepTime = subTime(realSleepTime, time(0, 30))

#final time printing
print("Tonight, try to sleep at ", realSleepTime)

#Done!