from importlib.resources import path
import re


g = [[0,100,0,300,1000],[100,0,500,0,0],[0,500,0,200,100],[300,0,200,0,600],[1000,0,100,600,0]]

def binarySearch(s,e,key):
    l = ["amravati","aurangabad","mumbai","nagpur","pune"]
    while(s<=e):
        mid = int((s+e)/2)

        if(l[mid]==key):
            return mid
        elif(l[mid]>key):
            e = mid -1
            binarySearch(s,e,key)
        else:
            s = mid + 1
            binarySearch(s,e,key)
    
    return -1

def printList(g):
    for i in range(len(g)):
        print(g[i],end=" ")

def printtwoDList(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            print(g[i][j],end=" ")
        print("")

distance_string = ""
path_string = ""

def getCityList():
    l = ["amravati","aurangabad","mumbai","nagpur","pune"]
    return l

def dijkstara(startnode,endnode):
    global path_string,distance_string,g
    city = getCityList()
    inf = 99999
    cost = [[]]
    distance = []
    pred = []
    visted = []
    nextnode = 0

    for i in range(len(g)):
        temp =[]
        for j in range(len(g[i])):
            if(g[i][j]==0):
                temp.append(inf)
            else:
                temp.append(g[i][j])
        cost.append(temp)
    
    del(cost[0])
    
    for i in range(len(g)):
        distance.append(cost[startnode][i])
        pred.append(startnode)
        visted.append(0)
    
    distance[startnode] = 0
    visted[startnode] = 0
    count = 1
    
    while(count<(len(g)-1)):
        mindistance = inf
        for i in range(len(g)):
            if(distance[i]<mindistance and visted[i]==0):
                mindistance = distance[i]
                nextnode = i
        
        visted[nextnode] = 1
        
        for i in range(len(g)):
            if(visted[i]==0):
                if(mindistance+cost[nextnode][i]<distance[i]):
                    distance[i] = mindistance+cost[nextnode][i]
                    pred[i] = nextnode
        
        count += 1
    
    ans = []      
    for i in range(len(g)):
        
        if(i==endnode):
            distance_string += "Distance of "+str(city[startnode].upper())+" from "+str(city[i].upper())+" = "+str(distance[i])
            path_string += "Path = "+str(city[i].upper())
            j = i
            while(True):
                j = pred[j]
                path_string += ("<-"+str(city[j].upper()))
                if(j==startnode):
                    break
            ans.append(distance_string)
            ans.append(path_string)
            distance_string = ""
            path_string = ""   
    return ans





    










