import pyrosim
from insect import INSECT
from individual import INDIVIDUAL
from population import POPULATION
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import copy
import pickle
from sklearn.naive_bayes import GaussianNB

data = {}
data_tot = {}
data_final = {}
neurons = 63
neuron_tot = {}
genome1_tot = {}
genome2_tot = {}
genome3_tot = {}
x = {}
y = {}
z = {}
ori = {}

genome1_val = {}
genome2_val = {}
x_val = {}
y_val = {}
z_val = {}
ori_val = {}
fitness_index = 0
fitness = {}
generations = 20
mutate_rate = 0.6
init_pop = 30
final_pop = 10
prev_pop = 10
iterations = 21

for num_loops in range(0,iterations):

    init_pop = 30
    final_pop = 10
    prev_pop = 10
    
#####Parent Initialization#####

    parents = POPULATION(10,10)
    parents.Initialize(neurons)
    data,neurons_val,genome1_val,genome2_val,x,y,z,ori = parents.Evaluate(True,fitness_index)
    #parents.Print(False)
    #print(data)
    #exit()
    print(0)
    parents.Print()
    data_tot[0] = data
    neuron_tot[0] = neurons_val

#####Children Evaluation#####

    for i in range(1,generations):
        print('\n')
        children = POPULATION(final_pop,prev_pop)
        children_copy = POPULATION(final_pop,final_pop)

        children.Initialize(neurons)
    
        children_copy = copy.deepcopy(parents)
        if i > 2:
            pop = children.Fill_From(parents,mutate_rate,1)
        else:
            pop = children.Fill_From(parents,mutate_rate,0)
        final_pop = pop
        print(final_pop)
        if i == (generations-1):
            data,neurons_val,genome1_val,genome2_val,x,y,z,ori = children.Evaluate(True,fitness_index)
            print(i)
            children.Print()
            genome1_tot[num_loops] = genome1_val
            genome2_tot[num_loops] = genome2_val
            genome3_tot[num_loops] = neurons_val
            x_val[num_loops] = x
            y_val[num_loops] = y
            z_val[num_loops] = z
            ori_val[num_loops] = ori
            fitness[num_loops] = data
        else:
            data,neurons_val,genome1_val,genome2_val,x,y,z,ori = children.Evaluate(True,fitness_index)
            print(i)
            children.Print()
        if i > 1:
            parents = POPULATION(final_pop,final_pop)
            parents.Initialize(neurons)
            parents.Clone(children_copy)

        parents.ReplaceWith(children)
    
        print(final_pop)
        data_tot[i] = data
        neuron_tot[i] = neurons_val

    data_final[num_loops] = data_tot
    fitness_index = fitness_index + 1
#print('\n', data_tot)
#print(len(data_tot[1]))


avg_fitness = []
best_fitness = []
avg_neurons = []
best_neurons = []
x_val_array = []
y_val_array = []
z_val_array = []
ori_val_array = []
data_array = []
mrg1_array = []
mrg2_array = []
genome1_array = []
genome2_array = []
genome3_array = []

indicators = {}
indic_val = 0
indic = 0
for k in range(0,iterations):
    for l in range(0,len(x_val[k])-1):
        val1_temp = float("{0:.2f}".format(x_val[k][l]))
        val2_temp = float("{0:.2f}".format(y_val[k][l]))
        val3_temp = z_val[k][l] / 100
        val4_temp = ori_val[k][l] / 100
        mrg1_tmp = float("{0:.4f}".format(abs(val1_temp)+abs(val3_temp)))
        mrg2_tmp = float("{0:.4f}".format(abs(val2_temp)+abs(val4_temp)))
        mrg1_array.append(mrg1_tmp)
        mrg2_array.append(mrg2_tmp)
        x_val_array.append(x_val[k][l])
        y_val_array.append(y_val[k][l])
        z_val_array.append(z_val[k][l])
        ori_val_array.append(ori_val[k][l])
        data_array.append(fitness[k][l])
        genome1_array.append(genome1_tot[k][l])
        genome2_array.append(genome2_tot[k][l])
        genome3_array.append(genome3_tot[k][l])
        indic = indic + 1
    if k == 5 or k == 10 or k == 15 or k == 20:
        indicators[indic_val] = indic
        indic_val = indic_val + 1

tot_avg_fitness_pop = 0
for l in range(0,iterations):
    pop = init_pop
    for j in range(0,generations):
        summ_value = 0
        neuron_sum = 0
        pop = len(data_final[l][j])
        for k in range(0,pop):
            if k == 1:
                best_fitness.append(data_final[l][j][k])
                best_neurons.append(neuron_tot[j][k])
            summ_value = summ_value + data_final[l][j][k]
            neuron_sum = neuron_sum + neuron_tot[j][k]
        avg_fitness_pop = summ_value/pop
        tot_avg_fitness_pop = tot_avg_fitness_pop + avg_fitness_pop

avg_fitness_sum = 0
for yu in range(0,len(best_fitness)-1):
    avg_fitness_sum = avg_fitness_sum + best_fitness[yu] 

avg_val = avg_fitness_sum/(iterations)
print(avg_val)

#############Creating test data#############
x_val_array_fin = np.zeros((len(x_val_array)-1,4), dtype='float')

for k in range(0,len(x_val_array)-1):
    x_val_array_fin[k,0] = x_val_array[k]
    x_val_array_fin[k,1] = y_val_array[k]
    x_val_array_fin[k,2] = z_val_array[k]
    x_val_array_fin[k,3] = ori_val_array[k]

data_array_fin = np.zeros(len(x_val_array)-1, dtype='float')

for k in range(0,len(data_array)-1):
    data_array_fin[k] = data_array[k]*1000

model = GaussianNB()

data_array_fin = data_array_fin.astype('int')
model.fit(x_val_array_fin,data_array_fin)

#x_rand = random.uniform(-1,1)
#y_rand = random.uniform(-1,1)
#z_rand = random.uniform(-1,1)
#ori_rand = random.uniform(-1,1)

#predicted = model.predict([[x_rand,y_rand,z_rand,ori_rand]])
#print(predicted)

################################################


##############Evaluating ON Unknown##############

best_fit_val = -100
best_indiv1 = -100
best_indiv2 = -100
best_genome11_array = []
best_genome12_array = []
best_genome13_array = 0

best_genome21_array = []
best_genome22_array = []
best_genome23_array = 0


for init in range(0,len(genome3_array)-1):
    pred = POPULATION(1,0)

    pred.Post_Initialize(genome3_array[init])

    fit_val,indiv1,indiv2 = pred.Post_Evaluate(True,genome1_array[init],genome2_array[init],genome3_array[init],genome1_array[init],genome2_array[init],genome3_array[init])
    
    if init == 0 or indiv1 > best_indiv1:
        best_indiv1 = indiv1
        best_genome11_array = genome1_array[init]
        best_genome12_array = genome2_array[init]
        best_genome13_array = genome3_array[init]
    
    if init == 0 or indiv2 > best_indiv2:
        best_indiv2 = indiv2
        best_genome21_array = genome1_array[init]
        best_genome22_array = genome2_array[init]
        best_genome23_array = genome3_array[init]

    if init == len(genome3_array)-2:
        pred.Post_Initialize(best_genome13_array)

        fit_val = pred.Post_Evaluate(False,best_genome11_array,best_genome12_array,best_genome13_array,best_genome21_array,best_genome22_array,best_genome23_array)
        print(fit_val)
        break

##################################################

#f1 = plt.figure()
#plt.plot(avg_fitness)
#plt.plot(best_fitness)

#f2 = plt.figure()
#plt.plot(avg_neurons)
#plt.plot(best_neurons)

f4 = plt.figure()
bx = Axes3D(f4)
for k in range(0,len(mrg1_array)-1):
    d = 'o'
    if k <= indicators[0]:
        d = 'o'
    if k > indicators[0] and k <= indicators[1]:
        d = '^'
    if k > indicators[1] and k <= indicators[2]:
        d = '*'
    if k > indicators[2] and k <= indicators[3]:
        d = '+'

    if data_array[k] >= 2.5:
        bx.scatter(mrg1_array[k], mrg2_array[k], data_array[k], c='y', marker=d)
    elif data_array[k] >= 1.0:
        bx.scatter(mrg1_array[k], mrg2_array[k], data_array[k], c='r', marker=d)
    elif data_array[k] > -10:
        bx.scatter(mrg1_array[k], mrg2_array[k], data_array[k], c='b', marker=d)

plt.show()
