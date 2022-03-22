import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func_log(x, a, b, c, d):
	temp = b*x + c
	return a * np.log(np.where(temp <= 0, 0.0001, temp)) + d


def func_gp(x, a, b, c, d):
	return (a * (1 - np.power(b, x)) / (1 - b)) - c


epochs = np.array([
	0.6175,
	0.6461,
	0.6828,
	0.7053,
	0.7063,
	0.7155,
	0.7068
])

n = epochs.shape[0]
up_to_epochs = 65
train_x = np.arange(n)
func = func_log

params, other = curve_fit(
	func,
	train_x,
	epochs,
	p0=[0, 0.5, 0.5, 1],
	bounds=(
		[-10000, -1, -10000, -10000],
		[10000, 1, 10000, 10000],
	)
)
pred_x = np.arange(up_to_epochs)
pred = func(pred_x, *params)

print(params)
plt.plot(train_x, epochs, 'bo', label='epochs')
plt.plot(pred_x, pred, '-', label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
