def max_bank_joltage(bank: str) -> int:
    digits = [int(char) for char in bank]

    max_value = 0
    max_right = digits[-1]

    # Traverse from right to left
    for i in range(len(digits) - 2, -1, -1):
        max_value = max(max_value, digits[i] * 10 + max_right)
        max_right = max(max_right, digits[i])

    return max_value


def total_output_joltage(banks: list[str]) -> int:
    return sum(max_bank_joltage(bank) for bank in banks)


#--------------------------------------------------------------
# Main execution
# --------------------------------------------------------------
if __name__ == "__main__":
    with open("input.txt") as f:
        banks = [line.strip() for line in f if line.strip()]
    # return sum of max bank joltage for all banks
    print(total_output_joltage(banks))