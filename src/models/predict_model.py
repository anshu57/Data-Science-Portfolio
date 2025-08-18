#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script uses a trained machine learning model to make predictions on new data.
It loads a pre-trained model and applies it to the input data, saving the predictions.
"""

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('model_filepath', type=click.Path(exists=True))
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(model_filepath, input_filepath, output_filepath):
    """
    Makes predictions using a trained model.
    """
    logger = logging.getLogger(__name__)
    logger.info('making predictions')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    project_dir = Path(__file__).resolve().parents[2]

    load_dotenv(find_dotenv())

    main()
