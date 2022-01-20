import numpy as np
import matplotlib.pyplot as plt

#mass of the lens
#M=10. #Msun
#distance of the source
#DS=8. #kpc
#distance of the lens
#DL=4. #kpc
#relative parallax
#pirel=1./DL - 1./DS
#Einstein Radius in [mas]
#thetaE=np.sqrt(8.144*M*pirel)
#angular distance of the source from the lens
#beta = 10 #mas

#### 1st part

thetaE=1
r = 0.1

j=20
xs = np.linspace(-2, 2, j)
ys = np.linspace(2, -1, j)
x = np.zeros(360)
y = np.zeros(360)

fig, ax = plt.subplots(figsize=(10,10))
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("[R_E]")
plt.ylabel("[R_E]")
plt.grid(linestyle='--')
ax.set_aspect(1)
circle = plt.Circle((0,0), thetaE, color='b', Fill=False, ls="--")
ax.add_artist(circle)
plt.scatter(0, 0, c='b', marker='x')

for k in range(j):
  for i in range(360):
    x[i] = xs[k] + r * np.cos(i)
    y[i] = ys[k] + r * np.sin(i)
    beta = np.sqrt( x ** 2 + y ** 2) #mas
    sin = y / beta
    cos = x / beta
    im1 = 0.5 * (beta + np.sqrt(beta ** 2 + 4 * thetaE ** 2))
    im2 = 0.5 * (beta - np.sqrt(beta ** 2 + 4 * thetaE ** 2))
    im1x = im1*cos
    im1y = im1*sin
    im2x = im2*cos
    im2y = im2*sin
    plt.scatter(x, y, c='r', marker='.')
    plt.scatter(im1x, im1y, c='g', marker='.')
    plt.scatter(im2x, im2y, c='blue', marker='.') 

plt.savefig('fig1.png')
plt.show()


#### 2nd part

thetaE = 1
for i in np.linspace(0.5, 1.5, 5):
  j=100
  x = np.linspace(-2, 2, j)
  y = np.linspace(i, i, j)

  beta = np.sqrt( x ** 2 + y ** 2) #mas
  sin = y/beta
  cos = x/beta
  im1 = 0.5 * (beta + np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im2 = 0.5 * (beta - np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im1x = im1*cos
  im1y = im1*sin
  im2x = im2*cos
  im2y = im2*sin 

  mi1 = (1 - (thetaE / im1) ** 4) ** (-1)
  mi2 = (1 - (thetaE / im2) ** 4) ** (-1)
  mitot = (np.abs(mi1) + np.abs(mi2))
  plt.plot(x, mitot, label="u = %.2f" % i)
plt.xlabel("time/$t_E$")
plt.ylabel("A")
plt.legend()
plt.savefig("krzywapacz.jpg")
plt.show()


plt.plot(x, beta)
plt.xlabel("x")
plt.ylabel("beta")
plt.show()



#### 3rd Part

#j=20
#x = np.zeros(j*360)
#y = np.zeros(j*360)
#xs = np.linspace(-7, 7, j)
#ys = np.linspace(4, -2, j)
#r = 0.2
#for k in range(j):
#  for i in range(360):
#    x[360 * k+i] = xs[k] + r * np.cos(i)
#    y[360 * k+i] = ys[k] + r * np.sin(i)
fig, ax = plt.subplots(figsize=(10,10))
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("[mas]")
plt.ylabel("[mas]")
plt.grid(linestyle='--')
ax.set_aspect(1)

circle = plt.Circle((0,0), thetaE, color='b', Fill=False, ls="--")
ax.add_artist(circle)

j = 1
plt.scatter(0, 0, c='b', marker='x')
xs = np.linspace(-0.5, 0, j)
ys = np.linspace(0.1, 0, j)
scale = 1 #2*16do serca
thetaE = 1

for i in range(j):
#serduszka
#  k=1
#  x = np.zeros(365*k)
#  y = np.zeros(365*k)
#  for t in range(365*k):
#    x[t] = 16 * np.sin(t/k) ** 3
#    y[t] = 13 * np.cos(t/k) - 5 * np.cos(2 * t/k)  - 2 * np.cos(3 * t/k) - np.cos(4 * t/k)

# litera P
  x = np.zeros(400)
  y = np.zeros(400)
  k=np.linspace(-1, 1, 100)
  for j in range(100):
    x[j] = 0
    y[j] = k[j]

  k=np.linspace(0, 0.5, 50)
  for j in range(50):
    x[j+100] = k[j]
    y[j+100] = 1    

  k=np.linspace(0, 0.5, 50)
  for j in range(50):
    x[j+150] = k[j]
    y[j+150] = 0

  k=np.linspace(0.5, 1, 100)
  for j in range(100):
    x[j+200] = k[j]
    y[j+200] = 0.5 + np.sqrt(0.25 - (x[j+200] - 0.5) ** 2)

  k=np.linspace(0.5, 1, 100)
  for j in range(100):
    x[j+300] = k[j]
    y[j+300] = 0.5 - np.sqrt(0.25 - (x[j+200] - 0.5) ** 2)

  x = x / scale + xs[i]
  y = y / scale + ys[i]
  beta = np.sqrt( x ** 2 + y ** 2) #mas
  sin = y/beta
  cos = x/beta
  im1 = 0.5 * (beta + np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im2 = 0.5 * (beta - np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im1x = im1*cos
  im1y = im1*sin
  im2x = im2*cos
  im2y = im2*sin
  plt.scatter(x, y, c='r', marker='o')
  plt.scatter(im1x, im1y, c='g', marker='.')
  plt.scatter(im2x, im2y, c='blue', marker='.')

plt.show()


#### 4th part
fig, ax = plt.subplots(figsize=(10,10))
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("[mas]")
plt.ylabel("[mas]")
plt.grid(linestyle='--')
ax.set_aspect(1)

circle = plt.Circle((0,0), thetaE, color='b', Fill=False, ls="--")
ax.add_artist(circle)

j = 9
plt.scatter(0, 0, c='b', marker='x')
xs = np.linspace(-2, 2, j)
ys = np.linspace(1.5, -0.5, j)
scale = 5*16
thetaE = 1

for i in range(j):
#serduszka
  k=1
  x = np.zeros(365*k)
  y = np.zeros(365*k)
  for t in range(365*k):
    x[t] = 16 * np.sin(t/k) ** 3
    y[t] = 13 * np.cos(t/k) - 5 * np.cos(2 * t/k)  - 2 * np.cos(3 * t/k) - np.cos(4 * t/k)



  x = x / scale + xs[i]
  y = y / scale + ys[i]
  beta = np.sqrt( x ** 2 + y ** 2) #mas
  sin = y/beta
  cos = x/beta
  im1 = 0.5 * (beta + np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im2 = 0.5 * (beta - np.sqrt(beta ** 2 + 4 * thetaE ** 2))
  im1x = im1*cos
  im1y = im1*sin
  im2x = im2*cos
  im2y = im2*sin
  plt.scatter(x, y, c='r', marker='o')
  plt.scatter(im1x, im1y, c='g', marker='.')
  plt.scatter(im2x, im2y, c='blue', marker='.')

plt.show()
