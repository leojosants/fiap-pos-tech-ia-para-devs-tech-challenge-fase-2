
import random
import math
import json
from typing import Any, List


def generate_random_population(cities_location: List[dict], population_size: int) -> List[List[dict]]:
    """
    Generates a starting population of random delivery routes for the Genetic Algorithm.

    This function separates the fixed starting point (Hospital) from the delivery points,
    shuffles the deliveries to create diversity, and ensures every route begins 
    at the Hospital.

    Args:
        cities_location (List[dict]): A list of dictionaries where the first element 
            is the Hospital (base) and the remaining elements are the delivery points.
        population_size (int): The number of individual routes (chromosomes) to generate.

    Returns:
        List[List[dict]]: A list containing 'population_size' routes, where each route 
            is a list of dictionaries starting with the Hospital.
    """
    hospital = cities_location[0]
    deliveries = cities_location[1:]     
    population = []

    for _ in range(population_size):
        random_route = random.sample(deliveries, len(deliveries))
        complete_route = [hospital] + random_route
        population.append(complete_route)
    
    return population


def calculate_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points.

    The function is flexible and accepts either a dictionary containing 
    a "local" key with (x, y) coordinates or the raw (x, y) coordinates 
    themselves as a list or tuple.

    Args:
        point1 (dict or Iterable): The first point. If a dict, must have a "local" key.
        point2 (dict or Iterable): The second point. If a dict, must have a "local" key.

    Returns:
        float: The straight-line (Euclidean) distance between the two points.
        
    Example:
        >>> calculate_distance({"local": [0, 0]}, {"local": [3, 4]})
        5.0
    """
    p1 = point1["local"] if isinstance(point1, dict) else point1
    p2 = point2["local"] if isinstance(point2, dict) else point2
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def calculate_fitness(path, fleet):
    """
    Calculates the fitness score of a specific path based on distance and priority penalties.

    This function evaluates a candidate solution by splitting the global path into
    individual vehicle routes based on fleet capacity. It calculates the 'Makespan' 
    (maximum distance traveled by any single vehicle) and applies a heavy penalty 
    for late or unfulfilled high-priority deliveries.

    The fitness uses a cubic penalty (priority^3) multiplied by delivery order 
    to ensure that critical points are handled as early as possible in the route.

    Args:
        path (List[dict]): The global sequence of delivery points, starting with the Hospital.
        fleet (List[dict]): A list of vehicle definitions, each containing a 'capacidade' key.

    Returns:
        float: The calculated fitness score. Lower values represent better (more optimized) 
               solutions as they minimize both distance and priority penalties.

    Note:
        The final score is composed of the max vehicle distance plus the weighted 
        total penalty (total_penalty * 20000).
    """

    hospital = path[0]
    vehicle_distances = []
    total_penalty = 0
    delivery_pointer = 1 
    
    for vehicle in fleet:
        capacity_v = vehicle['capacidade']
        deliveries_v = path[delivery_pointer : delivery_pointer + capacity_v]
        
        if not deliveries_v:
            vehicle_distances.append(0)
            continue

        complete_route = [hospital] + deliveries_v + [hospital]
        
        dist_v = 0
        for i in range(len(complete_route) - 1):
            dist_v += calculate_distance(complete_route[i], complete_route[i+1])
        
        vehicle_distances.append(dist_v)
        
        for idx, delivery in enumerate(deliveries_v):
            priority = delivery.get("prioridade", 0)
            total_penalty += (priority**3 * (idx + 1))
            
        delivery_pointer += capacity_v 

    # Makespan + Penalidade
    return max(vehicle_distances) + (total_penalty * 20000)


def order_crossover(parent1, parent2):
    """
    Performs Order Crossover (OX) between two parent routes to create a child.

    The Order Crossover is a permutation-based operator that maintains the 
    relative order of cities from Parent 1 (the slice) and fills the remaining 
    positions with genes from Parent 2, avoiding duplicates. This ensures 
    valid delivery routes where each location is visited exactly once.

    The Hospital (index 0) is preserved as the starting point for all routes.

    Args:
        parent1 (List[dict]): The first parent route (sequence of locations).
        parent2 (List[dict]): The second parent route (sequence of locations).

    Returns:
        List[dict]: A new child route starting with the Hospital, combining 
            traits from both parents.

    Steps:
        1. Keep the Hospital at index 0.
        2. Select a random subset (slice) from Parent 1 and copy it to the child.
        3. Fill the remaining empty slots with the elements of Parent 2 
           in the order they appear, skipping those already in the child.
    """

    hospital = parent1[0]
    p1_delivery = parent1[1:]
    p2_delivery = parent2[1:]
    
    length = len(p1_delivery)
    if length == 0: return [hospital]

    start_index = random.randint(0, length - 1)
    end_index = random.randint(start_index + 1, length)

    child_delivery = [None] * length
    child_delivery[start_index:end_index] = p1_delivery[start_index:end_index]

    p2_remaining = [gene for gene in p2_delivery if gene not in child_delivery]
    
    curr = 0
    for i in range(length):
        if child_delivery[i] is None:
            child_delivery[i] = p2_remaining[curr]
            curr += 1

    return [hospital] + child_delivery


def mutate(solution: List[Any], mutation_probability: float) -> List[Any]:
    """
    Applies Inversion Mutation to a candidate solution to maintain genetic diversity.

    This function introduces random variations into the population. If the 
    mutation trigger is met, it performs three consecutive segment inversions 
    (reversing a sub-route). This process helps the algorithm escape local 
    minima by "shaking up" the delivery sequence while strictly preserving 
    the Hospital at index 0.

    Args:
        solution (List[Any]): The current route (list of locations) to be mutated.
        mutation_probability (float): A value between 0 and 1 representing the 
            chance of mutation occurring.

    Returns:
        List[Any]: The mutated route if the probability check passed, 
            otherwise the original route.

    Note:
        The function specifically samples indices starting from 1 to ensure 
        the Hospital (index 0) is never displaced during the inversion.
    """
    mutated_solution = list(solution) 

    # 1. Verificamos se a mutação vai ocorrer (com base na probabilidade)
    if random.random() < mutation_probability:
        # 2. Precisamos de pelo menos 3 itens para inverter um trecho (hospital + 2 cidades)
        if len(solution) < 3: 
            return solution
        
        # 3. Fazemos 3 tentativas de inversão para garantir uma boa "sacudida" na rota
        for _ in range(3):
            # Sorteamos 2 índices ignorando o hospital (índice 0)
            points = random.sample(range(1, len(mutated_solution)), 2)
            points.sort()
            i, j = points
            
            # 4. A mágica da inversão: o trecho de i até j é invertido 🔄
            mutated_solution[i:j] = mutated_solution[i:j][::-1]
            
    return mutated_solution


def sort_population(population: List[Any], fitness: List[float]):
    """
    Sorts the population and their corresponding fitness scores in ascending order.

    This function pairs each candidate route with its fitness value, sorts the 
    entire population from best to worst (lower fitness values are better in 
    this minimization problem), and then unpacks them back into two separate lists.

    Args:
        population (List[Any]): A list of routes (individuals) currently in the generation.
        fitness (List[float]): A list of numerical scores representing the quality 
            of each route in the 'population' list.

    Returns:
        Tuple[List[Any], List[float]]: A tuple containing:
            - The sorted list of routes (best to worst).
            - The sorted list of fitness scores (lowest to highest).

    Note:
        Since the goal is to minimize distance and penalties, the sorting 
        is performed in ascending order (min to max).
    """
    combined_lists = list(zip(population, fitness))
    sorted_combined_lists = sorted(combined_lists, key=lambda x: x[1])
    sorted_population, sorted_fitness = zip(*sorted_combined_lists)
    return list(sorted_population), list(sorted_fitness)


def get_nearest_neighbor(current_city, unvisited_cities):
    """
    Identifies the closest city to the current location from a list of unvisited cities.

    This is a core component of the Nearest Neighbor heuristic. It performs 
    a linear search through all remaining cities to find the one with the 
    minimum Euclidean distance relative to the current position.

    Args:
        current_city (dict or tuple): The starting point or current location 
            of the vehicle.
        unvisited_cities (List[dict] or List[tuple]): A list of candidate 
            locations that have not yet been included in the route.

    Returns:
        dict or tuple: The city object/coordinates that are geographically 
            closest to the 'current_city'. Returns None if 'unvisited_cities' is empty.

    Complexity:
        O(n), where n is the number of unvisited cities.
    """

    nearest_city = None
    min_dist = float('inf')
    
    for city in unvisited_cities:
        # Precisamos calcular a distância entre a cidade atual e a cidade do loop
        dist = calculate_distance(current_city, city)
        
        # Se a distância for menor que a mínima encontrada até agora...
        if dist < min_dist:
            min_dist = dist
            nearest_city = city
            
    return nearest_city


def generate_nearest_neighbor_path(cities_location):
    """
    Constructs a complete delivery route using the Nearest Neighbor (Greedy) heuristic.

    Starting from the Hospital (base), the algorithm iteratively builds a path by 
    selecting the geographically closest unvisited city at each step. This provides 
    a fast, intuitive solution that serves as a baseline for more advanced 
    optimization methods like Genetic Algorithms.

    Args:
        cities_location (List[dict]): A list of location dictionaries where index 0 
            is the Hospital and subsequent indices are delivery points.

    Returns:
        List[dict]: A complete route starting with the Hospital and visiting all 
            delivery points exactly once, ordered by proximity.

    Process:
        1. Initialize the path with the Hospital.
        2. Identify the nearest unvisited city from the current location.
        3. Append the city to the path and remove it from the unvisited pool.
        4. Repeat until all cities are visited.
    """

    unvisited = cities_location[1:]  # Todas as entregas (exceto o hospital)
    current_city = cities_location[0] # Começamos no Hospital 🏥
    path = [current_city]

    while unvisited:
        # 1. Encontra a mais próxima
        next_city = get_nearest_neighbor(current_city, unvisited)
        
        # 2. Adiciona ao caminho
        path.append(next_city)
        
        # 3. Remove das disponíveis
        unvisited.remove(next_city)
        
        # 4. Define onde o motorista está agora
        current_city = next_city

    return path


def save_best_result(generation, fitness, path, filename="melhor_resultado.json"):
    """
    Exports the optimal route and metadata to a JSON file for post-processing.

    This function serializes the best candidate solution found by the Genetic 
    Algorithm, including the final generation count, the best fitness score 
    (distance/penalty), and the complete ordered list of delivery locations.

    Args:
        generation (int): The index of the generation where the best result was found.
        fitness (float): The final fitness score (distance + penalties) of the route.
        path (List[dict]): The ordered list of city/hospital dictionaries representing 
            the optimized route.
        filename (str, optional): The target file path for the JSON export. 
            Defaults to "melhor_resultado.json".

    Returns:
        None: The function writes directly to the filesystem and prints a 
            confirmation message.

    Usage in Pipeline:
        The output JSON is designed to be consumed by 'gerar_mapa.py' for 
        visualization and by LLM prompts for mission briefing generation.
    """
    
    # Criamos um dicionário com as informações que você considerou importantes
    dados_para_salvar = {
        "geracao_final": generation,
        "melhor_distancia": round(fitness, 2),
        "rota": path  # A lista de dicionários das cidades
    }
    
    # Abrimos o arquivo em modo de escrita ('w')
    with open(filename, "w", encoding="utf-8") as f:
        # dump transforma o dicionário em texto JSON
        json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)
    
    print(f"\n💾 Resultado salvo com sucesso em: {filename}")

    