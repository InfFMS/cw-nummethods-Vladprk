import matplotlib.pyplot as plt
a = 0.1382
b = 3.19*10**-5
R = 8.314
T1 = -140 + 273.15
T2 = -130 + 273.15
T3 = -120 + 273.15
T4 = -110 + 273.15
T5 = -100 + 273.15
P1 = []
P2 = []
P3 = []
P4 = []
P5 = []
V_mas = []
V = b + 10**-5
col1 = 'red'
col2 = 'red'
col3 = 'red'
col4 = 'red'
col5 = 'red'
while V < 10**-3:
    V_mas.append(V)
    p1 = R * T1 / (V - b) - a / V ** 2
    p2 = R * T2 / (V - b) - a / V ** 2
    p3 = R * T3 / (V - b) - a / V ** 2
    p4 = R * T4 / (V - b) - a / V ** 2
    p5 = R * T5 / (V - b) - a / V ** 2
    P1.append(p1)
    P2.append(p2)
    P3.append(p3)
    P4.append(p4)
    P5.append(p5)
    try:
        if P1[-1] > P1[-2]:
            col1 = 'blue'
    except:pass
    try:
        if P2[-1] > P2[-2]:
            col2 = 'blue'
    except:pass
    try:
        if P3[-1] > P3[-2]:
            col3 = 'blue'
    except:pass
    try:
        if P4[-1] > P4[-2]:
            col4 = 'blue'
    except:pass
    try:
        if P5[-1] > P5[-2]:
            col5 = 'blue'
    except:pass
    V += 10**-6

if col1 == 'red':
    col2, col3, col4, col5 = 'blue', 'blue', 'blue', 'blue'
elif col2 == 'red':
    col3, col4, col5 = 'blue', 'blue', 'blue'
elif col3 == 'red':
    col4, col5 = 'blue', 'blue'
elif col4 == 'red':
     col5 = 'blue'

fig, ax = plt.subplots(1, 5)
ax[0].plot(V_mas, P1, label='T1', color=col1)
ax[1].plot(V_mas, P2, label='T2', color=col2)
ax[2].plot(V_mas, P3, label='T3', color=col3)
ax[3].plot(V_mas, P4, label='T4', color=col4)
ax[4].plot(V_mas, P5, label='T5', color=col5)

while V > b + 10**-5:
    V_mas.append(V)
    P1.append(R * T1 / (V - b) - a / V ** 2)
    P2.append(R * T2 / (V - b) - a / V ** 2)
    P3.append(R * T3 / (V - b) - a / V ** 2)
    P4.append(R * T4 / (V - b) - a / V ** 2)
    P5.append(R * T5 / (V - b) - a / V ** 2)
    V -= 10**-6


def f(V):
    return R * T2 / (V - b) - a / V ** 2


B = b + 10**-5
A = 10**-3
while B - A > 10**-6:
    mid1 = A + (B-A)/3
    mid2 = B - (B-A)/3
    if f(mid1) < f(mid2):
        B = mid2
    else:
        A = mid1

min = plt.Circle((A, f(A)), 5*10**-5, facecolor='#3aab17')
ax[1].add_patch(min)


plt.show()


