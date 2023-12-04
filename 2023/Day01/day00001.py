from time import time

NUM_PARSER = {'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9'}


def calibrate_document_naive(sequence: list) -> int:
    """Naive solution suited only for challenge part 1"""
    number_list = []
    for row in sequence:
        start = None
        end = None
        for el in row:
            if str.isdigit(el) and start is not None:
                end = el
            elif str.isdigit(el) and start is None:
                start = el
            else:
                ...
        if start is None:
            raise ValueError(f'Something wrong with row: {row}')

        if end is None and start is not None:
            end = start

        number_list.append(int(start+end))
    return sum(number_list)


def calibrate_document_opposite(sequence: list, enable_parser: bool = True) -> int:
    number_list = []

    for idx, row in enumerate(sequence):
            start = 0
            end = len(row)
            left_num = None
            right_num = None
            while left_num is None or right_num is None:
                try:
                    if left_num is None:
                        if str.isdigit(row[start]):
                            left_num = row[start]
                        else:
                            if enable_parser:
                                for key in NUM_PARSER.keys():
                                    if str.startswith(row[start:], key):
                                        left_num = NUM_PARSER[key]
                                start += 1
                            else:
                                start += 1

                    if right_num is None:
                        if str.isdigit(row[end-1]):
                            right_num = row[end-1]
                        else:
                            if enable_parser:
                                for key in NUM_PARSER.keys():
                                    if str.endswith(row[:end], key):
                                        right_num = NUM_PARSER[key]
                                end -= 1
                            else:
                                end -= 1

                except Exception as e:
                    """Check system status during error"""
                    print(f"Sequence element #{idx if idx is not None else 'N/A'}")
                    print(f"Left value: {left_num if left_num is not None else 'N/A'}")
                    print(f"Right value: {right_num if right_num is not None else 'N/A'}")
                    print(f"Current start index: {start if start is not None else 'N/A'}")
                    print(f"Current end index: {end if end is not None else 'N/A'}")

                    raise e
            number_list.append(int(left_num+right_num))

    return sum(number_list)


if __name__ == '__main__':
    activate_part_two = True
    with open('input.txt', 'r') as cal_doc:
        cal_seq = cal_doc.read().split()

    start = time()
    cal_sum = calibrate_document_naive(sequence=cal_seq, enable_part_two=activate_part_two)
    print(f"Calibration sum naive: {cal_sum}")
    print(f"Execution time naive: {round(time()-start,8)}s")

    start = time()
    cal_sum = calibrate_document_opposite(sequence=cal_seq, enable_parser=activate_part_two)
    print(f"Calibration sum opposite: {cal_sum}")
    print(f"Execution time opposite: {round(time()-start,8)}s")
