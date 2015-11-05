import copy

class actions:
	LEFT = (0,-1)
	UP = (-1,0)
	RIGHT = (0,1)
	DOWN = (1,0)

class node:
	def __init__(self, parent, action):
		print "self:",id(self)
		if id(parent) == id(None):
			self._state = [[1,4,8],[3,6,2],[0,5,7]]
		else:
			self._parent = parent
			self._state = copy.deepcopy(parent.get_state())
		self._update_state_map()
		self._exec_action(action)
		self._goal_state = [[8,7,6],[5,4,3],[2,1,0]]
		self._goal_state_map = dict( (i,(x,y)) for x,l in enumerate(self._goal_state) for y,i in enumerate(l))


	def __eq__(self, other):
		if self.get_state() == other.get_state():
			return True
		else:
			return False

	def _update_state_map(self):
		self._state_map = dict( (i,(x,y)) for x,l in enumerate(self._state) for y,i in enumerate(l))

	def _exec_action(self, action):
		if not action == None:
			null_index = self._state_map[0]
			target_index = (null_index[0] + action[0], null_index[1] + action[1])
			self._state[null_index[0]][null_index[1]] = self._state[target_index[0]][target_index[1]] 
			self._state[target_index[0]][target_index[1]] = 0
			self._update_state_map()

	def get_state(self):
		return self._state

	def get_state_map(self):
		return self._state_map

	def get_successors(self):
		valid_actions = []
		null_index = self._state_map[0]
		if null_index[0] > 0:
			valid_actions.append(actions.UP)
		if null_index[0] < 2:
			valid_actions.append(actions.DOWN)
		if null_index[1] > 0:
			valid_actions.append(actions.LEFT)
		if null_index[1] < 2:
			valid_actions.append(actions.RIGHT)
		successor_list = []
		for action in valid_actions:
			successor = node(self,action)
			successor_list.append(successor)
		return successor_list

	def h_manhattan(self):
		manhattan = 0
		for row in self._state:
			for field in row:
				actual_coords = self._state_map[field]
				target_coords = self._goal_state_map[field]
				manhattan = manhattan + abs(actual_coords[0] - target_coords[0]) + abs(actual_coords[1] - target_coords[1])
		return manhattan

	def h_misplaced(self):
		misplaced = 0
		for row in self._state:
			for field in row:
				if self._state_map[field] != self._goal_state_map[field]:
					misplaced = misplaced + 1
		return misplaced

	def is_goal(self):
		if self._state_map == self._goal_state_map:
			return True
		else:
			return False

class greedy_algorithm:
	def __init__(self, misplaced):
		self._misplaced_heuristic = misplaced

	def tree_search(self):
		visited = 0
		current_node = node(None,None)
		fringe = []
		while not current_node.is_goal():
			for successor in current_node.get_successors():
				if self._misplaced_heuristic:
					fringe.append((successor.h_misplaced(), successor))
				else:
					fringe.append((successor.h_manhattan(), successor))
			visited = visited + 1
			fringe = sorted(fringe)
			current_node = fringe.pop(0)[1]

			print "visited",visited,"heuristic",current_node.h_manhattan()

	def graph_search(self):
		visited = 0
		current_node = node(None,None)
		fringe = []
		closed = []
		while not current_node.is_goal():
			print current_node.h_misplaced()
			for successor in current_node.get_successors():
				if successor not in closed:
					if self._misplaced_heuristic:
						fringe.append((successor.h_misplaced(), successor))
					else:
						fringe.append((successor.h_manhattan(), successor))
			closed.append(current_node)
			visited = visited + 1
			fringe = sorted(fringe)
			current_node = fringe.pop(0)[1]

			print "visited",visited

if __name__ == "__main__":
	agent = greedy_algorithm(False)	
	agent.tree_search()
