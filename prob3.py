#
# (c) 2023 Michael Fitzgerald (mpfitz@ucla.edu)
#
# Some code for querying Vizier for catalog to construct a CMD.
#


from astroquery.vizier import Vizier

catalog_name = "J/AJ/133/1658/acssggc" 
cluster_name = "NGC 7089"
Vizier.ROW_LIMIT = 100
Vizier.ROW_LIMIT = 1000
Vizier.ROW_LIMIT = -1 # get all sources
result = Vizier.query_constraints(Cluster = cluster_name, catalog = catalog_name)
#print(result[0].colnames)

# parse the result to get the source list

data = result[0]
vi = data['V-I']
vmag = data['Vmag']


# plot the color-magnitude diagram
import matplotlib as mpl
import pylab
fig = pylab.figure(0)
fig.clear()
ax = fig.add_subplot(111)

ax.scatter(vi, vmag,
           marker='.',
           c='k',
           s=1., # experiment with marker size
           )

# plot title and axes labels
ax.set_xlabel('V - I')
ax.set_ylabel('V (mag)')
ax.set_title('Color Magnitude Diagram for M2')
# invert the y axis
ax.invert_yaxis()

pylab.draw()
pylab.show()
fig.savefig('hw4prob2.pdf', dpi=300)

