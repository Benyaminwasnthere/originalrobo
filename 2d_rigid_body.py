import math
import sys
from random import uniform, randint
import matplotlib.pyplot as plt
import numpy
import numpy as np
from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt, patches
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

from collision_checking import print_scene, check_polygons

SCENE_X=800
SCENE_Y=800
ROBO_LEN = SCENE_X*0.2
ROBO_HEIGHT = SCENE_Y*0.1
STEP = 5

START = (0,600)


create_rectangle = lambda x,y: [(x, y), (x, y + ROBO_HEIGHT), (x + ROBO_LEN, y + ROBO_HEIGHT), (x + ROBO_LEN, y)]


print("2d_rigid_body.npy is the name to copy for tas")
file = input("file name: ")
polygons = np.load(file, allow_pickle=True)



fig, ax = plt.subplots(dpi=100)
ax.set_aspect('equal')

# Create a figure and axis





plt.xlim(0, SCENE_X)  # Set x-axis limits
plt.ylim(0, SCENE_Y)  # Set y-axis limits

def check_arm(arm_vert):
    polygon_no = polygons.shape[0]
    for i in range(polygon_no - 1):
        if check_polygons(arm_vert, polygons[i]):
            return True
    return False

def on_key(event):
    print(event.key)
    # Check if the pressed key is an arrow key
    if event.key in ['left', 'right', 'up', 'down']:
        # Get the current position of the text
        x, y = rectangle.get_xy()


        # Update the position based on the arrow key
        if event.key == 'left':
            x -= STEP
        elif event.key == 'right':
            x += STEP
        elif event.key == 'up':
            y += STEP
        elif event.key == 'down':
            y -= STEP

        arm_vert = create_rectangle(x,y)

        # Set the new position for the text
        if not check_arm(arm_vert):
            rectangle.set_xy((x, y))
            plt.draw()



print_scene(polygons,ax)

# Create a Rectangle patch
rectangle = patches.Rectangle(START, ROBO_LEN, ROBO_HEIGHT, fill=False,  edgecolor='blue')

# Add the rectangle to the plot
ax.add_patch(rectangle)

# Connect the key press event to the on_key function
fig.canvas.mpl_connect('key_press_event', on_key)

plt.show()
