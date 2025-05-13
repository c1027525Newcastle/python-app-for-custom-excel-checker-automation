import pandas as pd

def create_audit_file(path: str):
    # Data to write
    data = {
        "Email": ["bana.com", "apple.com", "coco.com"],
        "Engineer": ["yes", "yes", "yes"],
        "Mathematician": ["no", "yes", "no"],
        "In group?": ["Yes", "No", "Yes"],
        "Group": ["Cool_Kids", "N/A", "CocoLoco"],
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Write to Excel
    df.to_excel(path, index=False)
    print(f"Audit file written to {path}")

if __name__ == "__main__":
    create_audit_file("Audit_FileB.xlsx")