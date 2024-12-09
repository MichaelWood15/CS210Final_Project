import sys
import numpy as np
import random
import math

def distance(A , B):
    
    # Set x and y values for each datapoint

    x1 = A[0][1]
    x2 = B[0][1]
    y1 = A[1]
    y2 = B[1]

    # use Pythagorean theorem to get distance with 2 dimensional datapoints

    return math.sqrt( (np.abs(x2-x1) ** 2 ) + (np.abs(y2-y1) ** 2 ) )


def kmeans(clusters, datapoints): # datapoint: Team dict ex. Team[Knicks] = [(Jalen Brusnon, 28.7) , 117.3]

    #program ends when loss doesn't change or changes by so little degree we deem any more itterations excessive
    loss = sys.maxsize

    # choose x random datapoints as the original centers

    random_keys = random.sample(datapoints.keys(), clusters)

    centers = []
    for index in random_keys:
        centers.append(datapoints[random_keys])

    # Assign datapoints to clusters

    for x in datapoints:
        min = sys.maxsize

        for centroids in centers:
            if distance(x , )



