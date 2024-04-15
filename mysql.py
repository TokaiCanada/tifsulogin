import random
import string

brands = ['Cartier', 'Dexter Marx', 'Boss', 'Gucci', 'Ray-Ban', 'Prada', 'Oakley', 'Oliver Peoples']
colors = ['Black', 'Brown', 'Red', 'Green', 'Tortoise', 'White', 'Clear']
shapes = ['Round', 'Cat eye', 'Rectangle', 'Square', 'Aviator', 'Geometric', 'Oval']
model_prefixes = ['Alf', 'Cl', 'Pat', 'GG', 'C', 'B', 'RX', 'OP', 'P', 'K']
descriptions = [
    "Elegant and stylish, perfect for everyday wear.",
    "Bold and modern, stands out in any crowd.",
    "Classic design with a contemporary twist.",
    "Lightweight frame with exceptional durability.",
    "Versatile style, ideal for any face shape.",
    "Fashion-forward with a vintage feel.",
    "Sleek and sophisticated, provides superior comfort.",
    "Distinctive design with cutting-edge features.",
    "Timeless aesthetics with modern functionality.",
    "Chic and refined, suits a professional look."
]
optical_sun = ['Optical', 'Sun']

def generate_model():
    prefix = random.choice(model_prefixes)
    number = random.randint(1000, 9999)
    suffix = random.choice(string.ascii_uppercase)
    return f"{prefix}{number}{suffix}"

def generate_sql():
    models_generated = set()
    for brand in brands:
        for _ in range(10):  # Generate 10 entries per brand
            model = generate_model()
            while model in models_generated:
                model = generate_model()
            models_generated.add(model)
            selected_colors = random.sample(colors, random.randint(1, 3))
            cost_price = random.uniform(50, 1000)
            shape = random.choice(shapes)
            size = random.randint(46, 56)
            description = random.choice(descriptions)
            optical_or_sun = random.choice(optical_sun)
            print(f"INSERT INTO BrandedEyewear (Brand, Model, Color, CostPrice, SellPrice, Shape, Size, OpticalSun, Description) "
                  f"VALUES ('{brand}', '{model}', '{','.join(selected_colors)}', {cost_price:.2f}, {cost_price * 2:.2f}, "
                  f"'{shape}', {size}, '{optical_or_sun}', '{description}');")

if __name__ == "__main__":
    generate_sql()
