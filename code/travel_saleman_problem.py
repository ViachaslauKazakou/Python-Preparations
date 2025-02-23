from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit_aer import Aer
import numpy as np

def create_tsp_circuit(distances, n_cities):
    """
    Create quantum circuit for TSP

    Args:
        distances (np.array): Distance matrix between cities
        n_cities (int): Number of cities
    """
    n_qubits = n_cities ** 2
    circuit = QuantumCircuit(n_qubits, n_cities)
    
    # Create superposition
    for i in range(n_qubits):
        circuit.h(i)
    
    # Add problem constraints
    # This is a simplified version - real implementation would need more complex constraints
    for i in range(n_cities):
        for j in range(n_cities):
            if distances[i][j] > 0:
                circuit.cp(distances[i][j], i, j)
    
    # Add measurement to obtain counts
    circuit.measure(range(n_cities), range(n_cities))
    return circuit

def decode_route(bitstring, n_cities):
    """
    Decode a bitstring (of length n_cities**2) into a route.
    Each row in the n x n grid corresponds to a city.
    The column index of the '1' in that row indicates its tour order.
    
    For example, an outcome for 4 cities:
      "0001000100010001" (bits grouped as 4 bits) becomes:
      Row 0: 0001 -> position 3
      Row 1: 0001 -> position 3  (if duplicate or missing ones occur, handle accordingly)
    
    This simple decoder assumes each row has exactly one '1'. 
    If not, it returns None.
    """
    # Ensure the bitstring has length n_cities^2
    if len(bitstring) != n_cities ** 2:
        return None
    
    route = [None] * n_cities
    # Break up the bitstring into rows (we use little-endian order,
    # so reverse each group for clarity)
    for i in range(n_cities):
        row = bitstring[i*n_cities:(i+1)*n_cities]
        # Reverse so that bit0 is on the right if needed
        row = row[::-1]
        if row.count('1') != 1:
            return None
        pos = row.index('1')
        route[i] = pos
    return route

# Example usage
if __name__ == "__main__":
    # Example with 4 cities
    distances = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ])
    
    # Create and run circuit
    n_cities = 4
    circuit = create_tsp_circuit(distances, n_cities)
    
    # Run on simulator using the new workflow
    backend = Aer.get_backend('qasm_simulator')
    
    # Transpile and run the circuit directly
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    # Get best route
    best_route = max(counts.items(), key=lambda x: x[1])[0]
    print(f"Best route found: {best_route}")
    
    # Decode the best outcome into a route order (each row gives the tour order for that city).
    route = decode_route(best_route, n_cities)
    if route is not None:
        # For clarity, we map numeric indices to city labels (City 0, City 1, etc.)
        city_order = [f"City {i}" for i in route]
        print("Decoded city order:", city_order)
    else:
        print("Ambiguous outcome; could not decode a valid route.")