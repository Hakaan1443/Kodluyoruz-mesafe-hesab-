import math

# 1. Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (2, 3)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# 3. Mesafelerin Hesaplanması ve Minimum Mesafenin Bulunması
min_distance = float('inf')
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        if dist < min_distance:
            min_distance = dist

print(f"En küçük mesafe: {min_distance}")
