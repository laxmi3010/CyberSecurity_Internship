import random
import matplotlib.pyplot as plt

# Real path (straight line)
real_path = [(x, 50) for x in range(100)]

# Spoofed path (altered by attacker)
spoofed_path = [(x, 50 + random.uniform(-10, 10)) for x in range(100)]

# Plotting both paths
x_real, y_real = zip(*real_path)
x_spoof, y_spoof = zip(*spoofed_path)

plt.plot(x_real, y_real, label="Real GPS Path", color="green")
plt.plot(x_spoof, y_spoof, label="Spoofed GPS Path", color="red", linestyle="--")
plt.legend()
plt.title("GPS Spoofing Simulation")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
