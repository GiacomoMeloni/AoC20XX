from time import time


# TODO: Add comments to your solution
def save_number(current_number: str, h_idx: int, w_idx: int, position_dictionary: dict):
    if position_dictionary.get((h_idx - 1, h_idx + 1), None):
        position_dictionary[(h_idx - 1, h_idx + 1)].append({"w_window": (w_idx - len(current_number) - 1, w_idx),
                                                            "content": int(current_number),
                                                            "valid": False})
    else:
        position_dictionary[(h_idx - 1, h_idx + 1)] = [{"w_window": (w_idx - len(current_number) - 1, w_idx),
                                                        "content": int(current_number),
                                                        "valid": False}]
    current_number = ''
    return position_dictionary, current_number


def get_engine_parts_sum(sequence: list) -> int:
    """solution valid for part 1 of the challenge"""
    number_position_dictionary = dict()
    symbols_position_dictionary = dict()
    target_simbols = set()
    valid_engine_part = []
    current_number = ''
    for h_idx in range(len(sequence)):
        if current_number:
            number_position_dictionary, current_number = save_number(current_number=current_number,
                                                                     h_idx=h_idx,
                                                                     w_idx=w_idx,
                                                                     position_dictionary=number_position_dictionary)
            current_number = ''
        for w_idx in range(len(sequence[0])):
            if str.isdigit(sequence[h_idx][w_idx]):
                current_number += sequence[h_idx][w_idx]
            elif sequence[h_idx][w_idx] == '.':
                if current_number:
                    number_position_dictionary, current_number = save_number(current_number=current_number,
                                                                             h_idx=h_idx,
                                                                             w_idx=w_idx,
                                                                             position_dictionary=number_position_dictionary)
            else:
                target_simbols.add(sequence[h_idx][w_idx])
                symbols_position_dictionary[(h_idx, w_idx)] = sequence[h_idx][w_idx]
                if current_number:
                    number_position_dictionary, current_number = save_number(current_number=current_number,
                                                                             h_idx=h_idx,
                                                                             w_idx=w_idx,
                                                                             position_dictionary=number_position_dictionary)


    for target_loc in symbols_position_dictionary.keys():
        for h_range in list(number_position_dictionary.keys()):
            if h_range[0] <= target_loc[0] <= h_range[1]:
                for value in number_position_dictionary[h_range]:
                    if value['w_window'][0] <= target_loc[1] <= value['w_window'][1]:
                        if not value['valid']:
                            value['valid'] = True
                            valid_engine_part.append(value['content'])

    return sum(list(valid_engine_part))


if __name__ == '__main__':
    activate_part_two = True
    with open('input.txt', 'r') as engine_doc:
        engine_schema = engine_doc.read().split()
        engine_schema = [[el for el in line] for line in engine_schema]

    start = time()
    engine_parts_sum = get_engine_parts_sum(sequence=engine_schema)
    print(f"Sum of valid engine parts: {engine_parts_sum}")
    print(f"Execution time: {round(time() - start, 8)}s")
