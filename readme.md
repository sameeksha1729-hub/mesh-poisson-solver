# 🔥 2D Mesh Generation and Poisson Solver

## 📖 Problem Statement  
This project generates an unstructured mesh for an elliptical domain (with one quadrant removed) and solves the Poisson equation on it.

---

## 🧠 Mathematical Model  

The governing equation:

∇²φ = f

- φ = scalar field (e.g., temperature)
- f = constant source term

Boundary condition:
- φ = 0 on boundary (Dirichlet condition)

---

## ⚙️ Methodology  

### 1. Geometry  
- Ellipse with major/minor axis ratio = 1.5  
- First quadrant removed  

### 2. Mesh Generation  
- Boundary points using parametric equation  
- Interior points using random sampling  
- Delaunay triangulation  

### 3. Solver  
- Neighbor-based discretization  
- Iterative (Jacobi method)  

---

## 📊 Results  

### 🔹 Mesh  
![Mesh](images/mesh.png)

### 🔹 Poisson Solution  
![Solution](images/solution.png)

---

## 🚀 How to Run  

pip install numpy matplotlib scipy  
python main.py  

---

## 📁 Project Structure  

mesh-poisson-solver/  
│── main.py  
│── README.md  
└── images/  
  ├── mesh.png  
  ├── solution.png  
  ├── convergence.png  

---

## 💡 Key Learnings  
- Unstructured mesh generation  
- Delaunay triangulation  
- Solving PDEs numerically  

---

## 🔥 Future Improvements  
- Finite Element Method (FEM)  
- Better solvers (Gauss-Seidel)  
- Adaptive mesh refinement  