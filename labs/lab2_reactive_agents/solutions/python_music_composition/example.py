    
import platform
import sys
import ctypes, sys
import time

import numpy as np

from constants import ID_START
    
from classes import Agent, Composition

class Random_Next(Composition):
    def __init__(self, BPM=60):
        Composition.__init__(self,BPM=BPM)
            
    def next(self):
        if self.id ==ID_START: 
            self.id=10
        if self.id >0:

            self.midinote=int(np.random.randint(60,84))
            self.dur =float(2**np.random.randint(-3, 0))
            self.amp = float(np.random.choice([0,1,1,1]))
            self.id-=1
        else:
            self.id=10
            self.BPM=np.random.randint(60, 120)
            self.next()
            

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if __name__=="__main__":
    if not is_admin() and "windows" in platform.platform().lower():        
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    n_agents=1
    composer=Random_Next()
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