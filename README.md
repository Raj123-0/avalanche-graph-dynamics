 # Avalanche Graph Dynamics

A Python simulation engine that models history-dependent state changes in dynamic complete graphs. 

This project explores the "Avalanche Effect" in discrete mathematics, where drawing a connection (a chord) between two nodes in a network not only alters their binary states but propagates the flip down all existing adjacent connections. 

## The Mathematics

This system behaves as a **dynamic state machine**. By representing the network's connections as an Adjacency Matrix and tracking state changes via Modulo 2 arithmetic (Galois Field of 2), the engine demonstrates that the final state of the network is **non-Abelian** (non-commutative). 

Building the exact same geometric network in a different chronological order results in completely different final node states. The state evolution is governed by:

`s_k ≡ s_{k-1} + (I + A_{k-1})v_k (mod 2)`

Where the network's state `s` depends entirely on the adjacency matrix `A` at the specific moment `k-1` before the new chord `v` is drawn.

## Getting Started

### Prerequisites
* Python 3.x

### Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/Raj123-0/avalanche-graph-dynamics.git](https://github.com/Raj123-0/avalanche-graph-dynamics.git)
cd avalanche-graph-dynamics


