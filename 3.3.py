import matplotlib.pyplot as plt

a=[1,2,3,4,5]
b=[0,0.6,0.2,15,10,8,16,21]
c=[4,2,6,8,3,20,13,15]

plt.plot(a)
plt.plot(b,"or")
plt.plot(range(0,22,3))
plt.plot(c,label="4th Rep")

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.legend()
plt.show()
