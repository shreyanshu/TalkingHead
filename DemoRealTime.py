import RealTimePhonemeCaller
import RealTimeRawFiles
import threading
import VedioFromImages
import time

def run(mouth):
    try:
        t = threading.Thread(target=RealTimeRawFiles.run(mouth))
        t.start()
        #
        # t_face = threading.Thread(target=VedioFromImages.makeFirstFace)
        # t_face.start()
        # # t.join()
        # time.sleep(1)

        # t2.join()


    except:
        print "failed"

# run()