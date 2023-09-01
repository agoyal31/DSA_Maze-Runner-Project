Part C: Maze Generation
In this last part of A3, you will use what you have created in this assignment and previous assignments to:

generate a new maze of a given size
run your mazerunner function from A1 on your new maze
Update import statement in a1_partd.py
Please alter the import statement for importing the maze to:

from a3_maze import Maze
it use to import from the file named maze.py but we need to update this to support alteration to data format. This object is essentially the same as the old maze and only differs on how the maze is loaded

Write the generat_maze function
Write the following function:

def generate_maze(number_of_rows, number_of_columns)
This function is given the size of the maze in terms of number of rows and columns. It will return a python list of tuples representing the walls for this maze.

Recall that a maze was defined by a set of walls that separated each cell. If you were given a 3 X 4 maze, you would have 12 cells that were numbered as follows:

  0 |  1 |  2 |  3 
--------------------  
  4 |  5 |  6 |  7
--------------------
  8 |  9 | 10 | 11
To create a maze, start by creating a list of all walls. Each wall can be represented as a tuple. For example in the above maze we would represent all walls as follows:

[(0,1),(1,2),(2,3), (4,5),(5,6),(6,7), (8,9),(9,10),(10,11),(0,4),(4,8), (1,5),(5,9),(2,6),(6,10),(3,7),(7,11)]

Once you have the list of walls, use it to create a graph. Each cell in the maze is represented as a vertex. Thus the number of vertices in the graph is equal to the total number of cells. For each of the walls in your list of walls:

each wall is made up a tuple of 2 numbers (cell_1,cell_2). These numbers represent the cells on either side of the wall.
generate a small random number between 1 and 50
create an edge from cell_1 to cell_2 with the random weight
create another edge from cell_2 to cell_1 one with the same random weight
The reason you need two edges is because your graph is undirected

Thus, for a 3X4 maze above, we would end up with a graph that looks something like the following (note weights are random, yours will not have same weight, but the existance of the edges will be the same):

![229268945-45ccbc4c-63a6-4e9c-ad46-09904a94e5fc](https://github.com/agoyal31/DSA_Maze-Runner-Project/assets/113165812/2ae62c05-45ea-4444-8b08-f55386172e4c)


The reason we wish to add this random edge weight is to allow an easy way to randomize the maze generation.

Once you have create the graph, a minimum spanning tree of this graph would represent a "hallway" that allows every cell to be reacheable by every other cell.

Use your function for finding a minimum spanning tree from part C to create a list of walls to remove.

Remove each of the walls in the MST from your original wall list.

This will create the list of walls that form your maze.

If your test passes for part C, four files will get generated. You will use these to generate a visual output for your maze as part of your submission.

The following files are the mazes:

a3_maze1.txt
a3_maze2.txt
The following files are runs for the corresponding mazes:

a3_run1.txt
a3_run2.txt
Go to this url:

https://seneca-dsa456.github.io/dsa456-s23/a3.html

Load each maze
Load each mazerunner
Take a screenshot of each the two maze



![262845418-4b99c4b7-ba61-4d7a-acd8-552acd370e98](https://github.com/agoyal31/DSA_Maze-Runner-Project/assets/113165812/764f26f2-f74c-4ec8-8c09-c8bef58f7712)

![262845584-2c8b7c07-750b-40e5-b085-ad803fabd32d](https://github.com/agoyal31/DSA_Maze-Runner-Project/assets/113165812/fa27bc0a-88c3-40cd-b608-8cebb100d3a5)


