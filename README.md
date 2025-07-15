# Aviation

Simple model of global aviation.

## Documentation 

### Constants 

| True Constant | Value |Unit | 
| ---- | ---- | --| 
| Days per year | 365 | $day \cdot year^{-1}$ | 

| Inputs | Value | Unit |Source |
| ------ | ---- | ------ | --|
| Passengers per year | $5\times 10^9$ | $year^{-1}$ | -|
| Flights per aircraft per day| 2 | $day^{-1}$| - |
| Seats per aircraft| 150 | - | - |


### Equations

$
\text{passengers per day} = \frac{\text{passengers per year}}{\text{days per year}}
$

$
\text{required global fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft}\ \times\ \text{flights per aircraft per day}}
$
