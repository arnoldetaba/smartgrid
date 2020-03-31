import socket
from threading import Thread
from devices import ElectricLamp
import time
import json
import pygame, sys
from pygame.locals import *

# Runner code for GridDevice.,
# the GridDevice is a home on the grid

# Features
#- constantly sends random value to server about current consumption
#- constantly sends a list of active processes on it to server
#- the active processes are supposed to mirror electric appliances in a home
#- can receive requests from a server to kill some processes (mirroring the requests
# made by a real control unit to end some devices activities on the grid),
#- can receive a requests to completely shutdown.
#- has the ability to accept or refuse discard the two orders above.

#- Each client initially possess some 0.0 FCFA cash on server-side.
#- A client that accept an order, and behave accordlingly to it is rewarded server side.

CU_IP, CU_PORT = ("127.0.0.1", 5550)
LISTEN_IP, LISTEN_PORT = ("0.0.0.0", 5551)

class Home:
    devices = []
    def __init__(self):
        # start Electric Lamp, TV, Fridge, Washing Machine processes
        self.sc = socket.socket()
        self.sc.connect((CU_IP, CU_PORT))
    def push2Cu(self):
        # emit in background thread
        pass
    def listenFromCu(self):
        # listen in background thread
        pass
    def _parseAction(self):
        pass
    def _execute(self, action, arg):
        # action = ("kill", "process_name")
        # action = ("shutdown")
        if action == "kill":
            for lamp in self.devices:
                if str(lamp) == arg:
                    lamp.kill()
        elif action == "up":
            for lamp in self.devices:
                if str(lamp) == arg:
                    print("calling lamp.up()")
                    lamp.up()
        elif action == "shutdown":
            subprocess.call(["shutdown", "0"])
    # shell exec here
    def _exec(self, cmd):
        pass
    def add_device(self, device):
        self.devices.append(device)
    # Periodically emits consumption information
    # of Electric Lamp
    def _emit(self, emitting):
        try:
            self.sc.send(emitting.encode()+b"\n")
        except Exception as e:
            print(e)
    def emit(self):
        while 1:
            emitting = {}
            for device in self.devices:
                #{"#lamp1":0, "#lamp2":38, "#lamp3":35, "#lamp4":0}
                emitting[str(device)] = device.emit()
            self._emit(json.dumps(emitting))
            time.sleep(2)
    # Constantly awaits for command from Grid Control Unit
    def listen(self):
        print("starting inner listener")
        while 1:
            data = self.sc.recv(1024)
            print(f"data recvd: {data}")
            data = json.loads(data)
            action = data[0]
            arg = data[1]
            self._execute(action, arg)
            #if data != None:
            #    print(f"Received order: {data}")
            #    #command(data)
    def draw(self):
        pygame.init()

        DISPLAY=pygame.display.set_mode((900,400),0,32)

        BLACK=(0,0,0)
        BLUE=(0,0,255)
        GREEN=(0,255,0)
        RED = (255,0,0)
        YELLOW=(255,255,0)
        color = BLUE

        lampImg = pygame.image.load("./lightbulb.jpeg")
        tvImg = pygame.image.load("./tv.png")
        fridgeImg = pygame.image.load("./fridge.png")

        DISPLAY.fill(BLACK)
        pygame.display.set_caption("lamp1")
        pygame.display.flip()

        #pygame.draw.rect(DISPLAY,color,(50,50,200,200))
        #pygame.draw.rect(DISPLAY,color,(300,50,200,200))
        #pygame.draw.rect(DISPLAY,color,(550,50,200,200))
        while True:
            if self.devices[0].state == True:
                #pygame.draw.rect(DISPLAY,GREEN,(50,50,200,200))
                DISPLAY.blit(lampImg, (50,50))
            else:
                pygame.draw.rect(DISPLAY,BLACK,(50,50,200,200))

            if self.devices[1].state == True:
                #pygame.draw.rect(DISPLAY,RED,(300,50,200,200))
                DISPLAY.blit(tvImg, (300,50))
            else:
                pygame.draw.rect(DISPLAY,BLACK,(300,50,200,200))

            if self.devices[2].state == True:
                #pygame.draw.rect(DISPLAY,YELLOW,(550,50,200,200))
                DISPLAY.blit(fridgeImg, (550,50))
            else:
                pygame.draw.rect(DISPLAY,BLACK,(550,50,200,200))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == "__main__":
    devices = []
    lamp1 = ElectricLamp("lamp1", 30, 44)
    lamp2 = ElectricLamp("lamp2", 45, 49)
    lamp3 = ElectricLamp("lamp3", 60, 100)
    home = Home()
    home.add_device(lamp1)
    home.add_device(lamp2)
    home.add_device(lamp3)
    thread0 = Thread(target=home.emit)
    thread0.start()
    thread1 = Thread(target=home.listen)
    thread1.start()

    home.draw()
