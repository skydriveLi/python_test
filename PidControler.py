
class PidControler:
    def __init__(self):
        self.pid_i=0#累计误差
        self.kp=0.1
        self.ki=0.0001
        
    def calculate_force_F(self,target,now_status):
        err=target-now_status
        self.pid_i=self.pid_i+err#计算累计误差
        f=err*self.kp+self.pid_i*self.ki
        return f