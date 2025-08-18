# Data Science Portfolio

This repository serves as a comprehensive collection of data science projects, demonstrating a wide array of machine learning techniques, data analysis methodologies, and visualization skills. The projects cover various domains, from time series forecasting to natural language processing, showcasing practical applications of data science principles.

## Project Structure

The repository is organized into the following main directories:

-   `ML Micro Projects/`: This directory contains various smaller, focused machine learning projects.
    -   `data/`: Stores raw, interim, processed, and external datasets used across the micro-projects. This includes diverse datasets such as air quality, energy consumption, and sales data.
        -   `raw/`: Original, immutable data sources.
        -   `interim/`: Intermediate data products.
        -   `processed/`: Final, cleaned, and transformed data ready for modeling.
        -   `external/`: Data from external sources.
    -   `docs/`: Documentation related to the micro-projects.
    -   `models/`: Trained machine learning models from the micro-projects.
    -   `notebooks/`: Jupyter notebooks for exploratory data analysis, model development, and experimentation.
        -   `NamedEntityRecognition.ipynb`: A notebook dedicated to Named Entity Recognition tasks.
        -   `Time Series Analysis/`: A collection of notebooks focused on various time series analysis techniques, including:
            -   `ACF&PACF.ipynb`: Autocorrelation and Partial Autocorrelation functions for time series.
            -   `complete-guide-on-time-series-analysis-in-python.ipynb`: A comprehensive guide to time series analysis in Python.
            -   `Deep Learning TIme Series Forecasting using Gluon TS.ipynb`: Deep learning approaches for time series forecasting using Gluon TS.
            -   `MovingAverages.ipynb`: Implementation and analysis of moving averages.
            -   `Multivariate Time Series using LSTM.ipynb`: Multivariate time series forecasting using Long Short-Term Memory (LSTM) networks.
            -   `PythoTimeSeriesFunction.ipynb`: Custom Python functions for time series operations.
            -   `Time Series Auto ARIMA.ipynb`: Automated ARIMA modeling for time series forecasting.
            -   `TIme Series Functions for Sequencing.ipynb`: Functions specifically designed for sequencing in time series.
            -   `TIme Series using Prophet.ipynb`: Time series forecasting using Facebook's Prophet library.
            -   `Time_series_Pollution_data.ipynb`: Analysis of pollution data using time series methods.
            -   `TimeSeries Stationarity Test.ipynb`: Notebooks for testing stationarity in time series data.
            -   `TimeSeriesBirthPrediction.ipynb`: A project on predicting births using time series.
            -   `TimeSeriesDecompose.ipynb`: Decomposition of time series into trend, seasonality, and residuals.
    -   `references/`: Reference materials and external resources.
    -   `reports/`: Reports and presentations summarizing project findings.
-   `src/`: Source code for modular and reusable components.
    -   `data/`: Scripts for data ingestion and cleaning (`make_dataset.py`).
    -   `features/`: Scripts for feature engineering (`build_features.py`).
    -   `models/`: Scripts for training and predicting models (`train_model.py`, `predict_model.py`).
    -   `visualization/`: Scripts for generating visualizations (`vizualization.py`).
-   `requirements.txt`: Lists all Python dependencies required to run the projects.
-   `setup.py`: Setup file for packaging the project.
-   `test.ipynb`: A Jupyter notebook for testing purposes.
-   `tox.ini`: Configuration file for tox, a generic virtualenv management and test tool.
-   `Makefile`: Contains commands for common tasks like data processing, model training, and project setup.
-   `LICENCE`: The license under which the projects in this repository are distributed.

## Getting Started

To set up the environment and run the projects, please refer to the `requirements.txt` and `Makefile` for detailed instructions.
