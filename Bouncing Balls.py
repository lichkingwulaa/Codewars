def bouncingBall(h, bounce, window):
    if h<= 0 or bounce>0 or bounce<1 or window >= h:
        return -1
    

x = bouncingBall(30, 0.66, 1.5)
print(x)