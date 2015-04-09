import random
import collections

jml_populasi = 10
Individu = collections.namedtuple('Individu', 'dna fitness')
dna_size = 8

def fungsi(x,y):
    return (3*(x**2) + 2*(y**2) - 4*x + (y*1.0)/2)

def fitness(ind):
    hasil = fungsi(decode(ind)[0],decode(ind)[1])
    return (1/((hasil*1.0)+0.1))

def encode(x,y):
    bin_x = '{0:04b}'.format(x)
    bin_y = '{0:04b}'.format(y)
    return bin_x+bin_y

def decode(biner):
    mid = len(biner)/2
    x = int(biner[:mid],2)
    y = int(biner[mid:],2)
    return [x,y]

def random_population():
    pop = [''.join([str(random.randint(0,1)) for _ in range(dna_size)]) for _ in range(jml_populasi)]
    current_generation = [Individu(dna,fitness(dna)) for dna in pop]
    return current_generation

def weighted_choice(pop,n):
    weight_total = sum(ind.fitness for ind in pop)
    for ind in pop:
        if n < (ind.fitness/weight_total):
            return ind
        n = n - (ind.fitness/weight_total)
    return ind

#seleksi orang tua menggunakan roulette wheel
def roulette_wheel(pop):
    n1 = random.uniform(0, 1)
    ind1 = weighted_choice(pop, n1)
    n2 = random.uniform(0, 1)
    ind2 = weighted_choice(pop, n2)
    return [ind1,ind2]

#seleksi orang tua menggunakan SUS
def sus(pop):
    n = random.uniform(0, 0.5)
    ind1 = weighted_choice(pop, n)
    ind2 = weighted_choice(pop, 0.5+n)
    return [ind1,ind2]

'''
#one point crossover
def crossover(ind1, ind2):
    poin = int(random.randint(0,dna_size))
    tmp1 = ind1.dna[:poin]+ind2.dna[poin:]
    tmp2 = ind2.dna[:poin]+ind1.dna[poin:]
    new_ind1 = Individu(tmp1, fitness(tmp1))
    new_ind2 = Individu(tmp2, fitness(tmp2))
    return new_ind1, new_ind2
'''

#n point crossover
def crossover(ind1, ind2):
    n = random.randint(1,dna_size-1)
    points = [int(random.randint(0,dna_size)) for _ in range(n)]
    print n, points
    tmp_dna1 = ind1.dna
    tmp_dna2 = ind2.dna
    for point in points:
        tmp1 = tmp_dna1[:point]+tmp_dna2[point:]
        tmp2 = tmp_dna2[:point]+tmp_dna1[point:]
        tmp_dna1 = tmp1
        tmp_dna2 = tmp2
    new_ind1 = Individu(tmp_dna1, fitness(tmp1))
    new_ind2 = Individu(tmp_dna2, fitness(tmp2))
    return new_ind1, new_ind2

def mutasi

population = random_population()
ind1 = roulette_wheel(population)[0]
ind2 = roulette_wheel(population)[1]
for ind in population:
    print ind
print "pilihan : " , ind1, ind2
print (crossover(ind1,ind2))
