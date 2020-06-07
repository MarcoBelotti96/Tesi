#! /usr/bin/env python3
import pandas as pd

def normalize_timeseries(model, data, **kwargs):
	n_preds = kwargs.get("n_preds", 1000)
	verbose = kwargs.get("verbose", False)

	dfs = []
	for i in range(n_preds):
		if(verbose and i%10 == 0):
			print(f"Making prediction {i}")

		scrambled_rows = data.sample(frac=1).reset_index(drop=True)
		scrambled_rows.index = data.index
		scrambled_rows.epoch = data.epoch
		preds = pd.DataFrame(model.predict(scrambled_rows.drop("inquinante", 1)), columns=["inquinante"])
		preds.index = data.index
		dfs.append(preds)
	predictions = pd.concat(dfs)
	return predictions.groupby(predictions.index).mean()
