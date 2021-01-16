

def xor(a, b):
    return bytes([x ^ y for (x, y) in zip(a, b)])

tmp = [b'{"ciphertext":"b9c6d46958209dc96da8458951"}\n', b'{"ciphertext":"b2dcca3a015782d921ab108f06ee7c5b998dd5cc6eec0f9944e7e0b0e004def6b6b40b2741623e1cee7e05f55a74a11d0fb64f95775d781c784232062880d42aca44cc5bd9128185ebd06896939a9290bf1dc2bff371e55834827da8155afa1dcf714d0f"}\n', b'{"ciphertext":"b7c0863f1e57bc9025a654db0fe96b10ce90cec53ab8299e4ba2acbcef52c3f0b4b4186e556f2952a05305fe4e69e40840"}\n', b'{"ciphertext":"bf93d53e191b999c6d8e179702a77e5fca9c9dc86ca934c75dafe5bbe652defef1fc0f2756683800ee3d51bd4c68ae1941b00e977217"}\n', b'{"ciphertext":"a1dcd33a1c57bc9025a6469e4ee5775cd09ccbc87eec32d64ca9aca1e913c3b898b40968476b3953f27f44fe4727b00902ba4f907c492c00630329407c80c435c64eca48c85ba7cbb9"}\n', b'{"ciphertext":"bfc786351919d2c46da555db1ae8605e9996c8d936ec24cb5de7e5a1a111d6f6f1f60f275b60331cf27f41b3"}\n', b'{"ciphertext":"bf94cb760d199dd13db749d74ece3254dc8ad8df6ca966d75debaca1e91797feb0e1067315747d1ee97440b10f65b608419b4899394c36007153365f7c89dd348f56cb4c9c41a9c8e3893b8ad68597c2b71495"}\n', b'{"ciphertext":"95c1df260c188edb7ebe05cc1cb4265de68b8ed82fff198f1c98eae1b646dbe5"}\n', b'{"ciphertext":"a6d6d43e1907869025a210930ff4325dd08acec87eec32d64ce7f8a7e01bd9b8b0fa0e275b747d11e1794ebd4d7ee3120ea541d44e58361c304e295439c8d92dc24bcf40dd46a1cae884"}\n', b'{"ciphertext":"b8dc8a76315099dc6da05fdb07e93244d6d9f9c276a03f9e48a9e8f5f517dbf4f1fc0f7512742901e17342f55b27ac0915"}\n', b'{"ciphertext":"bf93d53e191b999021a8439e4ee26455cb80c9c573a2219e48a9e8f5ef1dc3b8b6f11e275a6e3053e27b46f601"}\n', b'{"ciphertext":"b4c6d276315782d921ab108806e86510d190d083"}\n', b'{"ciphertext":"b2c1c3250b5a98d126ae5e9c4ee67c5499b4d4c176a528db5bbe"}\n', b'{"ciphertext":"bedcd17608059ac529e751950aa77a51c989c48d72a961d245e7eeb0a105dffdbfb4026212603807f33a48e40f69ac0804f3"}\n', b'{"ciphertext":"a1dbc7225816d5de2cb444824ef47f55d5959dd972a5359e59a6e5bbf552dff9b5ba"}\n', b'{"ciphertext":"a1dbc7225816d5dc22b3109408a76658d097dade3ab82edf5de7f8bde41c97ebb4f107625627291ca07740bd5c68e31100a019917555371d6303274838c8c436ce56d748d55ca9c7eac037c2db889187fa13defcfe79a01133cc7aa91714e409c97c4b4ff80568d51c90ac6c5bdd1ab850a2d8792c6d389dae5e491250c912d5fc0bd3ecf6362cd3cce73c23d142af5a813c6daf4991cf56eb6a1aa59b9071"}\n', b'{"ciphertext":"a2dbc3760c1287c224a55c9e4ef37a59d79e9dc469ec32d648b3aca1e91797e8b0e71e2751663354f43a47f80f73ac0e0ff200816d193a11304a32557c9ade37db518d"}\n', b'{"ciphertext":"badcd033545785c222a5519902fe2d10ed91d8d43aa829d00eb3acbeef1dc0b8b9fb1d2756753812f26305f45b27aa0f4df2079b6e19301d7d4a2a4f3d9cd836c80c8d079c46a0c0a6e46d87dd9c82c2bb1fdfbff27cac5d3ed06cae5e"}\n', b'{"ciphertext":"a1dbdf761c18d5c425a249db09e8325fd7d9cdcc73a232d747a0acb4ef1697faa4fd06635b693a53e17649bd5b6fa65c15bb029126"}\n', b'{"ciphertext":"b7ddc276315786d82cab5cdb07e07c5fcb9c9dc46ee2"}\n', b'{"ciphertext":"a2dbc3251d579ddf3fb4558842a76658d08a9dce7bbe34d748a0e9f5ac52dff7a6b423275e683c07e87f05f05674a61007f2069a394d3001630325472e9ad839c84783049c46a0c0ff82698793888b8efa19d2ecaa34a7442e8240e00312ec03cc3f4444fa4c3a940191e93847d05fa118aad17f36235f"}\n', b'{"ciphertext":"a2dbd4331d5797df34b410891be97c59d79e918d6aa027c740a9ebf5e00697f0bee61962412b7d20e5685cf2556fa25d"}\n']
thoughts=[]
for t in tmp:
    thoughts.append(bytes.fromhex(t.strip().decode()[15:-2]))
firstParts = []     #actually I dont even need this, I could ahve used only the thoughts, because after i find the first part of the mask I bruteforce
for t in thoughts:
    firstParts.append(t[:32])


key = xor(b'crypto{', thoughts[7])
key = b'\xf6\xb3\xa6Vxw\xf5\xb0M\xc70\xfbn\x87'
def bruteforce(CTList, key):    #CTList means CypherTextsList
    print("Decoding using key:", key)
    for i in range(0, len(CTList)):
        print(i, "->", xor(CTList[i], key))

    character = input("Next character to try?").encode()
    position = int(input("In which row?"))
    while character != "done":
        if character == "bruteforce":
            print("Still to implement BF")
            character = input("Next character to try?").encode()
            position = int(input("In which row?"))

        elif character == "nope":
            print("Back to previous key")
            key = key[:-1]
            print("Decoding using key:", key)
            for i in range(0, len(CTList)):
                print(i, "->", xor(CTList[i], key))
            character = input("Next character to try?").encode()
            position = int(input("In which row?"))

        else:
            nextKeyCharacter = CTList[position][len(key)] ^ int.from_bytes(character,'big')
            key = key + nextKeyCharacter.to_bytes(1,'big')
            print("Decoding using key:", key)
            for i in range(0,len(CTList)):
                print(i, "->", xor(CTList[i], key))
            character = input("Next character to try?").encode()
            position = int(input("In which row?"))


bruteforce(thoughts, key)



"""
FIRST PART
I get all the thohugts from the server
# Maybe I must use the fac that I know the plaintext of the flag, which starts with crypto{, so as I
#Did with the ctf chalalnge, I will get info 1 byte at the time till I get all the messges
import requests

messages = []
for i in range(0,300):
    response = requests.get("http://aes.cryptohack.org/stream_consciousness/encrypt/")
    if response.content not in messages:
        messages.append(response.content)

print(messages)
print(len(messages))
"""

"""
SECOND PART
I find out tha meask
#I must find what is the mask for the AES output. The counter starts always from 0, and no nounce is used I think, so for
# each thought, the first block will be crypted using AES(key, counter at 1), then second block with AES(key, counter at 2)
# now I bruteforce the first block. For each message I xor it with crypto{ , if the result is the chosen one, that mask will
# reaveal some english words in all the other messages
# By doing this I find out that thoughts[7] contains the FLAG, and I have recovered the first part if the mask

i=0
for trial in firstParts:
    print("TRIAL", i)
    i=i+1
    print(trial)
    mask = xor(bytes.fromhex(trial), b"crypto{")
    for message in firstParts:
        print(xor(mask,  bytes.fromhex(message)))

"""