from time import time

# TODO: Add comments to your solution

BOX_ITINERARY = {'red': 12,
                 'blue': 14,
                 'green': 13}


def get_boxes_sum(sequence: dict) -> int:
    possible_games = []

    for game_id, game in sequence.items():
        valid = True
        for withdrawls in game.values():
            extracted_colours = list(withdrawls.keys())

            for colour in extracted_colours:
                if BOX_ITINERARY[colour] < withdrawls[colour]:
                    valid = False
                    break
            if not valid:
                break

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
    box_ids_sum = get_boxes_sum(sequence=game_seq)
    print(f"Sum of possible Game IDs: {box_ids_sum}")
    print(f"Execution time: {round(time() - start, 8)}s")
