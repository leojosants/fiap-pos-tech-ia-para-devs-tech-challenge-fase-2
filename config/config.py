# --- Configurações de Tela (Pygame) ---
WIDTH, HEIGHT = 1200, 700
NODE_RADIUS = 10
FPS = 30
PLOT_X_OFFSET = 400

# --- Configurações do Algoritmo Genético ---
POPULATION_SIZE = 200
N_GENERATIONS = 1000
MUTATION_PROBABILITY = 0.6
LIMIT_STAGNATION = 150

# --- Cores (RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)     
ORANGE = (255, 165, 0)  

# --- Dados do Problema ---
HOSPITAL_DELIVERIES = [
    {"id": "Hospital",    "local": (400, 300), "tipo": "inicio",  "prioridade": 0},
    {"id": "Posto A",     "local": (450, 250), "tipo": "critico",  "prioridade": 10},
    {"id": "Clinica B",   "local": (550, 150), "tipo": "regular",  "prioridade": 2},
    {"id": "Farmacia C",  "local": (600, 400), "tipo": "critico",  "prioridade": 10},
    {"id": "Posto D",     "local": (700, 100), "tipo": "regular",  "prioridade": 2},
    {"id": "Unidade E",   "local": (200, 100), "tipo": "critico",  "prioridade": 10},
    {"id": "Centro F",    "local": (100, 450), "tipo": "regular",  "prioridade": 2},
    {"id": "Lab G",       "local": (300, 500), "tipo": "regular",  "prioridade": 2},
    {"id": "Posto H",     "local": (650, 350), "tipo": "critico",  "prioridade": 10},
    {"id": "UPA I",       "local": (500, 550), "tipo": "critico",  "prioridade": 10},
    {"id": "Clinica J",   "local": (50, 200),  "tipo": "regular",  "prioridade": 2},
    {"id": "Farmacia K",  "local": (750, 500), "tipo": "regular",  "prioridade": 2},
    {"id": "Posto L",     "local": (400, 50),  "tipo": "critico",  "prioridade": 10},
    {"id": "Centro M",    "local": (250, 250), "tipo": "regular",  "prioridade": 2},
    {"id": "Lab N",       "local": (600, 50),  "tipo": "regular",  "prioridade": 2},
    {"id": "Unidade O",   "local": (150, 350), "tipo": "critico",  "prioridade": 10},
    {"id": "Posto P",     "local": (700, 450), "tipo": "regular",  "prioridade": 2},
    {"id": "Clinica Q",   "local": (350, 450), "tipo": "regular",  "prioridade": 2},
    {"id": "Farmacia R",  "local": (50, 550),  "tipo": "critico",  "prioridade": 10},
    {"id": "Posto S",     "local": (200, 550), "tipo": "regular",  "prioridade": 2},
]

FLEET = [
    {"id": "Moto_01", "capacidade": 4},
    {"id": "Van_01", "capacidade": 6},
    {"id": "Caminhao_01", "capacidade": 10}
]