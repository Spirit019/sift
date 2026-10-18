import typer 
from pydantic import BaseModel, ValidationError
from rich.console import Console
from rich.table import Table

app = typer.Typer()

class LogEntry(BaseModel):
    timestamp: str
    level: str
    message: str
    service: str = ""

@app.command()
def log_analyzer(filename: str, level : str = typer.Option("ERROR", "--level", "-l")):
    console = Console()
    table = Table(title="LOG ANALYZER")
    entries = []
    with open(filename, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    try:
                        user = LogEntry.model_validate_json(line)
                        if user.level.upper() != level.upper():
                            continue
                        else:
                            entries.append((user.timestamp, user.level, user.service or "-", user.message))
                    except (ValidationError, ValueError) as e:
                         pass
                        # print(f"Skipping line {line_number}")

    table.add_column("Timestamp")
    table.add_column("Level")
    table.add_column("Service")
    table.add_column("Message")
    for row in entries:
         table.add_row(*row)
    
    if len(entries) == 0:
         print("no matches")
    else:
        console.print(table)
if __name__ == "__main__":
    app()