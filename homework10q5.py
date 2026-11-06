
from graphics import *
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def getFrequencies(url):
    """Download a text file and count character frequencies."""

    with urlopen(url) as response:
        text = response.read().decode("utf-8").upper()

    # Create 256 buckets for character counts
    counts = [0] * 256

    for character in text:
        value = ord(character)

        if value < 256:
            counts[value] += 1

    # Calculate total letters A-Z
    total_letters = sum(counts[ord(letter)] for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if total_letters == 0:
        raise ValueError("No letters were found in the downloaded text.")

    # Calculate letter frequency ratios
    frequencies = {}

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        frequencies[letter] = counts[ord(letter)] / total_letters

    return counts, frequencies


def writeFrequencies(counts, filename):
    """Write letter counts to an output file."""

    with open(filename, "w", encoding="utf-8") as outfile:

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            outfile.write(
                f"{letter} {counts[ord(letter)]}\n"
            )


def drawGraph(frequencies):
    """Draw the frequency analysis graph."""

    win = GraphWin("Internet Book Frequency Analysis", 850, 550)
    win.setBackground("white")

    highest = max(frequencies.values())

    left = 70
    bottom = 440
    graph_width = 740
    graph_height = 350

    # Draw axes
    Line(
        Point(left, bottom),
        Point(left + graph_width, bottom)
    ).draw(win)

    Line(
        Point(left, bottom),
        Point(left, bottom - graph_height)
    ).draw(win)

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

        label = Text(
            Point((x1 + x2) / 2, bottom + 15),
            letter
        )
        label.draw(win)

    # Display title
    title = Text(
        Point(425, 30),
        "Internet Book Letter Frequency Analysis"
    )
    title.setSize(16)
    title.draw(win)

    # Display instructions
    instruction = Text(
        Point(425, 510),
        "Click anywhere to close the graph."
    )
    instruction.draw(win)

    win.getMouse()
    win.close()


def main():
    # Ask for Internet address
    url = input("Enter the URL of the book: ")

    # Ask for output filename
    filename = input("Enter the output filename: ")

    try:
        counts, frequencies = getFrequencies(url)

        # Save frequency data
        writeFrequencies(counts, filename)

        print("Frequency data saved to", filename)

        # Display graph
        drawGraph(frequencies)

    except (HTTPError, URLError) as error:
        print("Unable to download the file:", error)

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
