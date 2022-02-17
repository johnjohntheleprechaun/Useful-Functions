def gprint(grid):
	for y in range(len(grid)):
		row = ""
		for x in range(len(grid[y])):
			row += str(grid[y][x]) + " "
		print(row)

grid = [["." for x in range(5)] for y in range(5)]
gprint(grid)