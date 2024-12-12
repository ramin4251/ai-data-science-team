def data_cleaner(data_raw):
    import pandas as pd
    import numpy as np
    from sklearn.impute import SimpleImputer

    # Step 1: Remove columns with more than 40% missing values
    threshold = 0.4 * len(data_raw)
    data_cleaned = data_raw.dropna(thresh=len(data_raw) - threshold, axis=1)

    # Step 2: Impute missing values
    for column in data_cleaned.columns:
        if data_cleaned[column].dtype in [np.int64, np.float64]:  # Numeric columns
            imputer = SimpleImputer(strategy='mean')
            data_cleaned[column] = imputer.fit_transform(data_cleaned[[column]]).ravel()
        elif data_cleaned[column].dtype == object:  # Categorical columns
            imputer = SimpleImputer(strategy='most_frequent')
            data_cleaned[column] = imputer.fit_transform(data_cleaned[[column]]).ravel()

    # Step 3: Convert columns to correct data types
    data_cleaned['TotalCharges'] = pd.to_numeric(data_cleaned['TotalCharges'], errors='coerce')

    # Step 4: Remove duplicate rows
    data_cleaned = data_cleaned.drop_duplicates()

    # Step 5: Remove rows with missing values
    data_cleaned = data_cleaned.dropna()

    # Note: Outlier removal is not performed as per user instruction

    return data_cleaned