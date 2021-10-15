    
import platform
import sys
import time
import numpy as np

    
from classes import Agent, Composition

class Gingerbread(Composition):
    def __init__(self, BPM=90):
        Composition.__init__(self,BPM=BPM)
        self.min=-3
        self.max=8
        self.range=self.max-self.min 
        self.midinote = 60
        self.duration = 0.1
        #intialize gingerbread function (it is not!)
        self.x=-0.1
        self.y=0.1
        n = 0
    def map(self, value_in, min_out, max_out):
        value_out = (value_in-self.min)/(self.range)
        value_out = min_out+ value_out * (max_out-min_out)
        return np.clip(value_out, min_out, max_out)

    def next(self):
        xn,yn = self.x, self.y
        self.x = 1-yn + abs(xn)
        self.y = xn
        self.midinote = self.map(self.x, 35, 55)
        self.duration = self.map(self.y, 0.25, 2)
        pass
    
if __name__=="__main__":
    n_agents=1
    composer=Gingerbread()
    agents=[_ for _ in range(n_agents)]
    agents[0] = Agent(57120, "/note_effect", composer)

    input("Press any key to start \n")
    for agent in agents:
        agent.start()
    try: # USE CTRL+C to exit     
        while True:
            time.sleep(10)
    except:         
        for agent in agents:              
            agent.kill()
            agent.join()
        sys.exit()

# %%