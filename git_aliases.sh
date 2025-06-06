# Git Aliases with Cowboat Celebration! 🐄⛵

# Your existing aliases
alias gs="git status"
alias ga="git add ."
alias gc="git commit"
alias bumpus="git commit -m 'k8s bumpus'"

# Dynamic git push with random cowboat celebration!
# Remove any existing gp alias first
unalias gp 2>/dev/null || true

gp() {
    local current_branch=$(git rev-parse --abbrev-ref HEAD)
    echo "🚀 Pushing to branch: $current_branch"
    
    if git push origin "$current_branch"; then
        echo "✅ Push successful! Celebrating with cowboat..."
        
        # Random boat types
        local boats=("raft" "ship" "yacht" "canoe" "submarine" "ferry" "pirate" "cruise")
        local random_boat=${boats[$((RANDOM % ${#boats[@]}))]}
        
        # Random number of cows (1-5)
        local random_cows=$((RANDOM % 5 + 1))
        
        # Random speed (0.02 to 0.12)
        local random_speed=$(echo "scale=2; (($RANDOM % 11) + 2) / 100" | bc)
        
        echo "🎉 Sailing away with $random_cows cow(s) on a $random_boat at speed $random_speed!"
        cowboat -b "$random_boat" -n "$random_cows" -s "$random_speed"
    else
        echo "❌ Push failed! No cowboat for you this time."
    fi
}

# Force push with EXTRA dramatic cowboat celebration! 💥
# Remove any existing gpf alias first
unalias gpf 2>/dev/null || true

gpf() {
    local current_branch=$(git rev-parse --abbrev-ref HEAD)
    echo "💥 FORCE PUSHING to branch: $current_branch"
    echo "⚠️  This will overwrite remote history!"
    
    if git push origin "$current_branch" --force; then
        echo "🔥 FORCE PUSH SUCCESSFUL! Epic celebration time..."
        
        # Force push gets more dramatic boats and settings
        local dramatic_boats=("pirate" "cruise" "ship" "yacht")
        local random_boat=${dramatic_boats[$((RANDOM % ${#dramatic_boats[@]}))]}
        
        # More cows for dramatic effect (3-5)
        local random_cows=$((RANDOM % 3 + 3))
        
        # Faster speed for more drama (0.02 to 0.06)
        local random_speed=$(echo "scale=2; (($RANDOM % 5) + 2) / 100" | bc)
        
        echo "💥 FORCE SAILING with $random_cows cow(s) on a $random_boat at speed $random_speed!"
        cowboat -b "$random_boat" -n "$random_cows" -s "$random_speed"
    else
        echo "❌ Force push failed! The git gods have spoken."
    fi
}

# Alternative: Super quick push (no cowboat, just dynamic branch)
alias gpp="git push origin \$(git rev-parse --abbrev-ref HEAD)"

# Fun variations you can add:
# Victory cowboat (always pirate ship with 5 cows)
alias victory="cowboat -b pirate -n 5 -s 0.05"

# Zen cowboat (always canoe with 1 cow, slow)
alias zen="cowboat -b canoe -n 1 -s 0.15"

# Epic cowboat (always cruise with max cows)
alias epic="cowboat -b cruise -n 5 -s 0.03" 