import sys
import subprocess

for i in range(1,6):
    daily_process = subprocess.Popen(['python3', 'dayTest.py', str(i)])
    daily_process.wait()
