# coin-flip-monte-carlo

A small NumPy and Matplotlib project that simulates multiple coin-flip random walks and plots their cumulative paths.

## What it does

- Generates fair coin flips encoded as `-1` and `+1`
- Builds multiple random-walk trajectories with `np.cumsum(..., axis=1)`
- Plots all simulated paths on the same graph
- Saves the figure as `average_evolution.png`

## Why this project

This project was a way to strengthen NumPy skills through hands-on practice with arrays, shapes, axes, vectorized operations, and cumulative sums. It was also a simple way to build quantitative intuition, since random walks are a basic building block for Monte Carlo simulation and more advanced quant models.

It also reflects practical Python skills: writing clean functions, running simulations efficiently with NumPy, and visualizing results with Matplotlib.

## Main ideas used

- `rng.integers(...)` to generate random values
- `* 2 - 1` to map `{0, 1}` to `{-1, +1}`
- `np.cumsum(..., axis=1)` for row-wise cumulative sums
- `plt.plot(...)` in a loop to draw multiple lines on one figure
- `plt.savefig(...)` to save the chart

## Run

```python
plot(100, 30)
```

This runs 30 simulated random walks of 100 tosses each and displays the result.