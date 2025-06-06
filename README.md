# 🐄 Cowboat 🚤
Watch cows sail away into the horizon on various boats!

## Installation

### Via Homebrew (Recommended)
```bash
brew install callumreid/cowboat/cowboat
```



### From Source
```bash
git clone https://github.com/yourusername/cowboat.git
cd cowboat
pip install .
```

## Usage

Basic usage:
```bash
cowboat
```

### Options

- `-n, --num-cows NUM`: Number of cows (1-5, default: 1) or boats for mini mode (1-10)
- `-b, --boat TYPE`: Type of boat (`raft`, `ship`, `yacht`, `canoe`, `submarine`, `ferry`, `pirate`, `cruise`, default: `raft`)
- `-s, --speed SPEED`: Animation speed in seconds (default: 0.1)
- `--mini`: Use mini cows (3 adorable tiny cows per boat with closer spacing)

### Examples

```bash
# Single cow on a raft (default)
cowboat

# Three cows on a yacht
cowboat -n 3 -b yacht

# Slow animation with two cows on a ship
cowboat -n 2 -b ship -s 0.2

# Fast sailing raft
cowboat -s 0.05

# Pirate ship adventure
cowboat -b pirate

# Submarine dive
cowboat -b submarine -s 0.15

# Mini cow fleet! 3 tiny cows per boat
cowboat --mini

# Mini cow armada on pirate ships
cowboat --mini -n 5 -b pirate -s 0.03

# Peaceful mini cow cruise
cowboat --mini -b canoe -n 2 -s 0.12
```

## Boat Types

- **raft**: Simple wooden raft (default)
- **ship**: Classic sailing ship with masts
- **yacht**: Fancy modern yacht
- **canoe**: Simple canoe for peaceful sailing
- **submarine**: Underwater vessel with periscope
- **ferry**: Multi-level passenger ferry
- **pirate**: Pirate ship with skull and crossbones flag
- **cruise**: Large luxury cruise ship

## Features

- ASCII art animation of cows sailing from bottom to top of terminal
- Multiple boat types to choose from (8 different boats!)
- Support for multiple cows sailing together
- **Mini cow mode**: 3 adorable tiny cows per boat with closer spacing
- Adjustable animation speed
- Cross-platform terminal support

## Requirements

- Python 3.6+
- Terminal with ANSI escape sequence support

## License

MIT License 