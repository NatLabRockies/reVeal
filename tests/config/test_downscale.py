# -*- coding: utf-8 -*-
"""
config.characdownscale module tests
"""
import pytest
import geopandas as gpd

from reVeal.config.downscale import BaseDownscaleConfig


@pytest.mark.parametrize(
    "baseline_year",
    [2020, 2023],
)
@pytest.mark.parametrize(
    "projection_resolution", ["regional", "total", "REGIONAL", "TOTAL"]
)
def test_basedownscaleconfig_valid_inputs(
    data_dir, baseline_year, projection_resolution
):
    """
    Test that BaseDownsaleConfig can be instantiated with valid inputs.
    """

    grid = data_dir / "downscale" / "inputs" / "grid_char_weighted_scores.gpkg"
    load_projections = (
        data_dir
        / "downscale"
        / "inputs"
        / "load_growth_projections"
        / "eer_us-adp-2024-central_national.csv"
    )
    config = {
        "grid": grid,
        "grid_priority": "suitability_score",
        "grid_baseline_load": "dc_capacity_mw_existing",
        "baseline_year": baseline_year,
        "load_projections": load_projections,
        "projection_resolution": projection_resolution,
        "load_value": "dc_load_gw",
        "load_year": "year",
    }

    BaseDownscaleConfig(**config)


@pytest.mark.parametrize(
    "update_parameters",
    [{"grid_priority": "best_site_score"}, {"grid_baseline_load": "existing_mw"}],
)
def test_basedownscaleconfig_missing_attribute(data_dir, update_parameters):
    """
    Test that BaseDownscaleConfig raises a ValueError when a non-existent column is
    specified for either the grid_priority or grid_baseline_load columns.
    """

    grid = data_dir / "downscale" / "inputs" / "grid_char_weighted_scores.gpkg"
    load_projections = (
        data_dir
        / "downscale"
        / "inputs"
        / "load_growth_projections"
        / "eer_us-adp-2024-central_national.csv"
    )
    config = {
        "grid": grid,
        "grid_priority": "suitability_score",
        "grid_baseline_load": "dc_capacity_mw_existing",
        "baseline_year": 2022,
        "load_projections": load_projections,
        "projection_resolution": "total",
        "load_value": "dc_load_gw",
        "load_year": "year",
    }
    config.update(update_parameters)

    with pytest.raises(ValueError, match="Specified attribute .* does not exist"):
        BaseDownscaleConfig(**config)


@pytest.mark.parametrize("test_col", ["suitability_score", "dc_capacity_mw_existing"])
def test_basedownscaleconfig_nonnumeric_attribute(data_dir, tmp_path, test_col):
    """
    Test that BaseDownscaleConfig raises a ValueError when a non-numeric column is
    specified for either the grid_priority or grid_baseline_load columns.
    """

    src_grid = data_dir / "downscale" / "inputs" / "grid_char_weighted_scores.gpkg"
    grid_df = gpd.read_file(src_grid)
    grid_df[test_col] = grid_df[test_col].astype(str)
    grid = tmp_path / "grid.gpkg"
    grid_df.to_file(grid)

    load_projections = (
        data_dir
        / "downscale"
        / "inputs"
        / "load_growth_projections"
        / "eer_us-adp-2024-central_national.csv"
    )
    config = {
        "grid": grid,
        "grid_priority": "suitability_score",
        "grid_baseline_load": "dc_capacity_mw_existing",
        "baseline_year": 2022,
        "load_projections": load_projections,
        "projection_resolution": "total",
        "load_value": "dc_load_gw",
        "load_year": "year",
    }

    with pytest.raises(ValueError, match="Specified grid attribute .* must be numeric"):
        BaseDownscaleConfig(**config)


# add tests for validate_load_growth validation errors:
# bad CSV format
# bad file format
# missing columns
# non-numeric columns
# invalid baseline year

# for grid dataset:
# TODO: check that the grid_priority and grid_load columns exist and are
# numeric

if __name__ == "__main__":
    pytest.main([__file__, "-s", "-k", "test_basedownscaleconfig_nonnumeric_attribute"])
