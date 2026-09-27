import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
rcParams['animation.ffmpeg_path'] = r"C:\\Users\\pardh\\Dropbox\\My PC (LAPTOP-I599KVKH)\\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
"""The above line needs to be modified according to the path to FFmpeg on the user's computer"""

total_AM_list = [] #list to hold values for angular momentum

class SolarSystem():
    def __init__(self):
        self.size = 600
        self.planets = []
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.dT = 1

    def add_planet(self, planet):
        self.planets.append(planet)

    def update_planets(self):
        self.ax.clear()
        for planet in self.planets:
            planet.move()
            planet.draw()

    def fix_axes(self):
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        self.ax.set_zlim((-self.size/2, self.size/2))

    def gravity_planets(self):
        for i, first in enumerate(self.planets):
            for second in self.planets[i+1:]:
                first.gravity(second)

    def total_angular_momentum(self):
        """This method computes the total angular momentum of the system and displays on graph"""
        total_angular_momentum = 0
        for i, planet in enumerate(self.planets):
            total_angular_momentum += planet.angular_momentum()
        total_AM_list.append("{:.5f}".format(total_angular_momentum))

class Planet():
    def __init__(self, SolarSys, mass, color,position=(0, 0, 0), velocity=(0, 0, 0)):
        self.SolarSys = SolarSys
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.SolarSys.add_planet(self)
        self.color = color
        

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0] * self.SolarSys.dT,
            self.position[1] + self.velocity[1] * self.SolarSys.dT,
            self.position[2] + self.velocity[2] * self.SolarSys.dT
        )

    def draw(self):
        self.SolarSys.ax.plot(
            *self.position,
            marker="o",
            markersize=10,
            color=self.color
        )

    def gravity(self, other):
        distance = np.subtract(other.position, self.position)
        distanceMag = np.linalg.norm(distance)
        distanceUnit = np.divide(distance, distanceMag)
        forceMag = self.mass * other.mass / (distanceMag ** 2)
        force = np.multiply(distanceUnit, forceMag)

        acceleration = np.divide(force, self.mass)
        velocity_change = acceleration * SolarSys.dT
        self.velocity = np.add(self.velocity, velocity_change)
        
    def angular_momentum (self):
        """ To compute the energy of a block"""
        return np.linalg.norm((self.mass)*np.cross(self.position,self.velocity))

SolarSys = SolarSystem()

planet1 = Planet(SolarSys, mass=10, color = "blue", position=(150, 50, 0), velocity=(0, 5, 5))
planet2 = Planet(SolarSys, mass=10, color = "green" ,position=(100, -50, 150), velocity=(5, 0, 0))
planet3 = Planet(SolarSys, mass=10, color = "red", position=(-100, -50, 150), velocity=( -4 , 0, 0))
sun = Planet(SolarSys, mass=10000, color = "yellow",position=(0, 0, 0), velocity=(0, 0, 0))

def animate(i):
    print("The frame is:", i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()
    SolarSys.total_angular_momentum()

frames = 200
anim = animation.FuncAnimation(SolarSys.fig, animate, frames=frames, interval=100, repeat = False)
writervideo = animation.FFMpegWriter(fps=60) 
anim.save("Planets.mp4", writer=writervideo, dpi =200)


