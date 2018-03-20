from gym_maze.envs import MazeEnv
from gym_maze.envs.generators import *
from gym_maze.envs.Astar_solver import AstarSolver

def solvemaze(maze, action_type='VonNeumann', render_trace=False, gif_file='video.gif'):
    env = MazeEnv(maze, action_type=action_type, render_trace=render_trace)
    env.reset()

    # Solve maze by A* search from current state to goal
    solver = AstarSolver(env, env.goal_states[0])
    if not solver.solvable():
        raise Error('The maze is not solvable given the current state and the goal state')

    for action in solver.get_actions():
        env.step(action)
        fig = env.render()

    return env._get_video(interval=200, gif_path=gif_file).to_html5_video()


maze = RandomBlockMazeGenerator(maze_size=4, obstacle_ratio=0.0)
env = MazeEnv(maze)
env.reset()
anim = solvemaze(maze, action_type='VonNeumann', render_trace=True, gif_file='data/simple_empty_maze.gif')
HTML(anim)