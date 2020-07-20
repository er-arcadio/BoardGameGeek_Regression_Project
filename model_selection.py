"""
This module contains functions that assist in the Linear Regression Analysis
 process. Both functions "train_test" and "cross_val" give the option of
 including polynomial features and/or inserting a unique model (ex.
 Ridge(), Lasso(), etc.). The 3rd function, "analysis_plot", uses seaborn
 to print out 3 graphs for linear assumptions.
"""

import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm


def train_test(X, y, X_test, y_test, model=LinearRegression(), poly=0,
               scale=False, dummy_idx=None):
    """
    Prints the r^2 of test set.

    This function does a linear regression fit on X & y and returns the
    r^2 score done on the X_test and y_test parameters.

    Parameters
    ----------
    :param X: pandas DataFrame
        The X matrix used to train the model.
    :param y: pandas Series
        The y vector used to train the model.
    :param X_test: pandas DataFrame
        The X matrix (typically hold out set) to test on.
    :param y_test: pandas Series
        The y vector (typically hold out set) to test on.
    :param model: sklearn.(linear_model|pipeline) type
        The model used to train the training set, X and y.
        If *None*, defaults to: LinearRegression()
    :param poly: int
        Degree in which to add polynomial features.
        If *None*, defaults to: 0 - no polynomial features will be added.
    :param scale: bool
        If *True*, performs standard scaler on variables before regression.
        If *None*, defaults to: False - no scaling will occur
    :param dummy_idx: int
        The index at where your dummy values start. Note: dummy values
        shouldn't be standardized nor made into polynomial features.
        If *None*, defaults to: None

    Return
    -------
    :return: N/A
        Prints the r^2 fit on the test set.
    """

    # Turning data into np arrays
    X, y = np.array(X), np.array(y)
    X_test, y_test = np.array(X_test), np.array(y_test)

    # Method adds polynomial features and/or scaling if required
    X, X_test = split_poly_scale_join([X, X_test], dummy_idx, poly, scale)

    # Fitting on the training set and printing the scored test set
    model.fit(X, y)
    print(f'R^2: {np.mean(model.score(X_test, y_test)):.2f}')
    # Only include coefficients if there was no polynomial features
    if not poly:
        print('\nCoefficients: ', model.coef_)
    return model


def cross_val(X, y, model=LinearRegression(), name='Linear',
              splits=10, poly=0, scale=True, dummy_idx=None):
    """
    Prints cross validation summary and returns predictions as list.

    This function takes in a training set and performs kFold cross validation
    of (default) 10 folds.  It then prints the individual validation r^2s, the mean
    training set's r^2, the mean validation set's r^2, and the average beta
    coefficients between the folds (if no polynomial features are included).

    Parameters
    ----------
    :param X: pandas DataFrame
        The X matrix used to train the model.
    :param y: pandas Series
        The y vector used to train the model.
    :param model: sklearn.(linear_model|pipeline) type
        The model used to train the training set, X and y.
        If *None*, defaults to: LinearRegression()
    :param name: string
        The name of the model used. This will be printed out as part of
        the results. (ex. 'Ridge', 'Lasso', 'Polynomial/Lasso', or custom)
        If *None*, defaults to: 'Linear'
    :param splits: int
        Number of folds to cross validate over.
    :param poly: int
        Degree in which to add polynomial features.
        If *None*, defaults to: 0 - no polynomial features will be added.
    :param scale: bool
        If *False*, no scaling will occur (not recommended).
        If *None*, defaults to: True - features will be StandardScaled
    :param dummy_idx: int
        The index at where your dummy values start (inclusive). Note:
        dummy values should neither be standardized nor made into polynomial
        features.
        If *None*, defaults to: None

    Return
    ------
    :return: NA
        Prints report. See description above
    """

    # List created to calculate mean Beta coefficients
    model_coefs = np.array([0]*len(X.columns))

    # Changing pandas objects to arrays for efficiency
    X, y = np.array(X), np.array(y)

    # Setting the K folds object
    kf = KFold(n_splits=splits, shuffle=True, random_state=71)

    train_r2s = []  # holds the training set's r^2s
    val_r2s = []  # holds the validation set's r^2s

    # performing train and validation on each split
    for train_idx, val_idx in kf.split(X, y):
        X_train, y_train = X[train_idx], y[train_idx]
        X_val, y_val = X[val_idx], y[val_idx]

        # method adds polynomial features and scales if needed
        X_train, X_val = split_poly_scale_join([X_train, X_val], dummy_idx,
                                               poly, scale)

        # Fitting the model and appending the r^2s
        model.fit(X_train, y_train)
        train_r2s.append(model.score(X_train, y_train))
        val_r2s.append(model.score(X_val, y_val))

        # Attempting to add the beta coefficients
        try:
            model_coefs = np.add(model_coefs, model.coef_)
        except:
            model_coefs = None

    # attempting to divide each coefficient by n (calculate mean)
    try:
        mean_coefs = model_coefs / len(y)
    except TypeError:
        mean_coefs = None

    # Displaying results
    print_results(name, train_r2s, val_r2s, mean_coefs, poly)

    # Returning predictions as a list
    return get_predicts(X.copy(), model, poly, scale, dummy_idx)


def analysis_plot(predictions, ys):
    """
    Prints 3 plots for linear assumptions analysis

    This function takes in a list of predicted y_hats and a list of the
    corresponding actual y values and uses seaborn to print out 3 graphs:
    a predicted vs actual plot, a residuals plot, and a QQPlot.

    Parameters
    ----------
    :param predictions: list, np.array type
        A list of predicted (y-hat) values. (to be compared with actuals)
    :param ys: list, np.array type
        A list of actual y values (to be compared with predicteds)

    Return
    ------
    :return: N/A
        Prints 3 graphs. See description above.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))

    residuals = ys - predictions

    # Plot 1 - Predicted vs Actual
    sns.scatterplot(predictions, ys, ax=ax1)
    ax1.set_title('Predicted vs Actual', fontsize=20)
    ax1.set(xlabel='Predicted Ys', ylabel='Actual Ys')

    # Plot 2 - Residuals PLot (predicted vs residuals)
    sns.scatterplot(predictions, residuals, ax=ax2)
    ax2.set_title('Residuals Plot', fontsize=20)
    ax2.set(xlabel='Predicted Ys', ylabel='Residuals')

    # Plot 3 - QQ Plot
    sm.qqplot(residuals, ax=ax3, line='s')
    ax3.set_title('QQ Plot- Distribution of Residuals', fontsize=20)

    plt.show();


'''

The following functions are for internal use only
'''


def print_results(name, train_r2, val_r2, coeffs, poly):
    """
    Prints report of a cross validation.

    This method takes in a list of the r^2s and the coefficients and prints
    a neat report of the results of a cross validation.

    :param name: string
        The name of the model used in the regression.
    :param train_r2: list
        A list of the training set's r^2s of each fold
    :param val_r2: list
        A list of the validation set's r^2s of each fold
    :param coeffs: numpy array type
        A list of the mean beta coefficients.
    :param poly: int
        The degree in which a polynomial regression was performed
        If 0, printed results won't include this information.

    :return: NA
        Prints report.
    """
    if poly:
        print(f"With Polynomial Features: degree = {poly}...\n")
    print(f'{name} Regression Scores: ', val_r2, '\n')

    print(f'{name}.R. Train - Mean R^2: {np.mean(train_r2):.3f} +- {np.std(train_r2):.3f}')
    print(f'{name}.R. Val - Mean R^2: {np.mean(val_r2):.3f} +- {np.std(val_r2):.3f}')

    print('\nCoefficients: ', coeffs)
    print('\n\n')


def get_predicts(x_matrix, model, poly, scale, dummy_idx):
    """
    Returns predictions made by a given model.

    This function takes in an X_matrix and uses the imported model to return
    the predicted (y-hat) values as a list.

    :param x_matrix: pd.DataFrame
        The matrix containing all the attributes needed to make predictions
    :param model: sklearn.linear_model type
        The prefitted model used to make predictions
    :param poly: int
        The degree in which a polynomial regression was performed
        If 0, printed results won't include this information.
    :param scale: bool
        If *False*, no scaling will occur.
        If *True*, features will be StandardScaled.
    :param dummy_idx: int
        The index at which dummy values start (inclusive).
    :return: list
        Returns a list of the predicted (y-hat) values
    """
    x_matrix = np.array(x_matrix)

    # adding polynomial features and/or scaling before prediction
    temp_list = split_poly_scale_join([x_matrix], dummy_idx, poly, scale)
    x_matrix = temp_list[0]

    return model.predict(x_matrix)


def split_poly_scale_join(matrices, dummy_idx, poly, scale):
    """
    Excludes dummy columns to add polynomial features and/or scale attributes.

    This function iterates over list of matrices and puts aside their dummy
    attributes in order to add polynomial features and scale the numerical
    values. Then, it combines the attributes and returns the resulting
    matrices.

    :param matrices: list
        The list of matrices in which to iterate over.
    :param dummy_idx: int
        The index at which dummy values start (inclusive).
    :param poly: int
        The degree in which a polynomial features will be added
        If 0, no polynomial features will be added.
    :param scale: bool
        If *False*, no scaling will occur.
        If *True*, features will be StandardScaled.

    :return: list
        A list of equal length will be returned. It will include the same
        corresponding matri(x|ces) with any appropriately added and/or
        scaled features.
    """

    adjusted_matrices = []

    for matrix in matrices:
        if dummy_idx:
            # Split the matrix into numerical and dummies
            matrix, matrix_dummies = np.split(matrix, [dummy_idx], axis=1)

        # add polynomial features to numerical attributes
        if poly:
            matrix = (PolynomialFeatures(poly).
                            fit_transform(matrix))
        # scale numerical attributes
        if scale:
            matrix = (StandardScaler().
                            fit_transform(matrix))
        if dummy_idx:
            # Join numerical and dummy attributes together again
            matrix = np.concatenate((matrix, matrix_dummies), axis=1)
        adjusted_matrices.append(matrix)

    return adjusted_matrices
