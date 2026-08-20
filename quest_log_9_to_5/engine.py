from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
import time

console = Console()

def clear_screen():
    console.clear()

def print_office(text, delay=0.02):
    """Prints text in a dull, grey style for the real world."""
    for char in text:
        console.print(f"[grey53]{char}[/grey53]", end="")
        time.sleep(delay)
    console.print()

def print_dream(text, delay=0.02):
    """Prints text in vibrant colors for the JRPG world."""
    for char in text:
        console.print(f"[bold cyan]{char}[/bold cyan]", end="")
        time.sleep(delay)
    console.print()

def show_panel(title, content, style="grey53"):
    """Displays a bordered panel."""
    console.print(Panel(content, title=title, border_style=style))

def ask_choice(question, choices):
    """Ask a multiple choice question and return the chosen index."""
    console.print(f"\n[bold yellow]{question}[/bold yellow]")
    for i, choice in enumerate(choices, 1):
        console.print(f"  [bold white]{i}.[/bold white] {choice}")
    
    while True:
        ans = Prompt.ask("Selecciona una opción", default="1")
        try:
            val = int(ans)
            if 1 <= val <= len(choices):
                return val - 1
            else:
                console.print("[red]Opción inválida.[/red]")
        except ValueError:
            console.print("[red]Por favor ingresa un número.[/red]")

def print_quest_log(day, content):
    """Prints the JRPG Quest Log at the start of the day."""
    panel = Panel(
        Text(content, justify="center", style="bold blue"),
        title=f"📜 Quest Log Transdimensional - Día {day}",
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)
