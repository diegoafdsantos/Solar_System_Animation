import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
semi_major_axis = [0.39, 0.72, 1.0, 1.52, 5.2, 9.58, 19.22, 30.05]  # in AU (astronomical units)
orbit_period = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]  # in years
planet_diameters = [4879, 12104, 12756, 6792, 139820, 116460, 50724, 49244]  # Diameters in kilometers

# Normalize sizes for better visualization
max_diameter = max(planet_diameters)
normalized_sizes = [(diameter / max_diameter) * 100 for diameter in planet_diameters]  # Scale for plotting

colors = ['gray', 'orange', 'blue', 'red', 'brown', 'gold', 'lightblue', 'darkblue']  # Colors for planets

# Create a larger figure without excessive white space
fig = plt.figure(figsize=(30, 30))  # Adjust figure size
plt.style.use('dark_background')
ax = fig.add_subplot(111, projection='3d')

# Initialize planet positions
planet_positions = [ax.scatter([], [], [], color=colors[i], s=normalized_sizes[i]) for i in range(len(planet_names))]

# Plot the orbits and add legend entries for each orbit
for i, planet in enumerate(planet_names):
    orbit_radius = semi_major_axis[i]
    orbit_theta = np.linspace(0, 2 * math.pi, 100)
    x = orbit_radius * np.cos(orbit_theta)
    y = orbit_radius * np.sin(orbit_theta)
    z = np.zeros_like(x)
    ax.plot(x, y, z, color=colors[i], alpha=0.5, label=f'{planet} Orbit')  # Plot the orbit line with label

# Set up the axes limits to ensure visibility
ax.set_xlim([-25, 25])  # Adjusted X limit
ax.set_ylim([-25, 25])  # Adjusted Y limit
ax.set_zlim([-5, 5])  # Adjusted Z limit for better visibility
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')

# Add title as text
ax.text2D(0.5, 0.95, 'Solar System Visualization', transform=ax.transAxes, fontsize=15, ha='center', color='white')

# Adjust the viewing angle for better perspective
ax.view_init(elev=30, azim=30)

# Add legends for orbits only
ax.legend(loc='upper right')

# Animation function
def update(frame):
    for i, planet in enumerate(planet_names):
        orbit_radius = semi_major_axis[i]
        # Calculate the planet's position based on the current frame
        planet_position_x = orbit_radius * np.cos(frame / (2 * orbit_period[i]))  # Adjust speed
        planet_position_y = orbit_radius * np.sin(frame / (2 * orbit_period[i]))  # Adjust speed
        planet_positions[i]._offsets3d = ([planet_position_x], [planet_position_y], [0])  # Update position

    return planet_positions

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), blit=False, interval=50)

plt.tight_layout()  # Adjust layout to remove excess white space
plt.show()

