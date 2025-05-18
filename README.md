# UtilitiesBestLagPredictor

This repository builds upon the `UtilForecast_LaggedOLS` model by selecting the best-performing lags for each macroeconomic predictor (CPI, 10-Year Treasury Yield, and Natural Gas Price) based on adjusted R² scores from an independent lag sweep analysis.


## Overview

The goal of this project is to build a refined regression model that uses the optimal lag for each independent variable in order to improve forecasting accuracy for utility stock returns (currently using Duke Energy - `DUK` as the representative stock).

This model may serve as a reference implementation for adaptive parameter-lag selection in macroeconomic forecasting applications.

## Features

- Loads and aligns macroeconomic data and utility stock returns
- Applies best-performing lags per variable (identified from previous lag sweep)
- Fits a multiple linear regression model using `statsmodels`
- Saves a detailed regression summary to file for reporting

## Requirements

```bash
pip install pandas numpy matplotlib seaborn statsmodels fredapi requests
```

## Setup

1. Clone this repository.
2. Create a `.env` file or securely inject your API keys into the environment:
   ```env
   FRED_API_KEY=your_fred_api_key
   POLYGON_API_KEY=your_polygon_api_key
   ```
3. Place your `macro_data_lagged.csv` and `stock_returns_lagged.csv` in the root directory (or let the script regenerate them).

## Running the Model

```bash
python main.py
```

The script will:
- Load data
- Apply best lags to each macroeconomic signal
- Merge and clean data
- Run the final OLS regression
- Output a formatted regression summary to `final_model_summary.txt`

## Output

- `final_model_summary.txt`: Contains coefficients, p-values, R², and diagnostics
- Optionally generate plots or export additional diagnostics in your own analysis

## Example Use Case

This project is ideal for researchers and practitioners interested in:
- Forecasting utilities under macroeconomic uncertainty
- Time series model tuning via lag structure optimization
- Building interpretable baseline models prior to more complex ML or ABM systems

## License

MIT License

## Citation

If you use this model in a publication or presentation, please cite:

**Baker, Peter C. (2025).** *Best-Lag Macroeconomic Forecasting Model for U.S. Utility Stocks*. GitHub Repository: [UtilitiesBestLagPredictor](https://github.com/pcbaker4669/UtilitiesBestLagPredictor)

---

For questions or contributions, feel free to open an issue or pull request.