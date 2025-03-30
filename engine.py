import time

m=1
g=10
u=0.1
v=1
dt=0.01
s=0
turn_off=True
while turn_off:
    f=0
    if v!=0:
        f=m*g*u*abs(v)/v*-1
    a=f/m
    v0=v
    v=v+a*dt
    s=s+ v0*dt + 0.5*a*dt*dt
    print(f"\r{s} {v} {a}")
    time.sleep(0.01)
