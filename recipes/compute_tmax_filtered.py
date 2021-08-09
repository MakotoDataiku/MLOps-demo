# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
weather_historical_copy = dataiku.Dataset("weather_historical_copy")
weather_historical_copy_df = weather_historical_copy.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

tmax_filtered_df = weather_historical_copy_df # For this sample code, simply copy input to output


# Write recipe outputs
tmax_filtered = dataiku.Dataset("tmax_filtered")
tmax_filtered.write_with_schema(tmax_filtered_df)
