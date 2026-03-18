# AINLP Pylint 10/10 Remediation Guide

## Overview

This guide documents the complete process for achieving Pylint 10/10 scores according to AINLP Bible v1.12 standards. The remediation follows the "Line Length Liberation" philosophy (AINLP.buffer[120]) and other AIOS ecosystem standards.

## AINLP Bible v1.12 Standards

### Line Length Liberation (AINLP.buffer[120])

**Philosophy**: In the age of AI tokens and editor soft-wrap (Alt+Z), line length limits are obsolete.

- **C0301 DISABLED** - Line length violations are ignored
- `max-line-length=120` set as backup safety only
- **DO NOT** wrap lines to 79 characters
- **DO** write naturally flowing code that's readable with soft-wrap

### Required Fixes

#### 1. W1514 - Missing Encoding in open()

**Issue**: All `open()` calls must explicitly specify `encoding='utf-8'`

**Before**:
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

**After**:
```python
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

#### 2. W0718 - Broad Exception Handling

**Issue**: Avoid bare `except:` or overly broad `except Exception:`

**Before**:
```python
try:
    risky_operation()
except Exception:
    logger.error("Something went wrong")
```

**After**:
```python
try:
    risky_operation()
except (IOError, ValueError) as exc:
    logger.error("Operation failed: %s", str(exc))
```

#### 3. C0114/C0115/C0116 - Missing Docstrings

**Issue**: All modules, classes, and functions need docstrings

**Module Docstring**:
```python
"""
Module Name - Brief description.

Extended description of module purpose and role in the system.
Explain key concepts and usage patterns.

AINLP.dendritic[CONNECT] Related modules: module1, module2
"""
```

**Class Docstring**:
```python
class Example:
    """
    Brief class description in one line.
    
    Extended description explaining the class purpose,
    behavior, and usage patterns.
    
    Attributes:
        attr1: Description of attribute1
        attr2: Description of attribute2
    """
```

**Function/Method Docstring**:
```python
def function(param1: str, param2: int) -> bool:
    """
    Brief function description.
    
    Extended description of what the function does,
    any important behaviors, and usage notes.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: Description of when this is raised
        IOError: Description of when this is raised
    """
```

#### 4. W1203 - Logging with f-strings

**Issue**: Use `%` formatting in logging, not f-strings (performance)

**Before**:
```python
logger.info(f"Processing {name} with {count} items")
```

**After**:
```python
logger.info("Processing %s with %d items", name, count)
```

**Rationale**: Lazy evaluation - string formatting only happens if log level allows

#### 5. R0917 - Too Many Positional Arguments

**Issue**: Functions with many parameters should use keyword-only arguments

**Before**:
```python
def create_circuit(name, qubits, depth, shots, backend):
    pass
```

**After**:
```python
def create_circuit(name, qubits, *, depth=10, shots=1024, backend="simulator"):
    """
    Create quantum circuit.
    
    Args:
        name: Circuit name
        qubits: Number of qubits
        depth: Circuit depth (keyword-only)
        shots: Number of shots (keyword-only)
        backend: Backend name (keyword-only)
    """
    pass
```

The `*` forces parameters after it to be keyword-only.

#### 6. Trailing Whitespace (W0311/W0293)

**Issue**: Remove all trailing whitespace

**Fix**: Configure your editor to strip trailing whitespace on save, or run:
```bash
# Strip trailing whitespace
find . -name "*.py" -exec sed -i 's/[[:space:]]*$//' {} +
```

### Import Errors (E0401)

**Special Case**: Qiskit and other runtime dependencies may not be installed during linting

**Solution**:
```python
# At top of file if needed
# pylint: disable=import-error

try:
    from qiskit import QuantumCircuit
except ImportError:
    QuantumCircuit = None  # Type stub or mock
```

Or in `.pylintrc`:
```ini
[MESSAGES CONTROL]
disable=E0401  # Only if all imports are runtime-only
```

## Pylint Configuration (.pylintrc)

The `.pylintrc` file in the root directory contains the complete AINLP-compliant configuration:

Key settings:
- `C0301` (line-too-long) is **DISABLED**
- `max-line-length=120` as backup
- `fail-under=10.0` requires perfect score
- `max-positional-arguments=5` enforces keyword-only patterns
- Proper exception handling enforcement enabled

## Remediation Workflow

### 1. Initial Assessment

```bash
cd aios-quantum
python -m pylint src/aios_quantum/*.py --exit-zero
```

Note the current score and all violations.

### 2. Fix Issues by Priority

**Priority 1: Critical (Prevents 10/10)**
- W1514 - Missing encoding
- C0114/C0115/C0116 - Missing docstrings
- W0718 - Broad exceptions

**Priority 2: Important**
- W1203 - Logging f-strings
- R0917 - Too many positional args
- Trailing whitespace

**Priority 3: Style**
- Naming conventions
- Import organization

### 3. Fix Each File

For each Python file:

1. Add module docstring at top
2. Add encoding to all `open()` calls
3. Replace broad exception handlers with specific ones
4. Add class and function docstrings
5. Fix logging statements (% instead of f-strings)
6. Add `*` for keyword-only arguments where needed
7. Strip trailing whitespace

### 4. Verify Each File

```bash
python -m pylint src/aios_quantum/specific_file.py
```

Aim for 10.00/10 on each file before moving to next.

### 5. Final Verification

```bash
# Check all files
python -m pylint src/aios_quantum/*.py --exit-zero

# Expected output:
# Your code has been rated at 10.00/10
```

## Example Files

See `examples/aios_quantum_template/` for fully compliant example files:

- `circuit_builder.py` - Demonstrates all fixes
- `backend_manager.py` - Complex example with enums
- `__init__.py` - Package initialization

All example files achieve 10/10 Pylint scores.

## Common Pitfalls

### 1. Forgetting encoding parameter
```python
# WRONG
open('file.txt', 'r')

# RIGHT
open('file.txt', 'r', encoding='utf-8')
```

### 2. Catching Exception instead of specific types
```python
# WRONG
except Exception as e:
    pass

# RIGHT
except (ValueError, IOError) as exc:
    pass
```

### 3. Using f-strings in logging
```python
# WRONG
logger.info(f"Value: {value}")

# RIGHT
logger.info("Value: %s", value)
```

### 4. Missing keyword-only marker
```python
# WRONG (too many positional args)
def func(a, b, c, d, e, f):
    pass

# RIGHT
def func(a, b, *, c, d, e, f):
    pass
```

## Testing the Configuration

To test the `.pylintrc` configuration on the example files:

```bash
cd examples/aios_quantum_template
python -m pylint src/aios_quantum/*.py --exit-zero
```

Expected output:
```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## PR Requirements

When creating the PR:

1. **Title**: `feat: Pylint 10/10 remediation (AINLP.buffer[120])`
2. **Description**: Include:
   - Before/after Pylint scores
   - List of files modified
   - Summary of changes per AINLP standard
   - Reference to AINLP Bible v1.12
3. **Branch**: `feat/pylint-remediation`

## Verification Command

Final verification command:
```bash
python -m pylint src/aios_quantum/*.py \
  --rcfile=.pylintrc \
  --exit-zero \
  --output-format=text
```

## AINLP Compliance Checklist

- [ ] `.pylintrc` configured with AINLP standards
- [ ] C0301 (line-too-long) disabled
- [ ] All `open()` calls have `encoding='utf-8'`
- [ ] No broad exception handlers
- [ ] All modules have docstrings
- [ ] All classes have docstrings
- [ ] All functions have docstrings
- [ ] Logging uses `%` formatting, not f-strings
- [ ] Functions with 5+ args use keyword-only pattern
- [ ] No trailing whitespace
- [ ] E0401 handled for qiskit imports
- [ ] Score: 10.00/10 ✓

---

**AINLP.orchestration[COMPLETE]** - Remediation guide complete  
**Version**: 1.0.0  
**Standard**: AINLP Bible v1.12  
**Target**: Pylint 10.00/10
