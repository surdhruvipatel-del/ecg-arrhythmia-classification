import wfdb
import glob
from collections import Counter

# Find all annotation files
annotation_files = glob.glob("data/raw/*.atr")

# Count heartbeat annotation symbols
counts = Counter()

for file in annotation_files:
    record_path = file[:-4]
    annotations = wfdb.rdann(record_path, "atr")
    counts.update(annotations.symbol)

# Display results
print("Total annotation symbols:", sum(counts.values()))

print("\nAnnotation distribution:")
for symbol, count in counts.most_common():
    print(f"{symbol}: {count}")