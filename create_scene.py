import math
import sys
from random import uniform, randint
import matplotlib.pyplot as plt
import numpy
import numpy as np
from scipy.spatial import ConvexHull

from collision_checking import check_polygons


def generate_random_polygon_vertices(num_vertices_range, scene_size, radius_range):
    vertices = []
    num_vertices = randint(*num_vertices_range)
    radius = randint(*radius_range)
    center = randint(radius, scene_size[0] - radius), randint(radius, scene_size[0] - radius)

    for _ in range(num_vertices):
        angle = uniform(0, 2 * math.pi)

        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        vertices.append((x, y))

    vertices.sort(key=lambda point: math.atan2(point[1] - center[1], point[0] - center[0]))

    return vertices  # , num_vertices, center, radius





if __name__ == "__main__":
    #input
    file = input("new file name, end it with .npy: ")
    num_polygons = int(input("Enter how many polygons: "))
    radius_min = int(input("radius minimum: "))
    radius_max = int(input("radius max: "))
    vert_min = int(input("vertex minimum: "))
    vert_max = int(input("vertex max: "))
    # Create a figure and axis
    fig, ax = plt.subplots(dpi=100)
    ax.set_aspect('equal')
    vertices_list = [generate_random_polygon_vertices(( vert_min, vert_max), (800, 800), (radius_min, radius_max)) for _ in range(num_polygons)]
    numpy_verticies = np.array(vertices_list, dtype=object)

    numpy.save(file,  numpy_verticies , allow_pickle=True, fix_imports=True)

    # Create a polygon patch using the generated vertices
    for i, vertices in enumerate(vertices_list):
        polygon = plt.Polygon(vertices, closed=True, edgecolor='teal',facecolor='none')
        ax.add_patch(polygon)

    # Add the polygon patch to the axis

    # Set axis limits
    ax.set_xlim(0, 800)
    ax.set_ylim(0, 800)

    # Display the plot
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    a = 1
