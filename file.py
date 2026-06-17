with open("demofile.txt","w") as f :
    f.write("Woops I am saskahm khadka")

with open("demofile.txt","r") as f:
    print(f.read())

with open("demofile.txt","a") as f :
    f.write("xyz and abc")

import os
os.remove("demofile.txt")