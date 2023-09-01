from a2d import Graph
from a1_partb import SetList
from a1_partc import DisjointSet
 # add imports for your DisjointSet or MinHeap as you see fit

def minimum_spanning_tree(graph):
    weightFromTo = [] #It stores 3 things, weight, (from)starting point in graph, (to),ending node point.

    for from_vertex in range(graph.num_verts()):
        for to_vertex, weight in graph.get_connected(from_vertex):
            weightFromTo.append((weight, from_vertex, to_vertex))

    weightFromTo.sort() #this will sort (weight, from, to) accoridng weight. So, have sorted 
    disSet = DisjointSet() #One disjoint set is made, that have empty dictionary and number of sets initialised to 0

    for from_vertex in range(graph.num_verts()): # we start from 0 to 6 (7 vertex in our graph lets say)
        disSet.make_set(from_vertex) #This is adding that vertex(0 initially) to dictionary key, and value will be (a setlist pointed by the setlist.front made for the from_vertex in the make set function)
   
    MST = []

    for weight, from_vertex, to_vertex in weightFromTo:
        ep1 = disSet.find_set(from_vertex) #this function will return the data pointed by setlist of (self.dict[element].set_list.front.data). 
        # Each value in the dictionary (if not union) will have its own setlist. Because each value is a node in the dictionary (node having 4 valuess, data, setlist, next and prev)
        ep2 = disSet.find_set(to_vertex) # same as above
        
        if ep1 != ep2: # if the setlists are seperate, ep1 and ep2 will never be the same
            disSet.union_set(ep1, ep2) # Here, one node is being added to the back of another node. This time, when we will try to do find_set (line 22 or 24), becasuse it is union, both will return
            # the data pointed by front setlist (because now both will have same setlist holder.) and hence they will not be duplicated now.
            MST.append((from_vertex, to_vertex)) # Finally, we are appending the from and to to to the MST list. It will only have values unique (for example, from 1 to 2 and 2 to 1, it will only have
            # either of two. because they must be unionised before so, for either one of them ep1 == ep2 because their setlist now became the same.)

            if disSet.get_num_sets() == 1: #because once the union is done, disSet's, setlist number kept decreasing (union_set function is doing -- and once we reach 1 ). 
                break

    return MST
