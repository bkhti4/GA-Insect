from individual import INDIVIDUAL
import copy
import random

class POPULATION:
    def __init__(self,popSize,prev_popSize):
        self.p = {}
        self.popSize = popSize
        self.prev_popSize = prev_popSize

    def Initialize(self,neuron_val):
        if self.popSize - self.prev_popSize == 0:
            for i in range(0,self.popSize):
                self.p[i] = INDIVIDUAL(i,neuron_val)
        else:
            self.p[self.popSize-1] = INDIVIDUAL(self.popSize-1,neuron_val)

    def Print(self):
        for i in self.p:
            if (i in self.p):
                self.p[i].Print()

    def Evaluate(self,pb,type_of_fitness):
        tst = 0
        genetic1 = {}
        genetic2 = {}
        data_ind = {}
        neuron_ind = {}
        x_dist = {}
        y_dist = {}
        z_dist = {}
        ori_val = {}
        for i in self.p:
            if(tst == 1):
                self.p[i].Start_Evaluation(pb)
            else:
                self.p[i].Start_Evaluation(True)
            tst = tst + 1
        indx = 0
        for i in self.p:
            x=0
            y=0
            z=0
            ori=0
            x,y,z,ori = self.p[i].Compute_Fitness(type_of_fitness)
            #indx = self.p[i].ID
            data_ind[indx] = self.p[i].fitness 
            neuron_ind[indx] = self.p[i].genome3
            genetic1[indx] = self.p[i].genome1
            genetic2[indx] = self.p[i].genome2
            x_dist[indx] = x
            y_dist[indx] = y
            z_dist[indx] = z
            ori_val[indx] = ori
            indx = indx + 1

        return data_ind,neuron_ind,genetic1,genetic2,x_dist,y_dist,z_dist,ori_val


    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()


    def ReplaceWith(self, other):
        for i in other.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]

    def Fill_From(self, other, mutate_rate, chance):
        self.Copy_Best_From(other)
        #self.Print()
        value = self.Collect_Children_From(other, mutate_rate, chance)
        #self.Print()
        return value

    def Copy_Best_From(self, other):
        index_success = 0
        for j in other.p:
            chk_against = other.p[j].fitness
        for i in other.p:
            if (chk_against < other.p[i].fitness):
                index_success = i
                chk_against = other.p[i].fitness
        child = copy.deepcopy(other.p[index_success])
        self.p[0] = child

    def Collect_Children_From(self, other, mutate_rate, chance):
        tk = 0
        crossover_rate = 0.3
        for j in other.p:
            if (tk > 0):
                winner = self.Winner_of_Tournament_Selection(other)
                self.p[tk] = copy.deepcopy(winner)
                #print(self.p[tk])
                if round(random.uniform(0,1),1) < mutate_rate:
                    self.p[tk].Mutate()
            tk = tk+1
        
        if chance == 1:
            if round(random.uniform(0,1),1) < crossover_rate:
                par1 = 0 
                par2 = 0
                while(par1 == par2):
                    par1 = random.randint(0,len(other.p)-1)
                    par2 = random.randint(0,len(other.p)-1)
        
                self.popSize = self.popSize+1
                self.p[self.popSize-1] = INDIVIDUAL(self.popSize-1,10)
                self.p[self.popSize-1].Crossover(self.p[par1].genome1,self.p[par1].genome2,self.p[par1].genome3,self.p[par2].genome1,self.p[par2].genome2,self.p[par2].genome3)

        return self.popSize

    def Winner_of_Tournament_Selection(self,other):
        p1 = 0
        p2 = 0
        while(p1 == p2):
            p1 = random.randint(0,len(other.p)-1)
            p2 = random.randint(0,len(other.p)-1) #len(other.p)-1
        if (other.p[p1].fitness >= other.p[p2].fitness):
            return other.p[p1]
        if (other.p[p1].fitness < other.p[p2].fitness):
            return other.p[p2]

    def Clone(self,other):
        for i in other.p:
            self.p[i] = other.p[i]
    
    def Post_Initialize(self, neurons):
        for i in range(0,self.popSize):
            self.p[i] = INDIVIDUAL(i,neurons)

    def Post_Evaluate(self, visualize, genome1, genome2, genome3, genome4, genome5, genome6):
        for i in self.p:
            self.p[i].Start_Post_Evaluation(visualize,genome3,genome1,genome2,genome6, genome4, genome5)
        for i in self.p:
            fit,indiv1,indiv2 = self.p[i].Compute_Post_Fitness()

        return fit,indiv1,indiv2
