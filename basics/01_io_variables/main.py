# Temporary script for manual dataset entry
# TODO: Connect a real database later when I learn how to do it

print("=== DATASET INGESTIOM SYSTEM ===", end="\n\n")

# Codllecting features )variables and inputs)
sample_id = input("Enter sample ID (e.g., 001): ")
text_data = input("Enter text string for analysis: ")
data_label = input("Enter label (Positive / Negative): ")

print()  # Just a blank line for clean terminasl output

# Testing output format with  sep and end parameters
print("Saved samples", sample_id, sep=": ")
print("Raw Text Data", text_data, sep="->")

# Checking how end parameter works on a single line
print("Final Processing Status", end="... ")
print("SUCCESS", "Label", data_label, sep=" | ")