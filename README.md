**Category**: crypto

**Title**: Access Not Authorized

**Author**: Nicolas Costes @ Simula UiB

**Description**: After many hours you finally managed to enter the target's network. An open API stands before you (accessnotauthorized.heltsikker.no), its source code fully revealed (main.py), and you even captured a legitimate message (message.txt) from another user. Unfortunately, there is still an obstacle. The message authentication is on, and you need admin rank to access the flag. Fortunately, the intern designed the authentication on a hangover day, and he made a crucial mistake. Can you cheat the system and reach the flag?

**Flag**: HSCTF{th1s_1s_why_hm4c_3x1st}

**Difficulty**: Hard

**Hint**: The choice of the Hash function used in the MAC computation matters. If SHA-3 or BLAKE2 were in place of RIPEMD160 this challenge would be impossible. Why?