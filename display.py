#import matplotlib.pyplot as plt
#plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()
figure, ax = plt.subplots()

# data here
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))

ax.barh(y_pos, performance, align='center', 
	color='green', ecolor='blue')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()