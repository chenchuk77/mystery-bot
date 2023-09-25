from selenium import webdriver
import subprocess
import time
import signal  # <-- Add this import
import os

timestamp=str(int(time.time() * 1000))

print ("this tool opens a webpage for ffmpeg recording testing")
url = "http://localhost:8282/index.html?t=30000&p[]=336&p[]=303&p[]=510&p[]=6042&p[]=318&p[]=285&p[]=285&p[]=4500&p[]=354&p[]=303&p[]=270&p[]=3300&p[]=270&p[]=270&p[]=510&p[]=2700&p[]=303&p[]=600&p[]=270&p[]=1950&p[]=900&p[]=510&p[]=303&p[]=1500&p[]=318&p[]=285&p[]=285&p[]=1200&p[]=510&p[]=510"
output_file = 'tester-output-{}.mp4'.format(timestamp)

cmd = "sleep 4s && ffmpeg -y -t 7 -f x11grab -video_size 500x400 -i :0.0+470,100 {}".format(output_file)

ffmpeg_process = subprocess.Popen(cmd, shell=True, preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_IGN))

# Start the Selenium WebDriver
driver = webdriver.Chrome()
driver.get(url)
driver.fullscreen_window()

time.sleep(10)

# bounty_won = driver.execute_script("return global_won")

ffmpeg_process.send_signal(subprocess.signal.SIGINT)

driver.quit()
