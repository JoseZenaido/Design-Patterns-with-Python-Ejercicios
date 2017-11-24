""""Author: Hernández Venegas José Zenaido
    gmail: josehdz3321@gmail.com
    date: 11/11/2017
    Description: En esta clase primero interactua con
    el usuario para ver el propósito proporcionar un
    subrogado o intermediario de un objeto para
    controlar su acceso."""

import time


class Producer:
    def producer(self):
        print("Producer has time to meet you know!")


class Proxy:
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def producer(self):
        print("Artist checking if Producer is available ...")

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(2)

            self.producer.meet()

        else:
            time.sleep(2)
            print("Producer is busy!")


p = Proxy()

# Make the proxy : Artist produce until Producer is available
p = Producer()

# Change the state to occupied
p.occupied = 'Yes'

# Make the Producer producer
p.producer()
