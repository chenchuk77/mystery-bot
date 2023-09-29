
def to_nice_numbers(number):
    nice_numbers = ''
    nice_dict = {
        '0': '0⃣',
        '1': '1⃣',
        '2': '2⃣',
        '3': '3⃣',
        '4': '4⃣',
        '5': '5⃣',
        '6': '6⃣',
        '7': '7⃣',
        '8': '8⃣',
        '9': '9⃣'
    }
    number_string = str(number)
    for digit in number_string:
        nice_numbers = nice_numbers + nice_dict[digit]
    return nice_numbers


def announce_winner(winner, prize, game):
    winning_message = ""
    if prize == game['1st']:
        winning_message = build_winning_string(game['messages']['first_prize']['text'], winner, prize)
    elif prize == game['2nd']:
        winning_message = build_winning_string(game['messages']['second_prize']['text'], winner, prize)
    elif prize == game['3rd']:
        winning_message = build_winning_string(game['messages']['third_prize']['text'], winner, prize)
    else:
        winning_message = build_winning_string(game['messages']['normal_prize']['text'], winner, prize)
    return winning_message


def build_winning_string(lines, winner, prize):
    s = "\n".join(lines)
    s = s.format(winner=winner, prize=to_nice_numbers(prize))
    return s


def build_starting_string(lines, game):
    s = "\n".join(lines)
    s = s.format(name=game['name'], num_of_prizes=str(len(game['prizes'])), prizepool=str(game['prizepool']))
    return s


def get_winner_image(prize, game):
    imagefile = ""
    if prize == game['1st']:
        imagefile = game['messages']['first_prize']['image']
    elif prize == game['2nd']:
        imagefile = game['messages']['second_prize']['image']
    elif prize == game['3rd']:
        imagefile = game['messages']['third_prize']['image']
    else:
        imagefile = game['messages']['normal_prize']['image']
    return imagefile


def message_from_list(list_of_lines):
    return "\n".join(list_of_lines)
