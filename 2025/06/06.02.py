#---------------------------------------------------------
# Read only the fresh ingredient ID ranges
#---------------------------------------------------------
def read_ranges(filename):
    ranges = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                break  # stop at blank line

            start, end = map(int, line.split("-"))
            ranges.append((start, end))

    return ranges


#---------------------------------------------------------
# Count total number of IDs covered by the ranges
#---------------------------------------------------------
def count_fresh_ids(ranges):
    if not ranges:
        return 0

    # Sort ranges by starting value
    ranges.sort()

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            # Overlapping or adjacent range
            current_end = max(current_end, end)
        else:
            # Disjoint range
            total += current_end - current_start + 1
            current_start, current_end = start, end

    # Add final range
    total += current_end - current_start + 1
    return total


#---------------------------------------------------------
# Main execution
#---------------------------------------------------------
if __name__ == "__main__":
    ranges = read_ranges("input.txt")
    result = count_fresh_ids(ranges)
    print("Total fresh ingredient IDs:", result)
