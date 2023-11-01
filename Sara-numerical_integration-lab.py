# 7-19 numerical integration lab

from vpython import *
import numpy as np


# box(size=vector(4,0.1,0.1))
# ball=sphere(pos=vector(-2,0.5,0), vel=vector(0,0,0), radius=0.4,
#             make_trail=True)
# dt=0.1
# t=0
# 
# while t<9:
#     acc=vector(0.1,0,0)
#     ball.vel+=acc*dt
#     ball.pos+=ball.vel*dt
#     t+=dt
#     rate(20)


G = 8.89e-10
dt=0.05
t=0
v0e = np.sqrt(333030*G)
v0m = np.sqrt(0.0012*G/0.002510)

# v = 0.0174
F = 0.00296
m2e_AU = 0.002510 
v0x = -2*pi*m2e_AU/28.5

earth = sphere(pos=vector(1,0,0), vel=vector(0,v0e,0), radius=0.05,
            make_trail=True, color=vec(0,0.7,1))
sun = sphere(pos=vector(0,0,0), vel=vector(0,0,0), radius=0.2,
            make_trail=True, color=vec(1,0.8,0.5))


moonpos = vec(1, m2e_AU,0)
moon = sphere(pos=moonpos, vel=vector(v0x,0.0174,0), radius=0.01,
            make_trail=True, color=vec(1,0.2,0.5))
# 

def accel(x,m):
    return x/mag(x)**3 * G*m



while t<100000000:
    epos = earth.pos
    spos = sun.pos
    mpos = moon.pos
    
    r0_se = spos - epos
    r0_sm = mpos-spos
    r0_em = mpos-epos
    
    eacc=accel(r0_se,333030) - accel(-r0_em, 0.012)
    earth.vel+=eacc*dt
    earth.pos+=earth.vel*dt
    
    
    sacc=accel(-r0_se, 1) - accel(-r0_sm, 0.012)
    sun.vel+=sacc*dt
    sun.pos+=sun.vel*dt

    
    macc= -1*accel(r0_sm, 333030) - accel(r0_em, 1)
    print(macc) 
    moon.vel+=macc*dt
    moon.pos+=moon.vel*dt

    
    t+=dt
    
    rate(1000000)
