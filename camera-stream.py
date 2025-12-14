from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

recieving = StreamingServer('192.168.1.8', 9999)

sending = CameraClient('192.168.1.7',9999)

t1 = threading.Thread(target = recieving.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target = sending.start_stream)
t2.start()

while input("") != "STOP":
    continue

recieving.stop_server()
sending.stop_stream()   
