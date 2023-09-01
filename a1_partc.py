from a1_partb import SetList

class DisjointSet:

	def __init__(self): #This is constructor function of class DisjointSet. In this constructor function the object of DisjointSet function is given an attribute 
		                # numberOfSet and initially iniialised to 0. Similarly, another attribute of type dictionary by name dict is assigned to object and is intialized 
						# to empty dictionary
		self.numberOfSet = 0;
		self.dict = {}

	def make_set(self, element): #This function checks whether the incoming element(dog,cat etc.)is in dictionary or not. If the element is not in dictionary
		                         # Created a new SetList Object and then the make_set function is called with an element as an argument that is responsible for
								 # formation of new Node object. After this the dictionary stores an 'incoming element' as a 'key' and has a value where the 
								 # SetList.front is pointing to. Finally, the numberOfSet is increased by 1 and returns true
								 # In opposite case the function simply returns false 
		if (element not in self.dict.keys()):
			listNew = SetList()
			listNew.make_set(element)
			self.dict[element] = listNew.front
			self.numberOfSet += 1;
			return True;
		return False;

	def get_set_size(self,element):
		#This function checks whether the incoming 'element' is present in dictionary and makes sures if that elements set_list.front is not None
		#If it is pointing to Node object then the count is incremented by 1 and this keeps on going till  self.dict[element].set_list.back
		#Once its next_node points to None the function returns the count(basically the size of a set of particular element)
		count = 0
		# for key in self.dict:
		if (element in self.dict):
			n = self.dict[element].set_list.front
			while (n is not None):
				count += 1
				n = n.next_node;
		return count;


	def find_set(self, element): #This function checks whether an incoming element is present in dictionary or not. If it is present the function returns
			                     #the data where elements' set_list.front is pointing to
		# for key in self.dict:
			if (element in self.dict):
				return self.dict[element].set_list.front.data;
		

	def union_set(self, element1, element2):

		#Basically, in this function element1 is added to element2
		#This function checks if incoming two elements are present in disjoint set and are not equal to one another using find_set function
		#If element2 has set_list.back then self.dict[element2].set_list.back.next_node will point to self.dict[element1].set_list.front and
		#self.dict[element1].set_list.front.prev will start pointing to self.dict[element2].set_list.back. Finally, self.dict[element2].set_list.back change its pointer to self.dict[element1].set_list.back;

		if ((self.find_set(element1) != self.find_set(element2))):
				if (self.dict[element2].set_list.back is not None):
					self.dict[element2].set_list.back.next_node = self.dict[element1].set_list.front;
					self.dict[element1].set_list.front.prev = self.dict[element2].set_list.back;
					self.dict[element2].set_list.back = self.dict[element1].set_list.back;
				
					
				nn = self.dict[element1].set_list.front
				nn.front = None;
				nn.back = None;
				self.numberOfSet -= 1;
		#Now the element1's set_list.back and front are pointed to None as pointing ends changed in above scenario
		#As now element1 is merged in element2 so number of sets got decreased by 1	as coded above.

		#In the code above, the while loop is checking for first node being not none, then traverse through all the nodes and 
		# check if the set list of each node is equal to set list of the element2's Set list. If not make them same, if yes, the skip.
		# finally, return true. If the data of element 1 = element2 (means same element union is to be performed) 
		# then skip the whole process and return false;

				while(nn is not None):
					if (nn.set_list != self.dict[element2].set_list):
						nn.set_list = self.dict[element2].set_list
						nn = nn.next_node
				return True;
		else:
			return False;
			

	def get_num_sets(self):  #This function returns the total number of sets inside disjoint set
		return self.numberOfSet;
			
	def __len__(self): # This function returns the number of elements present in the dictionary (keys).
		return len(self.dict.keys());
