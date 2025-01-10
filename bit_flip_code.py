from qiskit import QuantumCircuit, Aer, execute

# Create a 3-qubit circuit
qc = QuantumCircuit(3, 3)

# Step 1: Encoding the logical qubit into three physical qubits
qc.cx(0, 1)  # Copy qubit 0 to qubit 1
qc.cx(0, 2)  # Copy qubit 0 to qubit 2
qc.barrier()

# Step 2: Introducing a bit-flip error on the second qubit
qc.x(1)  # Simulates a bit-flip error
qc.barrier()

# Step 3: Error Detection using parity checks
qc.cx(0, 1)
qc.cx(0, 2)
qc.measure([1, 2], [1, 2])  # Measure error syndromes

# Step 4: Error Correction based on syndromes
qc.x(1)  # Correct the error on qubit 1
qc.measure([0], [0])  # Measure the final logical qubit

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts()
print(counts)
