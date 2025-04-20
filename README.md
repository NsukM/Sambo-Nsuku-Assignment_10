# Fitness Tracker – Assignment 10: Creational Patterns and Class Implementation

This project implements:
- All UML-based classes from the Fitness Tracker system
- Six major creational design patterns in Python
- Unit tests using pytest
- Project board updates (Assignment 7 link)

---

## Folder Structure

/src/
Core class files like User, Device, ActivitySession, etc.

/creational_patterns/
Six creational pattern modules:
- Simple Factory
- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton

/tests/
Unit tests using pytest

---

## Creational Pattern Rationales

- *Simple Factory*: Creates VitalStat instances based on stat type (HR, HRV, Sleep).
- *Factory Method*: Dynamically generates Recommendation objects depending on input.
- *Abstract Factory*: Builds grouped DailyReport and WeeklySummary objects.
- *Builder*: Builds complex FitnessProfile in steps.
- *Prototype*: Clones templates of Recommendation objects.
- *Singleton*: Ensures single shared access to a database connection object.

---

## Getting Started

To run the tests:
bash
pip install pytest
pytest tests/



⸻

Author
	•	Name: Nsuku Sambo
	•	Student Number: 221358986
	•	Module: Software Engineering

---
