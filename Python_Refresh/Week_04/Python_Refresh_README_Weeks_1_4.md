# Python Refresh — Weeks 1–4

This folder documents my Python foundation refresh as part of the **SmartOps AI/LLM Engineer Roadmap**.

The goal of these first four weeks was to strengthen core Python skills before moving into async programming, FastAPI, LLM APIs, RAG, LangChain, LangGraph, and AWS.

> **Note:** DSA practice is intentionally excluded from this README and will be maintained in a separate branch and folder.

---

## Repository Structure

```text
Python_Refresh/
├── Week_1/
├── Week_2/
├── Week_3/
├── Week_4/
└── README.md
```

Each weekly folder contains exercises, problem-set work, tests, and small projects completed during that week.

---

# Week 1 — Functions, Variables, and Conditionals

## Topics Covered

- Python syntax and indentation
- Variables and data types
- Functions and parameters
- User input and formatted output
- Conditional statements
- Boolean expressions
- Basic error handling

## Exercises

- Temperature converter
- FizzBuzz
- Palindrome checker
- Four-operation calculator
- Vowel counter
- CS50P Problem Sets 0 and 1

## Main Takeaway

Week 1 refreshed the fundamentals of writing small Python programs using functions, input, conditions, and reusable logic.

---

# Week 2 — Loops, Exceptions, and Libraries

## Topics Covered

- `for` loops
- `while` loops
- `break` and `continue`
- `try` and `except`
- Raising and handling errors
- Importing Python libraries
- Installing packages with `pip`
- Calling external APIs with `requests`

## Exercises

- CS50P Problem Sets 2, 3, and 4
- API request script using JSONPlaceholder
- Parsing JSON API responses
- Printing selected values from returned API data
- Practice with `requests`, `pandas`, and `numpy`

## Main Takeaway

Week 2 focused on controlling repeated program flow, preventing crashes with exception handling, and using external Python libraries.

---

# Week 3 — Unit Testing and File I/O

## Topics Covered

- Unit testing with `pytest`
- Writing test functions
- Using `assert`
- Reading and writing text files
- Reading and writing CSV files
- Reading and writing JSON files
- Using `csv.DictReader`
- Using `csv.DictWriter`
- Separating valid and invalid data

## Exercises and Projects

- CS50P Problem Sets 5 and 6
- JSON file reader and editor
- SmartOps lead CSV cleaner
- Email validation
- Phone validation
- Clean lead CSV output
- Rejected lead CSV output with reasons
- Pytest tests for validation logic

## Main Takeaway

Week 3 introduced automated testing and data-processing workflows. The lead cleaner was the first exercise directly connected to a SmartOps business use case.

---

# Week 4 — Regular Expressions and Object-Oriented Programming

## Topics Covered

- Regular expressions with `re`
- `re.search`
- `re.fullmatch`
- Capture groups
- Classes and objects
- `__init__`
- Instance attributes
- Instance methods
- `__str__`
- Properties
- Getters and setters
- Internal attributes such as `_size` and `_capacity`
- Inheritance concepts
- Type hints, decorators, and generators

## CS50P and Practice Exercises

- YouTube iframe URL parser
- Date-of-birth-to-minutes calculator
- Cookie Jar class
- CS50 shirtificate PDF generator
- Student class with validated house property
- Lead class for SmartOps-style lead data
- CS50P Problem Sets 7, 8, and 9

## Lead Class Features

The Lead class includes:

- Lead name
- Email
- Phone
- Company
- Stage
- Regex-based email validation
- Regex-based phone validation
- Lead score calculation
- Dictionary conversion
- Readable string representation

## Main Takeaway

Week 4 moved from procedural scripts into object-oriented design. It also introduced controlled access to internal data using properties and validation.

---

# Skills Strengthened Across Weeks 1–4

- Writing reusable Python functions
- Organizing programs with `main()`
- Validating user input
- Handling errors safely
- Processing JSON and CSV data
- Calling external APIs
- Writing automated tests
- Using regular expressions
- Creating and working with Python classes
- Reading third-party library documentation
- Converting business requirements into Python logic

---

# Running the Exercises

Navigate into the relevant weekly folder:

```bash
cd Python_Refresh/Week_4
```

Run a Python file:

```bash
python filename.py
```

Run tests:

```bash
pytest
```

Run one test file:

```bash
pytest test_filename.py
```

---

# Git Workflow

Each roadmap week is maintained in its own branch.

Example:

```bash
git switch main
git pull origin main
git switch -c week-4
```

After completing the week:

```bash
git add Python_Refresh/Week_4
git commit -m "week-4: add regex and OOP exercises"
git push -u origin week-4
```

Then create a pull request and merge the weekly branch into `main`.

---

# DSA

DSA exercises are not included in this folder.

They will be maintained separately so the Python-refresh work and interview-problem practice remain clearly organized.

---

# Next Step — Week 5

Week 5 moves from Python foundations into:

- Inheritance through `HighValueLead`
- Async programming with `asyncio`
- Exercism Python exercises
- SmartOps Lead Cleaner CLI
- Command-line arguments
- Pandas-based data processing
- More complete pytest coverage

The Week 5 project will be the first larger portfolio-style Python project in the roadmap.
