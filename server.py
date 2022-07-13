#!/usr/bin/env python3

from rudp import RUDPServer
import threading


class Request:
    def __init__(self, file):
        self.file = file
# a

def handle_connection():
    pass


def main():
    server = RUDPServer(10000)

    available_files = ["file.txt"]

    while True:
        # new connection
        message, address = server.receive()
        print(message)
        if (message == "NEW CONNECTION"):
            # iniciar una nueva coneccion
            print("starting a new connection")
            print(f"{address}: {message}")
            # enviar la cantidad de archivos disponibles
            files_string = "Available files:\n"
            for i in available_files:
                files_string += f"\t{i}\n"
            server.reply(address, files_string)
            # que archivo sera descargado
            message, address = server.receive()
            print(message + " will be downloaded")
            file = open(message, "rb")
            text = file.read()
            file.close()
            # enviar archivo seleccionado
            server.reply(address, text)
            server.reply(address, b"chao")


if __name__ == "__main__":
    main()
