#---------------------------------------------------------
# Read the grid (matrix) from a text file
#---------------------------------------------------------
def readmatrix(filename):
    """Reads the grid into a list of lists."""
    with open("matrix.txt", "r") as f:   # NOTE: ignores 'filename' argument
        return [list(line.strip()) for line in f]


#---------------------------------------------------------
# Count rolls of paper ('@') that have fewer than 4
# adjacent '@' rolls in the surrounding 8 positions
#---------------------------------------------------------
def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])

    #-----------------------------------------------------
    # Define the 8-direction adjacency offsets
    # (up, down, left, right, and diagonals)
    #-----------------------------------------------------
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    accessible = 0

    #-----------------------------------------------------
    # Loop through every cell in the grid
    #-----------------------------------------------------
    for r_rows in range(rows):
        for c_cols in range(cols):

            # Skip positions that are not rolls of paper
            if grid[r_rows][c_cols] != '@':
                continue

            adjacent_count = 0

            #-------------------------------------------------
            # Check all 8 neighbor positions
            #-------------------------------------------------
            for dr, dc in directions:
                nr = r_rows + dr
                nc = c_cols + dc

                # Count only neighbors that are in bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adjacent_count += 1

            #-------------------------------------------------
            # A roll is accessible if it has fewer than 4
            # adjacent '@' rolls
            #-------------------------------------------------
            if adjacent_count < 4:
                accessible += 1

    return accessible


#---------------------------------------------------------
# Main execution: read the grid and compute result
#---------------------------------------------------------
if __name__ == "__main__":
    grid = readmatrix("input.txt")   # place your puzzle input in input.txt
    result = count_accessible_rolls(grid)
    print("Accessible rolls:", result)
