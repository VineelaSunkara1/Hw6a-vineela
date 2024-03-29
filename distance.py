import numpy as np
import time


def distance(vector_a, vector_b):
    """
    Returns the Euclidean distance between two one-dimensional vectors
    """
    assert len(vector_a.shape) == 1
    assert vector_a.shape == vector_b.shape
    dim = vector_a.shape[0]
    raise NotImplementedError
   
if __name__ == "__main__":
    dim = 20000
    start = time.time()
    d = distance(np.ones(dim), np.zeros(dim))
    end = time.time()
    print("Time:", end - start)
    assert np.isclose(d, np.sqrt(dim))
