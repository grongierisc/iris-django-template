#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 [-e exclude1,exclude2,...]"
    exit 1
}

# Parse command line arguments
while getopts ":e:" opt; do
    case $opt in
        e)
            IFS=',' read -r -a EXCLUDE_FOLDERS <<< "$OPTARG"
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            usage
            ;;
    esac
done

# Construct the exclude pattern for tree command
EXCLUDE_PATTERN=""
for folder in "${EXCLUDE_FOLDERS[@]}"; do
    EXCLUDE_PATTERN+="--prune -I \"$folder\" "
done

# Execute tree command with exclude pattern
eval "tree $EXCLUDE_PATTERN"

# End of script
