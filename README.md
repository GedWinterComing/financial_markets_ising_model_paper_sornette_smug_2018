# 📈 2D-Dynamical Ising Model for Financial Crises

## Project Overview
This repository contains a Python implementation of the 2D-dynamical mean-field Ising model, inspired by the paper by Smug, Sornette, and Ashwin (2018): *"A Generalized 2D-Dynamical Mean-Field Ising Model with a Rich Set of Bifurcations (Inspired and Applied to Financial Crises)."*

The model translates the classical physical representation of spins into traders' opinion dynamics, capturing the interplay between instantaneous social imitation and past market trends.

## Model Features & Implementation
* **2D-Dynamical Map (`Isingmap.py`):** Implementation of the discrete-time 2D map to simulate the endogenized external field and traders' opinion evolution over time.
* **Lyapunov Exponents & Chaos (`Isinglyapunov.py`):** Procedural scripts developed to compute Lyapunov exponents and identify chaotic regimes and bifurcations.
* **Critical Analysis on Chaotic Regimes:** The simulation successfully replicates the core dynamics of the paper. However, as inherently expected in complex systems with a rich set of bifurcations, reproducing the exact visual phase space in highly chaotic parameter regimes (e.g., paper's Fig. 8b) highlights the extreme sensitivity to numerical precision and initial conditions.

## Tech Stack
* **Language:** Python.
* **Libraries:** NumPy, Matplotlib.
* **Methodology:** Complex Systems, Chaos Theory, Dynamical Systems (Bifurcations, Lyapunov Exponents).

## 📄 Theoretical Framework & Presentation
Included in this repository is the `presentation_ising_model_market_sornette_paper.pdf` slide deck. This document was created for a university exam and serves as a visual summary of the theoretical and mathematical foundations of the original Smug et al. (2018) paper. It provides the necessary context on the 2D-Ising model and its bifurcations prior to the Python implementation.
