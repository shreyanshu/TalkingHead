import RealTimePhonemeCaller
import RealTimeRawFiles
import threading
import time


try:
    t= threading.Thread(target=RealTimeRawFiles.run)
    t.start()
    # t.join()
    # time.sleep(1)
    t2 = threading.Thread(target=RealTimePhonemeCaller.run())
    t2.start()
    # t2.join()


except:
    print "failed"
