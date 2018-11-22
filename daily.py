import sys
import subprocess

day = sys.argv[1]

for i in range(1,4):
    commands = open('io/commands/day_'+str(day)+"/"+str(i)+".txt")
    front_process = subprocess.Popen(['python', 'front/front.py', 'io/vsl/'+ day + ".txt", 'io/tsf/day_'+day+'/'+str(i)+'.txt'], stdin=commands)
    front_process.wait()
    commands.close()

mtsf = open('io/mtsf/'+ day +'.txt', "w")

for i in range(1,4):
    tsf = open('io/tsf/day_'+day+'/'+str(i)+'.txt', "r")
    for line in tsf:
        if not "EOS" in line:
            mtsf.write(line)

mtsf.write("EOS 00000 0 00000 **** 0")
mtsf.close()

back_process = subprocess.Popen(
    [
        'python', 'back/back.py', 
        'io/csf/'+ day + ".txt", 
        'io/mtsf/'+ day + ".txt", 
        'io/csf/'+ str(int(day) + 1) + ".txt", 
        'io/vsl/'+ str(int(day) + 1) + ".txt", 
    ]
)

back_process.wait()
