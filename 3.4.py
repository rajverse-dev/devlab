import matplotlib.pyplot as plt

a=[1,2,3,4,5]
b=[0,0.6,0.2,15,10,8,16,21]
c=[4,2,6,8,3,20,13,15]

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.plot(a,'sb')
plt.title("1st Rep")

plt.subplot(2,2,2)
plt.plot(b,'or')
plt.title("2nd Rep")

plt.subplot(2,2,3)
plt.plot(range(0,22,3),'vg')
plt.title("3rd Rep")

plt.subplot(2,2,4)
plt.plot(c,'Dm')
plt.title("4th Rep")

plt.show()
