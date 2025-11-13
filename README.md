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
- `--mini`: Use mini cows (3 adorable cow emojis 🐄 per boat with closer spacing)

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

# Mini cow fleet! 3 cow emojis per boat
cowboat --mini

# Mini cow armada on pirate ships
cowboat --mini -n 5 -b pirate -s 0.03

# Peaceful mini cow cruise
cowboat --mini -b canoe -n 2 -s 0.12
```

## Don't forget to update your `.zshrc` or shell of choice to make all git pushes set them heiffers a sail!
```
 # Cowboat push celebrations triggered by any git push
  if ! typeset -f git >/dev/null; then
    git() {
      local subcmd=$1
      shift || true

      if [[ $subcmd != "push" ]]; then
        command git "$subcmd" "$@"
        return $?
      fi

      local branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
      branch=${branch:-unknown}
      echo "🚀 Pushing to branch: $branch"

      command git push "$@"
      local status=$?

      if [[ $status -eq 0 ]]; then
        local force=false
        for arg in "$@"; do
          case $arg in
            --force|-f|--force-with-lease|--force-with-lease=*) force=true ;;
          esac
        done

        if $force; then
          echo "💥 Force push success! Dispatching the ultimate cowboat..."
          cowboat -b pirate -n 5 -s 0.03
        else
          echo "✅ Push successful! Celebrating with cowboat..."
          local boats=(raft ship yacht canoe submarine ferry pirate cruise)
          local random_boat=${boats[$RANDOM % ${#boats[@]}]}
          local random_cows=$((RANDOM % 5 + 1))
          local random_speed=$(echo "scale=2; (($RANDOM % 11) + 2) / 100" | bc)
          echo "🎉 Sailing with $random_cows cow(s) on a $random_boat at speed
  $random_speed!"
          cowboat -b "$random_boat" -n "$random_cows" -s "$random_speed"
        fi
      else
        echo "❌ Push failed. Cowboat stays docked."
      fi

      return $status
    }
  fi
```

## Boat Types

- **raft**: Simple wooden raft with plank deck (default)
- **ship**: Classic sailing ship with mast, sail, and proper deck
- **yacht**: Modern yacht with cabin and main deck
- **canoe**: Curved canoe where cows sit inside
- **submarine**: Underwater vessel with periscope and command deck
- **ferry**: Multi-level passenger ferry with realistic deck structure
- **pirate**: Pirate ship with skull flag mast and deck below
- **cruise**: Large luxury cruise ship with multiple decks

## Features

- ASCII art animation of cows sailing from bottom to top of terminal
- **8 realistic boat types** with proper decks where cows actually stand
- Support for multiple cows sailing together (no more floating on masts!)
- **Mini cow mode**: 3 adorable cow emojis 🐄 per boat with closer spacing
- Adjustable animation speed
- Cross-platform terminal support

## Requirements

- Python 3.6+
- Terminal with ANSI escape sequence support

## License

MIT License 
