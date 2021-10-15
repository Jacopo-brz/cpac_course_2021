   
import sys
import time
import numpy as np

from classes import Agent, Composition, ID_START

class Simple_Next(Composition):
    def __init__(self, BPM=120):
        Composition.__init__(self,BPM=BPM)
            
    def next(self):
        if self.id ==ID_START: 
            self.id=12  #chromatic scale
        if self.id > 0:
            self.midinote= 72 - self.id
            self.dur = 1
            self.amp = 1
            self.id-=1
        else:
            self.id= 12
            self.BPM= 120
            self.next()

if __name__=="__main__":
    n_agents=1
    composer=Simple_Next()
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