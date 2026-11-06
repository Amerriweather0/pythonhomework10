
import ast


def readPath(filename):
    """Read grid size and path from a file."""
    with open(filename, "r") as infile:
        rows, cols = map(int, infile.readline().split())
        path = ast.literal_eval(infile.read())

    return rows, cols, path


def encrypt(message, rows, cols, path):
    """Encrypt a message using the grid path."""
    message = "".join(message.upper().split())

    size = rows * cols

    if len(message) > size:
        raise ValueError("Message is too long for the grid.")

    message = message.ljust(size, "X")

    grid = []

    for row in range(rows):
        currentRow = []

        for col in range(cols):
            index = row * cols + col
            currentRow.append(message[index])

        grid.append(currentRow)

    ciphertext = ""

    for row, col in path:
        ciphertext += grid[row][col]

    return ciphertext


def decrypt(ciphertext, rows, cols, path):
    """Decrypt a message using the grid path."""
    ciphertext = "".join(ciphertext.split())

    if len(ciphertext) != rows * cols:
        raise ValueError("Ciphertext must fill the entire grid.")

    grid = [[""] * cols for _ in range(rows)]

    index = 0

    for row, col in path:
        grid[row][col] = ciphertext[index]
        index += 1

    message = ""

    for row in range(rows):
        for col in range(cols):
            message += grid[row][col]

    return message.rstrip("X")


def main():
    filename = input("Enter the path file name: ")

    rows, cols, path = readPath(filename)

    message = input("Enter the message to encrypt: ")

    encrypted = encrypt(message, rows, cols, path)

    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, rows, cols, path)

    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
