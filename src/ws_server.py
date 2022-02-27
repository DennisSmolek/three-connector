import threading
import json
import inspect

from websocket_server import WebsocketServer

clients = []

class WS:

    global clients

    def __init__(self):
        self.server = None
    
    def new_client(self, client, server):
        print('open')
        clients.append(client)

    def client_left(self, client, server):
        print('close')

    def message_received(self, client, server, message):
        print('receive')
    
    def start_server(self, host, port):
        
        if self.server:
            return False
        
        self.server = WebsocketServer(host, port)
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received) 
        self.wserver_thread = self.server.run_forever(True)

        return True

    def stop_server(self):
        if not self.server:
            return False

        # shutdown server
        self.server.shutdown_gracefully()
        self.server = None

        # clear clients
        clients.clear()
        
        return True
    
    def broadcast(self, message):
        for client in clients:
            self.server.send_message(client, message)

