# f=open("myfile.txt","x")
with open("myFile.txt","w") as f:
    f.write("Oppps  yayaaa ah ah ah ah ah chew chew ")

    
file=open("myFile.txt","a")
file.write("\n Welcome")
file.close()

file=open("myFile.txt","r")
content=file.read()
print(content)

