# Numpy Exercises

import numpy as np

np.zeros(10)

np.ones(10)

np.ones(10) * 5

np.arange(10,51)

np.arange(10,51,2)

np.arange(0,9).reshape(3,3)

np.eye(3)

#random number between 0 and 1
np.random.rand(1)

# gausian
np.random.randn(25)

#100 evenly spaced points between 0 and 1
np.linspace(0,1,100)

#A matrix
mat = np.arange(1,26).reshape(5,5)



# A few different slices
mat[2:,1:]

mat[0:3,1]

y = mat[4,]

#Sum all values in mat
np.sum(mat)

#Standard Deviation of Value in mat
np.std(mat)

# sum each column in matrix(recall passing in axis = to sum all columns)
mat.sum(axis = 0)

print(mat[y].sum(axis =0 ))





def learn(x,y):
    z = [y[value] for value in range(0,len(x)) if x[value] =='m']
    return z

print(learn(['m','f','m','f','m'],[1,2,3,4,5]))


def rake_garden(a):
    z = a.split()
    b = ' '
    y = ['gravel' if x != 'rock' else x for x in z]
    return b.join(y)


things = [['a','b'],['c','d'],['e','f']]
trees = [1,2,3]

for index,item in enumerate(things):
    item.append(trees[index])
    print(things)
















