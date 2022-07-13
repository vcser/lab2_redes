#!/usr/bin/env python3
import sys
import os
import time

from rudp import RUDPClient


PROGRESS_BAR_LENGTH = 50


def progress_bar(percent):
    length = percent * PROGRESS_BAR_LENGTH / 100
    print("\r[" + "#" * length + " " * (PROGRESS_BAR_LENGTH -
          length) + "]" + str(percent) + "%", end="")


def main():
    client = RUDPClient("localhost", 10000)

    while True:
        try:
            # iniciar una nueva coneccion
            reply = client.send_recv("NEW CONNECTION")
            # imprimir archivos disponibles
            print(reply, end="")
            # seleccionar archivo para descargar
            selection = input()
            # obtener archivo seleccionado
            file = client.send_recv(selection)
            print(file)
        except:
            print("no response; giving up", file=sys.stderr)

            # Necesitamos usar os._exit en lugar de sys.exit,
            # pues el proceso de esperar una respuesta del servidor
            # utiliza hilos y la salida "forzosa" que nos ofrece
            # os._exit mata esos hilos a la vez que mata el proceso
            # principal
            os._exit(1)

        time.sleep(1)


if __name__ == "__main__":
    main()
