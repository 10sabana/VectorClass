class Vector:      #Declare Class
    def __init__(self,Vectorlen, *args):   # Constructor, 
      self.dimension = Vectorlen
      
      if type(args[0])==tuple:
        self.tupleVectors = tuple(args[0])
        self.entries=self.tupleVectors
      else:
        self.listVectors=list(args[0])
        self.entries=self.listVectors

    def vectorMethod(self):
      return self.entries


v = Vector(4, (1,2,3,4))
v2 = Vector(4, [1,2,3,4])

# 검출 로직 
# assert isinstance(v,Vector)
# assert type(v.entries)==tuple #이상없음
# assert type(v.dimension)==int #이상없음
# assert type(v.entries)==list # false 뜸 


# Inheritance 

# Make "vector" objects 
# a = (1, )  #tuple
# v = Vector(4, (1,2,3,4))

# a = [1, 2, 3]  #list
# v2 = Vector(4, [1,2,3,4])





