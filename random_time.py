import time
import random
def getRandomDate(startdate, enddate):
    print("Printing random dates between", startdate,"and",enddate)
    randomg = random.random()
    dateformate = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startdate, dateformate))
    endtime = time.mktime(time.strptime(enddate, dateformate))

    randomTime = starttime + randomg * (endtime - starttime)
    randomDate = time.strftime(dateformate, time.localtime(randomTime))
    return randomDate

print("Random date is:", getRandomDate("1/20/2025", "10/7/2025"))