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
passengers\ per\ day = \frac{passengers\ per\ year}{days\ per\ year}
$

$
required\ global\ fleet = \frac{passengers\ per\ day}{seats\ per\ aircraft\ \times\ flights\ per\ aircraft\ per\ day}
$
