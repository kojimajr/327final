import sys

day = sys.argv[1]



for i in range(1,4):
    commands = open('io/commands/day_'+str(day)+"/"+str(i)+".txt")
    front_process = subprocess.Popen(['python', 'front/front.py', 'io/vsl/'+ day + ".txt", 'io/tsf/day_'+day+'/'+str(i)+'.txt'], stdin=commands)
    front_process.wait()

