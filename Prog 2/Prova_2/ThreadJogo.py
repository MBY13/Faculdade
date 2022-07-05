import random
import threading
import time

############################################################

class ThreadJogo:
    __Total=None
    __LEd=None
    __Thr=None

    def __init__(self, LEd_a):
        self.__LEd = LEd_a

    def iniciar(self, Total_a):
        try:
            if (self.__Thr is None):
                self.__Total = Total_a
                self.__Thr = threading.Thread(target=self.run)
                self.__Thr.start()
        except Exception as ex:
            print("Error: unable to start thread: %s" % (ex))

    def parar(self):
        try:
            self.__Total = 0 
            self.__Thr = None
        except Exception as ex:
            print("Error: unable to stop thread: %s" % (ex))

    def run(self):
        count = 0
        valor = 0
        while count < self.__Total:
            count += 1
            dado = random.randint(1,6)
            if dado == 5:
                valor += dado * 1000
                self.__LEd.setText("%d" % valor)
                break
            elif dado == 6:
                self.__LEd.setText("perde tudo")
                break
            else:
                valor += dado * 1000
                self.__LEd.setText("%d" % valor)
            time.sleep(60)
        self.__Thr = None

###########################################################