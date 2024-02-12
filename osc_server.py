from pythonosc import dispatcher
from pythonosc import osc_server
import threading

def print_handler(address, *args):
    print(f"Received message from {address}")
    for arg in args:
        print(f"Argument: {arg}")

# Set the IP and port for the OSC server
ip = "127.0.0.1"
port = 12345

# Create a dispatcher and register a handler for a specific address
disp = dispatcher.Dispatcher()
disp.map("/filter", print_handler)  # This will catch messages sent to the "/filter" address

# Set up server with the dispatcher
server = osc_server.ThreadingOSCUDPServer((ip, port), disp)

# Start the server
print(f"Serving on {server.server_address}")
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()
