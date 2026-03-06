# 📈 2D-Dynamical Ising Model for Financial Crises

## Project Overview
This repository contains a Python implementation of the 2D-dynamical mean-field Ising model, inspired by the paper by Smug, Sornette, and Ashwin (2018): *"A Generalized 2D-Dynamical Mean-Field Ising Model with a Rich Set of Bifurcations (Inspired and Applied to Financial Crises)."*

The model translates the classical physical representation of spins into traders' opinion dynamics, capturing the interplay between instantaneous social imitation and past market trends.
The model explores how traders' opinion can lead to financial crises, chaotic regimes, and critical transitions.

## Model Features & Implementation
* **2D-Dynamical Map (`Isingmap.py`):** Implementation of the discrete-time 2D map to simulate the endogenized external field and traders' opinion evolution over time.
* **Lyapunov Exponents & Chaos (`Isinglyapunov.py`):** Numerical scripts developed to compute the Lyapunov exponents, aiming to identify the boundaries of chaotic regimes and bifurcation points.
* **Critical Analysis on Chaotic Regimes:** The code successfully implements the core mathematical framework. The project also highlights the standard numerical challenges in exactly reproducing specific bifurcation phase spaces (e.g., the paper's Fig. 8b), often due to undocumented grid resolutions, transient discard times, or specific numerical setups in the original literature.

## Tech Stack
* **Language:** Python.
* **Libraries:** NumPy, Matplotlib.
* **Methodology:** Complex Systems, Chaos Theory, Dynamical Systems (Bifurcations, Lyapunov Exponents).

## 📄 Theoretical Framework & Presentation
Included in this repository is the `presentation_ising_model_market_sornette_paper.pdf` slide deck. This document was created for a university exam and serves as a visual summary of the theoretical and mathematical foundations of the original Smug et al. (2018) paper. It provides the necessary context on the 2D-Ising model and its bifurcations prior to the Python implementation.
