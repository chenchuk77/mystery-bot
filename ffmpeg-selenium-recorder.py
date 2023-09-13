from selenium import webdriver
import subprocess
import time
import signal  # <-- Add this import
import os


def get_wheel_url(prizes, prizepool):
    url = 'http://localhost:8282/index.html?t={}'.format(prizepool)
    for prize in prizes:
        url += '&p[]={}'.format(prize)
    #final_url = base_url.replace('&', '?', 1)
    return url



def spin_and_record(prizes, prizepool):
    output_file='output-{}.mp4'.format(str(len(prizes)))
    # cmd = "sleep 2s && ffmpeg -f x11grab -video_size 500x510 -i :0.0+700,75 {} > /dev/null 2>&1".format(output_file)
    cmd = "sleep 4s && ffmpeg -y -t 7 -f x11grab -video_size 500x500 -i :0.0+700,100 {}".format(output_file)
    ffmpeg_process = subprocess.Popen(cmd, shell=True, preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_IGN))

    # Start the Selenium WebDriver
    driver = webdriver.Chrome()


    # example request (prizepool=30000)
    # url = 'http://localhost:8282/index.html?t=30000&p[]=336&p[]=303&p[]=510&p[]=6042&p[]=318&p[]=285&p[]=285&p[]=4500&p[]=354&p[]=303&p[]=270&p[]=3300&p[]=270&p[]=270&p[]=510&p[]=2700&p[]=303&p[]=600&p[]=270&p[]=1950&p[]=900&p[]=510&p[]=303&p[]=1500&p[]=318&p[]=285&p[]=285&p[]=1200&p[]=510&p[]=510'

    url = get_wheel_url(prizes, prizepool)
    print(url)
    # Navigate to the desired webpage
    driver.get(url)
    driver.fullscreen_window()

    # Do some interactions or wait for some time
    time.sleep(10)

    bounty_won = driver.execute_script("return global_won")

    # Stop the ffmpeg recording process
    ffmpeg_process.send_signal(subprocess.signal.SIGINT)

    # Close the browser
    driver.quit()

    time.sleep(1)

    # kill_cmd = "pkill -f ffmpeg || true"
    # kill = subprocess.Popen(kill_cmd, shell=True)
    # time.sleep(2)
    #
    # ffmpeg_process.send_signal(subprocess.signal.SIGTERM)
    # ffmpeg_process.wait()
    return int(bounty_won), output_file

#
# #prizes_example = ["100", "150", "100", "1270" ]
# prizes_example = ["100", "150", "100", "1270", "100", "150", "3700", "150", "4300", "150" ]
#
#
# #url = get_wheel_url(prizes_example)
# won, output_file = spin_and_record(prizes_example)
# print('len: {}, player won: {}, output_file: {}'.format(str(len(prizes_example)), won, output_file))
# #
# # prizes_example.remove(won)
# # won, output_file = spin_and_record(prizes_example)
# # print('len: {}, player won: {}, output_file: {}'.format(str(len(prizes_example)), won, output_file))
# #
# # prizes_example.remove(won)
# # won, output_file = spin_and_record(prizes_example)
# # print('len: {}, player won: {}, output_file: {}'.format(str(len(prizes_example)), won, output_file))
# #
