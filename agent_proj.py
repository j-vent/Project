from simple_kanerva import * 
from env_proj import *


States,Actions = returnVal()
E = [0]*len(States)#initialize where 1 is seen and 0 is everything else
numfeat = 8
numactfeat = 4



'''
    def returnE():
        return E #how do you differentiate E between different points in time (t vs t+1)#keep a counter for each timestep   
'''
def retProb(t,oc,probability_o):
        if t==0:
                probability =1
        else:
                probability = probability_o + (1.0/t)*(occurred - probability_o) #occurred = 1 if happened, 0 if did not happen
        
        return probability

    
    
def updateE(obsd_state, t):
        
        for i in range(len(States)):
                if (States[i] == obsd_state).all(): #(A==B).all()
                        E[i] = retProb(t,1,E[i]) 
                else:
                        E[i] = retProb(t,0,E[i])
        return E

kanerva = KanervaCoding([-1.6,-1.6,-1.6,-1.6], [1.6,1.6,1.6,1.6], numfeat, random_seed = 26, bias = True)
s1,s2,s3,s4 = returnServos()
observations = init(s1,s2,s3,s4)
state = kanerva.get_x(observations, numactfeat, ignore=None)

def returnKanerva():
        return state
    
def returnNums():
        return numactfeat,numfeat


