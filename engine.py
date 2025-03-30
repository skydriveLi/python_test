import time

def calculate_force_F(target,now_status):
    kp=0.01
    err=target-now_status
    f=err*kp
    return f


m=1
g=10
u=0.1
v=10
dt=0.01
s=0
all_time=0
turn_off=True

aim_target=100

while turn_off:


    add_f=calculate_force_F(aim_target,s)

    f=0
    if v!=0:
        f=m*g*u*abs(v)/v*-1
    elif  add_f!=0:
        f=m*g*u*abs(add_f)/add_f*-1
        if abs(add_f)<abs(f):
            add_f=-1*f

    
    f=f+add_f

    a=f/m
    v0=v
    v=v+a*dt
    dt_=dt

    if v*v0<0:
        v=0
        dt_=abs(v0/a)

    s=s+ v0*dt_ + 0.5*a*dt_*dt_
    if dt_ > 0:
        time.sleep(dt_)
        all_time=all_time+dt_
    else:
        time.time(dt)
        all_time=all_time+dt
    print(f"\r time:{format(all_time,'4.4f')} {format(s,'4.8f')} {format(v,'4.8f')} {format(a,'4.8f')}",end="")

    if all_time>100:
        turn_off=False
