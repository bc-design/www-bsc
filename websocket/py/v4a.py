#!/usr/bin/env python

import asyncio
import serial.aio
import websockets
import random
import time
import functools

wsdelay = 0.5
MSGMAX = 100000
SERPATH = '/dev/arduino-uno'
BAUDRATE = 9600
WSPORT = 8801

class serPort(asyncio.Protocol):
    msgpart = ""
    msgs = []
    def connection_made(self, transport):
        self.transport = transport
        transport.serial.flush()
        print('port opened', transport)
        transport.serial.rts = False
    def data_received(self, data):
        datastr = data.decode('utf-8')
        #print("msg is currently: {}".format(self.msg))
        self.msgpart += datastr
        if '\n' in self.msgpart:
            for m in self.msgpart.split('\n'):
                mparse = m.strip().split(',')
                if (len(mparse) == 3 and mparse[-1] == ''):
                    self.msgs.append(m)
                    print("{!s}".format(self.msgs[-1]))
            self.msgpart = ""
        if len(self.msgs) > MSGMAX:
            self.msgs.pop(0)
        #self.transport.close()
    def connection_lost(self, exc):
        print('port closed')
        asyncio.get_event_loop().stop()

async def listener(websocket, path):
    name = await websocket.recv()
    return name

async def consumer(websocket, path, message):
    print("< {}".format(message))
    greeting = "Hello {}!".format(message)
    await websocket.send(greeting)
    print("> {}".format(greeting))

async def producer(websocket, ser):
    while True:
        await asyncio.sleep(wsdelay)
        #mstime = int(time.time()*1000)
        mstime = int(ser.msgs[-1].split(',')[0])
        val = float(ser.msgs[-1].split(',')[1])
        message = "{:d},{:0.2f}".format(mstime, val)
        return message

async def lookback(websocket, ser):
    print(len(ser.msgs))
    for msg in (ser.msgs[i] for i in range(0,len(ser.msgs),10)):
        try:
            mstime = int(msg.split(',')[0])
            val = float(msg.split(',')[1])
            message = "{:d},{:0.2f}".format(mstime, val)
            await websocket.send(message)
            print("lookback: {}".format(msg))
        except:
            pass

async def handler(websocket,path,mytasks=[],mycallbacks=[],ser=''):
    #await lookback(websocket, ser)

    while True:
        listener_task = asyncio.ensure_future(listener(websocket, path))
        producer_task = asyncio.ensure_future(producer(websocket, ser))
        tasks = [listener_task, producer_task]
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        if listener_task in done:
            ## new data has arrived from the websocket
            print("listener_task triggered!")
            message = listener_task.result()
            await consumer(websocket, path, message)
            mycallbacks[0](message.encode('utf-8'))
            print(message.encode('utf-8'))
        else:
            listener_task.cancel()

        if producer_task in done:
            message = producer_task.result()
            await websocket.send(message)
            print("{} sent".format(message))


def main():
    loop = asyncio.get_event_loop()
    coro = serial.aio.create_serial_connection(loop, serPort, url=SERPATH, baudrate=BAUDRATE)
    #ser_task = asyncio.ensure_future(coro)
    ser_transport, ser_protocol = loop.run_until_complete(coro) # instead of coro?

    #ser_transport = ser_task.result()[0]
    #ser_protocol = ser_task.result()[1]

    myhandler = functools.partial(handler,mytasks=[],mycallbacks=[ser_transport.write],ser=ser_protocol)
    start_server = websockets.serve(myhandler, '0.0.0.0', WSPORT) # NOT localhost
    #ws_task = asyncio.ensure_future(start_server)
    asyncio.get_event_loop().run_until_complete(start_server)
    #print("ws_task results: {}".format(ws_task.result()))
    #ws_serv = ws_task.result()

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
