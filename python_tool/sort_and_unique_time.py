import numpy as np

time = np.array([3, 1, 2, 2])
density = np.array([30, 10, 20, 21])

# 1. 排序
idx = np.argsort(time)
time_sorted = time[idx]
density_sorted = density[idx]

print("After sort:")
print("time_sorted:", time_sorted)
print("density_sorted:",density_sorted)

# 2. 去除重複時間（保留第一筆）
time_unique, unique_idx = np.unique(time_sorted, return_index=True)
density_unique = density_sorted[unique_idx]
print("\nAfter unique:")
print("unique_idx:", unique_idx)
print("time_unique:",time_unique)
print("density_unique:",density_unique)