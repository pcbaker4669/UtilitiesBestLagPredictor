import pandas as pd
import statsmodels.api as sm

# === FILE LOCATIONS ===
MACRO_CSV = "macro_data_lagged.csv"
STOCK_CSV = "stock_returns_lagged.csv"

# === OPTIMAL LAGS FROM SWEEP ===
LAGS = {
    'cpi': 0,
    '10yr_yield': 2,
    'natgas': 0
}

# === LOAD DATA ===
macro_df = pd.read_csv(MACRO_CSV, index_col=0, parse_dates=True)
stock_df = pd.read_csv(STOCK_CSV, index_col=0, parse_dates=True)

# === APPLY LAGS ===
lagged_macro = pd.DataFrame(index=macro_df.index)
for var, lag in LAGS.items():
    lagged_macro[var] = macro_df[var].shift(lag)

# Compute delta_yield AFTER lag
lagged_macro['delta_yield'] = lagged_macro['10yr_yield'].diff()

# === MERGE AND CLEAN ===
merged_df = pd.concat([stock_df, lagged_macro], axis=1).dropna()

# === REGRESSION ===
X = merged_df[['delta_yield', 'cpi', 'natgas']]
X = sm.add_constant(X)
y = merged_df['weekly_return']

model = sm.OLS(y, X).fit()

# === OUTPUT ===
summary_file = "final_best_lag_model_summary.txt"
with open(summary_file, "w") as f:
    f.write(model.summary().as_text())

print(f"Model summary saved to {summary_file}")
