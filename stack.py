import os,time
class bcolors:
    FAIL = '\033[91m' #RED
os.system('clear')
filenames = ["0.txt","0,1.txt","1.txt","2.txt"]
frames = []
i = 0

for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
while (i < 10) :
    for frame in frames:
        print(bcolors.FAIL + "".join(frame))
        time.sleep(1)
        os.system('clear')
        i = 0
#hmoulard
