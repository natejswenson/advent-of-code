def count_zero_hits(rotations: list[str]) -> int:
    position = 50
    hits = 0

    for r in rotations:
        direction = r[0]
        distance = int(r[1:]) % 100  # normalize large rotations

        if direction == "L":
            position = (position - distance) % 100
        elif direction == "R":
            position = (position + distance) % 100
        else:
            raise ValueError(f"Invalid rotation: {r}")

        if position == 0:
            hits += 1

    return hits


if __name__ == "__main__":
    with open("input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    print(count_zero_hits(rotations))
