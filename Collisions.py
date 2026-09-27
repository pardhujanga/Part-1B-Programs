# Collision.py

import matplotlib . pyplot as plt
import matplotlib . animation as animation
import itertools
from matplotlib import rcParams
rcParams['animation.ffmpeg_path'] = r"C:\\Users\\pardh\\Dropbox\\My PC (LAPTOP-I599KVKH)\\Downloads\\ffmpeg-master-latest-win64-gpl\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
"""The above line needs to be modified according to the path to FFmpeg on the user's computer"""

class Canvas () :
    """ This class creates the canvas object . """
    def __init__ ( self ):
        """ With self you can access private attributes of
        the object."""
        self . size = 20
        self . blocks = []
        self . fig = plt . figure ()
        self . ax = self . fig . add_subplot ()

    def add_block ( self , block ):
        """ Every time a block is created it gets put into
        the array."""
        self . blocks . append ( block )

    def update_blocks ( self ):
        """ This method moves and draws all blocks . """
        self . ax . clear ()
        for i , block in enumerate ( self . blocks ):
            block . move ()
            block . draw ()

    def fix_axes ( self ):
        """ The axes would change with each iteration
        otherwise ."""
        self . ax . set_xlim (( - self . size /2 , self . size /2) )
        self . ax . set_ylim (( -1 , 1) )

    def check_collision ( self ) :
        """ This method checks if blocks are colliding . """
        combinations = list ( itertools . combinations (
        range (len ( self . blocks ) ) , 2) )

        for pair in combinations :
            self . blocks [ pair [0]].collide ( self . blocks [ pair [1]])

    def total_energy(self):
        """This method computes the total energy of the system"""
        total_energy = 0
        for i, block in enumerate ( self.blocks ):
            if block.inverse_mass != 0:
                total_energy += block.energy()
        total_energy = "{:.5f}".format(total_energy)
        plt.text(3,0.75, f"Total energy is {total_energy}", fontsize = 10)
        


class Block () :
    """ This class creates the block object . """
    def __init__ (self, canvas, inverse_mass, position =0, velocity =0) :
        self . canvas = canvas
        self . inverse_mass = inverse_mass
        self . position = position
        self . velocity = velocity
        # The block is automatically added to the canvas.
        self . canvas . add_block ( self )
        self . color = " black "

    def move ( self ) :
        """ The block is moved based on the velocity . """
        self . position = self . position + self . velocity

    def draw ( self ) :
        """ The method to draw the block . Note : if you don't
        specify color of the block the color of each new
        element that is plotted will be randomly asigned .
        """
        canvas.ax.plot(self.position, 0, " o")

    def energy (self):
        """ To compute the energy of a block"""
        return 0.5*(self.inverse_mass)**(-1)*(self.velocity)**2

    def collide (self, other):
        # Watch out with the threshold, this should
        # be greater than velocity. If, in a single
        # iteration, blocks move relatively more than
        # what is the threshold, the collision might
        # not be triggered.
        if abs (self.position - other.position) < 0.1:
            # The velocity after collision is derived from the conservaation of energy and momentum
            intial_velocity_self = self.velocity
            intial_velocity_other = other.velocity
            self.velocity = ((2*self.inverse_mass*intial_velocity_other) + (other.inverse_mass - self.inverse_mass)*intial_velocity_self)/(self.inverse_mass + other.inverse_mass) 
            other.velocity = ((2*other.inverse_mass*intial_velocity_self) + (self.inverse_mass - other.inverse_mass)*intial_velocity_other)/(self.inverse_mass + other.inverse_mass)


canvas = Canvas ()
Right_Wall = Block( canvas, inverse_mass = 0, position = -canvas.size/2, velocity = 0.01)
block1 = Block ( canvas , inverse_mass = 1 , position = -2 , velocity = 0.07)
block2 = Block ( canvas , inverse_mass = 1 , position = 0 , velocity = -0.09)
block3 = Block ( canvas , inverse_mass = 1 , position = 4 , velocity = -0.05)
block4 = Block ( canvas , inverse_mass = 1 , position = -5 , velocity = 0.09)
Left_Wall = Block( canvas, inverse_mass = 0, position = canvas.size/2, velocity = 0)


def animate (i):
    """ This controls the animation . """
    print (" The frame is : ", i)
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()
    canvas.total_energy()


# This calls the animate function and creates animation.
anim = animation.FuncAnimation ( canvas.fig, animate, frames =1000 , interval =10, repeat = False, save_count = 500)
writervideo = animation.FFMpegWriter(fps=60) 
anim.save("collisions.mp4", writer=writervideo, dpi =200)
