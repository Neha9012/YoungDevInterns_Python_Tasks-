import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import stft
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split
import pandas as pd

# Simulated complex signal data (IoT signals)
t = np.linspace(0, 10, 1000)  # Time axis (example: 10 seconds of data)
freqs = [10, 20, 30]  # Example dominant frequencies in Hz
signal = np.sum([np.sin(2 * np.pi * f * t) for f in freqs], axis=0)

# Add noise to simulate realistic IoT signal
np.random.seed(42)
noise = np.random.normal(0, 0.1, signal.shape)
signal_noisy = signal + noise

# Perform Short-Time Fourier Transform (STFT)
f, t_stft, Zxx = stft(signal_noisy, fs=1.0/(t[1] - t[0]), nperseg=100, noverlap=75)
magnitude_stft = np.abs(Zxx)

# Feature extraction (example: use dominant frequency as feature)
dominant_freq = np.argmax(magnitude_stft, axis=0)

# Normalize features
scaler = StandardScaler()
dominant_freq_scaled = scaler.fit_transform(dominant_freq.reshape(-1, 1))

# Split data into train and test sets (simulated data, adjust for real data)
X_train, X_test, t_train, t_test = train_test_split(dominant_freq_scaled, t_stft, test_size=0.2, random_state=42)

# Machine learning model for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

# Predict anomalies on test set
anomaly_scores = model.decision_function(X_test)
anomalies = np.where(anomaly_scores < 0)[0]

# Root cause analysis using clustering (DBSCAN)
dbscan = DBSCAN(eps=0.3, min_samples=10)
clusters = dbscan.fit_predict(dominant_freq_scaled)

# Create a DataFrame for all data points
all_data_df = pd.DataFrame({
    'Time': t_stft,
    'Dominant Frequency': dominant_freq_scaled.flatten(),
    'Cluster': clusters,
    'Anomaly Score': np.concatenate([model.decision_function(dominant_freq_scaled[:len(t_train)]), anomaly_scores])
})

# Ensure we correctly map the test set indices to the DataFrame
test_indices = all_data_df.index.isin(t_train.shape[0] + np.arange(len(t_test)))

# Filter for anomalies only
anomaly_df = all_data_df[test_indices].iloc[anomalies]

# Visualizing clusters to identify root cause
plt.figure(figsize=(14, 10))

# Plot time-domain signal
plt.subplot(4, 1, 1)
plt.plot(t, signal_noisy, color='black')
plt.title('Complex IoT Signal: Time Domain with Noise')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot STFT spectrogram
plt.subplot(4, 1, 2)
plt.pcolormesh(t_stft, f, 20 * np.log10(magnitude_stft), shading='gouraud')
plt.title('STFT Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Magnitude (dB)')
plt.grid(True)

# Plot dominant frequency feature
plt.subplot(4, 1, 3)
plt.plot(t_stft, dominant_freq_scaled, color='blue')
plt.title('Dominant Frequency (Scaled)')
plt.xlabel('Time')
plt.ylabel('Scaled Value')
plt.grid(True)

# Plot anomalies and clusters
plt.subplot(4, 1, 4)
plt.scatter(t_stft, dominant_freq_scaled, c=clusters, cmap='viridis', label='Cluster')
plt.scatter(t_stft[anomalies], dominant_freq_scaled[anomalies], color='red', marker='o', label='Detected Anomaly')
plt.title('Anomaly Detection and Clustering')
plt.xlabel('Time')
plt.ylabel('Scaled Value')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Root cause analysis report (example)
print("Root Cause Analysis Report:")
print(anomaly_df)

# Example automated mitigation strategy
def mitigate_anomalies(anomaly_df):
    for idx, row in anomaly_df.iterrows():
        if row['Cluster'] == -1:
            print(f"Mitigation action: Reset device at time {row['Time']}")
        else:
            print(f"Mitigation action: Adjust operational parameters for cluster {row['Cluster']} at time {row['Time']}")

mitigate_anomalies(anomaly_df)
