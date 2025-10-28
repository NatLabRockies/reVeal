# -*- coding: utf-8 -*-
"""
load module
"""


def apportion_load_to_regions(load_df, region_weights):
    return load_df


def downscale_regional(
    grid_df,
    grid_priority_col,
    grid_baseline_load_col,
    baseline_year,
    grid_region_col,
    load_df,
    load_value_col,
    load_year_col,
    load_region_col,
):
    # TODO: drop grids with unknown regions
    # TODO: rename columns for consistency across the input datasets

    return grid_df


def downscale_total(
    grid_df,
    grid_priority_col,
    grid_baseline_load_col,
    baseline_year,
    load_df,
    load_value_col,
    load_year_col,
):
    # TODO: rename columns for consistency across the input datasets

    return grid_df
