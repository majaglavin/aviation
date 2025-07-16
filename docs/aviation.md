# Aviation

### Constants 

| True Constant | Value |Unit | 
| ---- | ---- | --| 
| Days per year | 365 | day year^-1^ | 

| Inputs | Value | Unit |Source |
| ------ | ---- | ------ | --|
| Passengers per year | $5\times 10^9$ | year^-1^ | ATAG[@atagFactsFigures]|
| Flights per aircraft per day| 2 | day^-1^| - |
| Seats per aircraft| 150 | - | - |


### Equations

$$
\begin{equation}
\text{passengers per day} = \frac{\text{passengers per year}}{\text{days per year}}
\label{equation: passengers-per-day}
\end{equation}
$$

The total required global fleet can then be calculated as a function of this intermediate value and the other inputs, as done in equation $\ref{equation: required-global-fleet}$.

$$
\begin{equation}
\text{required global fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft}\ \times\ \text{flights per aircraft per day}}
\label{equation: required-global-fleet}
\end{equation}
$$

[ATAG]: [@atagFactsFigures]