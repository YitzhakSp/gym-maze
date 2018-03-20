from gym_maze.envs import MazeEnv
from gym_maze.envs.generators import *
import sys, gym, time
import json
import numpy as np


maze = RandomBlockMazeGenerator(maze_size=4, obstacle_ratio=0.0)
env = MazeEnv(maze,live_display=True)
env.reset()

if not hasattr(env.action_space, 'n'):
    raise Exception('Keyboard agent only supports discrete action spaces')
n_act = env.action_space.n
SKIP_CONTROL = 0    # Use previous control decision SKIP_CONTROL times, that's how you
                    # can test what skip is still usable.

human_agent_action = 0
human_wants_restart = False
human_sets_pause = False

def key_press(key, mod):
    global human_agent_action, human_wants_restart, human_sets_pause
    if key==32: human_sets_pause = not human_sets_pause
    human_agent_action = int( key - ord('0') )
    if human_agent_action==66: human_wants_restart=True

def key_release(key, mod):
    global human_agent_action
    a = int( key - ord('0') )
    if a <= 0 or a >= n_act: return
    if human_agent_action == a:
        human_agent_action = 0

env.render()
env.unwrapped.viewer.window.on_key_press = key_press
#env.unwrapped.viewer.window.on_key_release = key_release
def rollout(env):
    global human_agent_action, human_wants_restart, human_sets_pause
    hd = np.empty((n_act, 0)).tolist()
    human_wants_restart = False
    obser = env.reset()
    total_reward = 0
    total_timesteps = 0
    i,next_key=0,62
    next_key_hit = True
    tmp=[(3,3),(4,4)]
    while 1:
        #print('debug action={}'.format(human_agent_action))
        if human_agent_action==next_key:
            next_key_hit=True
        if next_key_hit:
            if human_agent_action < 0 or human_agent_action >= n_act:
                print ( "{} is not valid action".format(human_agent_action))
                print('choose valid action ({} attempts)'.format(i))
                i+=1
            else:
                print('action={}'.format(human_agent_action))
                hd[human_agent_action].append( np.round(obser,2).tolist() )
                print('hd=',hd)
                total_timesteps += 1
                obser, r, done, info = env.step(human_agent_action)
                print("reward %0.3f" % r)
                total_reward += r
                next_key_hit = False
                print('press next')
                i = 0
        window_still_open = env.render()
        if done: break
        if human_wants_restart: break
        time.sleep(.5)
    print("timesteps %i reward %0.2f" % (total_timesteps, total_reward))
    with open('human_demo.json', 'w') as fp:
        json.dump(hd, fp)
        #json.dumps([[ob.__dict__ for ob in lst] for lst in hd])
        #json.dumps([lst for lst in hd])



print("ACTIONS={}".format(n_act))
print("Press keys 0 1 2 3 to take actions")

window_still_open = rollout(env)
