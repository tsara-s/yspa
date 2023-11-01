from vpython import *
import numpy as np

scene.camera.rotate(angle=pi/2, axis=vector(1,0,0))
scene.camera.rotate(angle=pi/2, axis=vector(0,0,1))

eclrad = 23.5*pi/180

# ring(pos=vector(1,1,1), axis=vector(0,1,0), radius=0.5, thickness=0.1)
equator = ring(axis=vector(0,0,1), color=vector(1,1,0), thickness=1, radius=100)

RA0 = ring(axis=vector(1,0,0), color=vector(0.5,0.2,0.75), thickness=1, radius=100)
RA6 = ring(axis=vector(0,1,0), color=vector(0.5,0.2,0.75), thickness=1, radius=100)    

ecliptic = ring(axis=vector(0,np.sin(eclrad)*pi/180,np.cos(eclrad)*pi/180), color=vector(0,1,0), thickness=1, radius=100)

# ecliptic = ring(axis=vector(0.016,0.00695,0), color=vector(0.5,1,0), thickness=1, radius=100)
ecliptic.rotate(angle=degrees(pi), axis=vector(1,0,0))
label( pos=vec(80,0,0), text='0h' )
label( pos=vec(-80,0,0), text='12h' )

label( pos=vec(0,80,0), text='6h' )
label( pos=vec(0,-80,0), text='18h' )

label( pos=vec(0,0,100), text='NCP' )
label( pos=vec(0,0,-100), text='SCP' ) 

NEP = arrow(axis=vector(0,-np.sin(eclrad)*pi/180,np.cos(eclrad)*pi/180), shaftwidth=5, length=100)
label(pos=vec(0,-40,90), text='NEP' )

earth = sphere(pos=vector(0,0,0), radius=100, opacity=0.25, color=vec(0.1,0.4,0.7))