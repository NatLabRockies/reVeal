# -*- coding: utf-8 -*-
"""
grid module tests
"""
import pytest
import geopandas as gpd

from loci.grid import create_grid


@pytest.mark.parametrize(
    "bounds,res,crs,i",
    [
        (
            [71281.01960453, 743256.58450656, 117361.01960453, 789336.58450656],
            11520,
            "EPSG:5070",
            2,
        ),
        ([-124.70999145, 24.3696785, -64.70999145, 49.3696785], 5, "EPSG:4326", 3),
    ],
)
def test_create_grid(data_dir, bounds, res, crs, i):
    """
    Unit test for create_grid().
    """

    grid_df = create_grid(res, *bounds, crs)
    expected_src = data_dir / "characterize" / "grids" / f"grid_{i}.gpkg"
    expected_df = gpd.read_file(expected_src)

    assert len(grid_df) == len(
        expected_df
    ), "Output grid does not have expected number of rows"

    grid_df["geometry"] = grid_df["geometry"].normalize()
    expected_df["geometry"] = expected_df["geometry"].normalize()
    grid_df.sort_values(by="geometry", inplace=True)
    grid_df.reset_index(drop=True, inplace=True)
    expected_df.sort_values(by="geometry", inplace=True)
    expected_df.reset_index(drop=True, inplace=True)

    equal_geoms = grid_df["geometry"].geom_equals_exact(
        expected_df["geometry"], tolerance=0.1
    )
    assert equal_geoms.all(), "Geometries do not match expected outputs"


if __name__ == "__main__":
    pytest.main([__file__, "-s"])
