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

def get_cow_boat_art(boat_type="raft"):
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
    
    cow_art = [
        "        ^__^",
        "        (oo)\\_______",
        "        (__)\\       )\\/\\",
        "            ||----w |",
        "            ||     ||"
    ]
    
    boat_art = boats.get(boat_type, boats["raft"])
    
    return cow_art + boat_art

def animate_cowboat(num_cows=1, boat_type="raft", speed=0.1):
    """Animate the cow(s) sailing away"""
    
    terminal_width, terminal_height = get_terminal_size()
    
    for frame in range(terminal_height + 10):
        clear_screen()
        
        # Calculate position
        y_pos = terminal_height - frame
        
        if y_pos < -10:
            break
            
        # Generate art for each cow
        for cow_idx in range(num_cows):
            # Offset each cow horizontally
            x_offset = cow_idx * 30
            
            if x_offset < terminal_width:
                cow_boat = get_cow_boat_art(boat_type)
                
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
    print(f"\033[{terminal_height//2};{terminal_width//2 - 10}HBon voyage, cow(s)!")
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
    
    args = parser.parse_args()
    
    if args.num_cows < 1 or args.num_cows > 5:
        print("Number of cows must be between 1 and 5")
        sys.exit(1)
    
    print("🐄 Cowboat is setting sail... 🚤")
    time.sleep(1)
    
    animate_cowboat(args.num_cows, args.boat, args.speed)

if __name__ == "__main__":
    main() 