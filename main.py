import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Step 1: Define ellipse parameters
a = 1.5
b = 1.0

# Step 2: Generate boundary points (exclude first quadrant)
theta = np.linspace(0, 2*np.pi, 200)
theta = theta[(theta > np.pi/2) | (theta < 0)]  # remove first quadrant

x_boundary = a * np.cos(theta)
y_boundary = b * np.sin(theta)

# Step 3: Generate interior points
n_points = 5

x_rand = np.random.uniform(-a, a, n_points)
y_rand = np.random.uniform(-b, b, n_points)

# Keep only valid points
mask = (x_rand**2 / a**2 + y_rand**2 / b**2 <= 1) & ~((x_rand > 0) & (y_rand > 0))
x_in = x_rand[mask]
y_in = y_rand[mask]

# Combine boundary + interior
points = np.vstack((np.column_stack((x_boundary, y_boundary)),
                    np.column_stack((x_in, y_in))))

# Step 4: Delaunay triangulation
tri = Delaunay(points)

# Step 5: Plot mesh
plt.triplot(points[:,0], points[:,1], tri.simplices, linewidth=0.5)
plt.scatter(points[:,0], points[:,1], s=5)
plt.gca().set_aspect('equal')
plt.title("Delaunay Mesh for Ellipse with Quarter Removed")
plt.show()

# Step 6: Identify boundary points
boundary_tol = 0.05

is_boundary = ((points[:,0]**2 / a**2 + points[:,1]**2 / b**2 > 0.95) |
               ((points[:,0] > 0) & (points[:,1] > 0)))

# Step 7: Build neighbor list from triangulation
neighbors = {i: set() for i in range(len(points))}

for simplex in tri.simplices:
    for i in range(3):
        for j in range(3):
            if i != j:
                neighbors[simplex[i]].add(simplex[j])

# Step 8: Initialize solution
phi = np.zeros(len(points))

# Source term
f = 1.0

# Step 9: Iterative solver (Jacobi method)
num_iter = 500

for _ in range(num_iter):
    phi_new = phi.copy()
    
    for i in range(len(points)):
        if not is_boundary[i]:  # interior points only
            neigh = list(neighbors[i])
            phi_new[i] = np.mean(phi[neigh]) - f*0.01  # small step
            
    phi = phi_new

# Step 10: Plot solution
plt.tricontourf(points[:,0], points[:,1], tri.simplices, phi, levels=20)
plt.colorbar(label="Phi")
plt.gca().set_aspect('equal')
plt.title("Poisson Solution on Unstructured Mesh")
plt.show()