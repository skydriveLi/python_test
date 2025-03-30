import time

def calculate_force_F(target,now_status):
    err=target-now_status


m=1
g=10
u=0.1
v=1
dt=0.01
s=0
all_time=0
turn_off=True
while turn_off:
    f=0
    if v!=0:
        f=m*g*u*abs(v)/v*-1
    a=f/m
    v0=v
    v=v+a*dt
    dt_=dt

    if v*v0<0:
        v=0
        dt_=abs(v0/a)

    s=s+ v0*dt_ + 0.5*a*dt*dt_
    if dt_ > 0:
        time.sleep(dt_)
        all_time=all_time+dt_
    else:
        time.time(dt)
        all_time=all_time+dt
    print(f"\r time:{format(all_time,'4.4f')} {s} {v} {a}",end="")

    if all_time>10:
        turn_off=False
