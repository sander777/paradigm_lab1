import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

n_xi = 1000
n_nu = 1000

nu = list(map(lambda x: max(np.random.uniform(0, 1, n_xi)), list(range(n_nu))))

plt.hist(nu)
plt.show()