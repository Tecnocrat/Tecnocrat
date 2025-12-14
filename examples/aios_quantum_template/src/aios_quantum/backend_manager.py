"""
Quantum Backend Manager - AINLP Compliant Example.

Manages quantum computing backends with proper error handling,
logging, and documentation according to AINLP Bible v1.12.

AINLP.dendritic[CONNECT] Related modules: circuit_builder, quantum_optimizer
"""

import logging
from typing import List, Dict, Any, Optional
from enum import Enum

# Initialize module logger
logger = logging.getLogger(__name__)


class BackendType(Enum):
    """
    Quantum backend types enumeration.

    Attributes:
        SIMULATOR: Quantum circuit simulator
        REAL_DEVICE: Physical quantum hardware
        CLOUD: Cloud-based quantum service
    """

    SIMULATOR = "simulator"
    REAL_DEVICE = "real_device"
    CLOUD = "cloud"


class QuantumBackend:
    """
    Represents a quantum computing backend.

    This class manages connections and operations on quantum backends,
    demonstrating AINLP compliance with proper docstrings and error handling.

    Attributes:
        name: Backend name
        backend_type: Type of backend (simulator, real device, or cloud)
        available_qubits: Number of available qubits
        is_connected: Connection status flag
    """

    def __init__(
        self,
        name: str,
        backend_type: BackendType,
        *,
        available_qubits: int = 5,
        config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize quantum backend.

        Args:
            name: Backend identifier name
            backend_type: Type of backend to initialize
            available_qubits: Number of qubits available (keyword-only)
            config: Optional configuration dictionary (keyword-only)
        """
        self.name = name
        self.backend_type = backend_type
        self.available_qubits = available_qubits
        self.is_connected = False
        self.config = config or {}

        logger.info("Backend initialized: %s (type: %s)", name, backend_type.value)

    def connect(self, *, timeout: int = 30) -> bool:
        """
        Connect to the quantum backend.

        Args:
            timeout: Connection timeout in seconds (keyword-only)

        Returns:
            True if connection successful, False otherwise

        Raises:
            ConnectionError: If connection fails after timeout
        """
        try:
            # Simulate connection logic
            logger.info("Connecting to backend: %s with timeout: %d", self.name, timeout)

            # In real implementation, this would connect to actual backend
            self.is_connected = True

            logger.info("Successfully connected to backend: %s", self.name)
            return True

        except ConnectionError as exc:
            # W0718 FIX: Specific exception handling
            logger.error("Connection failed for backend %s: %s", self.name, str(exc))
            raise

    def disconnect(self) -> None:
        """
        Disconnect from the quantum backend.

        Properly closes connection and logs the action.
        """
        if self.is_connected:
            self.is_connected = False
            logger.info("Disconnected from backend: %s", self.name)
        else:
            logger.warning("Backend %s was not connected", self.name)

    def execute_circuit(
        self,
        circuit_data: Dict[str, Any],
        *,
        shots: int = 1024,
        optimization_level: int = 1
    ) -> Dict[str, Any]:
        """
        Execute a quantum circuit on this backend.

        Args:
            circuit_data: Circuit configuration dictionary
            shots: Number of measurement shots (keyword-only)
            optimization_level: Circuit optimization level 0-3 (keyword-only)

        Returns:
            Dictionary containing execution results

        Raises:
            RuntimeError: If backend is not connected
            ValueError: If circuit_data is invalid
        """
        if not self.is_connected:
            raise RuntimeError("Backend %s is not connected" % self.name)

        if not circuit_data:
            raise ValueError("Circuit data cannot be empty")

        # W1203 FIX: Use % formatting in logging, not f-strings
        logger.info("Executing circuit on backend: %s with shots: %d", self.name, shots)

        # Simulate execution with dynamic results based on shots
        half_shots = shots // 2
        results = {
            "backend": self.name,
            "shots": shots,
            "optimization_level": optimization_level,
            "success": True,
            "results": {"00": half_shots, "11": shots - half_shots}  # Even distribution
        }

        return results


class BackendManager:
    """
    Manages multiple quantum backends.

    Provides interface for backend discovery, connection management,
    and circuit execution across different backend types.

    Attributes:
        backends: List of managed backends
        active_backend: Currently active backend name
    """

    def __init__(self):
        """Initialize backend manager with empty backend list."""
        self.backends: Dict[str, QuantumBackend] = {}
        self.active_backend: Optional[str] = None

        logger.info("Backend manager initialized")

    def add_backend(self, backend: QuantumBackend) -> None:
        """
        Add a backend to the manager.

        Args:
            backend: QuantumBackend instance to add

        Raises:
            ValueError: If backend with same name already exists
        """
        if backend.name in self.backends:
            raise ValueError("Backend %s already exists" % backend.name)

        self.backends[backend.name] = backend
        logger.info("Backend added: %s", backend.name)

    def remove_backend(self, name: str) -> None:
        """
        Remove a backend from the manager.

        Args:
            name: Name of backend to remove

        Raises:
            KeyError: If backend does not exist
        """
        if name not in self.backends:
            raise KeyError("Backend %s not found" % name)

        backend = self.backends[name]
        if backend.is_connected:
            backend.disconnect()

        del self.backends[name]

        if self.active_backend == name:
            self.active_backend = None

        logger.info("Backend removed: %s", name)

    def set_active_backend(self, name: str) -> None:
        """
        Set the active backend for operations.

        Args:
            name: Name of backend to set as active

        Raises:
            KeyError: If backend does not exist
        """
        if name not in self.backends:
            raise KeyError("Backend %s not found" % name)

        self.active_backend = name
        logger.info("Active backend set to: %s", name)

    def get_backend_info(self, name: str) -> Dict[str, Any]:
        """
        Get information about a specific backend.

        Args:
            name: Name of backend to query

        Returns:
            Dictionary containing backend information

        Raises:
            KeyError: If backend does not exist
        """
        if name not in self.backends:
            raise KeyError("Backend %s not found" % name)

        backend = self.backends[name]

        return {
            "name": backend.name,
            "type": backend.backend_type.value,
            "qubits": backend.available_qubits,
            "connected": backend.is_connected
        }

    def list_backends(self) -> List[str]:
        """
        List all managed backend names.

        Returns:
            List of backend names
        """
        return list(self.backends.keys())


def create_example_backends() -> BackendManager:
    """
    Create example backends for demonstration.

    Returns:
        BackendManager instance with example backends configured
    """
    manager = BackendManager()

    # Create simulator backend
    simulator = QuantumBackend(
        "local_simulator",
        BackendType.SIMULATOR,
        available_qubits=32
    )
    manager.add_backend(simulator)

    # Create cloud backend
    cloud = QuantumBackend(
        "cloud_backend",
        BackendType.CLOUD,
        available_qubits=127,
        config={"provider": "ibm"}
    )
    manager.add_backend(cloud)

    logger.info("Example backends created")

    return manager


def main() -> None:
    """
    Main entry point for backend manager demonstration.

    Demonstrates proper AINLP-compliant code with exception handling,
    logging, and documentation.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    try:
        # Create backend manager
        manager = create_example_backends()

        # Connect to simulator
        simulator = manager.backends["local_simulator"]
        simulator.connect(timeout=10)

        # Set as active
        manager.set_active_backend("local_simulator")

        # Get info
        info = manager.get_backend_info("local_simulator")
        logger.info("Backend info retrieved: %s", str(info))

        logger.info("Backend manager demonstration completed")

    except (ConnectionError, KeyError, ValueError) as exc:
        logger.error("Error in backend manager: %s", str(exc))
        raise


if __name__ == "__main__":
    main()
