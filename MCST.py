
import os
os.system('clear')
# MCST tree
from curses import KEY_MIN
from random import shuffle
class Graph():
    def __init__(self,vertex) -> None:
        self.vx=vertex
        self.graph=[]
        self.p=set()
        self.P=set()
    def addege(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
        self.graph.append([u,v,w])
        print('{}---{} with weight {} '.format(u,v,w))
    # def shuffle(self):
    #  # doing it this way allows us to shuffle self
    #     shuffle(self)
    def arbitrary_vertex(self):
        self.d=[]
        for g in self.graph:
            self.d.append(g[0:2])
        shuffle(self.d)
        return self.d[0][0]
    def sets(self,vertex, tuple_min):
        self.p.add(vertex)
        self.P.add(tuple_min)
        

    def find_vx(self,svx):
        self.svx=svx
       
        d=[]
        for sg in self.graph:
            i,j=sg[0:2]
            if (i in self.svx or j in self.svx) and not {i,j}.issubset(self.svx):
                d.append(sg)
            else:
                pass
        
        return d

    def mincost(self,set_vx):
        self.svx=set_vx
        d=self.find_vx(self.svx)
        index=d.index(min(d, key=lambda x:x[2]))
        # print(self.find_vx(self.svx))
        # index=self.find_vx(self.svx).index(m)
        # print('i',index)
        # print(self.find_vx(self.svx)[index][0],self.svx)
        # print(self.find_vx(self.svx)[index][1],self.svx)
        if self.find_vx(self.svx)[index][0] not in set_vx:
           self.sets(self.find_vx(self.svx)[index][0],tuple(self.find_vx(self.svx)[index]))
        elif self.find_vx(self.svx)[index][1] not in set_vx:
           self.sets(self.find_vx(self.svx)[index][1],tuple(self.find_vx(self.svx)[index]))
        else:
            pass

    
g1=Graph(8)
g1.addege(1,2,4)
g1.addege(1,3,7)
g1.addege(1,4,6)
g1.addege(2,3,3)
g1.addege(2,4,8)
g1.addege(2,5,11)
g1.addege(3,4,5)
g1.addege(3,5,7)
g1.addege(4,5,3)
g1.addege(5,1,5)
g1.addege(6,2,4)
g1.addege(6,3,7)
g1.addege(6,4,6)
g1.addege(7,3,3)
g1.addege(7,4,8)
g1.addege(7,5,11)
g1.addege(8,4,5)
g1.addege(8,5,7)
g1.addege(8,3,9)
g1.addege(8,1,5)
arb=g1.arbitrary_vertex()
tuple_arb=tuple()
g1.sets(arb,tuple_arb)
arb_set=g1.p


g1.mincost(arb_set)
print('s=  ',set([gg[0] for gg in g1.graph]).union(set([gg[1] for gg in g1.graph])))

while(g1.p!=set([gg[0] for gg in g1.graph]).union(set([gg[1] for gg in g1.graph]))):
    g1.mincost(g1.p)
    print('vertices set is:  ', g1.p,'MCS tree is  ',g1.P.difference({()}))
        
            


        




        


    
