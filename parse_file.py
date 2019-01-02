import re
import sys
import os.path


expDate = '2018-11-27'
# Large Loop
expTime = '12-54-05'

# Small Loop
#expTime = '11-21-09'


infile = r"/home/xenial/Datasets/CIVIT/Nov_27/rover/NMND17420010S_"+expDate+"_"+expTime+".LOG"

keep_phrases = ["FINESTEERING"]

with open(infile) as f:
    f = f.readlines()

with open('/home/xenial/Datasets/CIVIT/Nov_27/rover/GPS_'+expDate+'_'+expTime+'.txt', 'w') as file:
    file.write("gpsWeek,gpsSOW\n")
    for line in f:
        for phrase in keep_phrases:
            if phrase in line:
                resFind = re.findall('\.*?FINESTEERING,(\d+).*?,(\d+\.\d*)',line)[0]
                gpsWeek = re.findall('\.*?FINESTEERING,(\d+)',line)[0]
                gpsWeekStr = str(gpsWeek)
                
                gpsSOW = re.findall('\.*?FINESTEERING,'+ gpsWeekStr + ',(\d+\.\d*)',line)[0]
                gpsSOWStr = str(gpsSOW)

                file.write(gpsWeekStr+','+gpsSOWStr+'\n')
                break

print ("------------------------------------")

