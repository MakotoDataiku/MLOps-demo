# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
weather_historical_copy = dataiku.Dataset("weather_historical_copy")
df = weather_historical_copy.get_dataframe()

df = df[df['Tmax'] > 70]

# Write recipe outputs
tMax_filtered = dataiku.Dataset("tMax_filtered")
tMax_filtered.write_with_schema(df)
