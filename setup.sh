echo "Starting to make system settings..."
echo "Actual time: $(date)"
echo "My username: $(whoami)"
echo "I locate in folder: $(pwd)"

# Folder for projects
mkdir -p my-projects
echo "Folder my-projects created"

# File with info about system
echo "System information:" > system-info.txt
uname -a >> system-info.txt
echo "Created file system-info.txt"

echo "Settings complete!"
echo "Folder contain:"
ls -la
