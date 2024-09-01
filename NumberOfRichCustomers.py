import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
  DF = store[(store['amount']> 500)]
  DF.drop_duplicates(subset = "customer_id", inplace= True)
  x = DF['customer_id'].nunique()

  return pd.DataFrame([{x}], columns=["rich_count"])