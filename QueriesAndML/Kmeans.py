import sys
import numpy as np
import random
import math

def percentChange(A , B):

    return (((A - B) / A ) * 100)

def distance(A , B):
   
    x1 = A[0]
    x2 = B[0]
    y1 = A[1]
    y2 = B[1]

    return math.sqrt( (np.abs(x2-x1) ** 2 ) + (np.abs(y2-y1) ** 2 ) )

def distanceDatapoint(A , B):
    
    # Set x and y values for each datapoint

    x1 = A[0][1]
    x2 = B[0]
    y1 = A[1]
    y2 = B[1]

    # use Pythagorean theorem to get distance with 2 dimensional datapoints

    return math.sqrt( (np.abs(x2-x1) ** 2 ) + (np.abs(y2-y1) ** 2 ) )


def kmeans(clusters, datapoints): # datapoint: Team dict ex. Team[Knicks] = [(Jalen Brusnon, 28.7) , 117.3]

    #program ends when loss doesn't change or changes by so little degree we deem any more itterations excessive
    MSE = 0

    # choose x random datapoints as the original centers
    #print(datapoints)

    keys = []
    for element in datapoints:
        keys.append(element)
    random_keys = random.sample(keys, clusters)
    # print(random_keys)
    clusters = []
    
    # initialize x lists in clusters to represent each cluster, with the first value of the list being 
    for element in random_keys:
        clusters.append([ (element[0][1] , element[1]) ])

    # print(clusters)
    MSE = 0
    for team in datapoints:
        minDist = sys.maxsize
        closest = None
        for i in range(len(clusters)):
            center = clusters[i][0]
            # evaluate which center each team is closest to
            # print(team)

            curDist = distanceDatapoint(team , center)

            if curDist < minDist:
                minDist = curDist
                closest = i
        
        MSE += minDist ** 2
        clusters[closest].append(team)
    

    MSE /= len(datapoints)

    

    itt = 0
    prevMSE = 0
    while itt == 0 or( abs(percentChange(MSE , prevMSE)) > 0.1 and itt < 300):
        prevMSE = MSE
        MSE = 0
        itt += 1
        
        newClusters = []
        # Calculate means of each group
        for cluster in clusters:
            x = 0
            y = 0
            count = 0
            for i in range(1 , len(cluster)):
                count+=1
                point = cluster[i]
                # print("point",point)

                x += point[0][1]
                y += point[1]

            newClusters.append( [ (x / count, y / count)  ] )

       

        for datapoint in datapoints:
            minDist = sys.maxsize
            closest = None
            for i in range(len(newClusters)):
                center = newClusters[i][0]
                # evaluate which center each team is closest to
                # print("error",team)

                curDist = distanceDatapoint(datapoint , center)

                if curDist < minDist:
                    minDist = curDist
                    closest = i
            
            MSE += minDist ** 2
            newClusters[closest].append(datapoint)
        
        clusters = newClusters
    

    return clusters, MSE
        


    