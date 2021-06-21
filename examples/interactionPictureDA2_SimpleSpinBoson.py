import numpy as np
from fishbonett.backwardSpinBoson import SpinBoson, SpinBoson1D, calc_U
from fishbonett.stuff import sigma_x, sigma_z, temp_factor, drude, _num, sigma_1
from time import time

bath_length = 200
phys_dim = 20
bond_dim = 1000
# a = [np.ceil(phys_dim - N*(phys_dim -2)/ bath_length) for N in range(bath_length)]
# a = [int(x) for x in a]

coup_num_CT1 = [38.46, 72.311, 11.494, 47.86, 12.09, 0.849, 51.231, 21.473, 19.948, 48.151, 8.679, 9.756, 35.145, 153.036, 5.57, 40.536, 103.972, 5.818, 342.326, 13.021, 10.055, 141.056, 1.881, 116.853, 115.694, 252.834, 548.3, 65.941, 101.2, 36.225, 98.895, 92.174, 162.691, 616.784, 64.987, 78.485, 17.11, 120.011, 10.718, 34.215, 61.117, 32.832, 16.505, 226.052, 31.559, 90.014, 21.722, 7.258, 34.631, 20.893, 43.818, 31.975, 241.635, 70.762, 214.506, 11.932, 15.302, 21.408, 16.794, 2.77, 376.122, 34.984, 6.195, 32.932, 75.081, 3.834, 21.297, 24.008, 80.191, 42.642, 89.863, 81.553, 43.611, 10.422, 42.857, 56.983, 0.661, 3.384, 2.738, 14.583, 17.196, 82.183, 47.897, 92.892, 382.607, 291.109, 12.722, 16.206, 25.91, 420.19, 29.549, 146.078, 20.106, 2.34, 16.628, 21.517, 426.757, 323.967, 286.112, 25.91, 400.871, 52.487, 174.991, 38.737, 35.419, 12.13, 86.247, 94.2, 19.449, 22.77, 15.812, 5.45, 1.102, 37.923, 37.888, 84.635, 90.901, 75.211, 13.869, 93.847, 35.146, 68.165, 42.751, 753.441, 21.858, 48.053, 142.031, 74.684, 52.455, 433.424, 50.633, 23.385, 78.42, 356.246, 3.832, 138.629, 101.504, 139.002, 55.17, 178.021, 12.598, 96.089, 1432.882, 1267.181, 5.739, 12.009, 99.554, 10.677, 118.769, 28.353, 119.251, 23.571, 9.043, 3.54, 56.876, 30.271, 143.977, 306.607, 215.583, 529.784, 97.707, 347.676]
coup_num_CT2 = [27.903, 3.446, 8.751, 97.112, 2.367, 16.221, 21.127, 4.089, 9.8, 53.85, 9.539, 2.658, 14.28, 93.328, 36.15, 35.214, 83.901, 7.898, 206.299, 7.536, 11.734, 43.621, 23.216, 32.49, 21.092, 51.2, 389.195, 123.651, 46.271, 116.504, 68.044, 1.589, 22.347, 298.773, 233.808, 196.414, 141.069, 72.065, 17.539, 43.359, 10.472, 10.073, 0.793, 97.259, 2.879, 16.2, 23.902, 7.614, 23.322, 131.83, 79.468, 10.502, 197.881, 77.625, 15.3, 0.254, 22.512, 51.787, 36.209, 14.489, 304.309, 1.888, 43.567, 3.366, 112.696, 0.357, 37.041, 38.421, 0.198, 2.45, 21.41, 43.089, 21.001, 0.497, 46.014, 44.995, 3.207, 6.186, 15.314, 5.517, 15.036, 53.366, 13.925, 40.879, 75.714, 272.283, 23.453, 10.822, 29.544, 189.982, 6.249, 27.779, 29.086, 6.198, 4.85, 37.511, 80.667, 245.497, 195.082, 12.643, 409.21, 57.47, 42.138, 24.887, 37.268, 12.675, 54.768, 11.292, 21.166, 9.36, 28.028, 18.198, 26.349, 30.2, 109.602, 9.051, 87.308, 53.483, 28.217, 58.232, 52.758, 91.358, 17.084, 923.816, 58.416, 55.906, 147.216, 23.844, 77.403, 393.996, 72.497, 8.505, 92.573, 369.584, 26.026, 82.665, 60.873, 91.46, 9.103, 144.702, 48.965, 62.267, 430.593, 1924.126, 1.879, 14.06, 9.052, 7.353, 3.002, 34.868, 36.786, 17.462, 15.645, 29.996, 36.256, 30.924, 24.971, 89.706, 3.417, 87.497, 27.459, 116.318]
freq_num = [16.249, 19.846, 35.653, 49.588, 57.673, 59.44, 60.057, 80.532, 85.923, 90.577, 111.945, 127.501, 141.613, 159.92, 193.66, 209.691, 238.118, 240.834, 270.594, 283.862, 287.039, 292.279, 300.843, 310.603, 355.737, 365.576, 405.085, 410.111, 415.261, 430.542, 435.183, 458.307, 465.436, 471.099, 478.408, 490.04, 518.135, 520.897, 525.63, 528.007, 556.408, 582.042, 591.525, 607.027, 613.02, 614.041, 618.992, 623.606, 636.531, 646.442, 677.633, 680.406, 691.537, 719.182, 732.211, 746.345, 746.737, 753.18, 768.546, 777.369, 778.911, 805.667, 817.151, 824.069, 827.332, 837.136, 859.594, 870.441, 878.217, 882.167, 883.447, 891.352, 895.106, 917.105, 922.729, 936.318, 945.27, 947.327, 962.695, 970.26, 971.992, 976.544, 998.449, 1004.578, 1016.13, 1028.409, 1043.473, 1045.956, 1074.587, 1078.306, 1082.563, 1116.653, 1123.052, 1125.876, 1139.078, 1150.564, 1154.377, 1167.874, 1173.031, 1183.676, 1199.643, 1209.393, 1213.868, 1227.811, 1238.084, 1238.937, 1243.64, 1254.306, 1286.735, 1298.122, 1303.0, 1320.062, 1324.757, 1329.949, 1342.895, 1356.404, 1377.9, 1380.408, 1387.469, 1389.685, 1421.035, 1423.662, 1445.401, 1453.921, 1467.516, 1479.636, 1491.142, 1515.203, 1531.046, 1563.043, 1564.287, 1608.664, 1632.35, 1636.418, 1643.163, 1679.803, 1681.104, 1696.021, 1715.921, 1733.36, 1761.317, 1770.266, 1815.073, 1948.134, 3184.027, 3184.905, 3185.911, 3193.894, 3194.837, 3201.169, 3205.093, 3205.691, 3206.991, 3208.301, 3208.422, 3216.61, 3220.436, 3220.87, 3224.797, 3224.912, 3235.545, 3236.148]
# low_freq_num = 0
# freq_num = freq_num[low_freq_num:]
# coup_num = coup_num[low_freq_num:]

a = [phys_dim]*bath_length
print(a)

pd = a[::-1] + [3]
eth = SpinBoson(pd)
etn = SpinBoson1D(pd)
# set the initial state of the system. It's in the high-energy state |0>:
etn.B[-1][0, 2, 0] = 0.
etn.B[-1][0, 1, 0] = 0.
etn.B[-1][0, 0, 0] = 1.


# spectral density parameters
g = 3500
eth.domain = [-g, g]
# temp = 226.00253972894595*0.5*1
temp = 295

def lorentzian (w, wi, delta, ki):
    return np.pi * (ki**2/np.pi/wi) * w * delta/((w-wi)**2 + delta**2)

j = lambda w: sum([lorentzian(w, wi=freq_num[n], delta=107, ki=coup_num_CT1[n]) for n in range(len(freq_num))])*temp_factor(temp,w)

# j_list = np.array([j(w) for w in range(1, 3000,30)])
# print(repr(j_list))

eth.sd = j

eth.he_dy = np.diag([0, 0.66517 ,1])
eth.h1e =  np.diag([0, -3213.31478+2481.76604, -5136.09683+ 3731.16273]) + np.array(
      [[             0,  -144.84282895,   -67.96758061],
       [ -144.84282895,              0,   575.79158116],
       [  -67.96758061,   575.79158116,               0]])

eth.build(g=1., ncap=20000)
# print(eth.w_list,eth.k_list)
#
# print(len(eth.w_list))
# exit()

# b = np.array([np.abs(eth.get_dk(t=i*0.2/100)) for i in range(1)])
# bj, freq, coef = eth.get_dk(1, star=True)
# indexes = np.abs(freq).argsort()
# bj = bj[indexes]
# bj = np.array(bj)
# print(b.shape)
# b.astype('float32').tofile('./DA2/dk.dat')
# bj.astype('float32').tofile('./output/j0.dat')
# freq.astype('float32').tofile('./output/freq.dat')
# coef.astype('float32').tofile('./DA2/coef.dat')
# print(coef.shape)
# print(repr(freq))
# print(repr(bj))


print(eth.w_list)
print(eth.k_list)


# U_one = eth.get_u(dt=0.002, t=0.2)

# ~ 0.5 ps ~ 0.1T
p = []


threshold = 1e-3
dt = 0.001/4
num_steps = 50*4

s_dim = np.empty([0,0])
num_l = np.empty([0,0])
t = 0.
tt0=time()
for tn in range(num_steps):
    U1, U2 = eth.get_u(2*tn*dt, 2*dt, factor=2)

    t0 = time()
    etn.U = U1
    for j in range(bath_length-1,0,-1):
        print("j==", j, tn)
        etn.update_bond(j, bond_dim, threshold, swap=1)

    etn.update_bond(0, bond_dim, threshold, swap=0)
    etn.update_bond(0, bond_dim, threshold, swap=0)
    t1 = time()
    t = t + t1 - t0

    t0 = time()
    etn.U = U2
    for j in range(1, bath_length):
        print("j==", j, tn)
        etn.update_bond(j, bond_dim, threshold,swap=1)

    dim = [len(s) for s in etn.S]
    s_dim = np.append(s_dim, dim)
    print("Length", len(dim))
    theta = etn.get_theta1(bath_length) # c.shape vL i vR
    rho = np.einsum('LiR,LjR->ij',  theta, theta.conj())
    sigma_LE = np.diag([1,0,0])

    pop = np.einsum('ij,ji', rho, sigma_LE)
    p = p + [pop]
    t1 = time()
    t = t + t1 - t0
    numExp = []
    for i, pd in enumerate(a[::-1]):
        theta = etn.get_theta1(i)
        rho = np.einsum('LiR,LjR->ij', theta, theta.conj())
        numExp.append(np.einsum('ij,ji', rho, _num(pd)).real)
    num_l = np.append(num_l, numExp)
tt1 = time()
print(tt1-tt0)
pop = [x.real for x in p]
print("population", pop)
pop = np.array(pop)

s_dim.astype('float32').tofile('./DA2/dim.dat')
pop.astype('float32').tofile('./DA2/pop.dat')
num_l.astype('float32').tofile('./DA2/num_ic.dat')