import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,200])
plt.plot(xpoints,ypoints)
plt.show()

#another one
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,8])
y = np.array([3,10])
plt.plot(x,y)
plt.show()

#Another one

import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,8])
y = np.array([3,10])
plt.plot(x,y,'o')
plt.show()

#
'''
Default X-Points
If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:
'''

import matplotlib.pyplot as plt
import numpy as np
y = np.array([1,2,3,4])
plt.plot(y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

# Line plot using matplot
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10])
plt.plot(ypoints)
plt.show()




import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()