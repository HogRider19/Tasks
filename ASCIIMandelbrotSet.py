"""
Implement mandelbrot_string(x, y, x_radius, y_radius, stepsize, max_iter) which returns
a visualization of the mandelbrot set. Every line (but the final line) ends in an addiotinal
newline character "\n" which makes the amount of chars of the
returned string: n  = (x_radius*2+1+1) * (y_radius*2+1) - 1
"""

import math


def is_mandelbrot_point(x: float, y: float, max_iter: int) -> str:
    grathic_map = {
        0: ' ', 1: '░', 2: '▒',
        3: '▓', 4: '█',}

    iteration = 0
    z_r, z_i = 0, 0
    for _ in range(max_iter):
        z_r_buff = z_r**2 + x
        z_i = 2*z_r*z_i**2 + y
        z_r = z_r_buff

        iteration += 1
        z_modul = math.sqrt(z_r**2 + z_i**2)
        if z_modul > 2:
            break

    char_idx = round(4 * iteration / max_iter)
    return grathic_map[char_idx]

def mandelbrot_string(x_center, y_center, width, height, stepsize, max_iter):

    mandelbrot_str = ''
    for x_index in range(round(stepsize)):
        x = x_center - width/2 + (width/stepsize)*x_index

        for y_index in range(round(stepsize)):
            y = y_center - height/2 + (height/stepsize)*y_index
            mandelbrot_str += is_mandelbrot_point(x, y, max_iter)

        mandelbrot_str += '\n'

    return mandelbrot_str

