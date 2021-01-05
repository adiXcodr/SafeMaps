import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

def getallpath(src,dest,visited,adj,path,final_path):
    visited[src]=1
    path.append(src)

    if(src==dest):
        final_path.append(list(path))
        pass
    else:
        for neighbours in adj[src]:
            if visited[neighbours]==0:
                getallpath(neighbours,dest,visited,adj,path,final_path)
    path.pop()
    visited[src]=0

def all_path(src,dest,adj):
    visited=[0]*11
    visited[0]=2
    path=[]
    final_path=[]
    getallpath(src, dest, visited, adj, path, final_path)
    return final_path

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
        if (arr[j] <= pivot): 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,low,high): 
    if (low < high): 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)


def nodeToLocality(nodes):
    localities=dict()
    for x in nodes:
        if(x==1):
            locality='Tezu'
        elif(x==2):
            locality='Paruwa'
        elif(x==3):
            locality='Mission'
        elif(x==4):
            locality='Civil'
        elif(x==5):
            locality='Dolabari'
        elif(x==6):
            locality='Bridge'
        elif(x==7):
            locality='Majgaon'
        elif(x==8):
            locality='ASTC'
        elif(x==9):
            locality='Kameng'
        elif(x==10):
            locality='Dekargaon'
        else:
             locality='Null'
        
        localities[x]=locality
    
    return(localities)
            

def localityToNode(G,locality):
    nodes=list(G.nodes())
    localities=nodeToLocality(nodes)
    p = dict(zip(localities.values(),localities.keys()))
    return(p[locality])


def getLocalityList(G,nodes):
    localities=[]
    for x in nodes:
        if(x==1):
            locality='Tezu'
        elif(x==2):
            locality='Paruwa'
        elif(x==3):
            locality='Mission'
        elif(x==4):
            locality='Civil'
        elif(x==5):
            locality='Dolabari'
        elif(x==6):
            locality='Bridge'
        elif(x==7):
            locality='Majgaon'
        elif(x==8):
            locality='ASTC'
        elif(x==9):
            locality='Kameng'
        elif(x==10):
            locality='Dekargaon'
        else:
             locality='Null'
        
        localities.append(locality)
    
    return(localities)
         
    
def getDayNight():
    date=datetime.now(pytz.timezone('Asia/Kolkata'))
    if date.hour < 6 or date.hour > 20:
        return('Night')
    else:
        return('Day')

def createGraph():
        G=nx.Graph()
        n=10
        for i in range(1,n+1):
            G.add_node(i)
            pass
        G.add_edge(1,2,DPA=30,TIL=8,CRL=2,DIS=0.5)
        G.add_edge(1,5,DPA=60,TIL=8,CRL=4,DIS=1.5)
        G.add_edge(2,3,DPA=20,TIL=4,CRL=2,DIS=1.0)
        G.add_edge(3,4,DPA=20,TIL=6,CRL=4,DIS=3.0)
        G.add_edge(3,6,DPA=30,TIL=6,CRL=1,DIS=2.0)
        G.add_edge(5,6,DPA=25,TIL=2,CRL=5,DIS=1.0)
        G.add_edge(6,7,DPA=20,TIL=6,CRL=3,DIS=0.5)
        G.add_edge(7,8,DPA=5,TIL=5,CRL=3,DIS=0.2)
        G.add_edge(7,10,DPA=10,TIL=6,CRL=4,DIS=0.5)
        G.add_edge(8,9,DPA=25,TIL=3,CRL=2,DIS=1.3)
        G.add_edge(9,10,DPA=15,TIL=3,CRL=2,DIS=1.5)
        
        adj=dict()
        for i in range(1,n+1):
            x=list(G.neighbors(i))
            adj[i]=x
        
        return(G,adj)


def displayGraph(G):
    print("Current Graph :  (hi-res image saved as Graph.png)")
    nodes=list(G.nodes())
    label_dict=dict()
    labels = nx.get_edge_attributes(G,'DPA')
    edges=list(labels.keys())
    dpa=list(labels.values())
    labels = nx.get_edge_attributes(G,'TIL')
    til=list(labels.values())
    labels = nx.get_edge_attributes(G,'CRL')
    crl=list(labels.values())
    labels = nx.get_edge_attributes(G,'DIS')
    dis=list(labels.values())
    for i in range(len(edges)):
      label_dict[edges[i]]='('+str(dpa[i])+', '+str(til[i])+', '+str(crl[i])+', '+str(dis[i])+')'
    
    pos = nx.circular_layout(G)
    f = plt.figure()
    nx.draw(G, pos, with_labels=False,node_color='yellow')
    node_label_dict=nodeToLocality(nodes)
    nx.draw_networkx_labels(G,pos,labels=node_label_dict)
    nx.draw_networkx_edge_labels(G,pos,font_size=7,edge_labels=label_dict)  
    plt.show(block=False)
    f.savefig("Graph.png",dpi=300)

def displayFinalGraph(G,path):
    print("Path :  (hi-res image saved as Path.png)")
    nodes=list(G.nodes())
    edges=list(G.edges())
    not_path=list(set(nodes) - set(path))
    path_edge_list=edgeList(path)
    not_path_edge_list=list(set(edges) - set(path_edge_list))
    edge_label_dict=dict()
    labels = nx.get_edge_attributes(G,'DPA')
    edges=list(labels.keys())
    dpa=list(labels.values())
    labels = nx.get_edge_attributes(G,'TIL')
    til=list(labels.values())
    labels = nx.get_edge_attributes(G,'CRL')
    crl=list(labels.values())
    labels = nx.get_edge_attributes(G,'DIS')
    dis=list(labels.values())
    for i in range(len(edges)):
      edge_label_dict[edges[i]]='('+str(dpa[i])+', '+str(til[i])+', '+str(crl[i])+', '+str(dis[i])+')'
    
    pos = nx.circular_layout(G)
    f = plt.figure()
    nx.draw(G, pos, with_labels=False,node_color='yellow')
    label_dict=nodeToLocality(nodes)
    nx.draw_networkx_labels(G,pos,labels=label_dict)
    nx.draw_networkx_nodes(G,pos,
                       nodelist=not_path,
                       node_color='red')
    nx.draw_networkx_nodes(G,pos,
                       nodelist=path,
                       node_color='green') 
    nx.draw_networkx_edges(G,pos,
                       edgelist=not_path_edge_list,edge_color='red')
    nx.draw_networkx_edges(G,pos,
                       edgelist=path_edge_list,edge_color='green')
    nx.draw_networkx_edge_labels(G,pos,font_size=7,edge_labels=edge_label_dict)
    plt.show(block=False)
    f.savefig("static/img/Path.png",dpi=300)
    
    

def edgeList(path):
    edges=[]
    for i in range(len(path)):
        if(i!=len(path)-1):
            tup=(path[i],path[i+1])
            edges.append(tup)
    return(edges)
        
        
def getDifference(attr):
    test_list=attr[:]
    n=len(test_list)
    quickSort(test_list,0,n-1) 
    a=test_list[0]
    b=test_list[1]
    return(abs(a-b))

def getOptimalSolution(DPA_paths,TIL_paths,CRL_paths,DIS_paths):

    if(getDifference(DPA_paths)<=5):
      if(getDayNight()=="Day"):
        flag=getDifference(TIL_paths)<=2
        if(flag):
            return(DIS_paths.index(min(DIS_paths)),'DIS')
        else:
            return(TIL_paths.index(min(TIL_paths)),'TIL')
      else:  #Night
        if(getDifference(CRL_paths)<=1):
            return(DIS_paths.index(min(DIS_paths)),'DIS')
        else:
            return(CRL_paths.index(min(CRL_paths)),'CRL')
    else:  #Return DPA if DIfference>5
      print(DPA_paths)
      return(DPA_paths.index(min(DPA_paths)),'DPA')

    
def getAttributeValue(att,u,v):
    try:
      val=att[(u,v)]
    except KeyError:
      try:
        val=att[(v,u)]
      except KeyError:
        val=0
    return(val)

def safestPath(G,all_paths):
    DPA=nx.get_edge_attributes(G,'DPA')
    TIL=nx.get_edge_attributes(G,'TIL')
    CRL=nx.get_edge_attributes(G,'CRL')
    DIS=nx.get_edge_attributes(G,'DIS')

    DPA_paths=[]
    TIL_paths=[]
    CRL_paths=[]
    DIS_paths=[]
    for path in all_paths:
      DPA_sum=0
      TIL_sum=0
      CRL_sum=0
      DIS_sum=0
      for i in range(len(path)):
          if(i!=len(path)-1):
            path[i]=int(path[i])
            path[i+1]=int(path[i+1])
            DPA_val=getAttributeValue(DPA,path[i],path[i+1])
            DPA_sum=DPA_sum+DPA_val
            TIL_val=getAttributeValue(TIL,path[i],path[i+1])
            TIL_sum=TIL_sum+TIL_val
            CRL_val=getAttributeValue(CRL,path[i],path[i+1])
            CRL_sum=CRL_sum+CRL_val
            DIS_val=getAttributeValue(DIS,path[i],path[i+1])
            DIS_sum=DIS_sum+DIS_val
      DPA_paths.append(DPA_sum)
      TIL_paths.append(TIL_sum)
      CRL_paths.append(CRL_sum)
      DIS_paths.append(DIS_sum)

    idx,criteria=getOptimalSolution(DPA_paths,TIL_paths,CRL_paths,DIS_paths)
    return(all_paths[idx],criteria)

def listToPath(arr):
    path=str(arr[0])
    for i in range(len(arr)):
        if(i!=len(arr)-1):
            path=path+'->'+str(arr[i+1])
    return(path)
        

def startProg(G,adj,s,d):
    G,adj=createGraph()
    displayGraph(G)
    s=int(localityToNode(G,s))
    d=int(localityToNode(G,d))
    if(s==10 and d==1):
        s,d=d,s
        all_paths=list(all_path(s, d, adj))
        safest_path,criteria=safestPath(G,all_paths)
        safest_path.reverse()
    else:
        all_paths=list(all_path(s, d, adj))
        safest_path,criteria=safestPath(G,all_paths)

    safest_path_text=getLocalityList(G,safest_path)
    safest_path_text=listToPath(safest_path_text)
    print('Safest Path is',safest_path_text,'and is based on',criteria)
    displayFinalGraph(G,safest_path)
    return(safest_path_text,criteria)