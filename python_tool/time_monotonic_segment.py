import numpy as np
# arr = np.array([1, 4, 9, 16])
# print(np.diff(arr, n=1)) # out1[i] = a[i+1] - a[i] ==> n=1: [3, 5, 7]
# print(np.diff(arr, n=2)) # out2[i] = out1[i+1] - out1[i] ==> n=2: [2, 2]


# 偵測時間序列中「第一次出現不連續（倒退）」的位置，並只保留前面正常的資料
time = np.array([0, 1, 2, 3, 4, 5, 11, 2, 3, 12, 30, 2 , 4, 5])
cut_idx = np.where(np.diff(time) < 0)[0]
end = cut_idx[0] + 1
print(time[:end])
# output : [0, 1, 2, 3, 4, 5, 11]

