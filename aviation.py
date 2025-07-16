# Simple model 

# Constants
days_per_year = 365.0
passengers_per_year = 5_000_000_000.0
flights_per_aircraft = 2.5
seats_per_aircraft = 180.0

passengers_per_day = passengers_per_year / days_per_year
required_global_fleet = passengers_per_day / (seats_per_aircraft * flights_per_aircraft)
print(f"{required_global_fleet =:.2f}")
