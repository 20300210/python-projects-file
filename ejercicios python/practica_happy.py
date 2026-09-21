from rich.console import Console
from rich.text import Text

console = Console()

text = "Happy Friendship Day"
colors = [
    "red", "yellow", "green", "cyan", "blue", "white", "magenta",
    "red", "yellow", "green", "cyan", "blue", "white", "magenta",
    "yellow", "green", "white", "cyan", "blue", "magenta", "red"
]

message = Text()
for char, color in zip(text, colors):
    message.append(char, style=color)

console.print(message)
