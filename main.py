import hashlib

with open('secret_key.txt') as f:
    secret = f.readline()

# importing our very secure 16 bytes key
secret = bytes.fromhex(secret)

# Waiting for orders
message = "order=open_all_chests"
mac = "50cb15dc7c9eac0d5532d78f3622c73d4369d803"

# Let's make sure that this message is REALLY legit
h = hashlib.new('ripemd160')
h.update(secret+bytes(message, "utf-8"))
print(h.hexdigest())
if mac == h.hexdigest():
    if ";verified=true" in message:
        with open('flag.txt') as f:
            flag = f.readline()
            print(flag)
    else:
        print("I'm sorry dave, I'm afraid I can't do that")
else:
    print("Invalid message. ABORT! ABORT!")
