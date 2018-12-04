import sys
import subprocess

# run the daily script 5 times, on 5 seperate "days" of input
for i in range(1,6):
    daily_process = subprocess.Popen(['python3', 'daily.py', str(i)])
    daily_process.wait()
