import time
import threading



class ThreadStart(object):

    def __init__(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        print("Thread up...")


    def run(self):  
       
       while True:
           print("I'm running")
           time.sleep(5)