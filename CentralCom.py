import BlobCreature
import random
import matplotlib.pyplot as mp
import math

Fulltime = 200


def replication(d_ch=0.05, r_ch=0.1):
    c = BlobCreature.Creature()
    c.death_ch = d_ch
    c.repl_ch = r_ch
    full_list.append(c)


def death(c):
    c.death_st = 1


ctr = 0
dead_ctr = 0
fo = open("C:/Users/tush_/Documents/records.txt", "wb")
for a in range(200):
    L = []
    K = []
    full_list = []
    timestep = 0
    replication()
    while timestep < Fulltime:
        K.append(timestep + 1)
        if random.random() > 10:
            replication()
        timestep = timestep + 1
        count = 0
        for i in full_list:
            if i.death_st == 0:
                count = count + 1
                i.age = i.age + 1
                i.death_ch = math.log(0.001 * math.pow(50, i.age) + 1.3) / (i.age) if i.age < 3 else (
                    0 if i.age < 50 else -1 * (i.age - 50) * (i.age - 100) * 0.0012)
                i.repl_ch = 0.15 + math.sin((math.pi / 180) * i.age) if 40 > i.age > 20 else 0
                if i.death_ch > random.random():
                    death(i)
                if i.repl_ch > random.random() and count > 0:
                    replication(0.09, 0.1)
        L.append(count)
    for k in L:
        print(k, end=' ')
    print("\n")
    mp.plot(K, L)
    if L[Fulltime-1] == 0:
        dead_ctr = dead_ctr + 1
print("\n")
print(dead_ctr, end=" lifelines went dead \n")
mp.ylabel("Number of Creatures")
mp.xlabel("Time Steps")
mp.show()
