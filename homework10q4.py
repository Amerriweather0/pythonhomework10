
import os
from graphics import *


def getFrequencies(folder):
    """Read all Python files in a folder and calculate letter frequencies."""

    counts = {}
    total_letters = 0

    # Find all files in the directory
    for filename in os.listdir(folder):

        if filename.endswith(".py"):
            filepath = os.path.join(folder, filename)

            if os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8") as infile:
                    text = infile.read().upper()

                # Count letters A-Z
                for character in text:
                    if character >= "A" and character <= "Z":
                        counts[character] = counts.get(character, 0) + 1
                        total_letters += 1

    if total_letters == 0:
        raise ValueError("No Python files containing letters were found.")

    # Calculate frequency ratios
    frequencies = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        frequencies[letter] = counts.get(letter, 0) / total_letters

    return frequencies


def drawGraph(frequencies):
    """Draw a frequency analysis graph."""

    win = GraphWin("Python Code Frequency Analysis", 850, 550)
    win.setBackground("white")

    highest = max(frequencies.values())

    left = 70
    bottom = 440
    graph_width = 740
    graph_height = 350

    # Draw axes
    Line(Point(left, bottom),
         Point(left + graph_width, bottom)).draw(win)

    Line(Point(left, bottom),
         Point(left, bottom - graph_height)).draw(win)

    # Draw bars
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

        # Display letter underneath each bar
        label = Text(
            Point((x1 + x2) / 2, bottom + 15),
            letter
        )
        label.draw(win)

    # Graph title
    title = Text(
        Point(425, 30),
        "Python Program Letter Frequency"
    )
    title.setSize(18)
    title.draw(win)

    # Instructions
    instruction = Text(
        Point(425, 510),
        "Click anywhere to close the graph."
    )
    instruction.draw(win)

    win.getMouse()
    win.close()


def main():
    folder = input("Enter the folder containing Python files: ")

    try:
        frequencies = getFrequencies(folder)
        drawGraph(frequencies)

    except FileNotFoundError:
        print("Folder not found.")

    except NotADirectoryError:
        print("Please enter a valid directory.")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
