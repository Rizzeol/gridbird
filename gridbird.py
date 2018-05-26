import time
import threading

class House:
    def __init__(self, houseName):
        self.houseName = houseName
        self.batteryState = 100

        self.session_stopping = False #stops the battery supply
        self.battery_thread = None
        self.demand = 0 #No demand nessesary

    def supplyPower(self):
        ticks = 0
        while True:
            print('%s ---- supplying-power----- battery %s'%(self.houseName,self.batteryState)) #the battery can supply power to the grid
            self.batteryState = self.batteryState-1
            time.sleep(1)
            if (self.session_stopping == True):
                 break

    def start_supply_power_thread(self):
        self._msghandler_thread = threading.Thread(target=self.supplyPower)
        self._msghandler_thread.setDaemon(True)
        self._msghandler_thread.start()

    def consumePower(self):
        ticks = 0
        while True:
            print('%s---- consume-power----- battery: %s'%(self.houseName,self.batteryState)) #the battery can supply power to the grid
            self.batteryState = self.batteryState+1
            time.sleep(1)
            if (self.session_stopping == True):
                 break

    def start_consume_power_thread(self):
        self._msghandler_thread = threading.Thread(target=self.consumePower)
        self._msghandler_thread.setDaemon(True)
        self._msghandler_thread.start()

    def stop_supply(self):
        self.session_stopping = True

def DataPoints(randomBaseInt):
        dirList = []

def testHouseBidding():
    house1 = House('H1')
    house1.batteryState = 100
    randomData = DataPoints(1)
    house1.start_supply_power_thread()

    house2 = House('H2')
    house2.batteryState = 50
    randomData = DataPoints(1)
    house2.start_consume_power_thread()
    time.sleep(5)
    house1.stop_supply()

if __name__ == "__main__":
    # Test all Houses and print its batterystatus
    #  print energy demand

    testHouseBidding()


