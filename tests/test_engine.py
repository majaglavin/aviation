import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import day, year

from aviation import transforms
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_day",
            13_689_254.0 * passenger / day,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            22_815.0 * aircraft,
        ),
        (
            {
                "passengers_per_day": 13_689_254.0 * passenger / day,
                "seats_per_aircraft": 200.0 * passenger / aircraft,
                "flights_per_aircraft_per_day": 3.0 * journey / (aircraft * day),
            },
            "required_global_fleet",
            22_815.0 * aircraft,
        ),
    ),
)
def test_transform_evaluation(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: typing.Any,  # noqa: ANN401
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected, atol=1.0)
