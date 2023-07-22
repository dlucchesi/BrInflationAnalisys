import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Load data
inpc_data = pd.read_csv('base.csv', sep=';')

print(inpc_data.tail(10))
print("######################")
print(inpc_data.info())
print("######################")
print(inpc_data.describe())

# Convert date to datetime
# inpc_data['DATE'] = str(inpc_data['YEAR']) + '-' + str(inpc_data['MONTH'])
# inpc_data['DATE'] = inpc_data['YEAR'].astype(str) + '-' + inpc_data['MONTH'].astype(str)
# inpc_data['DATE2'] = pd.to_datetime(inpc_data['DATE'], format="%Y-%m")

