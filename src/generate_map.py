import json
import matplotlib.pyplot as plt

# 1. Carregando os dados do seu arquivo
with open('melhor_resultado.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

route_whole = data['rota']
hospital = route_whole[0]

# 2. Criando os circuitos fechados (Hospital -> Entregas -> Hospital)
motorcycle = [hospital] + route_whole[1:5] + [hospital]
van = [hospital] + route_whole[5:11] + [hospital]
truck = [hospital] + route_whole[11:21] + [hospital]

# 3. Extraindo as coordenadas (O que você acabou de fazer!)
def extract_coords(list):
    x = [p["local"][0] for p in list]
    y = [p["local"][1] for p in list]
    return x, y

mx, my = extract_coords(motorcycle)
vx, vy = extract_coords(van)
cx, cy = extract_coords(truck)

# 4. Criando o gráfico
plt.figure(figsize=(10, 8))

# Desenhando as rotas
plt.plot(mx, my, label='Moto 01 (Rápida)', color='blue', marker='o', linewidth=2)
plt.plot(vx, vy, label='Van 01 (Mista)', color='green', marker='s', linewidth=2)
plt.plot(cx, cy, label='Caminhão 01 (Volume)', color='red', marker='^', linewidth=1, linestyle='--')

# Destacando o Hospital
plt.plot(hospital["local"][0], hospital["local"][1], 'kX', markersize=15, label='Hospital (Base)')

# Configurações finais
plt.title('Mapa de Rotas Otimizadas - Tech Challenge')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.legend()
plt.grid(True)

# 5. SALVANDO A IMAGEM (Para o seu relatório!)
plt.savefig('mapa_final_rotas.png')
print("Mapa gerado com sucesso: mapa_final_rotas.png")
plt.show()