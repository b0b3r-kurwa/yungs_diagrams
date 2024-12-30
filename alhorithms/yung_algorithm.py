from PIL import Image, ImageDraw

def make_diagram(n: int) -> list:
    k_sorted = []
    diagrams = [[[1]], [[1, 1], [2, 0]]]

    for i in range(1, n - 1):
        previous = list(diagrams[i])
        for p in previous:
            p.append(0)
        new_array = []

        for j in previous:
            for l in range(len(j)):
                u = j.copy()
                u[l] += 1
                new_array.append(u)

        new_array_sorted = []
        for s in new_array:
            if all(s[i] >= s[i + 1] for i in range(len(s) - 1)) and s not in k_sorted:
                new_array_sorted.append(s)
            else:
                pass
        diagrams.append(new_array_sorted)

    return new_array_sorted


def create_pictures(n: int):
    diagrams = make_diagram(n)
    imgs = []

    for diagram in diagrams:
        img = Image.new('RGBA', (n * 50 + 100, n * 50 + 100), 'white')
        idraw = ImageDraw.Draw(img)
        x_i = 50
        y_i = 50
        for number in diagram:
            if number != 0:
                for _ in range(number):
                    idraw.rectangle(xy=(x_i, y_i, x_i + 50, y_i + 50),
                                    width=5,
                                    fill=None,
                                    outline='black')
                    x_i += 50
            else:
                break
            x_i = 50
            y_i += 50

        imgs.append(img)

    return imgs


