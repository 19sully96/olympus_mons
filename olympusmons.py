
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# constants
g     = 3.71	# m s^-2
m     = 50.0	# kg
rho   = 0.20	# kg m^-3
C     = 0.47	# unitless
R     = 0.08    # m
h     = 0.001   # seconds
theta = 30.0*(np.pi/180) # radians
v0    = 10000.0	# m s^-1
const = (rho*C*np.pi*R**2)/(2.0*m)

# define the equations of motion
def f(r,const):
    x   = r[0]
    y   = r[1]
    vx  = r[2]
    vy  = r[3]
    fx  = vx
    fy  = vy
    fvx = -const*vx*np.sqrt(vx**2+vy**2)
    fvy = -g-const*vy*np.sqrt(vx**2+vy**2)
    return np.array([fx,fy,fvx,fvy],float)

# containers for output
r = np.array([0.0,0.0,v0*np.cos(theta),v0*np.sin(theta)],float)
xpoints = []
ypoints = []


# try different values of theta
p2 = plt.figure(2)
for angle in [10,16,22,28,34,40]:
    theta = angle*np.pi/180
    const = (rho*C*np.pi*R**2)/(2.0*m)
    r = np.array([0.0,0.0,v0*np.cos(theta),v0*np.sin(theta)],float)
    xpoints = []
    ypoints = []

    # use fourth-order Runge-Kutta
    while r[1]>=0:
        k1 = h*f(r,const)
        k2 = h*f(r+0.5*k1,const)
        k3 = h*f(r+0.5*k2,const)
        k4 = h*f(r+k3,const)
        r += (k1+2*k2+2*k3+k4)/6
        xpoints.append(r[0])
        ypoints.append(r[1])

    plt.plot(xpoints,ypoints,label=str(angle)+' deg')

plt.xlabel("x [m]")
plt.ylabel('y [m]')
plt.title('Mars')
plt.legend()
plt.show()
p2.savefig('olympus.png')

