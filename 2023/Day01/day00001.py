from time import time

def calibrate_document_naive(sequence: list) -> int:
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

def calibrate_document_opposite(sequence: list) -> int:
    number_list = []
    for row in sequence:
        start = 0
        end = len(row)
        left_num = None
        right_num = None
        while left_num is None or right_num is None:
            if left_num is None:
                if str.isdigit(row[start]) and left_num is None:
                    left_num = row[start]
                else:
                    start += 1

            if right_num is None:
                if str.isdigit(row[end-1]) and right_num is None:
                    right_num = row[end-1]
                else:
                    end -= 1
        number_list.append(int(left_num+right_num))
    return sum(number_list)


if __name__ == '__main__':
    with open('input.txt', 'r') as cal_doc:
        cal_seq = cal_doc.read().split()

    start = time()
    cal_sum = calibrate_document_naive(sequence=cal_seq)
    print(f"Calibration sum naive: {cal_sum}")
    print(f"Execution time naive: {round(time()-start,8)}s")


    start = time()
    cal_sum = calibrate_document_opposite(sequence=cal_seq)
    print(f"Calibration sum opposite: {cal_sum}")
    print(f"Execution time opposite: {round(time()-start,8)}s")