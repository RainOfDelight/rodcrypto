import base64
import Crypto.Util.number

import telnetlib
import json
import codecs
HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


response = json_recv()

while response:
    print(response)
    enc = response['type']
    encoded = response['encoded']

    if enc == 'rot13':
        #{"type": "rot13", "encoded": "Pbznapur_uhax_ireonyyl"}
        print("decoding rot13 ... ->", end = " ")
        result = (codecs.decode(encoded, 'rot_13'))
    elif enc == 'hex':
        print("decoding hex ... ->", end = " ")
        result = ""
        for index in range(0, len(encoded), 2):
            result = result + chr(int(encoded[index : index+2], 16))
    elif enc == 'utf-8':
        print("decoding utf ... ->", end = " ")
        #{"type": "utf-8", "encoded": [115, 104, 101, 115, 95, 66, 117, 116, 108, 101, 114, 95, 114, 101, 112, 114, 101, 115, 101, 110, 116, 105, 110, 103]}
        result = ""
        for elem in encoded:
            result = result + chr(elem)
    elif enc == 'base64':
        print("decoding base64 ... ->", end = " ")
        #{"type": "base64", "encoded": "cmVmZmluZ19pbnRyb3ZlcnRzX211enpsaW5n"}
        result = base64.b64decode(encoded).decode("utf-8")
    elif enc == 'bigint':
        print("decoding bigInt ... ->", end = " ")
        #{"type": "bigint", "encoded": "0x657870656e7365735f64656d6f6e73747261626c655f706f6c696379686f6c64657273"}
        if(encoded[:2] == '0x'):
            number = int(encoded[2:], 16)
            result = Crypto.Util.number.long_to_bytes(number).decode("utf-8")

    print(result)

    toSend = {
        "decoded": result
    }
    json_send(toSend)
    response = json_recv()