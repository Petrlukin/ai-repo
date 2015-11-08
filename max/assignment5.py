import copy
import sys
import time

class actions:
	LEFT = (0,-1)
	UP = (-1,0)
	RIGHT = (0,1)
	DOWN = (1,0)

class node:
	def __init__(self, parent, action):
		if id(parent) == id(None):
			self._state = [[1,4,8],[3,6,2],[0,5,7]]
		else:
			self._parent = parent
			self._state = copy.deepcopy(parent.get_state())
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
		self._update_state_map()
		if action != None:
			null_index = self._state_map[0]
			target_index = (null_index[0] + action[0], null_index[1] + action[1])
			self._state[null_index[0]][null_index[1]] = self._state[target_index[0]][target_index[1]] 
			self._state[target_index[0]][target_index[1]] = 0
			self._update_state_map()

	def get_state(self):
		return self._state

	def get_state_map(self):
		return self._state_map

	def print_state(self):
		for line in self.get_state():
			print line[0],line[1],line[2]

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

	def _h_manhattan(self):
		manhattan = 0
		for row in self._state:
			for field in row:
				if field != 0:
					actual_coords = self._state_map[field]
					target_coords = self._goal_state_map[field]
					manhattan = manhattan + abs(actual_coords[0] - target_coords[0]) + abs(actual_coords[1] - target_coords[1])
		return manhattan

	def _h_misplaced(self):
		misplaced = 0
		for row in self._state:
			for field in row:
				if field != 0:
					if self._state_map[field] != self._goal_state_map[field]:
						misplaced = misplaced + 1
		return misplaced

	def heuristic(self,misplaced):
		if misplaced:
			return self._h_misplaced()
		else:
			return self._h_manhattan()

	def is_goal(self):
		if self._state_map == self._goal_state_map:
			return True
		else:
			return False

class greedy_algorithm:
	def __init__(self, misplaced):
		self._heuristic = misplaced

	def graph_search(self):
		visited = 0
		initial_node = node(None,None)
		frontier = [(0,initial_node)]
		explored = []

		while len(frontier) > 0:
			current_node = frontier.pop(0)[1]
			current_node.print_state()
			print current_node.heuristic(self._heuristic),"\n"
			if current_node.is_goal():
				print "Goal found","visited",visited,"nodes"
				return 0

			explored.append(current_node)
			frontier_nodes = [tuple_[1] for tuple_ in frontier]
			for successor in current_node.get_successors():
				if successor not in explored and successor not in frontier_nodes:
					frontier.append((successor.heuristic(self._heuristic), successor))

			visited = visited + 1
			frontier = sorted(frontier)

			# ------ FOR OUTPUT ONLY ------
			# if set to True, frontier will be printed after every insertion of successor nodes
			if False:
				frontier_nodes = [tuple_[1] for tuple_ in frontier]
				for i in range(3):
					for nodes in frontier_nodes:
						state = nodes.get_state()
						print state[i][0],state[i][1],state[i][2]," ",
					print ""
				for nodes in frontier_nodes:
					print nodes.heuristic(self._heuristic),
				print ""
				raw_input("Waiting for ENTER")
			# -----------------------------

		print "visited",visited,"nodes"

if __name__ == "__main__":
	h = int(raw_input("Which heuristic? Misplaced (1), Manhattan (0) "))
	if h not in [0,1]:
		print "Wrong input!"
		sys.exit()
	agent = greedy_algorithm(h)	
	before = time.clock()
	agent.graph_search()
	after = time.clock()
	print "Time:", after - before,"s"

