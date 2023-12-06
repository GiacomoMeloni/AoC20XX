from time import time


# TODO: Add comments to your solution


def get_engine_parts_sum(sequence: dict) -> int:
    """solution valid for part 1 of the challenge"""
    ...
    return None


if __name__ == '__main__':
    activate_part_two = True
    with open('input.txt', 'r') as engine_doc:
        engine_schema = engine_doc.read().split()

    start = time()
    engine_parts_sum = get_engine_parts_sum(sequence=engine_schema)
    print(f"Sum of valid engine parts: {engine_parts_sum}")
    print(f"Execution time: {round(time() - start, 8)}s")

