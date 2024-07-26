#!/bin/bash

# Define the routing-related files to display
declare -a files=(
    "app/frontend/src/App.vue"
    "app/frontend/src/main.js"
    "app/frontend/src/components/DocumentManager.vue"
    "app/frontend/src/components/HelloWorld.vue"

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
