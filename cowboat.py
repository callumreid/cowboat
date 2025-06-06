#!/usr/bin/env python3

import argparse
import time
import os
import sys
import shutil

def get_terminal_size():
    """Get terminal dimensions"""
    return shutil.get_terminal_size((80, 24))

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_cow_boat_art(boat_type="raft", mini=False):
    """Generate ASCII art for cow on boat"""
    
    boats = {
        "raft": [
            "    ~~~~~~~~~~~~~~~~~~~~",
            "  /                    \\",
            " (  ==================  )",
            "  \\____________________/",
            "   ~~~~~~~~~~~~~~~~~~~~"
        ],
        "ship": [
            "                |\\",
            "               /| \\",
            "              / |__\\",
            "             /     /",
            "    ~~~~~~~(  ~~~(~~~~~~~",
            "           |     |",
            "         __|_____|__",
            "        (         )",
            "         ~~~~~~~~~"
        ],
        "yacht": [
            "           |\\   /|",
            "          /  \\ /  \\",
            "         |    |    |",
            "         |    |    |",
            "    ~~~~(     |     )~~~~",
            "        |           |",
            "       (  ~~~~~~~~~~~  )",
            "        \\             /",
            "         ~~~~~~~~~~~~~"
        ],
        "canoe": [
            "    ~~~~~~~~~~~~~~~~~~~",
            "  /                   \\",
            " (  =================  )",
            "  \\___________________/",
            "    ~~~~~~~~~~~~~~~~~~~"
        ],
        "submarine": [
            "        __|__",
            "       |  o  |",
            "    ===|     |===",
            "  (             )",
            "   \\___________/",
            "    ~~~~~~~~~~~"
        ],
        "ferry": [
            "    ||     ||     ||",
            "   _||_   _||_   _||_",
            "  |               |",
            "  |  ===========  |",
            " (  =============== )",
            "  \\_______________/",
            "   ~~~~~~~~~~~~~~~"
        ],
        "pirate": [
            "        ☠️",
            "        /|\\",
            "       / | \\",
            "      /  |  \\",
            "     /   |   \\",
            "    ~~~~( )~~~~",
            "        | |",
            "      __|_|__",
            "     (       )",
            "      ~~~~~~~"
        ],
        "cruise": [
            "   ||  ||  ||  ||  ||",
            "  |                 |",
            "  |  ============   |",
            "  |  ============   |",
            " (  ===============  )",
            " |  ===============  |",
            "(  =================  )",
            " \\___________________/",
            "  ~~~~~~~~~~~~~~~~~~~"
        ]
    }
    
    if mini:
        # Mini cows - 3 cows per boat!
        cow_art = [
            "  ^_^    ^_^    ^_^",
            " (oo)\\ (oo)\\ (oo)\\",
            "  ||-w  ||-w  ||-w"
        ]
    else:
        # Regular cow - 1 cow per boat
        cow_art = [
            "        ^__^",
            "        (oo)\\_______",
            "        (__)\\       )\\/\\",
            "            ||----w |",
            "            ||     ||"
        ]
    
    boat_art = boats.get(boat_type, boats["raft"])
    return cow_art + boat_art

def animate_cowboat(num_cows=1, boat_type="raft", speed=0.1, mini=False):
    """Animate the cow(s) sailing away"""
    
    terminal_width, terminal_height = get_terminal_size()
    
    # Adjust spacing based on mini mode
    cow_spacing = 12 if mini else 30
    
    for frame in range(terminal_height + 10):
        clear_screen()
        
        # Calculate position
        y_pos = terminal_height - frame
        
        if y_pos < -10:
            break
            
        # Generate art for each cow
        for cow_idx in range(num_cows):
            # Offset each cow horizontally (closer spacing for mini cows)
            x_offset = cow_idx * cow_spacing
            
            if x_offset < terminal_width:
                cow_boat = get_cow_boat_art(boat_type, mini)
                
                # Print each line of the cow boat art
                for line_idx, line in enumerate(cow_boat):
                    actual_y = y_pos + line_idx
                    if 0 <= actual_y < terminal_height:
                        # Position cursor and print line
                        print(f"\033[{actual_y + 1};{x_offset + 1}H{line}")
        
        # Add some ocean waves at bottom
        if frame < terminal_height:
            wave_line = "~" * terminal_width
            print(f"\033[{terminal_height};1H{wave_line}")
        
        sys.stdout.flush()
        time.sleep(speed)
    
    # Final message
    cow_type = "mini cow(s)" if mini else "cow(s)"
    print(f"\033[{terminal_height//2};{terminal_width//2 - 10}HBon voyage, {cow_type}!")
    time.sleep(2)
    clear_screen()

def main():
    parser = argparse.ArgumentParser(description='Watch cows sail away on boats!')
    parser.add_argument('-n', '--num-cows', type=int, default=1, 
                       help='Number of cows (default: 1)')
    parser.add_argument('-b', '--boat', choices=['raft', 'ship', 'yacht', 'canoe', 'submarine', 'ferry', 'pirate', 'cruise'], 
                       default='raft', help='Type of boat (default: raft)')
    parser.add_argument('-s', '--speed', type=float, default=0.1,
                       help='Animation speed in seconds (default: 0.1)')
    parser.add_argument('--mini', action='store_true',
                       help='Use mini cows (3 cows per boat, closer spacing)')
    
    args = parser.parse_args()
    
    # Adjust limits for mini mode - more boats allowed since each has 3 mini cows
    max_boats = 10 if args.mini else 5
    
    if args.num_cows < 1 or args.num_cows > max_boats:
        cow_type = "boats (with 3 mini cows each)" if args.mini else "cows"
        print(f"Number of {cow_type} must be between 1 and {max_boats}")
        sys.exit(1)
    
    if args.mini:
        print("🐄 Mini cowboat fleet is setting sail... 🚤✨")
    else:
        print("🐄 Cowboat is setting sail... 🚤")
    time.sleep(1)
    
    animate_cowboat(args.num_cows, args.boat, args.speed, args.mini)

if __name__ == "__main__":
    main() 