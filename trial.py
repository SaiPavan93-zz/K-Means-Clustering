from __future__ import division
import numpy as np
import math
from scipy.spatial import distance
import sys

#Calculate the Euclidean Distance
def euclidean(centroidlist,cordinatelist,req):
    total=[]
    clusassign = {}
    if(len(str(centroidlist[0])) is not 1):

        for each in cordinatelist:
            a = []
            for ech in centroidlist:
                dst = distance.euclidean(ech, each)
                a.append(math.pow(dst,2))
            req.append(a)
        #print(req,"\n",len(req))
    else:

        for each in cordinatelist:
            a = []
            for ech in centroidlist:
                dst = distance.euclidean(ech, each)
                a.append(math.pow(dst, 2))
            req.append(a)

    #print(req)
    for each in req:
        key = each.index(min(each))
        clusassign.setdefault(key, [])
        clusassign[key].append(cordinatelist[req.index(each)])

    return clusassign


def calculate(value,last,cood):
    req=[]
    clusassign={}
    print(value)
    clusassign=euclidean(value,cood,req)
    return clusassign

def calculateMeanSquareError(value,clusterassign):
    #print(value,"\n",clusterassign)
    sse=[]
    sum1=0
    for each in clusterassign.keys():
        sum=0
        #print(each,":---",len(clusterassign[each]))
        err=clusterassign[each]
        #print(value[each],":--",clusterassign[each])
        for every in err:
            dst=distance.euclidean(value[each],every)
            dst=math.pow(dst,2)
            sum=sum+dst
        sse.append(sum)
    for i in sse:
        sum1=sum1+i
    return (round(sum1,2))

def calculateMean(clusterassign,value):
    #print(value)
    req=[]
    avg=[]
    for each in clusterassign.keys():
        print(each, len(clusterassign[each]))
        a=clusterassign[each]
        #a.append(value[each])
        avg = np.mean(a, axis=0)
        avg = np.round(avg, decimals=2)
        avg = np.array(avg).ravel().tolist()
        req.append(avg)
    #print(req)
    return req


def converge(mean,value):
    sum2=0
    #print(mean,"\n",value)

    for i,j in zip(mean,value):
        #print(i,j)
        dst = distance.euclidean(i, j)
        sum2=sum2+dst
    #print(sum2)
    return (sum2)

def display(cood,k,t,value,sse,clusassign):
    print("The number of data points in the input file",len(cood),"\n","The diemension of the data is",len(cood[1]),"\n","The value of k is",k)
    print("No of iterations for convergence",t)
    print("The final mean of each cluster is",value,"\n","The SSE score is",sse)
    print("The final cluster assignment is",clusassign)
    for dm in clusassign.keys():
        print(value[dm],"-->",len(clusassign[dm]))


#Calculating purity for iris data
def purity(cood,clusterassign):
    first=cood[0:50]
    second=cood[50:100]
    third=cood[100:150]
    count = 0
    count2 = 0
    count3 = 0
    #print(first)
    f=clusterassign[0]
    f=f[0:(len(f))]
    s=clusterassign[1]
    s = s[0:(len(s))]
    t=clusterassign[2]
    t = t[0:(len(t))]
    #print(len(f),len(s),len(t))
    #print(len(first),len(second),len(third))

    #print(clusterassign,len(clusterassign))
    for each in f:

        for i in first:
            if(each == i):
                count=count+1

    if(count>len(f)):
        count=len(f)
    for each in s:
        for i in second:
            if(each==i):
                count2=count2+1
    if (count2 > len(s)):
        count2 = len(s)
    for each in t:
        for i in third:
            if(each==i):
                count3=count3+1
    if (count3 > len(t)):
        count3 = len(t)

    #print(count,count2,count3)
    #print(count+count2+count3)
    return((count+count2+count3)/150)





def main():
    #print(len(sys.argv),sys.argv[3])
    f=open(sys.argv[1],"r")
    file=f.read()
    data=file.split("\n")
    value=[]
    cood=[]
    last=[]
    old=[]
    req=[]
    clusterassign={}
    t=0
    k=sys.argv[2]
    if(len(sys.argv)==3):
        randomitems=np.random.choice(data,int(k))

        try:
            for each in randomitems:
                a=each.split(",")

                n = []
                for i in range(len(a)):
                    # print("i am",len(a))
                    n.append(float(a[i]))
                value.append(n)
            #value.append([float(a[0]),float(a[1]),float(a[2]),float(a[3])])
        except ValueError:
            for each in randomitems:
                a=each.split(",")
            #print(a)
                n = []
                for i in range(len(a)-1):
                    n.append(float(a[i]))
                value.append(n)
    elif(len(sys.argv) == 4):
        f = open(sys.argv[3], "r")
        file1 = f.read()
        line = file1.split("\n")
        try:
            for each in line:
                raw=[]
                #print(int(each),data[int(each)])
                l=data[int(each)].split(",")
                #print(l)
                for i in range(len(l)):
                    raw.append(float(l[i]))
                value.append(raw)

        except ValueError:
            for each in line:
                raw=[]
                #print(int(each),data[int(each)])
                l=data[int(each)].split(",")
                #print(l)
                for i in range(len(l)-1):
                    raw.append(float(l[i]))
                value.append(raw)
    #print(value)
    try:
        for each in data[0:(len(data)-1)]:
            r=[]
            l=each.split(",")

            for i in range(len(l)):
                r.append(float(l[i]))
            cood.append(r)

    except ValueError:
        for each in data[0:len(data)]:
            r=[]
            l=each.split(",")

            for i in range(len(l)-1):
                r.append(float(l[i]))
            cood.append(r)
    #print(len(cood))


    v=10
    while(v>=0.0001):
        t+=1
        clusterassign = calculate(value,last,cood)
        sse = calculateMeanSquareError(value, clusterassign)
        mean = calculateMean(clusterassign,value)
        v=converge(mean,value)
        value = mean
        print(v, value, t)

    display(cood, k, t, value, sse, clusterassign)
    p=purity(cood,clusterassign)
    print(p)

if __name__=="__main__":
    #for i in range(10):
    main()