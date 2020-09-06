import zoom, gmeet
from pandas import DataFrame
import pandas



meet_id = []
meet_time = []
meet_pass = []


chose = int(input("1. Zoom Meeting\n2. Google Meeting (Meet)\n"))

# f_open = open('meeting.csv', 'w')
# f_open.truncate(0)
# f_open.close()

if chose == 1:
    C = {'Time': 0,
         'Meeting_ID': 0,
         'Password': 0
         }
    no_of_meetings = int(input("Enter No. of Meetings: "))
    for meeting in range(no_of_meetings):
        meet_time.append(input("Enter Time in 24 Hrs Format (HH:MM:SS): "))
        ids = input("Enter Meeting ID: or Link: ")
        if ids.isdigit():
            meetid = '`'+ids
            meet_id.append(meetid)
            meet_pass.append(input("Enter Passcode: "))
        else:
            meet_id.append(ids)
            meet_pass.append('nan')
    C['Time'], C['Meeting_ID'], C['Password'] = meet_time, meet_id, meet_pass
    df = DataFrame(C, columns=['Time', 'Meeting_ID', 'Password'])
    export_csv = df.to_csv(r'meeting.csv', index=None, header=True)
    # here you have to write path, where result file will be stored
    print("Your Inputed Data: ",pandas.read_csv('meeting.csv'))

    #Call to Zoom Meet Module
    zoom.zoommeeting()



else:
    C = {
        'Time': 0,
        'Meeting_Link': 0,
        }

    no_of_meetings = int(input("Enter No. of Meetings: "))
    for meeting in range(no_of_meetings):
        meet_time.append(input("Enter Time in 24 Hrs Format (HH:MM:SS): "))
        meet_id.append(input("Enter Meeting Link: "))
    C['Time'], C['Meeting_Link'] = meet_time, meet_id
    df = DataFrame(C, columns=['Time', 'Meeting_Link'])
    export_csv = df.to_csv(r'meeting.csv', index=None, header=True)
    # here you have to write path, where result file will be stored
    print("Your Inputed Data: ", pandas.read_csv('meeting.csv'))

    #Call to Google Meet Module
    gmeet.googlemeeting()
