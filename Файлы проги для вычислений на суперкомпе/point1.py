Nup = 2
num = 1
import pyalps

parms = [ {
           'LATTICE'                   : "open square lattice",
           'MODEL'                     : "fermion Hubbard",
           'CONSERVED_QUANTUMNUMBERS'  : 'Nup, Ndown',
           'Nup_total'                  : 1,
           'Ndown_total'                  : 1,
           't'                         : 1,
           'U'                         : -7,
           'SWEEPS'                    : 12,
           'NUMBER_EIGENVALUES'        : 2,
           'L'                         : 40,
           'W'                         : 2,
           'MAXSTATES'                 : 600
          } ]
# e4 = E(Nup, 0)
# e5 = E(Nup + 1, 1)
# e6 = E(Nup - 1, 1)
f = list()
g = list()
i = list()
e4 = list()
e5 = list()
e6 = list()

file_name1 = 'e4-' + str(num)
file_name2 = 'e5-' + str(num)
file_name3 = 'e6-' + str(num)

#e4
parms[0]['Nup_total'] = Nup
parms[0]['Ndown_total'] = 0

input_file = pyalps.writeInputFiles(file_name1, parms)
res = pyalps.runApplication('dmrg', input_file, writexml=True)

data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=file_name1))
for s in data[0]:
    f.append(s.y[0])

for m in range(0, len(f), 2):
    e4.append(f[m])

print(f)
# e5
parms[0]['Nup_total'] = Nup + 1
parms[0]['Ndown_total'] = 1

input_file = pyalps.writeInputFiles(file_name2, parms)
res = pyalps.runApplication('dmrg', input_file, writexml=True)

data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=file_name2))
for s in data[0]:
    g.append(s.y[0])

for q in range(0, len(g), 2):
    e5.append(g[q])

print(g)
#e6
parms[0]['Nup_total'] = Nup - 1
parms[0]['Ndown_total'] = 1

input_file = pyalps.writeInputFiles(file_name3,parms)
res = pyalps.runApplication('dmrg',input_file,writexml=True)

data = pyalps.loadEigenstateMeasurements(pyalps.getResultFiles(prefix=file_name3))
for s in data[0]:
    i.append(s.y[0])


for d in range(0, len(i), 2):
    e6.append(i[d])

print(i)

h2 = list()
h2.append((e6[0] - e4[0]) / (-2))
print(h2)

mu2 = list()
mu2.append((e5[0] - e4[0]) / 2)
print(mu2)



en = 'point' + str(num) + ' ' + str(f) + ', ' + str(g) + ', ' + str(i) + '\n'
stroka = 'point' + str(num) + ' ' + str(mu2) + ', ' + str(h2) + '\n'

result_mu_h = open('result-W=2.txt', 'a')
for x in stroka:
    result_mu_h.write(x)
result_mu_h.close()

result = open('result-energy-W=2.txt', 'a')
for y in en:
    result.write(y)
result.close()
