import gspread
import pandas as pd

gc = gspread.service_account()

doc = gc.open_by_url("https://docs.google.com/spreadsheets/d/1tWA19YK1g2oSVWcXFv-H2XyfMcc677z4ukpwFCv-Ycg/edit?usp=sharing")

ws = doc.worksheet('Base')
df = pd.DataFrame(ws.get_all_records())

print(df.head())