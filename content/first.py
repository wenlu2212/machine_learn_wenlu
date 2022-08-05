# import matplotlib.pyplot as plt
# plt.figure(figsize=(10,10),dpi=100)
# plt.plot([1,2,3,4,5,6,7],[17,17,18,15,11,11,13])
# plt.show
# print(plt.show)

import pandas as pd
import numpy as np

pd.Series(data=None, index=None, dtype=None)
a = pd.Series(np.arange(10), dtype=np.int64)

print(a)
# 创建ndarray
# score = np.array(
# [[80, 89, 86, 67, 79],
# [78, 97, 89, 67, 81],
# [90, 94, 78, 67, 74],
# [91, 91, 90, 67, 69],
# [76, 87, 75, 67, 86],
# [70, 79, 84, 67, 84],
# [94, 92, 93, 67, 64],
# [86, 85, 83, 67, 80]])


# df = pd.DataFrame({'COL1' : [2,3,4,5,4,2],
#                    'COL2' : [0,1,2,3,4,2]})
# print(df.median())
# print("打印 数组：")
# print(score)
