# SmartOps Lead Cleaner CLI

A Python command-line project that reads lead data from a CSV file, validates each lead, detects duplicate records, separates invalid data, and generates clean output files with a summary.

This project was built as part of my AI/LLM engineering roadmap to strengthen Python fundamentals, file processing, data validation, object-oriented programming, Pandas, CLI arguments, and automated testing.

---

## Features

* Reads leads from a CSV file
* Accepts the input file through a command-line argument
* Validates required CSV columns
* Normalizes lead data before processing
* Normalizes email addresses to lowercase
* Removes formatting characters from phone numbers
* Validates email format
* Validates phone format
* Checks required fields:

  * Name
  * Email
  * Phone
  * Company
  * Stage
* Detects duplicate email addresses
* Detects duplicate phone numbers
* Calculates a lead score
* Creates three output CSV files:

  * `clean.csv`
  * `duplicates.csv`
  * `errors.csv`
* Provides a reason for duplicate and invalid records
* Prints a processing summary in the terminal
* Includes pytest tests for important project functions

---

## Project Structure

```text
Project1_LeadCleaner/
│
├── lead.py
├── lead_cleaner.py
├── leads.csv
├── clean.csv
├── duplicates.csv
├── errors.csv
├── test_lead_cleaner.py
└── README.md
```

### `lead.py`

Contains the `Lead` class and the business logic for an individual lead.

The class handles:

* Lead attributes
* Email validation
* Phone validation
* Lead scoring
* Lead validity
* Conversion of a Lead object into a dictionary

### `lead_cleaner.py`

Main CLI application.

It handles:

* Command-line arguments
* Reading the CSV with Pandas
* Checking required columns
* Normalizing rows
* Creating `Lead` objects
* Validating leads
* Detecting duplicates
* Categorizing records
* Writing output CSV files
* Printing the summary

### `test_lead_cleaner.py`

Contains pytest tests for functions such as:

* `normalize_phone()`
* `normalize_row()`
* `get_validation_errors()`
* `get_duplicate_reason()`
* `process_leads()`

---

## Required Input Columns

The input CSV must contain the following columns:

```csv
name,email,phone,company,stage
```

Example:

```csv
name,email,phone,company,stage
John Smith,john@example.com,5195551234,Secure North,Qualified
Sara Khan,sara@example.com,4165559876,CleanPro,New
Mike Brown,bad-email,6475554567,Staffing Plus,Proposal
```

---

## Installation

Install the required Python packages:

```bash
python -m pip install pandas pytest
```

---

## How to Run

Run the program from the project directory:

```bash
python lead_cleaner.py --input leads.csv
```

The `--input` argument tells the program which CSV file should be processed.

To view the CLI help:

```bash
python lead_cleaner.py --help
```

---

## Data Normalization

Before validation, lead data is normalized.

### Email

Email addresses are:

* Trimmed
* Converted to lowercase

Example:

```text
 JOHN@EXAMPLE.COM
```

becomes:

```text
john@example.com
```

### Phone

All non-digit characters are removed.

Example:

```text
(519) 555-1234
```

becomes:

```text
5195551234
```

This also allows duplicate phone numbers to be detected even when they are formatted differently.

---

## Validation Rules

A lead is checked for the following problems:

* Missing name
* Invalid email
* Invalid phone
* Missing company
* Missing company stage

If one lead has multiple problems, all reasons are recorded.

Example:

```text
Invalid Email; Company Name Missing
```

The record is written to:

```text
errors.csv
```

---

## Duplicate Detection

Only valid leads are checked for duplicates.

A lead is considered a duplicate when its normalized:

* Email has already appeared

or

* Phone number has already appeared

Example:

```text
Duplicate Email
```

or:

```text
Duplicate Email; Duplicate Phone
```

The first valid occurrence remains in:

```text
clean.csv
```

Later matching records are written to:

```text
duplicates.csv
```

---

## Output Files

### `clean.csv`

Contains valid and unique leads.

### `duplicates.csv`

Contains valid leads whose email or phone number already appeared in an earlier clean record.

A `Reason` column explains the duplicate.

### `errors.csv`

Contains invalid leads.

A `Reason` column explains why each record failed validation.

---

## Console Summary

After processing finishes, the program prints a summary similar to:

```text
SmartOps Lead Cleaner Summary
-----------------------------
Total rows:       10
Clean leads:      5
Duplicate leads:  2
Invalid leads:    3
```

Every input row belongs to exactly one category:

```text
Clean + Duplicates + Errors = Total Rows
```

---

## Running Tests

Run the automated tests with:

```bash
python -m pytest test_lead_cleaner.py -v
```

Example output:

```text
test_normalize_phone PASSED
test_normalized_row PASSED
test_validation_errors PASSED
test_duplicate_reason PASSED
test_process_leads PASSED
```

---

## Key Python Concepts Practiced

This project uses:

* Python classes
* Object-oriented programming
* Regular expressions
* Dictionaries
* Lists
* Sets
* Functions
* Exception handling
* File processing
* Pandas DataFrames
* Command-line arguments with `argparse`
* Data normalization
* Duplicate detection
* pytest unit testing

---

## Processing Flow

```text
Command Line
    ↓
python lead_cleaner.py --input leads.csv
    ↓
Read CSV using Pandas
    ↓
Check Required Columns
    ↓
Loop Through Every Row
    ↓
Normalize Data
    ↓
Create Lead Object
    ↓
Validate Lead
    ↓
Invalid?
    ├── Yes → errors.csv
    │
    └── No
         ↓
      Duplicate?
         ├── Yes → duplicates.csv
         │
         └── No → clean.csv
    ↓
Print Console Summary
```

---

## Future Improvements

Possible future improvements include:

* Configurable validation rules
* Support for additional lead fields
* Logging
* Larger file processing
* Database integration
* API-based lead enrichment
* Async processing for external API calls
* SmartOps integration
* AI-assisted lead scoring

---

## Author

Built as part of an AI/LLM engineering roadmap and SmartOps applied engineering projects.
