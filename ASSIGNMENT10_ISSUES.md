# Assignment 10 – GitHub Issues for Creational Pattern Tasks

This document contains the full list of GitHub issues used to track and manage the implementation of Assignment 10: Class Implementations, Six Creational Design Patterns, Unit Testing, and Documentation. These issues are also linked to the GitHub Kanban board to fulfill the Project Management (10%) requirement.

---

## 1. Implement Singleton Pattern for DB Access

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Implement the Singleton design pattern in `singleton.py` to manage a shared database connection.

- Create class: `DatabaseConnection`
- Implement Singleton logic using `__new__()`
- Add `connect()` and `disconnect()` methods
- File path: `creational_patterns/singleton.py`
- Related test: `tests/test_singleton.py`

---

## 2. Implement Simple Factory for VitalStat Creation

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Use a simple factory in `simple_factory.py` to instantiate `VitalStat` objects based on input.

- Create class: `VitalStatFactory`
- Method: `create_stat(stat_type, value)`
- Output class: `VitalStat`
- File path: `creational_patterns/simple_factory.py`

---

## 3. Implement Factory Method for Recommendations

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Use the Factory Method pattern in `factory_method.py` to dynamically return different `Recommendation` types.

- Create abstract class: `Recommendation`
- Concrete classes: `SleepRecommendation`, `ActivityRecommendation`
- Generators: `SleepRecGenerator`, `ActivityRecGenerator`
- File path: `creational_patterns/factory_method.py`

---

## 4. Implement Abstract Factory for Reports

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Apply the Abstract Factory pattern in `abstract_factory.py` to generate related objects together.

- Abstract class: `ReportFactory`
- Concrete factory: `FitnessDataFactory`
- Output objects: `DailyReport`, `WeeklySummary`
- File path: `creational_patterns/abstract_factory.py`

---

## 5. Implement Builder Pattern for FitnessProfile

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Create a builder class in `builder.py` to step-by-step construct `FitnessProfile` objects.

- Class: `FitnessProfileBuilder`
- Chaining methods: `set_age()`, `set_weight()`, `set_height()`, `set_activity_level()`
- Finalize with `build()`
- File path: `creational_patterns/builder.py`

---

## 6. Implement Prototype Pattern for Recommendations

**Labels**: `enhancement`, `creational-pattern`, `assignment10`

**Description**:  
Use the Prototype pattern in `prototype.py` to clone existing `Recommendation` instances.

- Add `clone()` method to `Recommendation`
- Create `RecommendationCache` to store and return deep copies
- Use `copy.deepcopy()`
- File path: `creational_patterns/prototype.py`

---

## 7. Add Unit Test for Singleton Pattern

**Labels**: `testing`, `assignment10`

**Description**:  
Add a test case in `test_singleton.py` to verify Singleton logic.

- Ensure all `DatabaseConnection()` instances refer to the same object
- Check shared `connected` state
- File path: `tests/test_singleton.py`

---

## 8. Update README.md for Assignment 10

**Labels**: `documentation`, `assignment10`

**Description**:  
Update `README.md` with complete documentation for Assignment 10.

- Add descriptions for all creational patterns
- Include folder structure
- Add pytest instructions
- Author: Nsuku Sambo – 221358986
- File path: `README.md`

---

## 9. Add CHANGELOG.md with Milestone Notes

**Labels**: `documentation`, `assignment10`

**Description**:  
Create `CHANGELOG.md` to document development progress and key additions.

- Mention implementation of:
  - Class diagram (`/src/`)
  - Six creational patterns (`/creational_patterns/`)
  - Unit test (`/tests/test_singleton.py`)
  - Project management issues (`/issues`)
- Format using versioned markdown headings
- File path: `CHANGELOG.md`
