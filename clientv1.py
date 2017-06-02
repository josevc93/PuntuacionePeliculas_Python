import zmq
import sys

ctx = zmq.Context()
sock = ctx.socket(zmq.PUSH)
sock.connect("tcp://localhost:6977")
try:
	sock.send_string(sys.argv[1])
except:
	print("Error. Debes de pasar un argumento.")