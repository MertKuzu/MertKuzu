import numpy as np

result = np.array([1,3,5,7,9])
result = np.arange(1,10)
result = np.arange(10,100,3)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5)
result = np.random.randint(1,10)
result = np.random.randint(1,100,5)
result = np.random.rand(3)
result = np.random.randn(3)
# npArray = np.arange(50)
# npMulti = npArray.reshape(5,10)
# print(npMulti.sum(axis=1))
# print(npMulti.sum(axis=0))

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max()
result = rnd_numbers.min()
result = rnd_numbers.mean()   #average
result = rnd_numbers.argmax()
result = rnd_numbers.argmin()



print(result)