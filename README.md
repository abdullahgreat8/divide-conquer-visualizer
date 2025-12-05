# Divide and Conquer Algorithms Visualization

A comprehensive Python project implementing and visualizing two classic divide-and-conquer algorithms: **Karatsuba's Integer Multiplication** and **Closest Pair of Points**.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [File Descriptions](#file-descriptions)
- [Contributors](#contributors)

## 🎯 Overview

This project demonstrates the power and efficiency of divide-and-conquer algorithms through interactive visualizations and GUI applications. It includes both computational implementations and visual simulations to help understand how these algorithms work step-by-step.

## ✨ Features

- **Interactive GUI Applications** with tkinter
- **Real-time Algorithm Visualization** showing recursive splits and combinations
- **Automated Test Data Generation** for both algorithms
- **Visual Step-by-Step Execution** with animations
- **Multiple Input File Support** (10 test cases for each algorithm)
- **Matplotlib Integration** for 2D point plotting
- **Comprehensive Test Suite** with pre-generated inputs

## 🧮 Algorithms Implemented

### 1. Karatsuba's Integer Multiplication
- **Complexity**: O(n^1.585) instead of O(n^2) for traditional multiplication
- **Features**:
  - Handles large integers (200-300 digits)
  - Visual representation of recursive splits
  - Step-by-step combination visualization
  - Animation of the divide-and-conquer process

### 2. Closest Pair of Points
- **Complexity**: O(n log n) instead of O(n^2) for brute force
- **Features**:
  - 2D plane point analysis
  - Visual representation of recursive partitioning
  - Strip band visualization
  - Real-time distance calculations
  - Interactive point plotting with matplotlib

## 🔧 Requirements

```
Python 3.7+
tkinter (usually comes with Python)
matplotlib
```

## 📥 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install required dependencies:
```bash
pip install matplotlib
```

3. Verify tkinter installation (should be included with Python):
```bash
python -m tkinter
```

## 🚀 Usage

### Option 1: Complete GUI Application (Q4.py)
Run the main GUI application that includes all features:
```bash
python Q4.py
```

This provides:
- Input file generation buttons
- File selection dropdowns
- Algorithm execution with visualization
- Results display windows

### Option 2: Individual Visualizations

#### Karatsuba Integer Multiplication Visualization
```bash
python simulation-IM.py
```
- Enter file number (1-10)
- Watch the step-by-step multiplication process
- See how numbers are split and combined

#### Closest Pair of Points Visualization
```bash
python simulation-CP.py
```
- Click "Run Simulation"
- See random points generated
- Watch the algorithm find the closest pair

### Option 3: Generate and Test Data (Q2.py)
Generate test input files:
```bash
python Q2.py
```
This creates:
- 10 closest pair input files (200-300 points each)
- 10 integer multiplication input files (200-300 digit numbers)

### Option 4: Batch Processing (Q3.py)
Run all test cases and visualize results:
```bash
python Q3.py
```
This will:
- Generate all input files
- Process all 10 closest pair test cases
- Process all 10 integer multiplication test cases
- Display matplotlib visualizations

## 📁 Project Structure

```
project-root/
│
├── Q2.py                           # Input file generator
├── Q3.py                           # Batch processing with visualization
├── Q4.py                           # Complete GUI application
├── simulation-IM.py                # Karatsuba visualization
├── simulation-CP.py                # Closest pair visualization
├── IM_input_1.txt                  # Sample integer multiplication input
│
├── closest_pair_point_inputs/      # Generated test files
│   ├── points_input1.txt
│   ├── points_input2.txt
│   └── ... (points_input10.txt)
│
└── integer_multiplication_inputs/  # Generated test files
    ├── multiplication_input1.txt
    ├── multiplication_input2.txt
    └── ... (multiplication_input10.txt)
```

## 📄 File Descriptions

### Main Applications
- **Q4.py**: Master GUI application with all features integrated
- **simulation-IM.py**: Interactive visualization of Karatsuba's algorithm
- **simulation-CP.py**: Interactive visualization of closest pair algorithm

### Utilities
- **Q2.py**: Generates random test input files for both algorithms
- **Q3.py**: Batch processes all test cases and displays results

### Input Files
- **closest_pair_point_inputs/**: Contains test files with 2D point coordinates
- **integer_multiplication_inputs/**: Contains test files with large integers
- **IM_input_1.txt**: Sample input file for integer multiplication

## 👥 Contributors

**Students**: 22K-4449, 22K-4601

## 📝 Notes

- The visualization speed can be adjusted by modifying `time.sleep()` values in the simulation files
- Input files are generated with random data for testing purposes
- The GUI applications provide user-friendly interfaces for non-technical users
- All algorithms are implemented using pure Python with divide-and-conquer approach

## 🎓 Educational Value

This project is ideal for:
- Understanding divide-and-conquer algorithm design
- Learning about computational complexity
- Visualizing recursive algorithms
- Comparing algorithmic efficiency
- Teaching data structures and algorithms concepts

## 📊 Performance

- **Karatsuba Multiplication**: Handles 200-300 digit integers efficiently
- **Closest Pair**: Processes 200-300 points in O(n log n) time
- Visual simulations include intentional delays for educational purposes

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## 📧 Contact

For questions or feedback, please contact the project contributors.

---

**Made with ❤️ for Algorithm Analysis and Design**
