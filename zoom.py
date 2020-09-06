import pandas as pd
import pyautogui as pg
import time
from datetime import datetime
import webbrowser
pg.FAILSAFE = True


def zoommeeting():
    #All Meeting Schedule in CSV file mentioned
    file = pd.read_csv('meeting.csv')

    #meeting scheduler time
    for meeting_iterate in range(len(file['Meeting_ID'])):
        meeting_id, meeting_time, meeting_pass = file['Meeting_ID'][meeting_iterate],file['Time'][meeting_iterate],file['Password'][meeting_iterate]

        #print - meeting_id, meeting_time, meeting_password
        print(meeting_id.replace('`', ''), meeting_time, meeting_pass)

        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            time.sleep(1)

            #set timing to login 2 min before
    #         l = meeting_time[-5:-3]
    #         l = int(l)-2
    #         meeting_time = meeting_time.replace(meeting_time[-5:-3],str(l))

            if now.strftime("%H:%M:%S") == meeting_time:

                #launch Zoom App
                x_cord, y_cord = pg.size()
                pg.move(x_cord//2, y_cord, duration=1)
                zoom_location = pg.locateOnScreen('ing/zoom_ico.png')
                pg.click(zoom_location, duration=0.25)
                time.sleep(10)
                join_ico = pg.locateCenterOnScreen('img/joinButton.png')
                pg.click(join_ico, duration=1)
                time.sleep(3)

                #pass meeting ID
                pg.press('enter', interval=1)
                pg.write(meeting_id)

                #pass meeting password
                pg.press('enter', interval=1)
                time.sleep(15)
                pg.write(meeting_pass)
                pg.press('enter')

                #sleep then exit from while
                while True:
                    if pg.locateOnScreen('img/zoomend.png'):
                        pg.press('enter')
                        break
                break

