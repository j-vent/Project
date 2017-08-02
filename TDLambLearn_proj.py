import numpy as np
#from simple_kanerva import *
import simple_kanerva
from agent_proj import *
from env_proj import *
import random
import sys, traceback

numSteps = 1000
numactfeat,numfeat = returnNums()
lamb = 0.4
alpha = 0.01/numactfeat #change in agent
epsilon = 0.1
weight = np.zeros(len(Actions) * numfeat) #^
gamma_prime = 1
gamma_orig = 1
numEpisodes = 50
x_origval =[]
States, Actions = returnVal() #change name 

#x_orig = getStateActionvector(returnKanerva(), action)


kanerva_obj = KanervaCoding([-1.6,-1.6,-1.6,-1.6], [1.6,1.6,1.6,1.6], numfeat, random_seed = 26, bias = True)
s1,s2,s3,s4 = returnServos()
observations = init(s1,s2,s3,s4)
state = kanerva_obj.get_x(observations, numactfeat, ignore=None)

def returnKanerva():
    return state

def getStateActionvector(s,a):
    sa_vector = np.zeros(len(Actions) * numfeat)
    ind = Actions.index(a)
    #print("This is ind:", ind ,"numfeat", numfeat, "s", s)
    #sa_vector[ind  * numfeat:(ind + 1) * numfeat]
    sa_vector[s+ ind*(numfeat)] = 1
    #print("This is s", s)
    #print("state action vector",sa_vector)
    #print(sum(sa_vector))
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

def return_V(state,action): 
    x = getStateActionvector(state,action)
    #print("x",x)
    #print("w",weight)
    v = np.dot(x,weight)
    #print("v", v)
    return v

#kanerva_obj = returnObj()
terminal = [-2,-2,-2,-2]
#print(greedyPolicy(returnKanerva()))
time = 0
retval = 0
delta = 0
elig_orig = np.zeros(len(Actions) * numfeat) 
state = returnKanerva()
action = epPolicy(state) 
E = updateE(action,time) #init = 1 for seen 0 everything else
entropyE_orig = entropy(E)
running = True

while(time <= numSteps): #keyboard interrupt
    with open("actions_reward_pos01.txt", "a") as f:
        #print("time", time)
        #print("This is e_orig",E_orig)
        ##print("Action taken:",action)
        observedprime = takeAction(state,action)#why do i even need to pass state? 
        #print("observation",observedprime)
        stateprime = kanerva_obj.get_x(observedprime, numactfeat, ignore=None, distance_metric='hamming')
        #print("encoded stateprime",stateprime)
        actionprime = (epPolicy(stateprime))
        E = updateE(actionprime, time)# oc= 1 if even happened; oc = 0 if not
        print("E", E)
        entropyE_prime = entropy(E)
        #print("This is E_orig", entropyE_orig, "This is E prime", entropyE_prime)
        
        
        reward = returnReward(entropyE_orig,entropyE_prime)
        print("reward", reward, "entropyE_orig", entropyE_orig, "entropyE_prime", entropyE_prime)
        #actionprime = (epPolicy(stateprime))
        #print(reward)
        f.write(str(time)+','+str(reward)+','+str(entropyE_orig)+'\n')
        #print("reward:",reward, "current state", state, "new state", stateprime)
        
        retval = retval + reward #return val: sum of all rewards in the episode
        
        
        delta = reward + (gamma_prime* return_V(stateprime,actionprime))- return_V(state,action) #reward is from curiosity
        elig_prime= (lamb * gamma_orig* elig_orig )#adding the last part; weird triangle
        elig_prime[state] = 1
        weight_prime = weight + (alpha * delta * elig_prime)
        #print("delta", delta, "elig_prime", elig_prime) 
        #print("sum of weight",sum(weight_prime))
        #print("elig_orig", elig_orig, "weight_prime", weight_prime)
        state = stateprime
        gamma_orig= gamma_prime
        action = actionprime 
        time += 1 #keeps track of "time"
        entropyE_orig = entropyE_prime
        weight = weight_prime
        elig_orig = elig_prime
        
print("average return: ", retval/numSteps)