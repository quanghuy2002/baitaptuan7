import numpy as np
a = np.zeros((2, 512 * 512), dtype=np.float32)
a[0, :] = 1.0
a[1, :] = 0.1

print("a.shape: ", a.shape)
print("mean a = ", np.mean(a))