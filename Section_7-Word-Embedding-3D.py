import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from gensim.models import Word2Vec

# Load the trained Word2Vec model
model = Word2Vec.load("Section-7-word2vec_model.bin")

# Get word embeddings for all words in the vocabulary
words = list(model.wv.key_to_index.keys())
embeddings = [model.wv[word] for word in words]

# Convert embeddings list to a NumPy array
embeddings = np.array(embeddings)

# Perform PCA to reduce the dimensionality to 3
pca = PCA(n_components=3)
embeddings_3d = pca.fit_transform(embeddings)

# Plot the word embeddings in 3D space
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for each word's 3D representation
ax.scatter(embeddings_3d[:, 0], embeddings_3d[:, 1], embeddings_3d[:, 2], marker='o', color='b')

# Annotate each point with the corresponding word
for i, word in enumerate(words):
    ax.text(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2], word, fontsize=8)

ax.set_xlabel('PCA Component 1')
ax.set_ylabel('PCA Component 2')
ax.set_zlabel('PCA Component 3')
ax.set_title('3D Visualization of Word Embeddings using Word2Vec')

plt.show()
