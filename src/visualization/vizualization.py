#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script generates various visualizations from the processed data or model
outputs. It helps in understanding data distributions, model performance,
and insights derived from the analysis.
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
    Runs visualization scripts to create plots and charts from processed data.
    """
    logger = logging.getLogger(__name__)
    logger.info('creating visualizations')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
