class SetList:
	class Node:
		def __init__(self, data = None, set_list = None, next_node = None, prev_node = None):
			#This is constructor function of Node and is responsible for setting some attributes of node object like data, set_list, next_node and prev_node
			# if no values are given, attributes are set to default.
			self.data = data
			self.set_list = set_list
			self.next_node = next_node
			self.prev_node = prev_node

		def get_data(self): # This function is returning data.
			return self.data

		def get_next(self): # This function is returning a Node object pointed by the next_node
			return self.next_node

		def get_previous(self): #This function is returning a Node object pointed by the previous_node
			return self.prev_node

		def get_set(self): # This function returns the SetList object of the current node (that the current node is pointing to).
			return self.set_list;


	def __init__(self): #This is constructor function of the SetList. It have two pointers front and back that will point to nodes. Initially they ar emade None or null
		self.front = None
		self.back = None

	def get_front(self): # This function will return the 1st node object pointed by the SetList object
		return self.front
		
	def get_back(self): #This function will return the last node object pointed by the SetList object
		return self.back


	def make_set(self, data): #This function is responsible for making a new node with the provided data and a self object of SetList. It assigns the 
								# callee object (SetList object or self) to the set_list attribute of node. New Node is made only if the SetList object's
								# front is pointing to the None. Finally, the new node object is returned. Otherwise, none is returned.
		if (self.front is None):
			#Setlist.Node(data, self)
			newNode = self.Node(data, self)
			self.front = newNode #Inititally both the front and back of the SetList object is pointing to the new node.
			self.back = newNode
			return newNode
		return None


	def find_data(self, data): #This function returns the a reference to the Node containing data. First Object of the SetList is assigned to n and a while
							# loop is used to keep the loop continue till n becomes none and n.data is not equal to the comming data. Once it is equal or the
							# n is none, loop is broken. n is constatly being updated with n.next node so that we keep moving to new node. Lastly, if the data
							# is found, that data's node is returned. Otherwise, none is returned.
		n = self.front;
		while(n is not None and n.data != data):
			n = n.next_node;
		if (n.data == data):
			return n;
		return None;


	def representative_node(self): #This function is responsible for returning the 1st node of the Set_list (where self.front is pointing). If self.front is 
									# pointing to none or if the Set_list is empty, it returns none.
		if (self.front is not None):
			return self.front;
		return None;

	def representative(self): #This function is same as the respresenttaive node(the above one). But just returns node's data instead of the node itself.
								# Similarly If self.front is pointing to none or if the Set_list is empty, it returns none.
		if (self.front is not None):
			return self.front.data;
		return None;

	def union_set(self, other_set): # This function joins two Set Lists. This function reutrns the count based on number of number of nodes tranferred.
									# The purpose of this function is to put the nodes of other_set into the callee set or self set. It first checks if the
									# other function have any nodes or not, if not then then 0 is returned as count. If present then count is added 1 by 1 till
									# all nodes are accessed thorugh while loop n.next_node. Once count is > 0, the next_node of the callee node is pointed  to
									# the front of the other SetList obejct. And the previous node of the other obejct is pointed to the last node of the callee.
									# Finally, other Set List front and back is set to none. Also, if the SetList object where we want to assign some nodes is empty,
									# means its front and back is pointing to none, we make both front and back points to the comming SetList fornt and back respectively.		

		n = other_set.front;
		count = 0;

		while (n is not None):
			count+=1;
			n.set_list = self;
			n = n.next_node;
		
		if count > 0:

			if (self.front is None and self.back is None):

				self.front = other_set.front;
				self.back = other_set.back;

			else:
				self.back.next_node = other_set.front
				other_set.front.prev_node = self.back
				self.back = other_set.back

		other_set.front = None
		other_set.back = None

		return count;


	def __len__(self): #This function retutns the number of Node objects belonging to or is pointed by SetList. It iterate from the front of the SetList and
						# keep adding 1 to the count till it find another node in the next_node. and finally return the count.
		n = self.front
		count = 0
		while (n is not None):
			count += 1;
			n = n.next_node
		return count;

