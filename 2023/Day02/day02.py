import math
from time import time


# TODO: Add comments to your solution

BOX_ITINERARY = {'red': 12,
                 'blue': 14,
                 'green': 13}


def get_power_boxes_sum(sequence: dict) -> int:
    """solution valid for part 2 of the challenge"""
    boxes_power_list = []
    for game_id, game in sequence.items():
        least_needed_boxes = {'red': 0,
                              'blue': 0,
                              'green': 0}

        for withdrawls in game.values():
            extracted_colours = list(withdrawls.keys())
            for colour in extracted_colours:
                if least_needed_boxes[colour] < withdrawls[colour]:
                    least_needed_boxes[colour] = withdrawls[colour]

        boxes_power_list.append(math.prod(list(least_needed_boxes.values())))
    return sum(boxes_power_list)


def get_possible_games_sum(sequence: dict) -> int:
    """solution valid for part 1 of the challenge"""
    possible_games = []

    for game_id, game in sequence.items():
        valid = True

        for withdrawls in game.values():
            extracted_colours = list(withdrawls.keys())

            for colour in extracted_colours:
                if BOX_ITINERARY[colour] < withdrawls[colour]:
                    valid = False

        if valid:
            possible_games.append(game_id)
    return sum(possible_games)


if __name__ == '__main__':
    activate_part_two = True
    with open('input.txt', 'r') as cal_doc:
        game_seq = cal_doc.read().split('\n')
        game_seq = {int(seq.split(':')[0].replace('Game ', '')):
                        {idx: {el.split()[1]: int(el.split()[0])
                               for el in game.split(',')}
                         for idx, game in enumerate(seq.split(':')[1].split(';'))}
                    for seq in game_seq}

    start = time()
    box_ids_sum = get_possible_games_sum(sequence=game_seq)
    print(f"Sum of possible Game IDs: {box_ids_sum}")
    print(f"Execution time: {round(time() - start, 8)}s")

    start = time()
    power_boxes_sum = get_power_boxes_sum(sequence=game_seq)
    print(f"Sum of Boxes' power: {power_boxes_sum}")
    print(f"Execution time: {round(time() - start, 8)}s")
