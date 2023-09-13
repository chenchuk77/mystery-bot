
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
    # used to generate specific announcements
    if prize == game['1st']:
        return "🤑🤑🤑 😱😱😱" + "\n" + winner + "מלך המיסטרי לוקח את הפרס הראשון" + "\n" + to_nice_numbers(prize) + "\n" + "🤑🤑🤑 😱😱😱"
    elif prize == game['2nd']:
        return "🤑🤑🤑 😱😱😱" + "\n" + winner + "האלוף לוקח את הפרס השני" + "\n" + to_nice_numbers(prize) + "\n" + "🤑🤑🤑 😱😱😱"
    elif prize == game['3rd']:
        return "🤑🤑🤑 😱😱😱" + "\n" + winner + "התותח לוקח את הפרס השלישי" + "\n" + to_nice_numbers(prize) + "\n" + "🤑🤑🤑 😱😱😱"
    else:
        return winner + "\n" + "🤦‍♂️ יכול להיות יותר טוב 🤦‍♂️" + "\n" + "🤦‍♂️ אבל כסף זה כסף ... 🤦‍♂️" + "\n" + "🤩🤩🤩🤩🤩🤩" + "\n" + "זכית ב" + "\n" + to_nice_numbers(prize) + "\n"
