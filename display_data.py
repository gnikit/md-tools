from PathHandling import *
from plotting_class import *


os.chdir('../../Archives of Data/')
obj = FilePlotting(10000, 1000)  # steps, particles

my_list = [0, 0.25, 0.50, 0.65, 0.7, 0.75, 0.8, 0.85, 0.90, 0.97, 1.00, 1.1, 1.2,
           1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 4.00]
a_list = [0.50, 0.75, 1.0, 1.25]
n_list = [6, 8, 10, 12]

# for i in n_list:
#     obj.rdf(1, 1, i, 0., iso_scale=False)
obj.potential_data(0.5, 0.5, 12, 0.5)

plt.show()
