import timeit
# import numpy as np
from math import factorial
from collections import deque
from state import State
from random import randint

empty_list=[0,0,0,0]
initial_state = list()
objective_state = list()
objective_node = State
comparative_node=State(empty_list,None,None)
movements = list()
lenght = 0
side = 0
expanded_nodes = 0



def reset_values():
    global empty_list,initial_state,objective_state,objective_node,comparative_node,movements,lenght,side,expanded_nodes
    empty_list=[0,0,0,0]
    initial_state = list()
    objective_state = list()
    objective_node = State
    comparative_node=State(empty_list,None,None)
    movements = list()
    lenght = 0
    side = 0
    expanded_nodes = 0

def move(state, position):
    new_state = state[:]
    index = new_state.index(0)
    if position == 1:  # Arriba
        if index not in range(0, side):
            auxiliary = new_state[index - side]
            new_state[index - side] = new_state[index]
            new_state[index] = auxiliary
            return new_state
        else:
            return None
    if position == 2:  # Abajo
        if index not in range(lenght - side, lenght):
            auxiliary = new_state[index + side]
            new_state[index + side] = new_state[index]
            new_state[index] = auxiliary
            return new_state
        else:
            return None
    if position == 3:  # Izquierda
        if index not in range(0, lenght, side):
            auxiliary = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = auxiliary
            return new_state
        else:
            return None
    if position == 4:  # Derecha
        if index not in range(side - 1, lenght, side):
            auxiliary = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = auxiliary
            return new_state
        else:
            return None


def expand(node):
    global expanded_nodes
    expanded_nodes += 1
    neighbors = list()
    neighbors.append(State(move(node.state, 1), node, 1))
    neighbors.append(State(move(node.state, 2), node, 2))
    neighbors.append(State(move(node.state, 3), node, 3))
    neighbors.append(State(move(node.state, 4), node, 4))
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes

def get_total_states(initial_state):
    length=len(initial_state)
    return factorial(length)

def modify_initial_state(initial_state):
    state=State(initial_state,None,None)
    i=1
    while i<=4:
        auxiliary_state=move(state.state,i)
        if auxiliary_state!=None:
            i=5
        else:
            i+=1
    return auxiliary_state

def modify_official_state(initial_state):
    initial_state += [initial_state.pop(0)]
    initial_state += [initial_state.pop(1)]
    return initial_state

def state_space(initial_state):
    global objective_node,expanded_nodes
    explored = set()
    queuee = deque([State(initial_state, None, None)])
    limite=get_total_states(initial_state)
    while queuee and expanded_nodes<limite:
        node = queuee.pop()
        explored.add(node.map)
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)
    estado_perturbado=modify_official_state(initial_state)
    queuee = deque([State(estado_perturbado, None, None)])
    while queuee and expanded_nodes<limite:
        node = queuee.pop()
        explored.add(node.map)
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)
    



def bfs(initial_state, objective_state):
    global objective_node
    explored = set()
    queuee = deque([State(initial_state, None, None)])
    while queuee:
        node = queuee.popleft()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return queuee
        neighbors = expand(node)
        for neighbor in neighbors:
            if neighbor.map not in explored:
                queuee.append(neighbor)
                explored.add(neighbor.map)


def dfs(initial_state, objective_state):
    global objective_node
    explored = set()
    stack = list([State(initial_state, None, None)])
    while stack:
        node = stack.pop()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return stack
        neighbors = reversed(expand(node))
        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)


def non_recursive_dls(initial_state, objective_state, limit):
    global objective_node
    explored = set()
    stack = list([State(initial_state, None, None)])
    cont = 0
    while stack:
        node = stack.pop()
        explored.add(node.map)
        if node.state == objective_state:
            objective_node = node
            return stack 
        if cont < limit:
            neighbors = reversed(expand(node))
            for neighbor in neighbors:
                if neighbor.map not in explored:
                    stack.append(neighbor)
                    explored.add(neighbor.map)
        cont += 1
        if cont == limit:
            stack = []
            return "CUTOFF"


def id(initial_state, objective_state):
    global objective_node
    i = 1000000000
    while i < 100000000000:
        result = non_recursive_dls(initial_state, objective_state, i)
        if result == 'CUTOFF':
            i += 1
        else:
            i = 100000000000
    return result


def path():
    actual_node = objective_node
    while initial_state != actual_node.state:
        if actual_node.movement == 1:
            movement = 'Up'
        elif actual_node.movement == 2:
            movement = 'Down'
        elif actual_node.movement == 3:
            movement = 'Left'
        else:
            movement = 'Right'
        movements.insert(0, movement)
        actual_node = actual_node.father
    return movements


    



def show_results(time):
    global movements
    if objective_node != comparative_node:
        movements = path()
        print("---------------------------------------------------------------------------------------------------------------------------")
        print()
        print("RESULTS")
        print("Steps: "+str(movements))
        print("Number of steps: "+str(len(movements)))
        print("Number of expanded nodes: "+str(expanded_nodes))
        print("Time run: " + format(time, '.8f'))
        print()
        print("---------------------------------------------------------------------------------------------------------------------------")
    else :
        print("Doesn't exist solution :C")


    

def read_random_state(inicial):
    global lenght, side
    initial_state.clear()
    objective_state.clear()
    for element in inicial:
        initial_state.append(int(element))
    lenght = len(initial_state)
    side = int(lenght**0.5)
    cont = 0
    while cont < lenght:
        objective_state.append(int(cont))
        cont += 1


def read_states(inicial, end):
    global lenght, side
    initial_state.clear()
    objective_state.clear()
    for element in inicial:
        initial_state.append(int(element))
    lenght = len(initial_state)
    side = int(lenght**0.5)
    for elementII in end:
        objective_state.append(int(elementII))


def map_list(lista):
    return list(map(int, lista))


def read_file_txt(name, limit):
    data = []
    aux = 1
    with open(str(name)+'.txt') as fname:
        for lines in fname:
            if limit == aux:
                data.extend(lines.split())
            aux += 1
    return data


def read_of_file(name):
    initial_state = []
    objective_state = []
    i = 0
    while i < 2:
        if i == 0:
            initial_state = read_file_txt(name, 1)
        if i == 1:
            objective_state = read_file_txt(name, 2)
        i += 1
    initial_state = map_list(initial_state)
    objective_state = map_list(objective_state)
    read_states(initial_state, objective_state)


def generate_random_board(length):
    initial_state_aux = []
    cont = 0
    while cont <= (length*length-1):
        random_number = randint(0, (length*length)-1)
        if random_number in initial_state_aux:
            pass
        else:
            initial_state_aux.append(random_number)
            cont += 1
    return initial_state_aux




def sub_main(length):
    option = 0
    random = generate_random_board(length)
    read_random_state(random)
    print("Resolve puzzle")
    print(initial_state)
    print("Target state if a search function is chosen")
    print(objective_state)
    generate_random_board(length)
    print("Choose an option")
    print("1)Resolve BFS")
    print("2)Resolve DLS")
    print("3)Resolve dfs")
    print("4)Resolve Iterative Deepening")
    print("5)Take a total number of states")
    print("Please choose an option: ")
    option = int(input())
    if option == 1:
        start = timeit.default_timer()
        bfs(initial_state, objective_state)
        end = timeit.default_timer()
        show_results(end-start)
    if option == 2:
        start = timeit.default_timer()
        answer = non_recursive_dls(initial_state, objective_state, 181440)
        if answer == "CUTOFF":
            print("No solution was found at the limit")
        else:
            end = timeit.default_timer()
            show_results(end-start)
    if option == 3:
        start = timeit.default_timer()
        dfs(initial_state, objective_state)
        end = timeit.default_timer()
        show_results(end-start)
    if option == 4:
        start = timeit.default_timer()
        answer = id(initial_state, objective_state)
        if answer == "CUTOFF":
            print("No solution was found at the limit")
        else:
            end = timeit.default_timer()
            show_results(end-start)
    if option==5:
        start = timeit.default_timer()
        state_space(initial_state)
        end = timeit.default_timer()
        print("The total number of states is: "+str(expanded_nodes))
        print("Run time: " + format(end-start, '.8f'))




def main():
    
    option = 1
    while option >= 1 and option <= 6:
        
        print("Welcome to N puzzle")
        print("1)Read the file")
        print("2)Resolve BFS")
        print("3)Resolve DLS")
        print("4)Resolve dfs")
        print("5)Resolve Iterative Deepening")
        print("6)Randomly test")
        print("Please choose an option: ")
        option = int(input())
        if option == 1:
            print("Put the name of the file")
            name = input()
            read_of_file(name)
        if option == 2:
            start = timeit.default_timer()
            bfs(initial_state, objective_state)
            end = timeit.default_timer()
            show_results(end-start)
        if option == 3:
            start = timeit.default_timer()
            answer = non_recursive_dls(initial_state, objective_state, 181440)
            if answer == "CUTOFF":
                print("No solution was found at the limit")
            else:
                end = timeit.default_timer()
                show_results(end-start)
        if option == 4:
            start = timeit.default_timer()
            dfs(initial_state, objective_state)
            end = timeit.default_timer()
            show_results(end-start)
        if option == 5:
            start = timeit.default_timer()
            answer = id(initial_state, objective_state)
            if answer == "CUTOFF":
                print("No solution was found at the limit")
            else:
                end = timeit.default_timer()
                show_results(end-start)
        if option == 6:
            print("Put the size of the matrix: ")
            lenght = int(input())
            sub_main(lenght)


if __name__ == '__main__':
    main()
