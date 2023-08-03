import random as rand
import math
import matplotlib.pyplot as plt

colorList = ['red','blue','green','yellow','orange','purple']

# Getting random data points
def getData():
    y = []
    x = list(range(100))
    for i in x:
        y.append(rand.randint(1,50))
    return x,y

# Plotting the points
def plotData(x,y,clr='blue',mkr='.'):
    plt.scatter(x,y,color=clr,marker=mkr)

def eucleadianDistance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def assignCentroid(x,y,cx,cy,cls):
    for i in range(len(x)):
        d = []
        for j in range(len(cx)):
            d.append(eucleadianDistance(x[i],y[i],cx[j],cy[j]))
            # print(j)
        dMin,a = min((di,a) for a,di in enumerate(d))
        # print(dMin,a)
        cls[a].append((x[i],y[i]))

    return cls

def findNewCentroids(cls,k):
    cx = []
    cy = []
    # print("k",k)
    for i in range(k):
        x,y = zip(*cls[i])
        cx.append(int(sum(x)/len(x)))
        cy.append(int(sum(y)/len(y)))
        cls[i]=[]
    # print(cx)
    return cx,cy,cls


def kmeans(X,Y,k):

    # get random centroids
    centroids_x = []
    centroids_y = []
    clusters = {}
    for i in range(k):
        centroids_x.append(rand.randint(1,100))
        centroids_y.append(rand.randint(1,50))
        clusters[i] = []

    # plot inital points
    plotData(X,Y)
    plotData(centroids_x,centroids_y,'red')
    plt.show()

    # iterate to fine tune centroids
    for iter in range(5):
        # print("iter",iter)
        clusters = assignCentroid(X,Y,centroids_x,centroids_y,clusters)
        for i in range(k):
            x,y = zip(*clusters[i])
            plotData(list(x),list(y),colorList[i])
            plotData(centroids_x[i],centroids_y[i],colorList[i],'s')
        plt.show()
        centroids_x, centroids_y, clusters = findNewCentroids(clusters,k)
    
if __name__ == '__main__':

    x,y = getData()
    k = 3
    kmeans(x,y,k)

