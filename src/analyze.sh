#!/bin/bash

set -e
CODE_DIR="/analysis/inputs/public/source-code"

grep -w -Hnir --include \*.ts --include \*.tsx --include \*.js --include \*.jsx --include \*.py -f /analyzer/bad-words "${CODE_DIR}" |
    python3 /analyzer/badwords.py "${CODE_DIR}" /analysis/output/output.json

exit 0