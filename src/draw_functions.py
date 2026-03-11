# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:03:11 2023

@author: SérgioPolimante
"""
import pylab
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib
import pygame
from typing import List, Tuple

matplotlib.use("Agg")


# def draw_plot(screen: pygame.Surface, x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness') -> None:
def draw_plot(screen: pygame.Surface, x: list, y: list, x_label: str = 'Generation', y_label: str = 'Fitness', position: Tuple[int, int] = (0, 0)) -> None:
    """
    Draw a plot on a Pygame screen using Matplotlib.

    Parameters:
    - screen (pygame.Surface): The Pygame surface to draw the plot on.
    - x (list): The x-axis values.
    - y (list): The y-axis values.
    - x_label (str): Label for the x-axis (default is 'Generation').
    - y_label (str): Label for the y-axis (default is 'Fitness').
    """
    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
    ax.plot(x, y)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    # raw_data = renderer.tostring_rgb()
    raw_data = canvas.buffer_rgba()

    # size = canvas.get_width_height()
    # surf = pygame.image.fromstring(raw_data.tobytes(), size, "RGBA")

    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data.tobytes(), size, "RGBA")
    # screen.blit(surf, (0, 0))
    screen.blit(surf, position)
    

def draw_cities(screen: pygame.Surface, cities_locations: List[Tuple[int, int]], rgb_color: Tuple[int, int, int], node_radius: int) -> None:
    """
    Draws circles representing cities on the given Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface on which to draw the cities.
    - cities_locations (List[Tuple[int, int]]): List of (x, y) coordinates representing the locations of cities.
    - rgb_color (Tuple[int, int, int]): Tuple of three integers (R, G, B) representing the color of the city circles.
    - node_radius (int): The radius of the city circles.

    Returns:
    None
    """
    # for city_location in cities_locations:
    #     pygame.draw.circle(screen, rgb_color, city_location, node_radius)

    for city in cities_locations:
        # Extraímos a tupla (x, y) da chave "local"
        posicao = city["local"]
        pygame.draw.circle(screen, rgb_color, posicao, node_radius)



def draw_paths(screen: pygame.Surface, path: List[dict], rgb_color: Tuple[int, int, int], width: int = 1):
    """
    Draw a path on a Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface to draw the path on.
    - path (List[Tuple[int, int]]): List of tuples representing the coordinates of the path.
    - rgb_color (Tuple[int, int, int]): RGB values for the color of the path.
    - width (int): Width of the path lines (default is 1).
    """

    # Criamos a lista de coordenadas extraindo o "local" de cada entrega
    coords_apenas = [entrega["local"] for entrega in path]

    pygame.draw.lines(screen, rgb_color, True, coords_apenas, width=width)


def draw_text(screen: pygame.Surface, text: str, position: Tuple[int, int], color: pygame.Color) -> None:
    """
    Renders arbitrary text on the Pygame surface.
    This function initializes the font module, creates a text surface using the Arial font, and draws it at the specified position.
    Args:
    screen(pygame.Surface): The surface (window) where the text will be drawn.
    text(str): The text content to be displayed.
    position(Tuple[int, int]): Coordinates (x, y) of the upper left corner of the text.
    color(pygame.Color): The text color in RGB format or pygame.Color object.
    Returns:
    None: The function performs the drawing directly on the 'screen' (inplace).
    """
    pygame.font.init()
    font_size = 15
    my_font = pygame.font.SysFont('Arial', font_size)
    text_surface = my_font.render(text, True, color)
    screen.blit(text_surface, position)
