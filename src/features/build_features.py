#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script builds features from the interim data, transforming them into a format
suitable for model training. It includes steps for feature engineering, scaling,
and other necessary data transformations.
"""

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """
    Runs feature engineering scripts to turn interim data (from ../interim)
    into features ready to be used by models (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('building features from interim data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
