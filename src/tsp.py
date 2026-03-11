import pygame
from pygame.locals import *
import random
import itertools
from src.genetic_algorithm import mutate, order_crossover, generate_random_population, calculate_fitness, sort_population, generate_nearest_neighbor_path, save_best_result
from src.draw_functions import draw_paths, draw_plot, draw_cities
import sys
from config.config import *


# GAo que sugere?
N_CITIES = 15

cities_locations = HOSPITAL_DELIVERIES

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP Solver using Pygame")
clock = pygame.time.Clock()
generation_counter = itertools.count(start=1)  # Start the counter at 1

# Create Initial Population
# TODO:- use some heuristic like Nearest Neighbour our Convex Hull to initialize
# 1. Criamos o "atleta de elite" usando a heurística
melhor_inicial = generate_nearest_neighbor_path(HOSPITAL_DELIVERIES)

# 2. Criamos o restante da população de forma aleatória
# Note que pedimos POPULATION_SIZE - 1
populacao_restante = generate_random_population(HOSPITAL_DELIVERIES, POPULATION_SIZE - 1)

# 3. Juntamos tudo
population = [melhor_inicial] + populacao_restante
# population = generate_random_population(cities_locations, POPULATION_SIZE)
best_fitness_values = []
best_solutions = []


# Main game loop
running = True
generation = 0
# Definindo o infinito e o contador
melhor_fitness_global = float('inf')
contador_estagnacao = 0

while running and generation <= 1000:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    generation = next(generation_counter)

    screen.fill(WHITE)

    population_fitness = [calculate_fitness(
        individual, FLEET) for individual in population]

    population, population_fitness = sort_population(
        population,  population_fitness)

    best_fitness = calculate_fitness(population[0], FLEET)

    # Se o fitness atual for melhor que o nosso recorde...
    if best_fitness < melhor_fitness_global:
        melhor_fitness_global = best_fitness
        contador_estagnacao = 0  # Resetamos a paciência! 🔄
    else:
        # Se não melhorou (ou seja, é igual ou pior)...
        contador_estagnacao += 1 # Adicionamos +1 ⏳

    if contador_estagnacao == 100:
        break

    best_solution = population[0]
    best_fitness_values.append(best_fitness)
    best_solutions.append(best_solution)
    posicao_grafico = (800, 50)

    draw_plot(
        screen, list(range(len(best_fitness_values))),
        best_fitness_values, y_label="Fitness - Distance (pxls)",
        position=posicao_grafico
    )

    draw_cities(screen, cities_locations, RED, NODE_RADIUS)
    
    # draw_paths(screen, best_solution, BLUE, width=3)
    # Definimos as cores para cada tipo de veículo
    # Moto = Azul, Van = Vermelho, Caminhão = Preto
    cores_veiculos = [BLUE, RED, BLACK] 
    ponteiro = 1

    for i, veiculo in enumerate(FLEET):
        capacidade = veiculo['capacidade']
        
        # 1. Pegamos a "fatia" das entregas deste veículo
        entregas_v = best_solution[ponteiro : ponteiro + capacidade]
        
        if entregas_v:
            # 2. Criamos a rota completa: Hospital -> Entregas -> Hospital
            rota_v = [best_solution[0]] + entregas_v + [best_solution[0]]
            
            # 3. Desenhamos a linha com a cor correspondente
            draw_paths(screen, rota_v, cores_veiculos[i], width=3)
        
        # 4. Movemos o ponteiro para o início das entregas do próximo veículo
        ponteiro += capacidade

    draw_paths(screen, population[1], rgb_color=(128, 128, 128), width=1)

    print(f"Generation {generation}: Best fitness = {round(best_fitness, 2)}")

    new_population = [population[0]]  # Keep the best individual: ELITISM

    while len(new_population) < POPULATION_SIZE:
        # Sorteio para o Pai 1
        competidores1 = random.sample(population, k=3)
        parent1 = min(competidores1, key=lambda ind: calculate_fitness(ind, FLEET))
        
        # Sorteio para o Pai 1
        competidores2 = random.sample(population, k=3)
        parent2 = min(competidores2, key=lambda ind: calculate_fitness(ind, FLEET))

        child1 = order_crossover(parent1, parent2)
        child1 = mutate(child1, MUTATION_PROBABILITY)

        new_population.append(child1)

    population = new_population

    pygame.display.flip()
    clock.tick(FPS)


print("\n--- 🏁 Simulação Finalizada ---")

# Verificamos por que o loop parou
if contador_estagnacao >= 100:
    print(f"🛑 Critério de parada: Estagnação (o fitness não melhorou por 100 gerações).")
else:
    print(f"✅ Critério de parada: Limite de 1000 gerações atingido.")

print(f"📈 Geração final: {generation}")
print(f"🏆 Melhor distância encontrada: {round(melhor_fitness_global, 2)} pixels")

# TODO: save the best individual in a file if it is better than the one saved.
save_best_result(generation, melhor_fitness_global, population[0])

# exit software
pygame.quit()
sys.exit()