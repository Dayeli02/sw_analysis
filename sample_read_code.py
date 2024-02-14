import pandas as pd
import matplotlib.pyplot as plt
"""
List of keys in the dataframe:
"sc_r_median": Median of the spacecraft radial distance from the sun in astronomical units.
"Tp_median": Median of the proton temperature in Kelvin.
"bm_median": Median of the magnetic field magnitude in nanoTesla.
"np_median": Median of the proton number density in numbers per per cubic centimeter.
"vp_m_median": Median of the proton velocity magnitude in kilometers per second.

"sc_r_iqr_10": 10th percentile of the spacecraft radial distance from the sun in astronomical units.
"Tp_iqr_10": 10th percentile of the proton temperature in Kelvin.
"bm_iqr_10": 10th percentile of the magnetic field magnitude in nanoTesla.
"np_iqr_10": 10th percentile of the proton number density in numbers per per cubic centimeter.
"vp_m_iqr_10": 10th percentile of the proton velocity magnitude in kilometers per second.

"sc_r_iqr_90": 90th percentile of the spacecraft radial distance from the sun in astronomical units.
"Tp_iqr_90": 90th percentile of the proton temperature in Kelvin.
"bm_iqr_90": 90th percentile of the magnetic field magnitude in nanoTesla.
"np_iqr_90": 90th percentile of the proton number density in numbers per per cubic centimeter.
"vp_m_iqr_90": 90th percentile of the proton velocity magnitude in kilometers per second.
"""

file_name = "all_spacecraft_data_binned_scaled_80_binned_v19_sample.p"

# Read the pickle file into a pandas dataframe.
df = pd.read_pickle(file_name)

# Print the first 5 rows of the dataframe.
print(df.head())

# Print the last 5 rows of the dataframe.
print(df.tail())

# Print the keys of the dataframe.
print(df.keys())

# Plot the median of the proton temperature as a function of the spacecraft radial distance from the
# sun.
plt.figure()
plt.errorbar(df["sc_r_median"], df["vp_m_median"], yerr=[df["vp_m_median"] - df["vp_m_iqr_10"], df["vp_m_iqr_90"] - df["vp_m_median"]], fmt='k.')
plt.plot(df["sc_r_median"], df["vp_m_median"], "k.")
plt.xlabel("Spacecraft radial distance from the sun (AU)")
plt.ylabel("Proton velocity magnitude (km/s)")
plt.title("Proton velocity magnitude vs spacecraft radial distance from the sun")
plt.xscale("log")
plt.yscale("log")
plt.show()
