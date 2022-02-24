from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

receiver = AudioReceiver('ip do reciver', 9999)
receiver_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender('ip do host', 5555)
sender_thread = threading.Thread(target=sender.start_stream)

receiver_thread.start()
sender_thread.start() 