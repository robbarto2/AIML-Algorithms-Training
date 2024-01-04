import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# Create a dataset with concentric circles
X, y = make_circles(n_samples=100, factor=0.2, noise=0.1, random_state=42)

# Train an SVM with RBF kernel
svm_rbf = SVC(kernel='rbf', C=1e3, gamma=0.1)
svm_rbf.fit(X, y)

# Create a mesh to plot decision boundary
h = .02  # Step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Project data into 3D using RBF kernel
Z = svm_rbf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the original data in 2D
#plt.figure(figsize=(12, 5))

#plt.subplot(1, 2, 1)
#plt.scatter(X[:, 0], X[:, 1], c=['red' if label == 1 else 'black' for label in y])
#plt.title('Original Data in 2D')
#plt.xlabel('Feature 1')
#plt.ylabel('Feature 2')

# Plot the projected data in 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], svm_rbf.decision_function(X), c=y, cmap=plt.cm.Paired)

# Plot decision boundary as a grid
ax.plot_wireframe(xx, yy, Z, rstride=10, cstride=10, color='gray', alpha=0.3)

ax.set_title('Projected Data with Decision Boundary (3D)')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Decision Function Value')

# Rotate the view for a better angle
ax.view_init(elev=20, azim=40)

plt.show()
