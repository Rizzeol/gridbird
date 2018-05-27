import time
import threading
import random


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
            print('%s ---- supplying-power----- battery  %s'%(self.houseName,self.batteryState)) #the battery can supply power to the grid
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

# test data for selling price for each houses
def sell_p(house_num):
        try:
            with open('sellprice.txt', 'w+') as myfile:
                for i in range(house_num):
                    p_s = round((random.uniform(0.002, 0.008)),4)
                    p_s = str(p_s)

                    myfile.write((p_s + "\n"))
        except IOError:
            print("Error opening file")
        finally:
            myfile.close()
# test data for buying price for each houses
def buy_p(house_num):
        try:
            with open('buyprice.txt', 'w+') as myfile:
                for i in range(house_num):
                    p_b = round((random.uniform(0.002, 0.008)), 4)
                    p_b = str(p_b)
                    myfile.write((p_b + "\n"))
        except IOError:
            print("Error opening file")
        finally:
            myfile.close()
#Battery percentage of each houses
# Some houses may not have battery, have to fix that as well.
def storage(house_num):

        try:
            with open('storage.txt', 'w+') as myfile:
                for i in range(house_num):
                    stor = random.randint(7,97)
                    stor = str(stor)
                    myfile.write((stor + "\n"))

        except IOError:
            print("Error opening file")
        finally:
            myfile.close()
# representating demand data as 0 or 1 for each houses
def demand(house_num):
    try:
        with open('demand.txt', 'w+') as myfile:
            for i in range(house_num):
                list = [0,1]
                random.shuffle(list)
                dem = random.choice(list)
                dem = str(dem)
                print(dem)
                myfile.write((dem + "\n"))

    except IOError:
        print("Error opening file")
    finally:
        myfile.close()

def testHouseBidding():

    house1 = House('H1')
    house1.batteryState = 100
    efi_comm_describe(house1.houseName)

    house2 = House('H2')
    house2.batteryState = 50

    send_efi_comm_supply_instruction() #SIMULATE EFI here
    house1.start_supply_power_thread()

    #start consuming the energy from the other house
    receive_efi_comm_charge_instruction() #SIMULATE EFI here again
    house2.start_consume_power_thread()

    time.sleep(5)
    house1.stop_supply()

def efi_comm_describe(houseName):
    print('<- EFI_Describe(%s, Storage)'%houseName)
    print('<- EFI_Actuator0:runningmode(IDLE)')

def receive_efi_comm_charge_instruction():
    print('-> EFI_flexibleInstruction(Actuator0: charge, upperbound=100)')
    print('<- EFI_instructionStatusUpdate(ACCEPTED, STARTED)')

def send_efi_comm_supply_instruction():
    print('<- EFI_flexibleInstruction(Actuator0: discharge, lowerbound=25')
    print('<- EFI_instructionStatusUpdate(ACCEPTED, STARTED)')

def find_lowest_bidder():
    return "h1"

if __name__ == "__main__":
    # Test all Houses and print its batterystatus
    #  print energy demand
    sell_p(5)
    buy_p(5)
    storage(5)
    demand(5)
    testHouseBidding()
    house = find_lowest_bidder()

    #ToDO!





