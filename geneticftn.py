import random
def compute_fitness(value):
    return 2 * value ** 2 + value
def binary_to_decimal(binary_string):
    return int(binary_string, 2)
def create_population(size, length):
    return [''.join(random.choice('01') for _ in range(length)) for _ in range(size)]
def tournament_selection(population, fitness_scores, tournament_size=3):
    selected = random.sample(list(zip(population, fitness_scores)), tournament_size)
    return max(selected, key=lambda ind: ind[1])[0]
def perform_crossover(parent_a, parent_b):
    point = random.randint(1, len(parent_a) - 1)
    child_a = parent_a[:point] + parent_b[point:]
    child_b = parent_b[:point] + parent_a[point:]
    return child_a, child_b
def apply_mutation(chromosome, mutation_probability=0.01):
    return ''.join(bit if random.random() > mutation_probability else '1' if bit == '0' else '0' for bit in chromosome)
def genetic_algorithm(pop_size, chrom_length, max_gens, mut_prob=0.01, mut_decay=0.99, preserve_elite=True, no_improvement_limit=10):
    population = create_population(pop_size, chrom_length)
    best_solution = None
    best_score = float('-inf')
    no_improvement_count = 0
    for gen in range(max_gens):
        fitness_scores = [compute_fitness(binary_to_decimal(ind)) for ind in population]
        current_best_score = max(fitness_scores)
        current_best_solution = population[fitness_scores.index(current_best_score)]
        if current_best_score > best_score:
            best_score = current_best_score
            best_solution = current_best_solution
            no_improvement_count = 0
        else:
            no_improvement_count += 1
        if no_improvement_count >= no_improvement_limit:
            print(f"Early stopping at generation {gen} due to no improvement.")
            break
        next_gen = []
        if preserve_elite:
            next_gen.append(best_solution)
        while len(next_gen) < pop_size:
            parent_a = tournament_selection(population, fitness_scores)
            parent_b = tournament_selection(population, fitness_scores)
            child_a, child_b = perform_crossover(parent_a, parent_b)
            child_a = apply_mutation(child_a, mut_prob)
            child_b = apply_mutation(child_b, mut_prob)
            next_gen.extend([child_a, child_b])
        population = next_gen[:pop_size]
        mut_prob *= mut_decay
        print(f"Gen {gen}: Best x = {binary_to_decimal(best_solution)}, Best fitness = {best_score}")
    return binary_to_decimal(best_solution), best_score
population_size = 20
chromosome_length = 5
max_generations = 100
mutation_probability = 0.05
mutation_decay_rate = 0.98
optimal_x, optimal_fitness = genetic_algorithm(population_size, chromosome_length, max_generations, mutation_probability, mutation_decay_rate)
print(f"\nFinal optimal solution: x = {optimal_x}, fitness = {optimal_fitness}")
