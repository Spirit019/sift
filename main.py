import typer 
from pydantic import BaseModel, ValidationError

app = typer.Typer()

class LogEntry(BaseModel):
    timestamp: str
    level: str
    message: str
    service: str = ""

@app.command()
def log_analyzer(filename: str, level : str = typer.Option("ERROR", "--level", "-l")):
    with open(filename, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    try:
                        user = LogEntry.model_validate_json(line)
                        if user.level.upper() != level.upper():
                            continue
                        else:
                            print(user) 
                    except (ValidationError, ValueError) as e:
                        print(f"Skipping line {line_number}")
        

if __name__ == "__main__":
    app()