import numpy as np

class Candidates(object):
    def __init__(self,popsize,chromsize,fitnessfun):
        self.popsize = popsize
        self.chromsize = chromsize
        self.fitnessfun = fitnessfun
        self.fitness = np.zeros(popsize,1)
        self.chroms = np.zeros(popsize,chromsize)

    def randinit(self):
        self.chroms = np.random.rand(self.popsize,self.chromsize)        

    def mutate(self,pmutate):
        
    
    def cross(self,pcross,lencross):

    
    def fit(self):
        for i in range(self.popsize):
            self.fitness[i] = self.fitnessfun(self.chroms[i])

    def eliminate(self,size):
        '''
        Leave size of best candidates and regenerate new generation in popsize-size
        '''
        
        self.fit()

    def getcandidate(self,index):
        return self.chroms[index]

