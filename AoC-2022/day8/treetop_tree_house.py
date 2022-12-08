grid = open("day8/input.txt", "r")
grid = grid.read().split("\n")

def get_num_visible_trees(): # O(number of trees * max(number of row, number of columns))
    num_visible_trees = 0
    forest_height = len(grid)
    for r in range(forest_height):
        forest_width = len(grid[r])
        for c in range(forest_width):
            tree_height = grid[r][c]
            is_visible_from_left_edge = not any(grid[r][lc] >= tree_height for lc in range(0, c))
            is_visible_from_right_edge = not any(grid[r][rc] >= tree_height for rc in range(c + 1, forest_width))
            is_visible_from_top_edge = not any(grid[tr][c] >= tree_height for tr in range(0, r))
            is_visible_from_bottom_edge = not any(grid[br][c] >= tree_height for br in range(r + 1, forest_height))
            is_visible = is_visible_from_left_edge or is_visible_from_right_edge or is_visible_from_top_edge or is_visible_from_bottom_edge
            if is_visible:
                num_visible_trees += 1
    return num_visible_trees

print(f"part1: {get_num_visible_trees()}")

def get_num_trees_in_view(tree_height, start_r, end_r, start_c, end_c): # O(max(number of row, number of columns))
    num_trees_in_view = 0
    for r in range(start_r, end_r, 1 if end_r > start_r else -1):
        for c in range(start_c, end_c, 1 if end_c > start_c else -1):
            if tree_height > grid[r][c]:
                num_trees_in_view += 1
            else:
                return num_trees_in_view + 1 # count taller tree
    return num_trees_in_view
    

def get_max_scenic_score(): # O(number of trees * max(number of row, number of columns))
    max_scenic_score = 0
    forest_height = len(grid)
    for r in range(forest_height):
        forest_width = len(grid[r])
        for c in range(forest_width):
            tree_height = grid[r][c]
            num_trees_in_view_from_left = get_num_trees_in_view(tree_height, r, r + 1, c - 1, -1)
            num_trees_in_view_from_right = get_num_trees_in_view(tree_height, r, r + 1, c + 1, forest_height)
            num_trees_in_view_from_top = get_num_trees_in_view(tree_height, r - 1, -1, c, c + 1)
            num_trees_in_view_from_bottom = get_num_trees_in_view(tree_height, r + 1, forest_width, c, c + 1)
            tree_scenic_score = num_trees_in_view_from_left * num_trees_in_view_from_right * num_trees_in_view_from_top * num_trees_in_view_from_bottom
            max_scenic_score = max(max_scenic_score, tree_scenic_score)
    return max_scenic_score

print(f"part2: {get_max_scenic_score()}")
