from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np

class AirNormalizer: 
	
	def __init__(self, data, **kwargs):
		n_est = kwargs.get("n_estimators", 300)
		max_depth = kwargs.get("max_depth", 20)
		max_features = kwargs.get("max_features", 5)
		use_oob = kwargs.get("oob_score", True)
		random_state = kwargs.get("random_state", 123)

		self.data = data
		self.model = RandomForestRegressor(n_estimators=n_est, max_depth=max_depth, max_features=max_features, oob_score=use_oob, random_state=random_state)
		x = data.drop("inquinante", 1)
		y = data.inquinante
		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, train_size=.8, random_state=random_state)
		self.model.fit(self.x_train, self.y_train) 

	def get_model(self):
		return self.model

	def get_trainingset(self):
		return self.x_train

	def evaluate_training(self):
		y_pred_train = self.model.predict(self.x_train)
		mse = metrics.mean_squared_error(self.y_train, y_pred_train)
		return pd.Series({"MSE": mse, "RMSE": np.sqrt(mse), "OOB Score": self.model.oob_score_})

	def evaluate_testing(self):
		y_pred = self.model.predict(self.x_test)
		mse = metrics.mean_squared_error(self.y_test, y_pred)
		return pd.Series({"MSE": mse, "RMSE": np.sqrt(mse), "R2": self.model.score(self.x_test, self.y_test)})

	def feature_importance(self):
		return pd.DataFrame({"cols": self.x_train.columns, "imp": self.model.feature_importances_}).sort_values("imp", ascending=False)

	def normalize_timeseries(self, **kwargs):
		n_preds = kwargs.get("n_preds", 1000)
		verbose = kwargs.get("verbose", False)

		dfs = []
		for i in range(n_preds):
			if(verbose and i%10 == 0):
				print(f"Making prediction {i}")

			scrambled_rows = self.data.sample(frac=1).reset_index(drop=True)
			scrambled_rows.index = self.data.index
			scrambled_rows.epoch = self.data.epoch
			preds = pd.DataFrame(self.model.predict(scrambled_rows.drop("inquinante", 1)), columns=["inquinante"])
			preds.index = self.data.index
			dfs.append(preds)
		predictions = pd.concat(dfs)
		return predictions.groupby(predictions.index).mean()
		
