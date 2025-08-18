#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script trains machine learning models using the processed data and saves
the trained models to the `models` directory. It includes steps for model
selection, training, and evaluation.
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
    Trains machine learning models using the processed data (from ../processed)
    and saves them to the models directory.
    """
    logger = logging.getLogger(__name__)
    logger.info('training model')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
