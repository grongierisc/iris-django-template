#!/bin/bash

# Define the routing-related files to display
declare -a files=(
    "app/app/urls.py"
    "app/community/urls.py"
    "app/documents/urls.py"
    "app/frontend/src/router/index.js"
)

# Output the contents of the routing-related files
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "=== Contents of $file ==="
        cat "$file"
        echo ""
    else
        echo "File $file does not exist."
    fi
done
