#---------------------------------------------------------
# Read the grid (matrix) from a text file
#---------------------------------------------------------
def readmatrix(filename):
    """Reads the grid into a list of lists."""
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f]


#---------------------------------------------------------
# Repeatedly remove accessible rolls of paper ('@')
#---------------------------------------------------------
def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    #-----------------------------------------------------
    # Define the 8-direction adjacency offsets
    #-----------------------------------------------------
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    total_removed = 0

    #-----------------------------------------------------
    # Repeat until no more rolls can be removed
    #-----------------------------------------------------
    while True:
        to_remove = []

        #-------------------------------------------------
        # Scan entire grid
        #-------------------------------------------------
        for r in range(rows):
            for c in range(cols):

                # Skip non-rolls
                if grid[r][c] != '@':
                    continue

                adjacent_count = 0

                #---------------------------------------------
                # Count adjacent '@' rolls
                #---------------------------------------------
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent_count += 1

                #---------------------------------------------
                # Mark for removal if accessible
                #---------------------------------------------
                if adjacent_count < 4:
                    to_remove.append((r, c))

        #-------------------------------------------------
        # Stop if nothing is removable
        #-------------------------------------------------
        if not to_remove:
            break

        #-------------------------------------------------
        # Remove marked rolls
        #-------------------------------------------------
        for r, c in to_remove:
            grid[r][c] = '.'
            total_removed += 1

    return total_removed


#---------------------------------------------------------
# Main execution: read the grid and compute result
#---------------------------------------------------------
if __name__ == "__main__":
    grid = readmatrix("matrix.txt")   # place your puzzle input in input.txt
    result = count_accessible_rolls(grid)
    print("Accessible rolls:", result)
