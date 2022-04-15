import json
import csv
from datetime import date, datetime
import jpholiday

for i in range(1,55):
    with open('./dynamodb/'+str(i)+'.csv') as source:
        firstLoop = True
        for line in source:
            if not firstLoop:
                row = line.split(',')
                row[0] = row[0].strip('"')
                row[1] = row[1].strip('"')
                row[2] = row[2].rstrip()
                row[2] = row[2].strip('"')
                if not row[2] == "":
                    peopleCount = int(row[2])
                    dateObserved = datetime.strptime(row[1],'%Y-%m-%d %H:%M:%S')
                    print([dateObserved,peopleCount])

                    if dateObserved.weekday() >= 5 or jpholiday.is_holiday(dateObserved):
                        if 9 <= dateObserved.hour < 12:
                            result = open('./generated/kyujitsu.csv', 'a')
                            writer = csv.writer(result)
                            writer.writerow([dateObserved,peopleCount])
                            result.close()
                    else:
                        if 8 <= dateObserved.hour < 19:
                            if dateObserved.hour == 8:
                                if dateObserved.minute >= 30:
                                    result = open('./generated/heijitsu.csv', 'a')
                                    writer = csv.writer(result)
                                    writer.writerow([dateObserved,peopleCount])
                                    result.close()
                            else:
                                result = open('./generated/heijitsu.csv', 'a')
                                writer = csv.writer(result)
                                writer.writerow([dateObserved,peopleCount])
                                result.close()
                            
                    
                    result = open('./result.csv', 'a')
                    writer = csv.writer(result)
                    writer.writerow([dateObserved,peopleCount])
                    result.close()

            else:
                firstLoop = False