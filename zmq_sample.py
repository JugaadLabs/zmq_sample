import numpy as np
from zmq_utils import zmqNode
import time


player1 = zmqNode('send', 9000)
player2 = zmqNode('recv', 9000)

while True:
    player1.send_array(np.random.rand(480, 640, 3))
    t1 = time.time()
    array = player2.recv_array()
    print(array)
    print(time.time() - t1)