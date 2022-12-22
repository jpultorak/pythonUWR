import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

# Size of grid [N x N]
N = 70 
# int values of OFF/ON, also intensity of color of dead/alive cells
ON = 0
OFF = 255

grid = np.array([])

# procentage of initial alive cells (fraction)
def random_init(alive_init = 0.2):
    return np.random.choice([ON, OFF], N*N, p = [alive_init, 1-alive_init]).reshape(N, N)

def blinker():
    g = np.full((N, N), OFF)
    for i in range(1, N, 4):
        g[1:N-2:4, i:i+3] = ON
    return g

def glider():
    g = np.full((N, N), OFF)
    g[1:4, 3] = g[3, 2] = g[2, 1] = ON
    return g

def total_neigbours(x, y):
    total = 0
    move = [-1, 0, 1]

    for dx in move:
        for dy in move:
            if dx == dy == 0:
                continue
            # I assume the cells outside the border are dead
            if (dx == -1 and x == 0) or (dx == 1 and x == N-1):
                continue 
            if (dy == -1 and y == 0) or (dy == 1 and y == N-1): continue 

            new_x, new_y = x + dx, y + dy
            total += 1 if grid[new_x, new_y] == ON else 0
    return total

def update_grid(i):
    global grid
    grid_new = grid.copy()
    for i in range(N):
        for j in range(N):
            total = total_neigbours(i, j) 
            if grid[i, j] == ON and (total <= 1 or total >= 4):
                grid_new[i, j] = OFF                    
            if grid[i, j] == OFF and total == 3:
                grid_new[i, j] = ON

    grid = grid_new
    mat.set_data(grid)
    return mat

if __name__ == '__main__':
    # grid = random_init()
    # grid = blinker()
    grid = glider()    
    fig, ax = plt.subplots()

    mat = ax.matshow(grid, cmap = 'gray_r', vmin=0, vmax=255)
    ani = animation.FuncAnimation(fig, update_grid, interval = 300, save_count = 500)
    plt.show()
