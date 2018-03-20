from gym_maze.envs import MazeEnv
from gym_maze.envs.generators import *
import time
import matplotlib.pyplot as plt


maze = RandomBlockMazeGenerator(maze_size=4, obstacle_ratio=0.0)
env = MazeEnv(maze,live_display=False)
env.reset()
fig1, ax1 = plt.subplots(figsize=(15,10))
for i in range(5):
    print(i)
    #fig=env.render()
    a=env.action_space.sample()
    s, r, done, info = env.step(a)
    ax1.imshow(s, cmap=env.cmap, norm=env.norm)
    #fig1.canvas.draw()
    #plt.draw()
    time.sleep(1)
    plt.show()

