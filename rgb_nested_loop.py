#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 2, 2025
# This program uses nested loops to
# display some of the RGB colors.


# Define the main function.
def main():
    # Display a newline for formatting.
    print()
    # Use a for loop to iterate over the red
    # intensity levels from 0 to 255 (inclusive).
    # Increment by 51 to prevent display issues.
    for red_counter in range(0, 256, 51):
        # Nest a for loop to iterate over the green
        # intensity levels from 0 to 255 (inclusive).
        # Increment by 51 to prevent display issues.
        for green_counter in range(0, 256, 51):
            # Nest a for loop to iterate over the blue
            # intensity levels from 0 to 255 (inclusive).
            # Increment by 51 to prevent display issues.
            for blue_counter in range(0, 256, 51):
                # Display the RGB notation and format
                # it to show the actual colour.
                print(
                    f"\033[38;2;{red_counter};{green_counter};{blue_counter}m"
                    f"RGB({red_counter}, {green_counter}, {blue_counter})"
                )


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
