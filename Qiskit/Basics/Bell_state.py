#!/usr/bin/env python
# coding: utf-8

# In[1]:


# --- Essential Imports ---
# Import core Qiskit components
from qiskit import QuantumCircuit, transpile

# Import the Aer simulator from its dedicated package
from qiskit_aer import Aer

# Import visualization tools
from qiskit.visualization import plot_histogram

# Import matplotlib explicitly for displaying plots (especially if you use plt.show())
import matplotlib.pyplot as plt


# In[2]:


# --- Jupyter Magic Command ---
# This line tells Jupyter to display matplotlib plots inline in the notebook output
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# --- Circuit Definition ---
# Create a Quantum Circuit with 2 qubits and 2 classical bits
circuit = QuantumCircuit(2, 2)


# In[4]:


# --- Initial Circuit Drawing ---
# Draw the circuit BEFORE applying the CX gate
print("--- Initial Circuit (Before H and CX) ---")
circuit.draw(output='mpl', style={'backgroundcolor': '#ffffff'}) # 'mpl' requires matplotlib and pylatexenc
plt.show() # Display the plot


# In[5]:


# --- Apply CX (CNOT) Gate ---
# Apply a Controlled-NOT (CX) gate:
# It flips the target qubit (1) if the control qubit (0) is in the |1> state.
# By default, qubits start in |0>, so this CX won't change the state yet unless qubit 0 is put in superposition/1.
print("\n--- Applying H and CX Gate (control=0, target=1) ---")
circuit.h(0)
circuit.cx(0, 1)


# In[6]:


# --- Measure Qubits ---
# Measure both qubits (0 and 1) and store their results in classical bits (0 and 1 respectively)
print("--- Measuring Qubits (0 and 1) ---")
circuit.measure([0, 1], [0, 1])


# In[7]:


# --- Circuit Drawing After Operations and Measurement ---
# Draw the circuit AFTER all operations and measurement are applied
print("\n--- Circuit After CX and Measurement ---")
circuit.draw(output='mpl', style={'backgroundcolor': '#ffffff'})
plt.show() # Display the plot


# In[8]:


# --- Simulation ---
# Get the QASM simulator from Qiskit Aer
print("\n--- Simulating the Circuit ---")
simulator = Aer.get_backend('qasm_simulator')


# In[9]:


# Transpile the circuit for the chosen simulator backend
# This optimizes the circuit for the specific target device/simulator.
transpiled_circuit = transpile(circuit, simulator)


# In[10]:


# Run the transpiled circuit on the simulator
# The .run() method returns a Job object.
job = simulator.run(transpiled_circuit, shots=1024) # Run 1024 times to get statistics


# In[11]:


# Get the results from the completed job
# The .result() method blocks until the job is finished.
result = job.result()


# In[12]:


# --- Get Measurement Counts ---
# Retrieve the measurement outcomes (counts of '00', '01', '10', '11' etc.)
counts = result.get_counts(circuit)
print(f"Measurement outcomes: {counts}")


# In[13]:


# --- Visualize Results ---
# Plot a histogram of the measurement outcomes
print("\n--- Plotting Histogram of Results ---")
plot_histogram(counts)
plt.show() # Display the histogram


# In[ ]:




