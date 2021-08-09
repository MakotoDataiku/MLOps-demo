# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
weather_filtered = dataiku.Dataset("weather_filtered")
weather_filtered_df = weather_filtered.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

s_df = weather_filtered_df # For this sample code, simply copy input to output


# Write recipe outputs
s = dataiku.Dataset("s")
s.write_with_schema(s_df)
