#import math as mt 
  
class Graph():  
    def __init__(self, vertices):  
        self.graph = [[0 for column in range(vertices)] 
                            for row in range(vertices)]  
        self.V = vertices  
  
    ''' Check if this vertex is an adjacent vertex  
        of the previously added vertex and is not  
        included in the path earlier '''
    def isSafe(self, v, pos, path):  
        # Check if current vertex and last vertex  
        # in path are adjacent  
        if self.graph[ path[pos-1] ][v] == 0:
            return False
  
        # Check if current vertex not already in path  
        for vertex in path:  
            if vertex == v:
                return False
  
        return True
  
    # A recursive utility function to solve  
    # hamiltonian cycle problem  
    def hamCycleUtil(self, path, pos):  
  
        # base case: if all vertices are  
        # included in the path  
        if pos == self.V:  
            # Last vertex must be adjacent to the  
            # first vertex in path to make a cyle  
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                
                return True
            
            else:  
                return False
  
        # Try different vertices as a next candidate  
        # in Hamiltonian Cycle. We don't try for 0 as  
        # we included 0 as starting point in hamCycle()  
        for v in range(1,self.V):  
  
            if self.isSafe(v, pos, path) == True:  
  
                path[pos] = v
                
  
                if self.hamCycleUtil(path, pos+1) == True:
                    
                    return True
  
                # Remove current vertex if it doesn't  
                # lead to a solution  
                path[pos] = -1
                print(path[pos])
  
        return False
  
    def hamCycle(self):  
        path = [-1] * self.V  
  
        ''' Let us put vertex 0 as the first vertex  
            in the path. If there is a Hamiltonian Cycle,  
            then the path can be started from any point  
            of the cycle as the graph is undirected '''
        path[0] = 0
  
        if self.hamCycleUtil(path,1) == False:  
            print ("Solution does not exist\n") 
            return False
  
        self.printSolution(path)  
        return True
  
    def printSolution(self, path):  
        print ("Υπάρχει λύση: Παρακάτω", 
                 "είναι ο κύκλος Hamilton") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 








# This function generates all n bit Gray  
# codes and prints the generated codes 
def generateGrayarr(n): 
  
    # base case 
    if (n <= 0): 
        return
  
    # 'arr' will store all generated codes 
    arr = list() 
  
    # start with one-bit pattern 
    arr.append("0") 
    arr.append("1") 
  
    # Every iteration of this loop generates  
    # 2*i codes from previously generated i codes. 
    i = 2
    j = 0
    while(True): 
  
        if i >= 1 << n: 
            break
      
        # Enter the prviously generated codes  
        # again in arr[] in reverse order.  
        # Nor arr[] has double number of codes. 
        for j in range(i - 1, -1, -1): 
            arr.append(arr[j]) 
  
        # append 0 to the first half 
        for j in range(i): 
            arr[j] = "0" + arr[j] 
  
        # append 1 to the second half 
        for j in range(i, 2 * i): 
            arr[j] = "1" + arr[j] 
        i = i << 1
  
    # prcontents of arr[] 
    for i in range(len(arr)): 
        print(arr[i])
    #for i in range(0, len(arr)):
        #arr[i] = int(arr[i])
    return arr
    



def bitdiffer(string1,string2):
    if len(string1) == len(string2):
        counterdiffs=0
        for a, b in zip(string1, string2):
            if a!=b:
                counterdiffs += 1
        if (counterdiffs==1): return True
            
    
   
      
n=int(input("Δώσε αριθμό:"))
if n<3:
    print("Δεν υπάρχει κύκλος hamilton")
AdjMatrix=[0]*(2**n)
for i in range((2**n)):
    AdjMatrix[i] = [0] * (2**n)

arr=generateGrayarr(n)

for i in range(len(arr)):
    temp1=arr[i]
    for j in range(len(arr)):
        temp2=arr[j]
        if bitdiffer(temp1,temp2):
            AdjMatrix[i][j]=1
            AdjMatrix[j][i]=1
        
        
#print (AdjMatrix)
Qn=Graph(2**n)
Qn.graph=AdjMatrix
Qn.hamCycle()
       








