# -*- coding: utf-8 -*-
"""loci command line interface"""
import click

from loci import __version__


@click.group()
@click.version_option(version=__version__)
@click.pass_context
def main(ctx):
    """loci command line interface."""
    ctx.ensure_object(dict)
