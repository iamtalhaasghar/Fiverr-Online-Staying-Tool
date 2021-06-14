# Tab Reloader
# Talha Asghar
# 16 April 2020

def startClicking():
    import os
    import time
    import pyautogui as pg
    from datetime import datetime
    from pathlib import Path

    clickTime = 0.1
    sleepTime = 30

    reloadPicturePath = str(Path.home()) + "/reload.png"

    if not os.path.exists(reloadPicturePath):
        print('File "%s" does not exists.' % reloadPicturePath)
        exit()

    input('Open Your Browser and then press any key to continue...')

    # keep finding reload button on screen
    pictureLocated = False
    x = y = 0
    while not pictureLocated:
        try:
            x, y = pg.locateCenterOnScreen(reloadPicturePath)
            pictureLocated = True
        except Exception as ex:
            print('Could not find reload button on screen.')
            time.sleep(5)


    startTime = datetime.now()
    clickCount = 0
    elapsedTime = 0
    while True:
        for i in range(0, sleepTime):
            print(sleepTime - i)
            time.sleep(1)
        pg.moveTo(x, y)
        pg.click(interval=clickTime)

        elapsedTime = (datetime.now() - startTime).total_seconds()
        print("Time Elapsed (in hrs) : %.2f" % (elapsedTime / 3600))
        clickCount += 1

startClicking()