#Normal Distribution

from numpy import random
x = random.normal(size=(2,3))
print(x)



[[-0.77866503 -1.33779882  0.19983178]
 [-0.9313218  -0.39871487  0.69361272]]

'''
Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
'''
from numpy import random
x=random.normal(loc=1,scale=2,size=(2,3))
print(x)

'''
[[0.70741516 1.21784461 5.16363946]
 [2.86765672 4.83507049 1.75101342]]
'''

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot([0,1,2,3,4,5])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()


# VIOLINPLOT

import seaborn as sns
import matplotlib.pyplot as plt
sns.violinplot([0,1,2,3,4,5,6,7,8,9])
plt.show()


#BOXPLOT

import seaborn as sns
import matplotlib.pyplot as plt
sns.violinplot([0,1,2,3,4,5,6,7,8,9])
plt.show()




# Visualization of Poisson Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()