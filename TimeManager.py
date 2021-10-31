import os as OS
import datetime as DT
from datetime import date as Date
import csv as CSV

def tm():
    ## inputs
    stTime = input("What time did you start working on this(HHMM)?: ")
    prjName = input("What's the project name?: ")
    prjNum = input("What's the project number?: ")
    comment = input("Any comments?: ")

    ## convert input time to DT obj --> finish - start --> convert back to strs and
    ## save date and times to vars
    endTimeDT = DT.datetime.now()
    ##convert start time to DTobj
    stDate = Date.today()
    stDayNum = stDate.strftime("%w")
    stDayNum = int(stDayNum)
    stDate = stDate.strftime("%Y-%m-%d")
    stTimeStr = stDate + " " + stTime[0:2] + ":" + stTime[2:]
    stTimeDT = DT.datetime.strptime(stTimeStr, "%Y-%m-%d %H:%M")
    ##find time difference --> round time difference to hr + 2 decimal pts
    diff = endTimeDT - stTimeDT
    diff = ((diff.seconds)/(60*60))
    diff = round(diff, 2)

    ## check OS for file name: open if yes, create if no (headings = date, prj name, prj num)
    ## start time, end time, comment

    ##create file name
    fromMon = stDayNum -1
    if (-1 < fromMon < 5):
        fromMon = DT.timedelta(days=fromMon)
        monday = (stTimeDT - fromMon)
        monday = monday.strftime("%m-%d")
        filename = "Week of " + monday
    elif (fromMon == -1):
        fromMon = DT.timedelta(days=1)
        monday = (stTimeDT + fromMon)
        monday = monday.strftime("%m-%d")
        filename = "Week of " + monday
    else:
        fromMon = DT.timedelta(days=2)
        monday = (stTimeDT + fromMon)
        monday = monday.strftime("%m-%d")
        filename = "Week of " + monday
    ##check if file exists
    filename = filename + ".csv"
    def makeEntry(csvWriter, stDate, prjName, prjNum, diff, stTimeDT, endTimeDT, comment):
            entry = [stDate, prjName, prjNum, diff, stTimeDT, endTimeDT, comment]
            csvWriter.writerow(entry)
    if ((OS.path.isfile(filename)) == False):
        with open(filename, 'w', newline='') as csvfile:
            csvWriter = CSV.writer(csvfile, delimiter=',')
            headers = ["Date", "Project Name", "Project Number", "Hours", "Start Time", "End Time", "Comments"]
            #for item in headers:
            csvWriter.writerow(headers)
            makeEntry(csvWriter, stDate, prjName, prjNum, diff, stTimeDT, endTimeDT, comment)
            
    else:
        with open(filename,'a', newline='') as csvfile:
            csvWriter = CSV.writer(csvfile, delimiter=',')
            makeEntry(csvWriter, stDate, prjName, prjNum, diff, stTimeDT, endTimeDT, comment)
    print("Hell yeah, man! You worked " + str(diff) + " on " + prjName)
            
tm()
