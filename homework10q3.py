
from graphics import *


def getFrequencies(filename):
    """Read a text file and calculate letter frequencies."""
    with open(filename, "r") as infile:
        text = infile.read().upper()

    # Count every character
    counts = {}

    for character in text:
        counts[character] = counts.get(character, 0) + 1

    # Count only alphabetic letters A-Z
    total_letters = sum(
        counts.get(letter, 0) for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    if total_letters == 0:
        raise ValueError("The file contains no letters.")

    # Calculate frequency ratios
    frequencies = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        frequencies[letter] = counts.get(letter, 0) / total_letters

    return frequencies


def drawGraph(frequencies):
    """Draw a frequency analysis graph."""
    win = GraphWin("Letter Frequency Analysis", 850, 550)
    win.setBackground("white")

    # Find highest frequency for graph scaling
    highest = max(frequencies.values())

    # Graph dimensions
    left = 70
    bottom = 440
    graph_width = 740
    graph_height = 350

    # Draw axes
    Line(Point(left, bottom), Point(left + graph_width, bottom)).draw(win)
    Line(Point(left, bottom), Point(left, bottom - graph_height)).draw(win)

    # Draw letter bars
    bar_width = graph_width / 26

    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        frequency = frequencies[letter]

        x1 = left + i * bar_width + 2
        x2 = left + (i + 1) * bar_width - 2

        bar_height = (frequency / highest) * graph_height

        bar = Rectangle(
            Point(x1, bottom),
            Point(x2, bottom - bar_height)
        )

        bar.setFill("blue")
        bar.setOutline("black")
        bar.draw(win)

        # Letter labels
        label = Text(
            Point((x1 + x2) / 2, bottom + 15),
            letter
        )
        label.draw(win)

    # Graph title
    title = Text(
        Point(425, 30),
        "English Letter Frequency Analysis"
    )
    title.setSize(18)
    title.draw(win)

    # Y-axis label
    y_label = Text(
        Point(25, 250),
        "Frequency"
    )
    y_label.draw(win)

    # Highest frequency label
    max_label = Text(
        Point(35, bottom - graph_height),
        f"{highest:.3f}"
    )
    max_label.draw(win)

    # Instructions
    instruction = Text(
        Point(425, 510),
        "Click anywhere to close the graph."
    )
    instruction.draw(win)

    win.getMouse()
    win.close()


def main():
    filename = input("Enter the name of the input text file: ")

    try:
        frequencies = getFrequencies(filename)
        drawGraph(frequencies)

    except FileNotFoundError:
        print("File not found. Please check the file name.")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
