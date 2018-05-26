import time
import threading

class House:
    def __init__(self, houseName):
        self.houseName = houseName
        self.batteryState = 100
        self.session_stopping = False #stops the battery charge
        self.battery_thread = None
        self.demand = 0 #No demand nessesary

    def keepalive(self):
        ticks = 0
        while True:
            print('================keepalive=================')
            print('battery:', self.batteryState)
            self.batteryState = self.batteryState-1
            time.sleep(1)
            if (self.session_stopping == True):
                 break

    def start_keepalive_thread(self):
        self._msghandler_thread = threading.Thread(target=self.keepalive)
        self._msghandler_thread.setDaemon(True)
        self._msghandler_thread.start()

    def stop_supply(self):
        self.session_stopping = True

def DataPoints(randomBaseInt):
        dirList = []

def testHouseBidding():
    house = House('H1')
    house.batteryState = 100
    randomData = DataPoints(1)
    house.start_keepalive_thread()
    time.sleep(5)
    house.stop_supply()


if __name__ == "__main__":
    # Test all Houses and print its batterystatus
    testHouseBidding()


