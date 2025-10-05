#testing for now 


from pathlib import Path
import json

def scan(file_name):
    file_path = Path(__file__).parent.parent / "data" / file_name
    with file_path.open() as f:
        data = f.read()
    return {"issues": 7}

if __name__ == "__main__":
    final = scan("testing.tf")
    print(json.dumps(final, indent=2))
