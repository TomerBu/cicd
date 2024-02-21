import os
# fetch param from command line:
import sys

if not 'VIRTUAL_ENV' in os.environ:
    print("Please run this script on a virtual environment")
    sys.exit(1)

# how to import art from pip if my file is named art.py
from art import text2art

DEFAULT_LOGO = "TomerBu"

text = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_LOGO

logo = text2art(text)
print(logo)
