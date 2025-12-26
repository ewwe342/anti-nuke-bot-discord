import sys
import datetime
from rich.console import Console
from rich.text import Text

class RichLogger:
    def __init__(self):
        self.console = Console(file=sys.__stdout__, highlight=False)
        self._stdout = sys.__stdout__

    def write(self, message):
        msg = message.strip()
        if msg:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            log_text = Text()
            
            log_text.append(" ┏", style="bold bright_black")
            log_text.append(f" $ {now} ", style="bold black on green")
            log_text.append(" ┓", style="bold bright_black")
            
            log_text.append("\n ┃ ", style="bold bright_black")
            log_text.append("» ", style="bold bright_cyan")
            log_text.append(msg, style="bold white")
            
            self.console.print(log_text)

    def flush(self):
        self._stdout.flush()

sys.stdout = RichLogger()