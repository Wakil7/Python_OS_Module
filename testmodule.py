import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sample data for the dot plot
data = [3, 7, 1, 9, 5, 4, 6, 2, 8, 10]

# Create a figure
plt.figure()
plt.xlim(0, 11)  # Set x-axis limits (for better spacing)
plt.ylim(0, 12)  # Set y-axis limits

# Hide only the y-axis
plt.gca().axes.yaxis.set_visible(False)

# Initialize an empty plot for the dots
dots, = plt.plot([], [], 'bo', markersize=8)  # 'bo' means blue dots

# Lists to hold x and y data for the dots
x_data = []
y_data = []

# Animation function to add dots sequentially
def animate(i):
    x_data.append(data[i])
    y_data.append(i + 1)  # Assign a unique y position for each dot
    dots.set_data(x_data, y_data)
    return dots,

# Create the animation using FuncAnimation
anim = FuncAnimation(plt.gcf(), animate, frames=len(data), interval=500, repeat=False)

# Display the animation
plt.show()

