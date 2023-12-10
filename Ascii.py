from PIL import Image
from rich.console import Console


class AsciiArtConverter:
    def __init__(self, path, intensity):
        self.image = Image.open(path)
        self.pixels = self.image.load()
        self.width, self.height = self.image.size
        self.intensity = intensity
        self.W = self.width // self.intensity
        self.H = self.height // self.intensity
        self.data = []
        self.new_data = []

    def read(self, x_start, y_start):
        cache = []
        y_end = y_start + self.intensity
        x_end = x_start + self.intensity
        for y in range(y_start, y_end):
            for x in range(x_start, x_end):
                cache.append(self.pixels[x, y])
        self.data.append(cache)

    def read_all(self):
        for y in range(self.H):
            for x in range(self.W):
                self.read(x * self.intensity, y * self.intensity)

    def calculate(self):
        for i in range(len(self.data)):
            square = self.data[i]
            red = green = blue = 0
            for p in square:
                red += p[0]
                green += p[1]
                blue += p[2]
            new_val = (red // len(square), green // len(square), blue // len(square))
            self.new_data.append(new_val)

    def convert_to_ascii(self):
        self.read_all()
        self.calculate()
        index = 0
        console = Console()
        for y in range(self.H):
            for x in range(self.W):
                r = self.new_data[index][0]
                g = self.new_data[index][1]
                b = self.new_data[index][2]
                console.print("@#", style="rgb({},{},{})".format(r, g, b), end="")
                index += 1
            print()
