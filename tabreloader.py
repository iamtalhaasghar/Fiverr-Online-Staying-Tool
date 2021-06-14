# Tab Reloader
# Talha Asghar
# 16 April 2020

def startClicking():
    import time
    from datetime import datetime
    import keyboard as kb
    clickTime = 0.1
    sleepTime = 3
 

    input('Open Your Browser and then press any key to continue...')

    startTime = datetime.now()
    clickCount = 0
    elapsedTime = 0
    while True:
        for i in range(0, sleepTime):
            print(sleepTime - i)
            time.sleep(1)
        
        kb.press_and_release('ctrl+r')

        elapsedTime = (datetime.now() - startTime).total_seconds()
        print("Time Elapsed (in hrs) : %.2f\nReload Count: %d" % (elapsedTime / 3600, clickCount))
        clickCount += 1
if __name__=="__main__":
	startClicking()