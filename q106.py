# Print command-line arguments.
import sys

if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])
else:
    print("No command-line arguments provided.")