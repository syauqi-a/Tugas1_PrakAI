# search.py
# ---------------
'''
Created by Kelompok 10 Ilmu Komputer C2 2019:
    - Farras Abdulaziz El-Fahd (1905484)
    - Khamidah Ahmad Syauqi (1904312)
    - M Fachri (1908969)
'''

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
#BFS graph search
def search(maze):
    fringe = queue.Queue()          #fringe berupa queue
    fringe.put(maze.getStart())
    visited = []                    #list of tuple node yang pernah dicek
    parent = {}                     #Dictionary of tuple hubungan node anak dengan node ortu
    stop = False                    #variabel penanda berhenti ketika fringe telah habis ditelusuri
    current = fringe.get()          #inisialisasi nilai awal node yang dicek

    #kami asumsikan ada maze yang tidak memiliki solusi, oleh karena itu kami membuat variabel penanda berhenti ketika node dalam fringe telah ditelusuri semua tetapi belum menemukan node goal

    #pengulangan sampai menemukan node goal atau sampai penanda berhenti bernilai True
    while ((current != maze.getObjectives()[0]) and (stop == False)):
        #ekspansi node tetangga dari node yang sedang dicek dan masukkan node tetangga ke dalam fringe
        for nb in maze.getNeighbors(current[0], current[1]):
            #pastikan node tetangga belum pernah dicek dan belum pernah dimasukkan ke dalam fringe
            if (nb not in visited) and (nb not in fringe.queue):
                fringe.put(nb)
                parent[nb] = current
        #masukkan node sekarang ke dalam list visited
        visited.append(current)
        #jika fringe belum habis maka ambil node selanjutnya menjadi node sekarang
        if not fringe.empty():
            current = fringe.get()
        #jika fringe telah habis maka berhentikan proses looping
        else:
            stop = True

    result = []                     #list of tuple path rekomendasi urutan state menuju goal
    #jika berhasil menemukan node goal
    if(current == maze.getObjectives()[0]):
        #salin urutan node goal menuju node awal
        node = current
        while node != maze.getStart():
            result.append(node)
            node = parent[node]
        result.append(node)
        #balik urutan dari node pada list result
        result.reverse()
    #jika tidak berhasil menemukan node goal
    else:
        print("Sorry, there is no solution :')")
        result.append(maze.getStart())

    return result