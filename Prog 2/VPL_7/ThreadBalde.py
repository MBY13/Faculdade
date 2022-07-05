import threading
import time

##################################################

class ThreadBalde:
    __Total = None
    __LEd = None
    __PBar = None
    __Thr = None
    
    def __init__(self, LEd_a, PBar_a):
        self.__LEd = LEd_a
        self.__PBar = PBar_a
        
    def iniciar(self, Total_a):
        try:
            if (self.__Thr is None):
                self.__Total = Total_a
                self.__Sair = False
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s" % (ex))
            
    def parar(self):
        try:
            self.__Sair = True
            self.__Thr = None
        except Exception as ex:
            print("Error: unable to stop thread: %s" % (ex))
            
    def isRunning(self):
        if (self.__Thr is None):
            return(False)
        else:
            return(True)
        
    def run(self):
        count = 0
        while count < self.__Total:
            count += 1
            self.__LEd.setText("%d" % count)
            self.__PBar.setValue(count)
            time.sleep(0.1)
            if (self.__Sair==True):
                break
        self.__Thr = None
        
        ##################################################
        