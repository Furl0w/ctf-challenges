import hashlib

with open('secret_key.txt') as f:
    secret = f.readline()

# importing our very secure 16 bytes key
secret = bytes.fromhex(secret)

# given for the challenge
message = "order=open_all_chests"
mac = "50cb15dc7c9eac0d5532d78f3622c73d4369d803"

# Waiting for orders
message = "6f726465723d6f70656e5f616c6c5f6368657374738000000000000000000000000000000000000028100000000000003b76657269666965643d74727565"
mac = "0525ec243f002176c458108ae55fd2a7a506b6dd"



# Let's make sure that this message is REALLY legit
h = hashlib.new('ripemd160')
h.update(secret+bytes.fromhex(message))
print(h.hexdigest())
if mac == h.hexdigest():
    message = message.decode('utf-8','ignore')
    if ";verified=true" in message:
        with open('flag.txt') as f:
            flag = f.readline()
            print(flag)
    else:
        print("I'm sorry dave, I'm afraid I can't do that")
else:
    print("Invalid message. ABORT! ABORT!")
