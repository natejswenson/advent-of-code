def max_bank_joltage(bank: str, k: int = 12) -> int:
    drops = len(bank) - k
    stack = []

    for digit in bank:
        while drops > 0 and stack and stack[-1] < digit:
            stack.pop()
            drops -= 1
        stack.append(digit)

    # Ensure exactly k digits
    result = ''.join(stack[:k])
    return int(result)


def total_output_joltage(banks: list[str]) -> int:
    return sum(max_bank_joltage(bank) for bank in banks)


if __name__ == "__main__":
    with open("input.txt") as f:
        banks = [line.strip() for line in f if line.strip()]

    print(total_output_joltage(banks))

