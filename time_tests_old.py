import pandas as pd
import time

def get_time(dsname, cols):
	start = time.time()
	data = pd.read_csv(dsname)
	data1 = data[cols]
	end = time.time()
	return end-start

print(get_time('green_tripdata_2017-01.csv',["RatecodeID","trip_distance"]))
print(get_time('yellow_tripdata_2017-01.csv',["RatecodeID","trip_distance"]))
print(get_time('yellow_tripdata_2017_all.csv',["RatecodeID","trip_distance"]))