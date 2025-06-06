# Installation Guide for Cowboat

## Quick Installation Methods

### Method 1: Direct Download and Run
```bash
# Download the script
curl -O https://raw.githubusercontent.com/yourusername/cowboat/main/cowboat.py
chmod +x cowboat.py

# Run it
python3 cowboat.py
```

### Method 2: Git Clone and Run
```bash
# Clone the repository
git clone https://github.com/yourusername/cowboat.git
cd cowboat

# Make executable and run
chmod +x cowboat.py
python3 cowboat.py
```

### Method 3: Using Virtual Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/cowboat.git
cd cowboat

# Create and activate virtual environment
python3 -m venv cowboat-env
source cowboat-env/bin/activate

# Install in virtual environment
pip install -e .

# Now you can run
cowboat
```

### Method 4: Using pipx (Recommended for Applications)
```bash
# Install pipx if you don't have it
brew install pipx

# Install cowboat
pipx install git+https://github.com/yourusername/cowboat.git

# Run from anywhere
cowboat
```

### Method 5: Homebrew (Future)
```bash
# This will work once the formula is submitted to Homebrew
brew install cowboat
cowboat
```

## For Developers

### Local Development
```bash
# Clone and enter directory
git clone https://github.com/yourusername/cowboat.git
cd cowboat

# Create development environment
python3 -m venv dev-env
source dev-env/bin/activate

# Install in development mode
pip install -e .

# Make changes and test
cowboat --help
```

### Creating a Distribution
```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (for maintainers)
twine upload dist/*
```

## Troubleshooting

### "externally-managed-environment" Error
If you see this error when using pip, your Python installation is managed by your system package manager. Use one of these alternatives:

1. Use pipx (recommended for applications)
2. Use a virtual environment
3. Use the direct download method
4. Add `--break-system-packages` flag (not recommended)

### Command Not Found After Installation
Make sure your Python scripts directory is in your PATH:
```bash
# Add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
export PATH="$PATH:$HOME/.local/bin"
```

### Permission Denied
Make sure the script is executable:
```bash
chmod +x cowboat.py
``` 