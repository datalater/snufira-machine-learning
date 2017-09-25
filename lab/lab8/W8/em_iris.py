import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

from sklearn import datasets
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import StratifiedKFold

print(__doc__)



def make_ellipses(gmm, ax):
    for n, color in enumerate(colors):
        covariances = gmm.covariances_[n][:2, :2]
      
        v, w = np.linalg.eigh(covariances)
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi  # convert to degrees
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        ell = mpl.patches.Ellipse(gmm.means_[n, :2], v[0], v[1],
                                  180 + angle, color=color)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.5)
        ax.add_artist(ell)


iris = datasets.load_iris()

X = iris.data
y = iris.target

# Create GMM for n_classes
n_classes = len(np.unique(y))
colors = ['navy', 'turquoise', 'darkorange'][0:n_classes]
estimator = GaussianMixture(n_components=n_classes,
                   covariance_type='full', max_iter=100, random_state=0)

plt.figure()

# Initialize the centroids
# - Randoml select a data point of each class as the starting centroid
estimator.means_init=np.array([X[y==i][np.random.choice(len(X[y==i]))] for i in range(n_classes)])

# We can do better at initializing the centroid with labeled data (i.e., for unlabeled data this is not possible)
# Since we have class labels for the training data, we can
# initialize the GMM parameters in a supervised manner.
# estimator.means_init = np.array([X[y == i].mean(axis=0)
#                                  for i in range(n_classes)])


# Train the other parameters using the EM algorithm.
estimator.fit(X)

h = plt.subplot()
make_ellipses(estimator, h)

for n, color in enumerate(colors):
    data = iris.data[iris.target == n]
    plt.scatter(data[:, 0], data[:, 1], color=color, marker='x',
                label=iris.target_names[n])

pred = estimator.predict(X)
train_accuracy = np.mean(pred.ravel() == y.ravel()) * 100

plt.text(0.01, 0.95, 'Train accuracy: %.1f' % train_accuracy,
             transform=h.transAxes)

plt.xticks(())
plt.yticks(())
plt.title("name")

plt.legend(scatterpoints=1, loc='lower right', prop=dict(size=12))


plt.show()