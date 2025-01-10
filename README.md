# Three-Qubit Bit-Flip Code

## Introduction
The **Three-Qubit Bit-Flip Code** is one of the simplest error correction methods in quantum computing. It protects a logical qubit from single bit-flip errors caused by noise, ensuring reliable quantum computations.

---

## How Does It Work?

### 1. Encoding
To protect against errors, a single logical qubit (`|ψ⟩`) is encoded into three physical qubits by creating redundancy.

For a logical qubit:
- If the qubit state is `|0⟩`, it becomes `|000⟩` (all three qubits in `|0⟩` state).
- If the qubit state is `|1⟩`, it becomes `|111⟩` (all three qubits in `|1⟩` state).

This is written as:
\[ |0_L⟩ = |000⟩ \quad \text{and} \quad |1_L⟩ = |111⟩. \]

For a general state:
\[ |\psi⟩ = \alpha |0⟩ + \beta |1⟩, \]
it is encoded as:
\[ |\psi_L⟩ = \alpha |000⟩ + \beta |111⟩. \]

---

### 2. Transmission (With Possible Errors)
The encoded qubits are transmitted through a noisy quantum channel. During this process, one of the qubits might flip:
- For example, `|000⟩` might turn into `|010⟩` if the second qubit flips.

---

### 3. Error Detection
We perform **parity checks** to detect which qubit has flipped. Parity checks compare pairs of qubits to find discrepancies:
- Compare Q0 with Q1.
- Compare Q0 with Q2.

This creates an **error syndrome**:
- A specific pattern that tells us which qubit is corrupted.

---

### 4. Error Correction
Once the error is detected, we flip the erroneous qubit back to its correct state using a Pauli-X gate.

---

## The Math Behind the Code

### Encoding
To encode, we use **CNOT gates**:
1. Copy the state of the first qubit (control) to the second and third qubits (targets).

This is represented as:
\[ \text{CNOT}(|a⟩|b⟩) = |a⟩|a \oplus b⟩, \]
where \( \oplus \) denotes XOR.

### Introducing an Error
An error flips one qubit. For example:
\[ |000⟩ \xrightarrow{\text{Error on 2nd qubit}} |010⟩. \]

### Error Detection
We check parity:
1. Compare qubit 1 with qubit 2.
2. Compare qubit 1 with qubit 3.

Error syndromes indicate which qubit flipped:
- Syndrome `(1, 0)` means qubit 2 flipped.
- Syndrome `(0, 1)` means qubit 3 flipped.

### Error Correction
Based on the syndrome, we apply a Pauli-X gate (`X`) to correct the flipped qubit.

For example:
- If the second qubit flipped (`|010⟩`), apply `X` to qubit 2:
\[ X|010⟩ = |000⟩. \]

---

## Visualizing the Process

1. **Encoding**:
   - Logical `|0_L⟩`: `|000⟩`.
   - Logical `|1_L⟩`: `|111⟩`.

2. **Error Introduction**:
   - A noisy channel flips one qubit.

3. **Error Detection**:
   - Measure the syndromes to locate the flipped qubit.

4. **Error Correction**:
   - Flip the erroneous qubit back to its original state.

---

## Why It Works
The Three-Qubit Bit-Flip Code relies on redundancy. If one qubit flips, the other two "outvote" it during parity checks. This ensures the original state can be restored.

---

## Requirements

- Python 3.8+
- [Qiskit](https://qiskit.org/)

Install Qiskit using:
```bash
pip install qiskit
