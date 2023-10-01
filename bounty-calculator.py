import matplotlib.pyplot as plt
import numpy as np

import os
import imageio
import time
import random
# import ffmpeg
# # pip install imageio
# pip install "imageio[ffmpeg]"


from PIL import Image
import glob


def spin_wheel(array_of_mystery_bounties, winner):
    ts = time.time()
    stop_angle = 36
    stop_angle = stop_angle + 1
    #data = np.array(['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'])
    # labels = ['100', '200', '300', '400', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    data = np.array(['1'] * len(array_of_mystery_bounties))

    #step is 10 degrees
    # /2 to find the middle poing
    # /10 to output steps and not degrees
    extra_steps = int(360/len(data) / 2 / 10)
    #print ('original stop_angle: {}'.format(stop_angle))
    #print ('original extra_steps: {}'.format(extra_steps))
    stop_angle = stop_angle + extra_steps + 1
    #print ('modified stop_angle: {}'.format(stop_angle))

    # Create a directory to store the output
    if not os.path.exists('output'):
        os.makedirs('output')

    # Create a series of pie charts with different rotations
    for i in range(stop_angle):
        plt.pie(data, labels=array_of_mystery_bounties, startangle=i * (-10))
        plt.axis('equal')

        # add arrow
        plt.annotate(''.format(array_of_mystery_bounties[0]), xy=(1, 0), xytext=(1.5, 0),
                     arrowprops=dict(arrowstyle='->', linewidth=5, mutation_scale=15))

        plt.savefig(f'output/pie_{i}.png')
        plt.close()

    # Create the animated gif
    # images = []
    # for i in range(stop_angle-1):
    #     png_file = f'output/pie_{i}.png'
    #     print (png_file)
    #     # images.append(imageio.imread(f'output/pie_{i}.png'))
    #     images.append(imageio.imread(png_file))
    # print ('done automating files')
    #
    # for i in range(30):
    #     png_file = f'output/pie_{stop_angle-2}.png'
    #     print (png_file)
    #     images.append(imageio.imread(png_file))
    # print('done stop files')

    # imageio.mimsave('wheel-{}.gif'.format(winner), images, loop=1)

    # add the last element 10 times because telegram loops gif for infinity

    #last_image = images[-1]

    # for i in range(10):
    #     images.append(last_image)


    images = []
    for i in range(stop_angle-1):
        png_file = f'output/pie_{i}.png'
        print (png_file)
        images.append(png_file)
    print ('done automating files')

    for i in range(stop_angle-1):
        #png_file = f'output/pie_{stop_angle-2}.png'
        png_file = images[-1]

        print (png_file)
        images.append(png_file)
    print('done stop files')

    # Create a list to store the image data
    frames = []
    for image in images:
        frames.append(imageio.imread(image))

    # Save frames as a movie file with 101ms delay between each frame
    imageio.mimsave(f'wheel-{winner}.mp4', frames, 'FFMPEG', fps=5)

    print('done recording video file')
    #Create the frames
    # imgs = glob.glob("*.png")
    #
    # for i in range(stop_angle-1):
    #     png_file = f'output/pie_{i}.png'

    # frames = []
    # for i in images:
    #     new_frame = Image.open(i)
    #     frames.append(new_frame)
    #
    # # Save into a GIF file that loops forever
    # frames[0].save(f'wheel-{winner}.gif', format='GIF',
    #                append_images=frames[1:],
    #                save_all=True,
    #                duration=100, loop=0)

    # imageio.mimsave('wheel-{}.gif'.format(winner), images, loop=1)

    # first cell is always winning

    # (
    #     ffmpeg
    #     .input('/path/to/jpegs/*.jpg', pattern_type='glob', framerate=25)
    #     .output('movie.mp4')
    #     .run()
    # )

    # List of JPEG files
    # images = ['/tmp/0001.jpg', '/tmp/0002.jpg', '/tmp/0003.jpg', '/tmp/0004.jpg', '/tmp/0005.jpg']

    # Execute FFmpeg sub-process, with stdin pipe as input, and jpeg_pipe input format
    # process = ffmpeg.input('pipe:', r='20', f='jpeg_pipe').output('/tmp/video.mp4',
    #                                                               vcodec='libx264').overwrite_output().run_async(
    #     pipe_stdin=True)
    #
    # # Iterate jpeg_files, read the content of each file and write it to stdin
    # for in_file in images:
    #     with open(in_file, 'rb') as f:
    #         # Read the JPEG file content to jpeg_data (bytes array)
    #         jpeg_data = f.read()
    #
    #         # Write JPEG data to stdin pipe of FFmpeg process
    #         process.stdin.write(jpeg_data)
    #
    # # Close stdin pipe - FFmpeg fininsh encoding the output file.
    # process.stdin.close()
    # process.wait()

    return array_of_mystery_bounties[0]


def generate_winning_pattern(itm, prizepool):
    # itm = 34
    #print('prizepool: {}'.format(prizepool))

    # default pattern for 25 ITM players
    first_25 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 4, 4]

    # default distribution ( note that last 4 have more than 1 winning options corresponds to [...2,4,4,4]
    prizes_percentage = [20, 15, 11, 9, 6.5, 5, 4, 3, 2, 1.18, 1.12, 1.06, 1.01, 0.95, 0.9]

    if itm > 25:
        # padding the rest with 0.8 % bounty
        extra = itm - sum(first_25)
        extra_percent = 8.5 / extra
        first_25.append(extra)
        prizes_percentage.append(extra_percent)

    final_prizes = []
    for i in range(len(first_25)):
        for num_of_bounties in range(first_25[i]):
            final_prizes.append(int(prizepool * (prizes_percentage[i]) / 100))
    #print('final prizes: {}'.format(final_prizes))
    #print('total prizes: {}'.format(sum(final_prizes)))

    # normalize (give the rest to the winner)
    final_prizes[0] = final_prizes[0]+  prizepool - sum(final_prizes)

    #print('final prizes modified: {}'.format(final_prizes))
    #print('total prizes modifies: {}'.format(sum(final_prizes)))

    max_prize = max(final_prizes)

    low_prizes = [x for x in final_prizes if x < prizepool*(4/100)]
    big_prizes = [x for x in final_prizes if x >= prizepool*(4/100)]

    random.shuffle(low_prizes)
    # return final_prizes


    # inject big prizes into the wheel
    wheel_prizes = []
    # low_prizes = [x for x in final_prizes if x < prizepool*(4/100)]
    # big_prizes = [x for x in final_prizes if x >= prizepool*(4/100)]

    low_bulk_size=int(len(low_prizes)/len(big_prizes))
    big_items_count=len(big_prizes)

    for k in range(big_items_count):
        for i in range(low_bulk_size):
            wheel_prizes.append(low_prizes.pop(0))
        wheel_prizes.append(big_prizes.pop(0))
    wheel_prizes = wheel_prizes + low_prizes + big_prizes

    return wheel_prizes


    # final_prizes_as_strings = [ str(x) for x in final_prizes ]
    # return final_prizes_as_strings


# generate_winning_pattern(34, 30000)


def main(game_name, bounty_prize_pool, itm_players, shuffle=True):
    print( "starting bounty calculator for {} .... ".format(game_name))

    prizes, max_prize = generate_winning_pattern(itm_players, bounty_prize_pool)
    if shuffle:
        random.shuffle(prizes)

    while len(prizes) > 0:

        winner_name = input()
        print('spinning for ' + winner_name)
        print('available bounties: {} : {}'.format(len(prizes), prizes))

        # generating animation
        prize = spin_wheel(prizes, winner_name)
        print ('winner: {}, bounty: {}.'.format(winner_name, prize))
        print ('gif generated: wheel-{}.gif'.format(winner_name))

        # remove winning bounty ( shorten and shuffle the list )
        prizes = prizes[1:]
        if shuffle:
            random.shuffle(prizes)
        print('waiting for new KO...[enter name of player]')


#main('NL mystery 50$', 34800, 35, False)









