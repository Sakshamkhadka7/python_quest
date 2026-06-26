import numpy as np 


arry_1d=np.array([1,2,3,4,5])
# print(arry_1d[0])
# print(arry_1d[1])


for item in arry_1d:
    print(item)


arry_2d=np.array([
    [1,2,3],[4,5,6],[7,8,9]
    ])


for row in arry_2d:
    for item in row:
        print("Item of 2d array",item)

zeroes_arr=np.zeros((2,3))

print(zeroes_arr)

print(arry_1d)
print(arry_2d)
print(arry_1d.ndim)
print(arry_2d.ndim)
