# Setting Up Your Custom Homebrew Tap

## Create Your Tap Repository

1. **Create another GitHub repository**:
   - Name: `homebrew-cowboat` (must start with `homebrew-`)
   - Public repository
   - Initialize with README

2. **Clone and set up the tap**:
```bash
git clone https://github.com/YOURUSERNAME/homebrew-cowboat.git
cd homebrew-cowboat
```

3. **Create the formula directory**:
```bash
mkdir Formula
```

4. **Move your formula**:
```bash
# Copy the cowboat.rb file to Formula/cowboat.rb
cp /path/to/cowboat/cowboat.rb Formula/cowboat.rb
```

5. **Update the formula with correct URLs**:
Edit `Formula/cowboat.rb` to point to your actual GitHub repository and get the real SHA256.

6. **Test your formula**:
```bash
# Install from your tap
brew install YOURUSERNAME/cowboat/cowboat

# Or add tap first
brew tap YOURUSERNAME/cowboat
brew install cowboat
```

## Update Formula After Releases

When you release new versions:

1. **Create a GitHub release**:
   - Tag: `v1.0.0`
   - Generate tarball URL

2. **Get SHA256**:
```bash
curl -L https://github.com/YOURUSERNAME/cowboat/archive/v1.0.0.tar.gz | shasum -a 256
```

3. **Update formula**:
   - Change URL to point to release tarball
   - Update SHA256 hash
   - Update version number

## Distribution

Users can then install with:
```bash
# Method 1: Direct install
brew install YOURUSERNAME/cowboat/cowboat

# Method 2: Add tap then install
brew tap YOURUSERNAME/cowboat
brew install cowboat
```

Your tap URL will be: `https://github.com/YOURUSERNAME/homebrew-cowboat` 