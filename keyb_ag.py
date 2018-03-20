from gym_maze.envs import MazeEnv
from gym_maze.envs.generators import *
import time
import matplotlib.pyplot as plt


maze = RandomBlockMazeGenerator(maze_size=4, obstacle_ratio=0.0,)
env = MazeEnv(maze)
env.reset()
for i in range(5):
    #env.render()
    a = int(input("next action ? "))
    s, r, done, info = env.step(a)
    #time.sleep(.5)
    plt.imshow(s, cmap=env.cmap, norm=env.norm)
    plt.show()
