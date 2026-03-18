"""
AIOS Quantum - Quantum Computing Module for AIOS Ecosystem.

This package provides quantum computing capabilities with AINLP Bible v1.12
compliance, achieving Pylint 10/10 scores through proper documentation,
error handling, and code quality standards.

AINLP.dendritic[CONNECT] Related modules: AIOS core, quantum backends

Example:
    >>> from aios_quantum import QuantumCircuitBuilder, BackendManager
    >>> circuit = QuantumCircuitBuilder("demo", 5)
    >>> manager = BackendManager()
"""

from .circuit_builder import QuantumCircuitBuilder, create_example_circuit
from .backend_manager import (
    QuantumBackend,
    BackendManager,
    BackendType,
    create_example_backends
)

__version__ = "1.0.0"
__author__ = "AIOS Team"
__all__ = [
    "QuantumCircuitBuilder",
    "create_example_circuit",
    "QuantumBackend",
    "BackendManager",
    "BackendType",
    "create_example_backends",
]
