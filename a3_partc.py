import random
from a2d import Graph
from a3_partb import minimum_spanning_tree

def generate_maze(number_of_rows, number_of_columns):
	totalVertex = number_of_rows*number_of_columns
	listOfWalls = []

	for x in range(number_of_rows):
		x = x*number_of_columns
		for y in range(number_of_columns-1):
			listOfWalls.append((x+y, x+y+1))

	for x in range(number_of_columns):
		for y in range(number_of_rows-1):
			y = y*number_of_columns
			listOfWalls.append((y+x, y+x+number_of_columns))
		

	myGraph = Graph(totalVertex)
	
	for x,y in listOfWalls:
		myGraph.add_edge(x, y, random.randint(1, 50))
		myGraph.add_edge(y, x, random.randint(1, 50))

	listOfWallsToRemove = minimum_spanning_tree(myGraph)


	for x,y in listOfWallsToRemove:
		count = 0
		for a,b in listOfWalls:
			if ((x == a or x == b) and (y == a or y == b)):
				listOfWalls.pop(count)
			count+=1

	return listOfWalls
