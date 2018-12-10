import numpy
from scipy.spatial import cKDTree

from sklearn.neighbors import NearestNeighbors
from sklearn.svm import SVC


def classifier(svm: SVC, state):
    taxirow, taxicol, passloc, destidx = state
    feature = [taxirow, taxicol, passloc, destidx]
    c = svm.decision_function(feature)
    a_p = svm.predict(feature)
    return a_p, c, None


def update_classifiers(states, actions):
    svm = SVC()
    svm.fit(states, actions)
    nn = NearestNeighbors()
    nn.fit(states, actions)
    return svm, nn


def nearest_neighbor(nn: NearestNeighbors, state):
    return nn.kneighbors(state, 1)


def update_threshold(states: list):
    kdt = cKDTree(states)
    dists, neighs = kdt.query(states, 2)
    dists = numpy.sum(dists, axis=1)
    avg_dist = numpy.mean(dists)
    return 0, avg_dist


def process_state(state):
    taxirow, taxicol, passloc, destidx = state
    return taxirow, taxicol, passloc, destidx