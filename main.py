import numpy as np

# Функція для перетворення бінарних зображень на вектори
def convert_to_vector(image):
    return np.where(image == 0, -1, 1)

# Задаємо зображення у вигляді масивів
images = [
    np.array([1, 1, 1, 1, 
              1, 0, 0, 1, 
              1, 0, 0, 1, 
              1, 1, 1, 1]),
    np.array([0, 1, 1, 1,
              0, 1, 0, 1,
              0, 1, 0, 1, 
              1, 1, 0, 1]),
    np.array([1, 1, 1, 0, 
              1, 0, 1, 0, 
              1, 1, 1, 0, 
              1, 0, 0, 0]),
]

# Функція для відображення зображення у вигляді ASCII-графіки
def display_image(image, width=4):
    for i in range(0, len(image), width):
        row = image[i:i+width]
        print("".join(['#' if pixel == 1 else ' ' for pixel in row]))

# Відображення всіх зображень
for i, img in enumerate(images):
    print(f"\nЗображення {i + 1}:")
    display_image(img)

# Перетворення зображень на вектори
vectors = [convert_to_vector(img) for img in images]

# Формування матриці ваг
def calculate_weight_matrix(vectors):
    p = len(vectors)
    n = len(vectors[0])
    W = np.zeros((n, n))

    for k in range(p):
        W += np.outer(vectors[k], vectors[k])  # Обчислюємо w_ij
    np.fill_diagonal(W, 0)  # Занулюємо діагональні елементи

    return W

# Обчислення порогів
def calculate_thresholds(weight_matrix):
    thresholds = np.mean(weight_matrix, axis=1) / 2
    return thresholds

# Основна частина програми
W = calculate_weight_matrix(vectors)
theta = calculate_thresholds(W)

# Виводимо результати
print("\nМатриця ваг зв'язків W:")
print(W)
print("\nПоріг для нейронів θ:")
print(theta)

# Функція для перевірки вхідних векторів
def check_pattern(input_vector, weight_matrix, threshold):
    output_vector = np.sign(np.dot(weight_matrix, input_vector) - threshold)
    return output_vector

# Додавання введення користувача
user_input = input("\nВведіть зображення у вигляді 16 бінарних чисел (0 або 1) без пробілів (наприклад, 0011010101011101): ")
user_image = np.array([int(bit) for bit in user_input])
user_vector = convert_to_vector(user_image)

# Перевіряємо розпізнавання
print("\nРезультати розпізнавання:")
for i, vec in enumerate(vectors):
    result = check_pattern(user_vector, W, theta)
    match = np.array_equal(result, vec)
    print(f"Порівняння зображення користувача з вектором {i + 1}: {'Співпадає' if match else 'Не співпадає'}")

# Відображення зображення користувача
print("\nВаше зображення у вигляді ASCII-графіки:")
display_image(user_image)