#---------------------------------------------------------
# Read the cephalopod math worksheet
#---------------------------------------------------------
def read_worksheet(filename):
    with open(filename, "r") as f:
        return [line.rstrip("\n") for line in f]


#---------------------------------------------------------
# Solve the worksheet (Part 1)
#---------------------------------------------------------
def solve_worksheet(grid, right_to_left=False):
    import re
    from operator import add, mul

    # Convert to list of lists of characters
    rows = [list(line) for line in grid]
    n_rows = len(rows)
    n_cols = max(len(r) for r in rows)
    # pad rows to same length
    for r in rows:
        r += [" "] * (n_cols - len(r))

    if right_to_left:
        cols = list(zip(*rows))  # columns
        cols = cols[::-1]  # right-to-left
    else:
        cols = list(zip(*rows))  # columns left-to-right

    # Split columns into problems by full-space columns
    problems = []
    current = []
    for col in cols:
        if all(c == " " for c in col):
            if current:
                problems.append(current)
                current = []
        else:
            current.append(col)
    if current:
        problems.append(current)

    total = 0

    for prob in problems:
        # Each prob: list of columns
        # Reconstruct numbers by joining characters in each column (top to bottom)
        numbers = []
        n_cols_prob = len(prob)
        n_rows_prob = len(prob)
        # Columns to numbers
        for col in prob:
            num_str = "".join(c for c in col[:-1] if c != " ").strip()
            if num_str:
                numbers.append(int(num_str))
        # Last row of each column contains operator
        op_chars = [col[-1] for col in prob if col[-1] in "+*"]
        op = op_chars[0] if op_chars else "+"

        # Evaluate the problem
        res = numbers[0]
        for num in numbers[1:]:
            if op == "+":
                res += num
            else:
                res *= num
        total += res

    return total


#---------------------------------------------------------
# Main execution
#---------------------------------------------------------
if __name__ == "__main__":
    grid = read_worksheet("input.txt")

    # Part 1
    total_part1 = solve_worksheet(grid, right_to_left=False)
    print("Grand total (part 1):", total_part1)

