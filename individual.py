import random
import pyrosim
from insect import INSECT
import math
import constants as c
import numpy

class INDIVIDUAL:
    def __init__(self,i,neuron_val):
        self.ID = i 
        self.neuron_val = neuron_val
        self.genome3 = random.randint(1,10)
        self.genome1 = numpy.random.random((12,self.genome3+1))*2 - 1
        self.genome2 = numpy.random.random((self.genome3+1,8))*2 - 1
        self.fitness = 0
    
    def Evaluate(self,pb=False):
        insect = INSECT()


    def Start_Evaluation(self,pb):
        self.sim = pyrosim.Simulator(play_paused=True,eval_time=1500,play_blind=pb)
        self.insect = INSECT()
        self.insect.send_objects(self.sim,True)
        self.insect.send_joints(self.sim,True)
        self.insect.send_sensors(self.sim,True)
        #self.genome2 = numpy.random.random((32,self.neuron_val+1))*2 - 1
        #self.genome3 = numpy.random.random((self.neuron_val+1,19))*2 - 1
        self.insect.send_neurons(self.sim,self.genome3,True)
        self.insect.send_synapses(self.sim,self.genome1,self.genome2,1)
        self.sim.start()

    def Compute_Fitness(self,fitness_index):

        self.sim.wait_to_finish()

        xact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=0)
        yact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=1)
        zact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=2)
        ori = self.sim.get_sensor_data(sensor_id=self.insect.P1)
        #light_pos = self.sim.get_sensor_data(sensor_id = self.insect.Obsense_Pos, svi=0)
        #light = self.sim.get_sensor_data(sensor_id=self.insect.Obsense)

        if fitness_index <= 5:
            summ = -xact[-1]
        if fitness_index <= 10:
            summ = -yact[-1]          #(yact[-1] - abs(xact[-1]))
        elif fitness_index <= 15:
            summ = yact[-1]
        elif fitness_index <= 21:
            summ = xact[-1]

        self.fitness = summ        
        del self.sim
        del self.insect
        return xact[-1],yact[-1],zact[-1],ori[-1]

    def Mutate(self):
        genetoMutate0 = random.randint(0,11)  #input
        genetoMutate1 = random.randint(0,self.genome3)  #hidden
        genetoMutate2 = random.randint(0,7)  #motor

        self.genome1[genetoMutate0,genetoMutate1] = random.gauss(self.genome1[genetoMutate0,genetoMutate1], math.fabs(self.genome1[genetoMutate0,genetoMutate1]))
        

        if (self.genome1[genetoMutate0,genetoMutate1] > 1):
            self.genome1[genetoMutate0,genetoMutate1] = 1
        if (self.genome1[genetoMutate0,genetoMutate1] < -1):
            self.genome1[genetoMutate0,genetoMutate1] = -1            

        self.genome2[genetoMutate1,genetoMutate2] = random.gauss(self.genome2[genetoMutate1,genetoMutate2], math.fabs(self.genome2[genetoMutate1,genetoMutate2]))

        if (self.genome2[genetoMutate1,genetoMutate2] > 1): 
            self.genome2[genetoMutate1,genetoMutate2] = 1
        if (self.genome2[genetoMutate1,genetoMutate2] < -1):
            self.genome2[genetoMutate1,genetoMutate2] = -1

        
        genome3_temp = int(random.gauss(self.genome3, math.fabs(self.genome3)))
        diff = self.genome3-genome3_temp

        if diff <= 0:
            genome_temp = numpy.random.random((12,-diff))*2-1
            self.genome1 = numpy.concatenate((self.genome1,genome_temp), axis=1)
            genome_temp2 = numpy.random.random((-diff,8))*2-1
            self.genome2 = numpy.concatenate((self.genome2,genome_temp2), axis=0)
            self.genome3 = self.genome3 - diff
        if self.genome3 > 100:
            self.genome3 = 100

    
    def Crossover(self, p1g1, p1g2, p1g3, p2g1, p2g2, p2g3):
        if round(random.uniform(0,1),1) < 0.5:
            self.genome3 = p1g3
            self.genome1 = p1g1
            self.genome2 = p1g2
        else:
            self.genome3 = p2g3
            self.genome1 = p2g1
            self.genome2 = p2g2
        
        if p1g2.shape[0]-p2g2.shape[0] >= 0:
            for i in range(0,p2g2.shape[0]-1):
                for j in range(0,7):
                    if round(random.uniform(0,1),1) < 0.5:
                        self.genome2[i,j] = p1g2[i,j]
                    else:
                        self.genome2[i,j] = p2g2[i,j]

        else:
            for i in range(0,p1g2.shape[0]-1):
                for j in range(0,7):
                    if round(random.uniform(0,1),1) < 0.5:
                        self.genome2[i,j] = p1g2[i,j]
                    else:
                        self.genome2[i,j] = p2g2[i,j]

        if p1g1.shape[1]-p2g1.shape[1] >= 0:
            for i in range(0,11):
                for j in range(0,p2g1.shape[1]-1):
                    if round(random.uniform(0,1),1) < 0.5:
                        self.genome1[i,j] = p1g1[i,j]
                    else:
                        self.genome1[i,j] = p2g1[i,j]

        else:
            for i in range(0,11):
                for j in range(0,p1g1.shape[1]-1):
                    if round(random.uniform(0,1),1) < 0.5:
                        self.genome1[i,j] = p1g1[i,j]
                    else:
                        self.genome1[i,j] = p2g1[i,j]


    def Print(self):
        print('[ ', self.ID, self.fitness, self.genome3, ']', end=' ')

    def Start_Post_Evaluation(self, visualize, neurons1, genome1, genome2, neurons2, genome3, genome4):
        self.sim = pyrosim.Simulator(play_paused=True,eval_time=1800,play_blind=visualize)
        self.insect = INSECT()
        self.insect.send_objects(self.sim,False)
        self.insect.send_joints(self.sim,False)
        self.insect.send_sensors(self.sim,False)
        #self.genome2 = numpy.random.random((32,self.neuron_val+1))*2 - 1
        #self.genome3 = numpy.random.random((self.neuron_val+1,19))*2 - 1
        self.insect.send_Post_neurons(self.sim,neurons1,neurons2)
        self.insect.send_Post_synapses(self.sim,genome1,genome2,genome3,genome4)
        self.sim.start()

    def Compute_Post_Fitness(self):
        self.sim.wait_to_finish()

        xact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=0)
        yact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=1)
        zact = self.sim.get_sensor_data(sensor_id=self.insect.P4, svi=2)
        ori = self.sim.get_sensor_data(sensor_id=self.insect.P1)
        
        xact1 = self.sim.get_sensor_data(sensor_id=self.insect.Q4, svi=0)
        yact1 = self.sim.get_sensor_data(sensor_id=self.insect.Q4, svi=1)
        zact1 = self.sim.get_sensor_data(sensor_id=self.insect.Q4, svi=2)
        ori1 = self.sim.get_sensor_data(sensor_id=self.insect.Q1)
        
        cxp1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_XP, svi=0)
        dxp1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_XP, svi=1)
        cxn1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_XN, svi=0)
        dxn1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_XN, svi=1)
        cyp1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_YP, svi=0)
        dyp1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_YP, svi=1)
        cyn1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_YN, svi=0)
        dyn1_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP1_YN, svi=1)
              
        cxp2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_XP, svi=0)
        dxp2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_XP, svi=1)
        cxn2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_XN, svi=0)
        dxn2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_XN, svi=1)
        cyp2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_YP, svi=0)
        dyp2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_YP, svi=1)
        cyn2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_YN, svi=0)
        dyn2_chk = self.sim.get_sensor_data(sensor_id=self.insect.RP2_YN, svi=1)
        
        light_pos = self.sim.get_sensor_data(sensor_id = self.insect.Obsense_Pos, svi=0)
        light_pos_y = self.sim.get_sensor_data(sensor_id = self.insect.Obsense_Pos, svi=1)
        light = self.sim.get_sensor_data(sensor_id=self.insect.Obsense)


        #if ((cxp1_chk[-1] == 1)or(cxn1_chk[-1] == 1)or(cyp1_chk[-1] == 1)or(cyn1_chk[-1] ==1)):
        indiv1 = ((light[-1]-light[1]) - (cxp1_chk[-1] + cxn1_chk[-1] + cyp1_chk[-1] + cyn1_chk[-1])) + (dxp1_chk[-1] + dxn1_chk[-1] + dyp1_chk[-1] + dyn1_chk[-1])


        #if ((cxp2_chk[-1] == 1)or(cxn2_chk[-1] == 1)or(cyp2_chk[-1] == 1)or(cyn2_chk[-1] ==1)):
        indiv2 = ((light[-1]-light[1]) - (cxp2_chk[-1] + cxn2_chk[-1] + cyp2_chk[-1] + cyn2_chk[-1])) + (dxp2_chk[-1] + dxn2_chk[-1] + dyp2_chk[-1] + dyn2_chk[-1])
        #else:
        #    indiv2 = -20 + ((light[-1]-light[1]) - (dxp2_chk[-1] + dxn2_chk[-1] + dyp2_chk[-1] + dyn2_chk[-1]))

        summ = indiv1 + indiv2


        self.fitness = summ
        del self.sim
        del self.insect
        return summ,indiv1,indiv2
