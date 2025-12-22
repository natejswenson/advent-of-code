#---------------------------------------------------------
# Read and parse the database file
#---------------------------------------------------------
def read_database(filename):
    with open(filename, "r") as f:
        blocks = f.read().strip().split("\n\n")

    ranges = []
    for line in blocks[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ids = [int(x) for x in blocks[1].splitlines()]
    return ranges, ids
#---------------------------------------------------------
# Count how many ingredient IDs are fresh
#---------------------------------------------------------
def count_fresh_ids(ranges, ids):
    fresh_count = 0

    for ingredient_id in ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break  # stop once found fresh

    return fresh_count


#---------------------------------------------------------
# Main execution
#---------------------------------------------------------
if __name__ == "__main__":
    ranges, ids = read_database("input.txt")
    result = count_fresh_ids(ranges, ids)
    print("Fresh ingredient IDs:", result)