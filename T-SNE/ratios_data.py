
from turtle import st
from sklearn.metrics import mean_squared_error
from tsne import gen_disk, bound_point, cal_radius_neigh
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

result_txt = "tsne_K_vs_R.txt"
diff_n = [500, 1000, 2000, 3000, 4000, 5000, 8000, 10000, 15000, 20000]
diff_k = [5, 7, 10, 22, 52, 61, 70, 82, 100]
diff_n = list(range(2000, 20000, 100))
diff_k = list(range(5, 200, 3))

X = np.zeros(len(diff_k) * len(diff_n)).reshape(-1, 1)
y_rad = np.zeros(len(diff_k) * len(diff_n)).reshape(-1, 1)
y_rad2 = np.zeros(len(diff_k) * len(diff_n))
with open(result_txt, "w") as f:
    for n in range(len(diff_n)):
        for k in range(len(diff_k)):
            disk = gen_disk(diff_n[n], d1=2, d2=5)
            bound_points = bound_point(disk, 20)
            #bound_points = [[1,0], [0,1], [0.5, np.sqrt(3)/2], [0.5, -np.sqrt(3)/2], [-0.5, -np.sqrt(3)/2], [-0.5, np.sqrt(3)/2]]
            neigh_rad = cal_radius_neigh(bound_points, disk, diff_k[k])
            X[n*len(diff_k)+k] = diff_k[k]
            y_rad[n*len(diff_k)+k] = neigh_rad
            f.write(f"n={diff_n[n]}, k={diff_k[k]}, neigh_rad={neigh_rad}, ratio_area={neigh_rad**2}")
            f.write("\n")

'''
X_train, X_test, y_train, y_test = train_test_split(X.reshape(-1, 1), y_rad.reshape(-1, 1), random_state=1, shuffle=True)
reg = LinearRegression(fit_intercept=True, positive=True).fit(X_train, y_train)

coeff = reg.coef_[0][0]
intercept = reg.intercept_[0]
print(coeff)
print(intercept)
print(mean_squared_error(reg.predict(X_test), y_test))
print(reg.score(X, y_rad))
print()

print(mean_squared_error(X_test, (y_test-intercept)/coeff))
print(X_test)
print(y_test/coeff)
'''