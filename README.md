# BO6-Terminus-Solver
Black Ops 6: Zombies - Terminus - Main Quest SOLVER

# Black Ops 6: Zombies - Terminus - Main Quest Solver

This is a web-based application designed to help players solve the main quest for the Zombies mode in "Black Ops 6." It computes values based on selected symbols and provides results in real-time. 

![Terminus Quest Solver Screenshot](screenshot.png) <!-- Add a screenshot of the app if you like -->

## Features

- **Real-time Calculation**: Results are computed instantly as you select symbols for X, Y, and Z.
- **User-Friendly Interface**: Designed to be mobile-friendly with an intuitive layout and easy-to-understand results table.
- **Dynamic Symbol Selection**: Users can select symbols that correspond to unique values, which are then used in predefined mathematical formulas.

## Setup Instructions

1. **Place Symbol Images**: Ensure the following PNG files are in the same directory as the HTML file:
   - `0.png`, `10.png`, `11.png`, `20.png`, `21.png`, `22.png`
   - Each file name corresponds to the initial values used in the calculations (e.g., `0.png` represents 0, `10.png` represents 10, etc.).

2. **Open the HTML File**:
   - Open the HTML file (`index.html`) in a web browser. It’s compatible with most modern browsers and is responsive for mobile devices.

3. **Use the Application**:
   - Select symbols for X, Y, and Z by clicking on the images. The app will automatically compute and display the results in the "Code" table.

## Math Behind the Solver

The app calculates three specific expressions based on values assigned to variables **X**, **Y**, and **Z**, corresponding to selected images.

### Expressions

1. **Line 1**: `2X + 11`
   - This formula doubles the value of **X** and then adds 11.

2. **Line 2**: `(2Z + Y) - 5`
   - This formula doubles **Z**, adds **Y**, and subtracts 5.

3. **Line 3**: `(Y + Z) - X`
   - This formula adds **Y** and **Z** together, then subtracts **X**.

Each result is displayed as the absolute value to ensure positive numbers.

### Example Calculation

If **X** = 10, **Y** = 20, and **Z** = 5:

- **Line 1**: `2(10) + 11 = 31`
- **Line 2**: `(2(5) + 20) - 5 = 25`
- **Line 3**: `(20 + 5) - 10 = 15`

The results would display as:


