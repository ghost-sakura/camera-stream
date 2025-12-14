from vidstream import CameraClient, StreamingServer
import threading
import time

# Streaming server (runs on the camera sender machine)
receiving = StreamingServer('0.0.0.0', 9999)

# Camera client (connects to the server IP)
sending = CameraClient('SERVER_IPV4_ADDRESS', 9999)

# Start server thread
t1 = threading.Thread(target=receiving.start_server)
t1.start()

time.sleep(2)

# Start client thread
t2 = threading.Thread(target=sending.start_stream)
t2.start()

# Stop streaming on user input
while input("Type STOP to end streaming: ") != "STOP":
    pass

receiving.stop_server()
sending.stop_stream()
