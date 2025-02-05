class Solution:
		def equalPairs(self, grid: list) -> int:
			pairs = 0
			l = len(grid[0])
			
			for i in range(l):
				temp = [x[i] for x in grid]
				if temp in grid:
					pairs += 1 * grid.count(temp)

			return pairs