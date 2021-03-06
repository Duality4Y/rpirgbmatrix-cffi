#!/usr/bin/env python
from rgbmatrix import Canvas
from rgbmatrix import Matrix

import time

matrix = Matrix(32, 1, 1)
canvas = Canvas(matrix)
w, h = canvas.get_size()
loops = 2 ** 12
start = time.time()

for i in range(0, loops):
    col = i % 0xFF
    for y in range(0, h):
        for x in range(0, w):
            canvas.set_pixel(x, y, col, 0, 0)

duration = time.time() - start

pixels = w * h * loops
pixels_per_sec = pixels / duration
print("%d pixels, %dms; %.1f MegaPixels/s; %.1fHz frame update rate" %
      (pixels, 1000.0 * duration, pixels_per_sec / 1e6, loops / duration))

matrix.close()
