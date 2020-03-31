import socket
from threading import Thread
import json

class GridController:
    def __init__(self):
        self.LHOST = "0.0.0.0"
        self.LPORT = 5550
        self.GRID_DEVICES = []
    def _emit(self, addr, data):
        print("in _emit")
        for (peer_addr,conn) in self.GRID_DEVICES:
            print(f"{addr} == {peer_addr[0]}")
            if peer_addr[0] == addr:
                print(f"sending data to conn: {peer_addr[0]}")
                conn.send(data.encode()+ b"\n")
    def command(self, action, addr=None, device_id=None):
        #command("kill", "<peer_ip>", "<device_id>")
        #command("shutdown", "<peer_ip>")
        data = (action, device_id)
        self._emit(addr, json.dumps(data))
    def _listen(self, conn, addr):
        while 1:
            data = conn.recv(1024)
            if data != None:
                data = json.loads(data)
                log = open("./log.txt", "a")
                log.write(f"{addr[0]}={data}\n")
                log.close()
                #print(f"Received from {addr} : {data}")
    def listen(self):
        sc = socket.socket()
        sc.bind((self.LHOST, self.LPORT))
        sc.listen()
        print("Started Server!\n")
        while 1:
            conn, addr = sc.accept()
            self.GRID_DEVICES.append((addr,conn))
            thread0 = Thread(target=self._listen, args=(conn,addr))
            thread0.start()

    def ui(self):
        while 1:
            line = input("(command)> ")
            if line != "":
                try:
                    # kill 127.0.0.1 lamp1
                    cmd = line.split()[0]
                    arg1 = line.split()[1] # peer_addr
                    arg2 = line.split()[2]
                except Exception as e:
                    print("help!\n")
                    print("- shutdown: To shutdown a home/pc")
                    print("- kill: To shutdown a specific device at a home/pc")
                    print("- up <IP_OF_PC> <DEVICE_ID>: To turn up a specific device at a home/pc")
                    print("- ls: To a show a list of connected clients")
                    print("[NOTE]")
                    print("there are currently only 3 devices registered for each home")
                    print("they are lamp1,lamp2,lamp3")
                    print("examples: ")
                    print("###### (command)> ls -l -a")
                    print("###### (command)> kill 127.0.0.1 lamp1")
                    print("###### (command)> up 127.0.0.1 lamp1")
                    print("###### (command)> shutdown 127.0.0.1 all")
                    print("\n")
                            
                    continue
                if (cmd == "shutdown"):
                    print(cmd)
                    self.command("shutdown", arg1)
                elif (cmd == "kill"):
                    self.command("kill", arg1, arg2)
                elif (cmd == "up"):
                    self.command("up", arg1, arg2)
                elif (cmd == "ls"):
                    for (addr,_) in self.GRID_DEVICES:
                        print(f"smart homes online :{addr}")

if __name__ == "__main__":
    grid_controller = GridController()
    thread0 = Thread(target=grid_controller.listen)
    thread0.start()
    thread1 = Thread(target=grid_controller.ui)
    thread1.start()

