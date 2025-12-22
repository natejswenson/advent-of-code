from pathlib import Path


def solve(input_text: str) -> int:
    lines = input_text.rstrip("\n").splitlines()
    width = max(len(line) for line in lines)

    # Normalize all rows to the same width
    grid = [line.ljust(width) for line in lines]
    height = len(grid)

    total = 0
    col = 0

    while col < width:
        # Skip empty columns
        if all(grid[row][col] == " " for row in range(height)):
            col += 1
            continue

        # Capture contiguous non-empty columns (one problem)
        start = col
        while col < width and not all(grid[row][col] == " " for row in range(height)):
            col += 1
        end = col

        # Extract numbers + operator from this problem
        column_data = [
            grid[row][start:end].strip()
            for row in range(height)
            if grid[row][start:end].strip()
        ]

        *nums, op = column_data
        values = list(map(int, nums))

        if op == "+":
            result = sum(values)
        elif op == "*":
            result = 1
            for v in values:
                result *= v
        else:
            raise ValueError(f"Unknown operator: {op}")

        total += result

    return total


def main() -> None:
    input_path = Path("input.txt")
    input_text = input_path.read_text()
    answer = solve(input_text)
    print(answer)


if __name__ == "__main__":
    main()
