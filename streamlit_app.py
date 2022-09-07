
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["animation.html"] = "jshtml"
plt.rcParams['figure.dpi'] = 150  
plt.ioff()

fig = plt.figure()

def animate(k):
    plt.cla()
    t = 0.1*k

    plt.scatter(186.64*t, 50*t - 0.5*10*t**2)#para 15graus (50/tg15=vox)
    plt.scatter(86.61*t, 50*t - 0.5*10*t**2)#para 30 graus (50/tg30=vox)
    plt.scatter(50*t, 50*t - 0.5*10*t**2)#para 45 graus (50/tg45=vox)
    plt.scatter(28.867*t, 50*t - 0.5*10*t**2)#para 60 graus (50/tg60=vox)
    plt.scatter(13.397*t, 50*t - 0.5*10*t**2)#para 75 graus (50/tg75=vox)
    
    plt.xlim(0,2000)
    plt.ylim(0,500)

anim = matplotlib.animation.FuncAnimation(fig, animate, frames=100, interval=10)
# to save the animation, uncomment the following three lines
f = r"Animacao.mp4" 
writervideo = matplotlib.animation.FFMpegWriter(fps=60) 
anim.save(f, writer=writervideo,dpi =150)
