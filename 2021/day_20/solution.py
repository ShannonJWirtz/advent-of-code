import numpy as np

def get_inputs(filename):
    with open(filename) as f:
        algorithm, image = f.read().split('\n\n')
    algorithm = {i: 0 if x == '.' else 1 for i, x in enumerate(algorithm.replace('\n', ''))}
    image = np.array(
        [[0 if x == '.' else 1 for x in line] for line in image.split('\n') if line]
    )
    return algorithm, image


def enhance_image_step(algorithm, image, dark_infinity_initially = True):
    if dark_infinity_initially:
        padded_image = np.pad(image, ((3,3), (3,3)), 'constant', constant_values=0)
    else:
        padded_image = np.pad(image, ((3,3), (3,3)), 'constant', constant_values=1)
    output_image = np.zeros(padded_image.shape)

    for i in range(0, len(padded_image)-2):
        for j in range(0, len(padded_image)-2):
            binary = padded_image[i:i+3,j:j+3].flatten()
            decimal = sum(b*2**(n) for n, b in enumerate(reversed(binary)))
            output_image[i+1,j+1] = algorithm[decimal]
    output_image = output_image[1:len(output_image)-1,1:len(output_image)-1]
    if algorithm[0] == 1 and dark_infinity_initially:
        dark_infinity_initially = False
    elif algorithm[511] == 0 and not dark_infinity_initially:
        dark_infinity_initially = True

    return output_image, dark_infinity_initially


def enhance(filename, iterations, print = False):
    algorithm, image = get_inputs(filename)
    dark_infinity_initially = True
    for i in range(iterations):
        image, dark_infinity_initially = enhance_image_step(algorithm, image, dark_infinity_initially)
    if not print:
        return int(np.sum(image))
    else:
        return image

a, i = get_inputs('input.txt')

image = enhance('input.txt', 50, print = True)
image.shape
# np.sum(image)
np.set_printoptions(threshold=np.inf, linewidth=np.inf)
with open('image.csv', 'w') as f:
    for line in image:
        print(line)
        f.write(','.join(str(int(i)) for i in line) + '\n')





if __name__ == '__main__':
    print('First answer is:', enhance('input.txt', 2))
    print('Second answer is:', enhance('input.txt', 50))
