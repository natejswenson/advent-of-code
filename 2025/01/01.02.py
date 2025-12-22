def count_zero_clicks(rotations: list[str]) -> int:
    position = 50
    zero_hits = 0

    for r in rotations:
        direction = r[0]
        distance = int(r[1:])

        step = -1 if direction == "L" else 1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zero_hits += 1

    return zero_hits


if __name__ == "__main__":
    with open("input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    print(count_zero_clicks(rotations))
