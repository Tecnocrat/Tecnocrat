# AINLP-Compliant Python Example Templates

This directory contains example Python files that demonstrate AINLP Bible v1.12 compliance and achieve Pylint 10/10 scores.

## Contents

- `src/aios_quantum/` - Example quantum computing module
  - `__init__.py` - Package initialization with proper docstrings
  - `circuit_builder.py` - Quantum circuit builder demonstrating all AINLP fixes
  - `backend_manager.py` - Backend management with complex patterns

## Pylint Score

All files in this directory achieve a perfect Pylint score:

```bash
cd examples/aios_quantum_template
python -m pylint src/aios_quantum/*.py --rcfile=../../.pylintrc

# Output:
# Your code has been rated at 10.00/10
```

## AINLP Standards Demonstrated

### 1. Line Length Liberation (AINLP.buffer[120])
- C0301 disabled - no line length restrictions
- Natural flowing code with soft-wrap support

### 2. Encoding Specification (W1514)
All `open()` calls include `encoding='utf-8'`:
```python
with open(path, 'w', encoding='utf-8') as file:
    file.write(content)
```

### 3. Specific Exception Handling (W0718)
No broad `except Exception:` - specific exceptions only:
```python
try:
    risky_operation()
except (IOError, OSError) as exc:
    logger.error("Operation failed: %s", str(exc))
    raise
```

### 4. Complete Docstrings (C0114/C0115/C0116)
- Module docstrings with AINLP.dendritic[CONNECT] references
- Class docstrings with Attributes sections
- Function docstrings with Args/Returns/Raises sections

### 5. Logging Format (W1203)
Uses `%` formatting instead of f-strings:
```python
# Good
logger.info("Processing %s with %d items", name, count)

# Avoid
logger.info(f"Processing {name} with {count} items")
```

### 6. Keyword-Only Arguments (R0917)
Functions with many parameters use `*` marker:
```python
def function(required1, required2, *, optional1=default, optional2=default):
    """Use keyword-only pattern for readability."""
    pass
```

### 7. No Trailing Whitespace
All files are clean of trailing whitespace (W0311/W0293).

## Usage as Templates

These files serve as templates for creating new AINLP-compliant Python modules:

1. Copy the structure to your new module
2. Update docstrings with your module's purpose
3. Implement your functionality following the patterns shown
4. Run Pylint to verify 10/10 score

## Testing

To verify the examples maintain 10/10:

```bash
# From repository root
cd examples/aios_quantum_template
python -m pylint src/aios_quantum/*.py --rcfile=../../.pylintrc --exit-zero
```

Expected output:
```
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Integration

To use these patterns in your AIOS project:

1. Copy `.pylintrc` to your project root
2. Follow the patterns shown in these example files
3. Run Pylint after each change
4. Aim for 10.00/10 before committing

## Documentation

See `docs/AINLP_PYLINT_REMEDIATION.md` for complete remediation guide and detailed explanations of each fix.

---

**AINLP.quality[VERIFIED]** - All examples achieve Pylint 10.00/10
