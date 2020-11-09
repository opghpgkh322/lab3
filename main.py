
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

t = np.linspace(0, 10 * np.pi)
x = 2 * (np.sin(2 * t) - (np.cos(t) / 2))
y = 2 * (np.cos(2 * t) - (np.sin(t) / 2))

fig = plt.figure(figsize=(5, 5))
plt.plot(x, y,)

plt.savefig('img.png')

img = Image.open('img.png')
img = img.convert('L')
img = img.save('result.bmp')

plt.show()