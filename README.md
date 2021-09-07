#                                                           Second practice IS
### Mauricio Balderrama
### Mercedes La Fuente
### Juan Luis Canedo
### Experiment I
### Description of the problem: 
      Expand states using (n^2-1)-puzzle1 where n=2, Report the number of states generated 
### Solution description: 
      A set of actions is performed, moving tiles to the blank space (up, down, right, left) without repeating the already existing state by generating the whole state space             manually on a sheet of paper.
### Results:
      We did two experiments, the first one starting with an initial state that resulted in 12 states leading to the target state, however the total number of possible states is         24 but 12 do not lead to the target state.


      For n = 2: generate the entire state space manually on a sheet of paper (or a word document). Scan this sheet (or take a clear photo of it) and include it in your report.         How many states are there?
            Applying the formula = (2*2)!/2 -> 12 (Possible states leading to the goal)
            Total number of states regardless of a possible target state=(2*2)!=24
### Number of state space with solution
![IMG-20210906-WA0028](https://user-images.githubusercontent.com/74753713/132289724-2791c9ad-b323-4f9a-9b3d-63a28be524e3.jpeg)


#### Total number of state space
![States](https://user-images.githubusercontent.com/74753713/132142994-1844ef15-4da8-4544-a909-16b29633c9b8.png)

### Conclusions: 
      With n=2 A tree is generated whose size is not exponential. The total number of expanded states does not always lead to the target state.


### Experiment II
### Description of the problem: 
      Expand states using (n^2-1)-puzzle1 where n=3, Report the number of states generated 
### Solution description: 
      Generate the entire state space using a computer program, Select a randomly generated initial state and expand it, taking care not to expand nodes that were previously             expanding nodes that already exist
### Results: 
      The random state generated to solve [8,4,6,2,5,3,7,0,1] and the number of total states is 362880 and its execution time 4.23303260 seconds
### Conclusions: 
      Based on the result of the total number of states of the experiment it is also possible to check with the formula n! that the result is as expected and not optimal due to         slow execution time 

### Experiment III
### Description of the problem: 
      Expand states using (n^2-1)-puzzle1 where n=4, Compares run time and space
### Solution description: 
      Generate the entire state space using a computer program with the algorithms: BFS and Iterative Deepening, Select an initial state and a target state which can be reached by       executing a set of actions 
### Results: 
      Initial state: [1 2 3 0 4 5 6 7 8 9 10 11 12 13 14 15], Target status: [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
      BFS: execution time 0.00038860 seconds , expanded nodes 16 to reach the target state and performs 3 steps in total.
      The execution time of Iterative Deepening takes too long so we do not have an exact result.  
### Conclusions: 
      BFS is optimal because it is complete by guaranteeing a solution if it exists, the execution time and space is exponential. Iterative Deepening consumes a lot of memory
      BFS uses less memory because the number of states it expands is smaller than Iterative Deepening.

### Bibliography:
      Class slides, Code reference: https://github.com/speix/8-puzzle-solver














# N-puzzle
### Problem-Solver Agent

### Objective Formulation:
      The first box has to be free and the numbers have to be ordered from least to greatest

### Problem Formulation:

### Initial State:
      Messy array with an empty space anywhere
      
![8-Puzzle](https://user-images.githubusercontent.com/74753713/132054522-fc84e30a-10ad-4ab8-b0db-c76c92a4af37.png)







### Objective State:
      Ordered matrix with last empty space
 
![8-Puzzle - copia](https://user-images.githubusercontent.com/74753713/132054536-42d15fd9-cb60-4c35-842d-28dffc1354c5.png)



### Test of Objective:
      The matrix is ordered from least to greatest with the first empty space?
 
### Actions:
      Moven Up
      Move Down
      Move Right
      Move Left



### Cost:
      1 Until you reach the goal
  
  
### NOTAS IMPORTANTES
      -El codigo inicialmente fue programado en español, pero al tratar de modificarlo para su traduccion en ingles ocasiono problemas con choques de variables de python lo cual 
       provoco que el programa no se ejecute correctamente por el factor tiempo no se lo pudo arreglar pero se envia el codigo en español el cual se ejecuta correctamente sin      fallas
      -Es importante poder verificar si se tiene instalada algunas herramientas de python en caso de no tenerlas instalar desde la línea de comandos con pip install "nombre"
      -Hay que tener suma precaución al inicializar estados finales y objetivos desde el menú principal dado que son variables globales y estas pueden provocar a veces errores por sobre escritura 
