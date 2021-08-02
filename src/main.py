import time
import os 

def main():

    # função gerar grafo nós e arestas do grafo
    
    print("Graph with {} nodes and {} edges".format(n, m))
    
    '''set the simulated annealing algorithm params'''
    temp_initial = 100000
    stopping_temp = 0.0001
    alpha = 0.7
    stopping_iter = m-n

    '''start time'''
    start_time = time.time()
    
    '''run simulated annealing'''
    sa = SimulatedAnnealing(G, temp_initial, alpha, stopping_temp, stopping_iter, matrix_cost, B, start_time)
    sa.anneal()
    
    '''show the improvement'''
    sa.print_solution(start_time)

    # '''ploting solution'''
    
if __name__ == "__main__":
    main()




