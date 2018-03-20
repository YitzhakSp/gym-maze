from gym_maze.envs import MazeEnv
from gym_maze.envs.generators import *
import time

maze = RandomBlockMazeGenerator(maze_size=4, obstacle_ratio=0.0)
env = MazeEnv(maze,live_display=True)
env.reset()
for i in range(100):
    fig=env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    time.sleep(.5)
