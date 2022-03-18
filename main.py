import hashlib
import sys

with open('secret_key.txt') as f:
    secret = f.readline()

# importing our very secure 16 bytes key
secret = bytes.fromhex(secret)

# Waiting for orders
message = sys.argv[1]
mac = sys.argv[2]



# Let's make sure that this message is REALLY legit
h = hashlib.new('ripemd160')
h.update(secret+bytes.fromhex(message))
if mac == h.hexdigest():
    message = bytes.fromhex(message).decode('utf-8','ignore')
    if ";verified=true" in message:
        with open('flag.txt') as f:
            flag = f.readline()
            print(flag)
    else:
        print("I'm sorry dave, I'm afraid I can't do that")
else:
    print("Invalid message. ABORT! ABORT!")
