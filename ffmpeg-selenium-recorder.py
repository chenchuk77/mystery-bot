from selenium import webdriver
import subprocess
import time
import signal
import sys
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)


def get_wheel_url(game):
    url = 'http://localhost:8282/index.html?t={}'.format(game['prizepool'])
    for prize in game['prizes']:
        url += '&p[]={}'.format(prize)
    return url


def spin_and_record(game):
    outfile='output-{}.mp4'.format(str(len(game['prizes'])))
    cmd = game['config']['ffmpeg']['command'].format(outfile=outfile)
    logger.info("starting ffmpeg as: {}".format(cmd))
    ffmpeg_process = subprocess.Popen(cmd, shell=True, preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_IGN))

    # Start the Selenium WebDriver
    driver = webdriver.Chrome()
    url = get_wheel_url(game)
    logger.info("openning url with selenium webdriver: {}".format(url))
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
    return int(bounty_won), outfile
