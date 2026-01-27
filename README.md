# MIU-Class — Problem Solving (Classwork/Homework)

This workspace contains different classwork/homework (Python, C, Java) organized in date-wise folders.
Below is a detailed index of **which file covers which problem/topic**.

---

## Root (Top Level)

- `note.excalidraw` — Diagram/notes (not code).
- `README.md` — This index file.

---

## 20-Jul-2025 (Python — List/Input/Sort/Max)

- `first.py` — Takes 10 numbers as input, stores them in a list, and prints the list.
- `second.py` — Takes 10 numbers as input, sorts the list in ascending order, and prints it.
- `third.py` — Prints numbers from largest → smallest (manual max selection); includes trace prints; also finds max.
- `forth.py` — Squares each list element, then sorts in descending order and prints.
- `sir1.py` — Takes 2 numbers as input, appends to a list, and prints (basic list append).
- `sir2.py` — Finds the maximum of 10 numbers using a `while` loop; prints a trace of `k`, `numList[k]`, and `mx`.
- `sir3.py` — Finds the maximum of 10 numbers using a `for` loop; prints a trace.
- `sir4.py` — Finds max and swaps it into index 0 (moves the max to the “front”).

---

## 27-Jun-2025 (Python — Tkinter Basics + Loop/Break)

- `sir1.py` — Tkinter minimal window (`Tk()` + `mainloop()`).
- `sir2.py` — Sets Tkinter window title and geometry.
- `sir3.py` — Creates a Tkinter label and places it using `grid()`.
- `sir4.py` — Label/grid practice (similar to `sir3.py`).
- `sir6.py` — Label/grid practice (similar).
- `gui1.py` — Tkinter window + label (“First July Celebration, 2025 !”).
- `sir5.py` — Takes input 5 times in a `while` loop; breaks early if `x == 0`.
- `hw1.py` — Empty file (placeholder).

---

## 03-Aug-2025 (Python — Summation + Tkinter Label)

- `cw1.py` — Computes the sum of 1..10 using a `for` loop.
- `sir1.py` — Computes the sum of 1..10 using a direct expression.
- `sir2.py` — Step-by-step summation using `s = s + n` style (demonstration).
- `sir3.py` — Sum of 1..9 (`range(1,10)`).
- `sir4.py` — Tkinter window; shows label “1 + 2 + 3 + .... + 10 = ?”.

---

## 17-Aug-2025 (Python — File I/O + Simple Tkinter Calculator)

- `calc1.py` — Tkinter: two input fields; performs **addition** and shows the result in a label.
- `sir1.py` — Writes to `b67.txt` (write mode) — “Assalamu alaikum” sample.
- `hw1.py` — Writes personal info to `b67.txt` (Name/Roll/Dept).
- `sir2.py` — Reads `b67.txt` and prints the content.
- `sir3.py` — Opens `bigger.txt` in write mode and attempts to iterate lines (won’t read in this mode; class demo/unfinished).
- `tempCodeRunnerFile.py` — VS Code temporary snippet (placeholder).

---

## 24-Aug-2025 (Python — Tkinter Calculator Variations)

- `cw1.py` — Tkinter: 4 separate rows for add/subtract/multiply/divide — each row has its own input pair + result label.
- `cw2.py` — Tkinter: 2 input fields; button-based calculator for add/subtract/multiply/divide.
- `sir1.py` — Tkinter: text field-based calculator; builds expression from button clicks and uses `eval()` for calculate/clear. (The `*` operator button text/command is empty here—may be unfinished/typo.)
- `hw1.py` — Tkinter: full button calculator (0-9, +, -, *, /, =, C) — expression string + `eval()`.

---

## 20-Sep-2025 (C — Basics/Print/Formatting/Notes)

- `mam1.c` — Prints “Hello World” (C basics).
- `mam2.c` — Escape sequence demo (newline/tab) + comment notes (`\n`, `\t`, etc.).
- `mam3.c` — Comment-only notes about C operators/precedence (no code).
- `cw1.c` — Prints a formatted product list using `printf` (tabs/newlines).

---

## 20-Nov-2025 (C — Function + Area of Circle)

- `cw1.c` — Computes circle area using a `calc(radius)` function; takes radius input and prints the area.

---

## 19-Jan-2026 (Java — Loop/Math/Conversion/Input)

- `cw1.java` — Prints 1..10 using a `for` loop.
- `cw2.java` — Computes and prints the square of a number (num = 6).
- `cw3.java` — Converts Celsius → Fahrenheit and prints the result.
- `cw4.java` — Takes an integer using `Scanner` and prints “You entered: …”.

---

## 26-Jan-2026 (Java — Loops/Continue/Pattern)

- `cw1.java` — `while` loop demo: prints 1..5.
- `cw2.java` — `for` loop + `continue`: skips 3.
- `cw3.java` — `for` loop + `continue`: skips 3 and 4.
- `cw4.java` — Prints a `*` triangle pattern using nested loops.

---

## Run Tips (Quick)

- Python: `python <file>.py`
- C (MinGW gcc): `gcc file.c -o file.exe` then `./file.exe`
- Java: `javac File.java` then `java File`

