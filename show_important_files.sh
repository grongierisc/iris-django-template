#!/bin/bash

# Define the important files to display
declare -a files=(
    "app/app/asgi.py"
    "app/app/settings.py"
    "app/app/urls.py"
    "app/app/wsgi.py"
    "app/community/admin.py"
    "app/community/models.py"
    "app/community/serializers.py"
    "app/community/tests.py"
    "app/community/urls.py"
    "app/community/views.py"
    "app/documents/embedding.py"
    "app/documents/models.py"
    "app/documents/rag.py"
    "app/documents/serializers.py"
    "app/documents/urls.py"
    "app/documents/views.py"
    "app/frontend/babel.config.js"
    "app/frontend/jsconfig.json"
    "app/frontend/package.json"
    "app/frontend/public/index.html"
    "app/frontend/README.md"
    "app/frontend/src/App.vue"
    "app/frontend/src/main.js"
    "app/frontend/components/ConversationManager.vue"
    "app/frontend/components/DocumentManager.vue"
    "app/frontend/router/index.js"
    "app/health_records/models.py"
    "app/health_records/serializers.py"
    "app/interop/apps.py"
    "app/interop/bo.py"
    "app/interop/bs.py"
    "app/interop/msg.py"
    "app/interop/settings.py"
    "app/interop/views.py"
    "app/manage.py"
    "app/sqloniris/apps.py"
    "app/sqloniris/views.py"
    "docker-compose.yml"
    "Dockerfile"
    "entrypoint.sh"
    "README.md"
    "requirements.txt"
)

# Output the contents of the important files
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "=== Contents of $file ==="
        cat "$file"
        echo ""
    else
        echo "File $file does not exist."
    fi
done
