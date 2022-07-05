import datetime
import threading
import time

########################################################

class ThreadClock:
    __Total = None
    __LEd = None
    __Thr = None

    ## Questo 01:  (Criar o construtor da classe ThreadClock
    ##               conforme diagrama da Figura 01)
    def __init__(self, __LEd_a):
        self.__LEd = __LEd_a

        ## Questo 02:  (Criar o mtodo que inicia a ThreadClock)
    def iniciar(self, Total_a):
        try:
            if (self.__Thr is None):
                self.__Total = Total_a
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s" % (ex))

            ## Questo 03:  (Criar o mtodo que encerra a ThreadClock)
    def parar(self):
        try:
            self.__Total = 0
            self.__Thr = None
        except Exception as ex:
            print("Error: unable to stop thread: %s" % (ex))

    def isRunning(self):
        if (self.__Thr is None):
            return(False)
        else:
            return(True)

    def run(self):
        count = 0.0
        while count < self.__Total:
            now = datetime.datetime.now()
            h = now.hour
            m = now.minute
            s = now.second
            count += 1.0
            self.__LEd.setText("%d:%d:%d" % (h,m,s))
            time.sleep(0.4)
        self.__Thr = None

########################################################