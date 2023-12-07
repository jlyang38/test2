import numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a.shape) #结果返回一个tuple元组 (2, 5) 2行，5列
print(a.shape[0]) #获得行数，返回 2
print(a.shape[1]) #获得列数，返回 5