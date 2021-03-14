# search.py
# ---------------
# Created by Khamidah Ahmad Syauqi (kahmadsyauqi@upi.edu) on 09/03/2021

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue

def search(maze):
    fringe = queue.Queue()
    fringe.put(maze.getStart())
    result = []
    visited = []
    parent = {}
    #count = 0
    stop = 0
    current = fringe.get()
    while ((current != maze.getObjectives()[0]) and (stop == 0)):
    #while (current != maze.getObjectives()[0]):
        for nb in maze.getNeighbors(current[0], current[1]):
            #if (nb not in visited):
            if (nb not in visited) and (nb not in fringe.queue):
                fringe.put(nb)
                parent[nb] = current
        visited.append(current)
        #print("Exp: " + str(count) + " in " + str(current))
        #count += 1
        if not fringe.empty():
            current = fringe.get()
        else:
            stop = 1
    #print("Start: " + str(maze.getStart()))
    #print("Goal: " + str(maze.getObjectives()[0]))
    if(current == maze.getObjectives()[0]):
        node = current
        while node != maze.getStart():
            #print(node)
            result.append(node)
            node = parent[node]
        #print(node)
        result.append(node)
        result.reverse()
    else:
        print("Sorry, there is no solution :')")
        result.append(maze.getStart())
    return result