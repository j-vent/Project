import numpy as np
#from simple_kanerva import *
import simple_kanerva
from agent_proj import *
from env_proj import *
import random

numactfeat,numfeat = returnNums()
lamb = 0
alpha = 0.01/numactfeat #change in agent
epsilon = 0.1
weight = np.zeros(len(Actions) * numfeat) #^
gamma = 1
numEpisodes = 1000
x_origval =[]
States, Actions = returnVal() #change name 

#x_orig = getStateActionvector(returnKanerva(), action)

def getStateActionvector(s,a):
    sa_vector = np.zeros(len(Actions) * numfeat)
    ind = Actions.index(a)
    #print("This is ind:", ind ,"numfeat", numfeat, "s", s)
    #sa_vector[ind  * numfeat:(ind + 1) * numfeat]
    sa_vector[s+ ind*(numfeat)] = 1
    #print("This is s", s)
    return sa_vector

def greedyPolicy(state):
    values = []
    for a in range (0,len(Actions)):
        x = getStateActionvector(state,Actions[a])
        v = x * weight
        #print("x", x, "w", weight, "v", v)
        values.append(v)
    index = numpy.argmax(values)
    return Actions[index]

def epPolicy(state):
    x = random.random()
    if x < epsilon:
        S,A = returnVal()
        action = random.choice(A)
    else:
        #find better way if more actions
        action =greedyPolicy(state)
    return action

def return_V(state,action, time): #remove time probably
    x = getStateActionvector(state,Actions[a])
    v = x * weight
    return v

#kanerva_obj = returnObj()
terminal = [-2,-2,-2,-2]
#print(greedyPolicy(returnKanerva()))
time = 0
for episodeNum in range(numEpisodes): 
    #idk what to put here
    delta = 0
    elig_orig = np.zeros(len(Actions) * numfeat) 
    state = returnKanerva()
    action = epPolicy(state)
    E_orig = updateE(state,time) #init = 1 for seen 0 everything else
    
    while((state != terminal).all()): #does not need a terminal 
        observedprime = takeAction(state,action)
        stateprime = kanerva_obj.get_x(observedprime, numactfeat, ignore=None, distance_metric='hamming')
        E_prime = updateE(stateprime, time)# oc= 1 if even happened; oc = 0 if not
        reward = returnReward(E_orig,E_prime)
        print("reward:",reward, "current state", state, "new state", stateprime)
        '''
        retval = retval + reward #return val: sum of all rewards in the episode
        
    
        delta = reward(E,E) + (gamma_prime* v_prime)- v_orig #reward is from curiosity
        elig_prime= lamb * gamma_orig* elig_orig 
        weight_prime = weight_prime + alpha * delta * elig_prime        
        
        state = stateprime
        gamma_orig= gamma_prime
        #action = actionprime 
        time += 1 #keeps track of "time"
        E_orig = E_prime
   
        '''
  