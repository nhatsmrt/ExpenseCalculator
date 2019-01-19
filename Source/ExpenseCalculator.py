import numpy as np
import pandas as pd

class ExpenseCalculator:
    def __init__(self, data_path):
        self._data_path = data_path

        try:
            self._expenses = pd.read_csv(data_path)
        except FileNotFoundError:
            self._expenses = pd.DataFrame(columns = ["amount", "time", "type"])

    def log(self, amount, time, type):
        self._expenses = self._expenses.append(
            {
                "amount": amount,
                "time": time,
                "type": type
            },
            ignore_index = True
        )

        with open(self._data_path, 'a') as f:
            new_df = pd.DataFrame([[amount, time, type]], columns = ["amount", "time", "type"])
            new_df.to_csv(f, index = False)


    def forecast(self, type, past_window = None, future_window = 1):
        past_expenses = self._expenses[self._expenses['type'] == type]
        return self.__simple_forecast(past_expenses, past_window, future_window)

    def __simple_forecast(self, past_expenses, past_window=None, future_window=1):
        if future_window < 1:
            raise ValueError

        if past_window is not None:
            if past_window > past_expenses.shape[0]:
                raise ValueError

        simulation = past_expenses

        for _ in range(future_window):
            if past_window is not None:
                prediction = np.mean(simulation[simulation.shape[0] - past_window: simulation.shape[0]])
            else:
                prediction = np.mean(simulation)
            simulation = np.append(simulation, np.array([prediction]))

        return simulation[simulation.shape[0] - future_window: simulation.shape[0]]
