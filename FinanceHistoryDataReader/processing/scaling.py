from sklearn.preprocessing import StandardScaler

def standardize(data_frame, target_column):
    scaler = StandardScaler()
    data_frame[target_column] = scaler.fit_transform(data_frame[target_column].values.reshape(-1,1))
    