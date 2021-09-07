class State:
    def __init__(self,state,father,movement):
        self.state=state
        self.father=father
        self.movement=movement
        if self.state:
            self.map=''.join(str(state) for state in self.state)
    
    def __eq__(self,goal_state):
        return self.map == goal_state.map
    
    def __lt__(self,goal_state):
        return self.map<goal_state.map
