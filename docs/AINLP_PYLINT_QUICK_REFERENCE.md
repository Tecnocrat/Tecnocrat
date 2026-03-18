# AINLP Pylint Quick Reference Card

## Common Fixes Cheat Sheet

### W1514: Missing encoding
```python
# ❌ Wrong
open('file.txt', 'r')
open('data.json', 'w')

# ✅ Right
open('file.txt', 'r', encoding='utf-8')
open('data.json', 'w', encoding='utf-8')
```

### W0718: Broad exception
```python
# ❌ Wrong
try:
    operation()
except:
    pass

except Exception:
    handle()

# ✅ Right
try:
    operation()
except (ValueError, IOError) as exc:
    handle(exc)
```

### C0114: Missing module docstring
```python
# ✅ Add at top of file
"""
Module Name - Brief description.

Extended description of module purpose.

AINLP.dendritic[CONNECT] Related modules: module1, module2
"""
```

### C0115: Missing class docstring
```python
# ✅ Add after class definition
class MyClass:
    """
    Brief class description.

    Attributes:
        attr1: Description
        attr2: Description
    """
```

### C0116: Missing function docstring
```python
# ✅ Add after function definition
def my_function(param: str) -> bool:
    """
    Brief function description.

    Args:
        param: Parameter description

    Returns:
        Return value description

    Raises:
        ValueError: When this occurs
    """
```

### W1203: Logging f-string
```python
# ❌ Wrong
logger.info(f"Processing {name} with {count} items")
logger.error(f"Failed: {error}")

# ✅ Right
logger.info("Processing %s with %d items", name, count)
logger.error("Failed: %s", error)
```

### R0917: Too many positional arguments
```python
# ❌ Wrong (>5 positional args)
def create(name, type, size, color, weight, width, height):
    pass

# ✅ Right (use keyword-only after *)
def create(name, type, *, size=10, color='red', weight=1, width=100, height=100):
    pass
```

### W0311/W0293: Trailing whitespace
```bash
# Run this to fix all files
find . -name "*.py" -exec sed -i 's/[[:space:]]*$//' {} +
```

### E0401: Import error
```python
# For runtime dependencies like qiskit
# Option 1: Per-file disable
# pylint: disable=import-error

# Option 2: Try/except
try:
    from qiskit import QuantumCircuit
except ImportError:
    QuantumCircuit = None
```

### C0301: Line too long
```ini
# In .pylintrc - DISABLED per AINLP.buffer[120]
[MESSAGES CONTROL]
disable=C0301
```

## Before/After Example

### Before (6.51/10)
```python
import os

def process_file(filename, mode, encoding, opts, flags, timeout):
    try:
        f = open(filename, mode)
        data = f.read()
        f.close()
        logger.info(f"Processed {filename}")
    except:
        pass
```

### After (10.00/10)
```python
"""
File Processing Module - Handles file operations.

Provides utilities for reading and processing files
with proper error handling and encoding.

AINLP.dendritic[CONNECT] Related modules: file_utils
"""

import logging

logger = logging.getLogger(__name__)


def process_file(
    filename: str,
    mode: str,
    *,
    encoding: str = 'utf-8',
    opts: dict = None,
    flags: list = None,
    timeout: int = 30
) -> str:
    """
    Process file with specified options.

    Args:
        filename: Path to file to process
        mode: File open mode ('r', 'w', etc.)
        encoding: File encoding (keyword-only)
        opts: Processing options (keyword-only)
        flags: Processing flags (keyword-only)
        timeout: Operation timeout in seconds (keyword-only)

    Returns:
        Processed file data as string

    Raises:
        IOError: If file cannot be opened
        ValueError: If mode is invalid
    """
    try:
        with open(filename, mode, encoding=encoding) as file:
            data = file.read()
        logger.info("Processed file: %s", filename)
        return data
    except IOError as exc:
        logger.error("Failed to process file %s: %s", filename, str(exc))
        raise
```

## Verification Command

```bash
# Check single file
python -m pylint myfile.py --rcfile=.pylintrc

# Check all files in directory
python -m pylint src/module/*.py --rcfile=.pylintrc --exit-zero

# Target: Your code has been rated at 10.00/10
```

## AINLP Compliance Checklist

- [ ] `.pylintrc` with C0301 disabled
- [ ] All `open()` have `encoding='utf-8'`
- [ ] No bare `except:` or broad `except Exception:`
- [ ] Module docstrings with AINLP.dendritic[CONNECT]
- [ ] Class docstrings with Attributes
- [ ] Function docstrings with Args/Returns/Raises
- [ ] Logging uses `%` not f-strings
- [ ] Functions with 5+ args use `*` for keyword-only
- [ ] No trailing whitespace
- [ ] Score = 10.00/10 ✓

---

**Quick Reference v1.0** | **AINLP Bible v1.12**
