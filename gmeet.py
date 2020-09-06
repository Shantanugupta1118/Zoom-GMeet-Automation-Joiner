import pandas as pd
import pyautogui as pg
import time
from datetime import datetime
import webbrowser
pg.FAILSAFE = True

def googlemeeting():
    file = pd.read_csv('meeting.csv')
    for meeting_iterate in range(len(file['Meeting_Link'])):
        webbrowser.open(file['Meeting_Link'][meeting_iterate],
                        new=2,
                        autoraise=True)
        meeting_time = file['Time'][meeting_iterate]

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

                while True:
                    if pg.locateCenterOnScreen('img/askgoogle.png') or pg.locateCenterOnScreen('img/googlejoin.png'):
                        pg.hotkey('ctrl','d')
                        pg.hotkey('ctrl','e')
                        if pg.locateCenterOnScreen('img/askgoogle.png'):
                            c = pg.locateCenterOnScreen('img/askgoogle.png')
                        else:
                            c = pg.locateCenterOnScreen('img/googlejoin.png')
                        break
                pg.click(c)
                break
