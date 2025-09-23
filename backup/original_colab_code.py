import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# CONJUNTO 1 - ORGANIZADO Latitude  3.9823   Longitude -68.9135
# =============================================================================
datos_1 = {
    1984: [5.0186, 4.8653, 5.3378, 4.7894, 4.4453, 4.3661, 4.2665, 4.896, 5.346, 4.7957, 4.6822, 4.6274],
    1985: [5.3568, 5.2762, 5.0508, 4.7688, 4.5922, 4.7261, 4.638, 5.13, 5.4953, 5.1271, 5.0086, 5.0318],
    1986: [4.9051, 4.812, 5.095, 4.6255, 4.44, 4.6234, 4.8254, 5.1302, 5.2181, 4.651, 4.4258, 4.5281],
    1987: [4.872, 5.1564, 5.3054, 4.9925, 4.4981, 4.1772, 4.4098, 4.6507, 5.2488, 5.0465, 4.8595, 4.6231],
    1988: [4.9406, 5.5879, 5.664, 4.59, 4.223, 4.4902, 3.767, 4.6841, 4.5334, 4.8782, 4.4894, 4.8588],
    1989: [4.7779, 4.8583, 4.8053, 4.5598, 4.3361, 4.4338, 4.2319, 4.9006, 4.6406, 4.6483, 4.6265, 5.0599],
    1990: [4.2422, 4.9793, 4.3481, 4.5038, 4.0457, 4.23, 4.1074, 4.9118, 4.843, 4.9361, 4.5041, 4.4122],
    1991: [5.22, 5.1475, 5.0578, 4.686, 4.2194, 4.1798, 4.5082, 4.194, 4.758, 5.0054, 4.7287, 4.9949],
    1992: [5.2399, 5.2469, 5.0306, 4.817, 4.8151, 4.4206, 4.0903, 4.7998, 4.9498, 4.7813, 4.1657, 4.5682],
    1993: [4.7431, 4.8161, 4.4251, 4.5931, 4.6162, 4.1707, 4.7162, 4.7035, 4.6342, 4.3507, 4.5955, 4.98],
    1994: [5.1852, 4.9622, 4.6879, 4.6853, 4.3582, 4.0762, 4.4971, 4.6745, 4.4892, 5.0285, 4.5122, 4.9001],
    1995: [5.2006, 5.1391, 4.925, 4.3476, 4.3829, 4.0478, 4.6346, 4.777, 4.8506, 4.8504, 4.5418, 4.6625],
    1996: [4.9817, 4.5857, 4.9505, 4.9238, 4.3334, 3.8246, 4.307, 4.7362, 4.7791, 4.5754, 4.3759, 4.5598],
    1997: [5.1324, 4.2737, 5.8339, 4.6908, 4.0236, 4.5, 4.596, 4.8173, 5.0506, 4.9601, 4.6644, 5.1223],
    1998: [5.5546, 5.0983, 4.735, 4.511, 4.1746, 4.181, 4.3858, 4.7076, 5.0688, 4.903, 4.5643, 4.8454],
    1999: [4.4258, 4.5938, 5.2507, 4.3771, 4.6238, 4.0934, 4.4326, 4.1556, 4.8809, 4.9843, 4.8629, 4.9586],
    2000: [5.3112, 5.4118, 5.0834, 4.2307, 4.3061, 4.0733, 4.0265, 4.7057, 4.7357, 4.4467, 4.747, 4.5886],
    2001: [5.4048, 5.2382, 4.7986, 4.5194, 4.4482, 4.2317, 4.3426, 4.3956, 5.1746, 5.0782, 4.6313, 4.1177],
    2002: [5.2886, 5.1257, 4.7539, 4.542, 4.0975, 4.2278, 4.302, 4.3306, 5.1055, 4.8317, 4.8622, 4.806],
    2003: [5.5886, 4.8624, 4.4299, 4.4822, 3.7805, 4.0865, 3.9686, 4.5499, 4.7242, 4.452, 4.6654, 4.8358],
    2004: [5.4322, 5.2526, 4.7309, 4.4806, 4.0543, 4.3243, 4.5262, 4.699, 5.1149, 4.8542, 4.6812, 4.9855],
    2005: [5.0407, 4.7472, 4.8703, 4.3642, 4.1321, 4.1311, 4.2286, 4.535, 4.7436, 4.7947, 4.2307, 4.7215],
    2006: [4.0222, 5.1264, 4.7537, 4.7083, 4.1479, 4.2091, 4.2264, 4.8538, 5.0858, 4.6414, 4.4916, 4.513],
    2007: [5.0138, 6.0036, 4.4762, 4.6826, 4.3526, 4.2473, 4.3531, 4.139, 4.9723, 4.7362, 4.9632, 4.6649],
    2008: [5.1374, 4.8643, 5.1602, 4.8482, 4.032, 4.0109, 4.3229, 4.6188, 4.8754, 4.843, 4.3754, 4.6306],
    2009: [4.3442, 4.8382, 4.4054, 4.3469, 4.5005, 4.2382, 4.5286, 4.7393, 4.9663, 4.9118, 5.0633, 4.98],
    2010: [5.5282, 4.9829, 4.9764, 4.297, 3.9607, 4.3435, 4.3901, 4.1021, 5.1067, 5.2246, 4.6462, 4.4712],
    2011: [5.1463, 4.9008, 5.0909, 4.6274, 4.0877, 4.2823, 4.4323, 5.028, 5.0227, 4.5562, 4.5043, 4.4532],
    2012: [4.6555, 4.7798, 4.3634, 4.4698, 4.2576, 4.2737, 4.0906, 4.6234, 5.0671, 5.0021, 4.6706, 4.836],
    2013: [5.2183, 4.4858, 4.7698, 4.4698, 4.3884, 4.3558, 4.4354, 4.3262, 5.1326, 5.2687, 4.8502, 4.927],
    2014: [5.2301, 4.7143, 4.9296, 4.7167, 4.5127, 4.0109, 4.2161, 4.4983, 5.1334, 4.7455, 4.7194, 4.8634],
    2015: [4.788, 4.9632, 4.7189, 4.391, 4.4388, 4.3718, 4.4326, 4.5336, 5.3071, 4.8082, 4.938, 4.7765],
    2016: [5.663, 4.6531, 4.4551, 4.4542, 4.0351, 4.3392, 4.278, 4.8154, 5.0239, 4.8953, 4.4318, 4.3692],
    2017: [4.5713, 5.3575, 4.7071, 4.8206, 4.4446, 4.1748, 4.0661, 5.0806, 4.8024, 4.8576, 4.8269, 5.1127],
    2018: [4.8007, 5.6998, 4.8566, 4.3337, 4.1107, 3.7013, 4.0356, 4.998, 4.9169, 4.889, 4.4863, 5.0928],
    2019: [4.7412, 4.963, 4.4335, 4.6099, 4.2674, 4.3186, 4.2211, 4.4906, 5.1094, 4.8401, 4.771, 4.4546],
    2020: [5.6134, 5.5286, 4.9325, 4.5398, 4.1342, 4.2221, 4.3603, 4.019, 5.1247, 4.8924, 4.6306, 4.5168],
    2021: [4.7914, 5.0174, 4.5895, 4.4388, 4.1686, 4.1165, 3.9562, 4.5734, 5.2217, 4.787, 4.8398, 4.519],
    2022: [5.5706, 4.9687, 4.3711, 4.842, 4.1345, 4.0346, 4.3894, 4.6198, 5.1494, 4.8996, 4.3234, 5.3522],
    2023: [4.7302, 4.9368, 4.8442, 4.3536, 4.0548, 3.8014, 4.14, 5.1485, 5.5817, 5.3798, 5.0042, 4.6891],
    2024: [5.2658, 5.0712, 4.3382, 4.6056, 4.0567, 4.2007, 4.075, 4.7702, 5.0722, 5.3659, 4.6867, 4.3466]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")

# =============================================================================
# CONJUNTO 2 - ORGANIZADO Latitude  4.1741   Longitude -67.9385
# =============================================================================
datos_2 = {
    1984: [5.2442, 5.7259, 6.1382, 5.1691, 4.8041, 4.4134, 4.6339, 5.3242, 5.179, 4.7947, 4.489, 4.0738],
    1985: [5.4062, 5.6405, 5.532, 5.0314, 4.6003, 4.5461, 4.8655, 5.035, 5.2008, 4.7491, 4.5307, 4.9553],
    1986: [4.8475, 4.7878, 5.341, 4.5847, 4.573, 4.6296, 4.8422, 5.0993, 5.0018, 4.6694, 4.5154, 4.7582],
    1987: [5.01, 5.2726, 5.5814, 5.2301, 4.89, 4.6378, 4.6795, 4.9973, 5.2603, 5.0422, 5.185, 5.1696],
    1988: [5.4874, 6.0358, 6.03, 4.5946, 4.5463, 4.8953, 4.1354, 5.0306, 5.0496, 5.0035, 4.8005, 4.9634],
    1989: [4.9522, 5.3366, 5.141, 5.1158, 4.6018, 4.5288, 4.7177, 5.1043, 4.908, 5.0472, 4.8142, 5.4156],
    1990: [4.5528, 5.3551, 4.6956, 4.6582, 4.5142, 4.6824, 4.6411, 5.358, 5.184, 5.1283, 4.9529, 4.6709],
    1991: [5.3964, 5.4269, 5.5087, 5.0069, 4.7002, 4.507, 4.8146, 4.4172, 5.2382, 5.1218, 5.1005, 4.8866],
    1992: [5.6669, 5.6206, 5.4449, 5.1499, 4.7678, 4.8298, 4.4352, 5.1816, 5.0131, 4.698, 4.5444, 5.0628],
    1993: [5.0318, 5.1334, 4.6826, 4.7395, 4.8914, 4.3502, 5.0318, 5.1396, 4.937, 4.746, 4.8782, 5.3263],
    1994: [5.4178, 5.173, 5.227, 4.9915, 4.6171, 4.4568, 4.6963, 4.9663, 5.047, 5.2896, 4.7011, 5.0868],
    1995: [5.549, 5.3911, 5.3554, 4.7942, 4.6286, 4.5108, 4.7333, 5.1686, 5.292, 5.0263, 4.885, 4.9075],
    1996: [5.4602, 4.8984, 5.5687, 5.2438, 4.5631, 4.1786, 4.5202, 5.1631, 5.1142, 4.902, 4.6313, 4.92],
    1997: [5.365, 4.9853, 6.0634, 5.1953, 4.1858, 4.8173, 4.7885, 5.0962, 5.1677, 5.2764, 5.0825, 5.424],
    1998: [5.9028, 5.4154, 5.2982, 4.8809, 4.2662, 4.6445, 4.8218, 5.0717, 5.3088, 5.1962, 5.0314, 5.0858],
    1999: [4.8094, 4.9742, 5.5548, 4.6865, 4.859, 4.4758, 4.7354, 4.5864, 5.1242, 4.955, 4.9574, 5.0105],
    2000: [5.441, 5.5728, 5.5248, 4.6488, 4.3934, 4.3786, 4.6524, 4.9488, 4.9502, 4.77, 4.9349, 4.8677],
    2001: [5.7715, 5.6407, 5.2932, 4.8838, 4.6673, 4.543, 4.8497, 4.7681, 5.3357, 5.2054, 5.033, 4.5103],
    2002: [5.5728, 5.4562, 5.3074, 4.8122, 4.1909, 4.4659, 4.5451, 4.8398, 5.3191, 5.0299, 4.9454, 5.1648],
    2003: [5.8994, 5.5462, 4.8924, 4.6399, 4.3073, 4.4074, 4.325, 4.9044, 4.8641, 4.6174, 4.8742, 5.2178],
    2004: [5.723, 5.6942, 5.2572, 4.7724, 4.3589, 4.7225, 4.68, 5.071, 5.2733, 4.943, 5.0628, 5.2618],
    2005: [5.3494, 5.239, 5.6518, 4.482, 4.4794, 4.6862, 4.571, 4.8478, 4.8895, 5.0702, 4.536, 4.9138],
    2006: [4.3594, 5.5836, 5.113, 5.004, 4.1904, 4.5766, 4.4302, 5.1607, 5.3736, 4.8631, 4.8514, 4.932],
    2007: [5.4192, 6.4205, 4.8684, 4.89, 4.3171, 4.5254, 4.5269, 4.7381, 5.1626, 4.9992, 5.0453, 4.6958],
    2008: [5.4355, 5.1994, 5.5222, 5.0417, 4.1693, 4.4906, 4.915, 4.8984, 5.0748, 4.957, 4.6879, 4.8377],
    2009: [4.8686, 5.4403, 4.8914, 4.9183, 4.7321, 4.409, 4.8386, 5.1026, 5.2685, 5.1163, 5.3436, 5.3285],
    2010: [5.7578, 5.3146, 5.1012, 4.3939, 4.1856, 4.7009, 4.6128, 4.5401, 5.2481, 5.4238, 4.7746, 4.7827],
    2011: [5.4473, 5.4209, 5.0928, 5.0213, 4.1894, 4.752, 4.7086, 5.1415, 5.1065, 4.6231, 4.6925, 4.7333],
    2012: [5.1372, 5.3304, 4.639, 4.6978, 4.6706, 4.5876, 4.3298, 4.7004, 4.9927, 5.1809, 5.0354, 4.9702],
    2013: [5.7211, 4.7731, 5.3479, 4.8389, 4.6668, 4.8211, 4.6922, 4.4839, 5.2469, 5.1938, 4.9675, 5.111],
    2014: [5.6827, 5.3184, 5.3784, 4.7429, 4.7453, 4.4671, 4.7455, 4.9942, 5.2114, 4.7023, 4.8703, 5.2051],
    2015: [5.3969, 5.5183, 5.1012, 4.6294, 4.7338, 4.6416, 4.5012, 4.6567, 5.3441, 5.1082, 4.997, 5.0832],
    2016: [5.922, 5.0388, 5.1007, 4.41, 4.2943, 4.7602, 4.6594, 5.1574, 5.065, 4.8338, 4.7162, 4.6937],
    2017: [4.8665, 5.6959, 5.022, 5.034, 4.6274, 4.5653, 4.2425, 5.4046, 5.1535, 4.8919, 5.1413, 5.3489],
    2018: [5.1713, 5.8754, 5.3448, 4.4035, 4.1614, 4.0906, 4.3181, 5.1456, 5.1487, 5.1211, 4.8348, 5.4982],
    2019: [5.3458, 5.375, 4.9558, 4.8122, 4.2972, 4.5569, 4.3942, 4.7294, 5.1706, 5.1341, 5.0962, 4.782],
    2020: [5.9659, 5.9026, 5.477, 4.812, 4.3855, 4.4947, 4.6118, 4.2799, 5.263, 5.087, 4.6483, 4.8859],
    2021: [5.2718, 5.513, 5.0688, 4.6339, 4.537, 4.6075, 4.3217, 4.7033, 5.2939, 5.1482, 5.1989, 4.7143],
    2022: [5.8944, 5.2229, 4.897, 4.8751, 4.3706, 4.224, 4.7035, 4.7666, 5.2584, 4.9747, 4.4635, 5.4266],
    2023: [5.081, 5.2642, 5.3647, 4.7381, 4.4923, 4.1242, 4.6114, 5.341, 5.5949, 5.4223, 5.2442, 5.1394],
    2024: [5.7766, 5.437, 4.6726, 4.7381, 4.2269, 4.265, 4.0188, 5.094, 5.315, 5.4533, 4.9663, 4.6586]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")

# =============================================================================
# CONJUNTO 3 - ORGANIZADO LAtitud 5.2745   Longitude -68.4768
# =============================================================================
datos_1 = {
    1984: [5.3738, 5.9971, 6.0773, 5.1643, 5.0503, 4.2826, 4.5194, 4.9934, 5.0561, 5.359, 4.7453, 5.0844],
    1985: [5.7823, 5.7494, 5.6784, 5.1965, 5.226, 4.5163, 5.1223, 5.2937, 5.2997, 5.1888, 4.6118, 5.1487],
    1986: [5.0782, 5.1737, 5.7334, 4.5415, 4.4806, 4.7004, 4.8528, 5.2375, 5.0136, 4.657, 4.8902, 5.0138],
    1987: [5.3076, 5.0402, 5.7876, 4.9097, 4.6666, 4.7717, 4.4645, 4.655, 5.4158, 5.3261, 5.2867, 5.3868],
    1988: [5.4698, 5.9866, 6.1591, 5.4559, 4.9416, 4.7918, 4.2742, 4.9706, 4.9301, 4.879, 4.7741, 5.1744],
    1989: [5.0952, 5.5471, 5.6066, 5.3582, 4.6404, 4.6445, 4.657, 5.0731, 4.9685, 5.0174, 4.9577, 5.4751],
    1990: [4.7954, 5.455, 4.9819, 4.8598, 4.6342, 4.4609, 4.5883, 5.0743, 5.1694, 5.5231, 4.9133, 5.0318],
    1991: [5.5651, 5.6573, 5.6213, 5.0616, 4.8218, 4.691, 4.5528, 4.2833, 5.0789, 4.998, 5.082, 5.1679],
    1992: [5.6753, 5.8649, 5.5404, 5.3119, 4.7424, 4.6255, 4.1911, 4.9102, 5.3237, 4.8816, 4.9706, 5.4847],
    1993: [5.285, 5.1298, 5.3057, 4.6838, 4.6709, 4.2737, 4.6896, 5.0774, 4.8617, 5.0347, 4.9675, 5.6268],
    1994: [5.6028, 5.5459, 5.2428, 4.9058, 4.4964, 4.5535, 4.4902, 4.776, 4.7234, 5.04, 5.2058, 5.4763],
    1995: [5.3976, 5.6357, 5.2536, 4.8974, 4.6483, 4.2322, 4.6505, 5.0609, 5.2452, 5.1763, 5.1346, 5.2046],
    1996: [5.8459, 5.4199, 5.6455, 5.1713, 4.5619, 4.0548, 4.5746, 4.9522, 4.9673, 5.011, 5.0969, 5.1115],
    1997: [5.6899, 5.1766, 6.1942, 5.1518, 4.2943, 4.915, 4.4352, 4.8178, 5.1142, 5.4581, 5.3098, 5.5085],
    1998: [5.8423, 5.3707, 5.3868, 4.7345, 4.5612, 4.5154, 4.5682, 5.0004, 5.5663, 5.1857, 5.3477, 5.3182],
    1999: [5.2193, 5.2433, 5.9616, 4.5415, 4.9133, 4.7899, 4.6411, 4.7201, 5.0062, 5.1696, 5.1708, 5.3659],
    2000: [5.671, 5.6417, 5.7962, 5.0544, 4.4604, 4.2737, 4.6159, 4.8278, 4.9171, 4.945, 5.2294, 5.1538],
    2001: [5.9863, 5.9978, 5.6854, 5.3086, 4.8283, 4.5655, 4.7342, 4.5634, 5.3251, 5.249, 5.3102, 4.621],
    2002: [5.7533, 5.718, 5.3686, 5.107, 4.379, 4.4258, 4.4741, 4.6682, 5.0818, 5.2963, 5.0681, 5.4924],
    2003: [5.8776, 5.8442, 5.0902, 4.5461, 4.1657, 4.5617, 4.1628, 5.1247, 4.7376, 4.8065, 5.1182, 5.1394],
    2004: [5.9242, 5.9328, 5.5673, 4.6673, 4.1993, 4.4419, 4.5806, 4.7467, 5.1718, 5.1761, 4.9634, 5.4226],
    2005: [5.5896, 5.4691, 5.8867, 4.4318, 4.2684, 4.5425, 4.5569, 4.7062, 4.8826, 5.267, 4.8593, 5.3158],
    2006: [4.7383, 5.9081, 5.3309, 4.9106, 4.4186, 4.5814, 4.2266, 4.705, 5.3933, 5.0026, 4.9051, 5.197],
    2007: [5.592, 6.2954, 5.2147, 5.0782, 4.6039, 4.5199, 4.7071, 4.5473, 5.0755, 4.8413, 5.1713, 5.0938],
    2008: [5.7206, 5.6551, 5.892, 5.4211, 4.4592, 4.6987, 4.6222, 4.8696, 5.173, 5.1367, 4.8158, 5.2574],
    2009: [5.0431, 5.6474, 5.2315, 5.262, 4.9562, 4.2756, 4.6483, 4.9488, 5.2505, 5.1242, 5.3765, 5.4586],
    2010: [5.8325, 5.2942, 4.9639, 4.3843, 4.3687, 4.6721, 4.5785, 4.4839, 5.197, 5.429, 4.9913, 4.938],
    2011: [5.7374, 5.7235, 5.3302, 4.7626, 4.3217, 4.626, 4.4287, 5.0474, 4.9668, 5.0911, 4.7359, 4.8398],
    2012: [5.4473, 5.6563, 4.777, 4.6759, 4.5982, 4.6339, 4.1542, 4.5636, 4.8554, 5.1029, 5.2498, 5.2819],
    2013: [5.9474, 5.2325, 5.3302, 4.9392, 4.4777, 4.439, 4.7268, 4.3121, 5.023, 5.099, 5.0441, 5.1818],
    2014: [5.8452, 5.5937, 5.5997, 4.6598, 4.9186, 4.2547, 4.6212, 4.8497, 4.9932, 4.5984, 5.0352, 5.394],
    2015: [5.4866, 5.6285, 5.6774, 4.8406, 4.681, 4.4767, 4.5178, 4.5504, 4.9764, 4.9783, 4.98, 5.1329],
    2016: [6.1188, 5.4598, 5.3292, 4.277, 4.2281, 4.4635, 4.451, 4.7813, 5.0232, 4.8535, 4.5818, 5.0098],
    2017: [5.2656, 5.9129, 5.2694, 5.1684, 4.6087, 4.4381, 4.14, 5.1574, 4.9855, 4.889, 5.1938, 5.6417],
    2018: [5.5526, 6.2424, 5.5418, 4.3666, 4.254, 4.1086, 4.2326, 4.8811, 4.9351, 4.8281, 5.1773, 5.7283],
    2019: [5.5262, 5.5627, 5.2368, 4.7114, 4.4698, 4.3536, 4.4143, 4.6205, 5.0628, 5.2541, 5.1943, 5.2555],
    2020: [6.0233, 6.1428, 5.6549, 4.9488, 4.5862, 4.5881, 4.5886, 4.4822, 5.1756, 5.0981, 4.7232, 5.2908],
    2021: [5.4602, 5.7986, 5.3983, 4.8686, 4.5902, 4.4825, 4.3646, 4.5389, 5.136, 5.0801, 5.4588, 5.2478],
    2022: [5.9873, 5.5531, 5.4485, 5.0674, 4.6159, 4.3534, 4.6063, 4.6344, 5.1869, 5.1504, 4.6752, 5.6652],
    2023: [5.4955, 5.653, 5.7252, 5.1862, 4.6469, 4.0411, 4.4618, 5.0486, 5.3878, 5.341, 5.2951, 5.2524],
    2024: [5.8469, 5.4206, 5.0268, 4.7582, 4.0706, 4.2658, 4.2048, 4.9634, 5.0297, 5.4667, 5.0196, 5.3561]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")


# =============================================================================
# CONJUNTO 4 - ORGANIZADO Latitude  6.0616   Longitude -67.7572
# =============================================================================
datos_1 = {
    1984: [5.4089, 6.3197, 6.4627, 5.3822, 5.4547, 4.2619, 4.5852, 5.347, 5.4677, 5.4758, 5.1062, 5.1197],
    1985: [5.8046, 6.18, 6.0175, 5.4847, 5.1031, 4.5017, 5.3623, 5.3724, 5.6287, 5.027, 4.7047, 5.2054],
    1986: [5.3676, 5.5594, 6.2849, 5.3885, 4.9735, 4.7587, 5.1199, 5.5745, 5.2598, 4.8569, 4.7292, 5.3179],
    1987: [5.4806, 5.7175, 6.1044, 5.5867, 4.7722, 4.7858, 4.8605, 4.8305, 5.5505, 5.3657, 5.3323, 5.5373],
    1988: [5.7043, 6.1692, 6.6118, 6.2376, 5.4194, 4.6296, 4.3068, 5.0549, 5.1082, 4.9961, 4.9879, 5.1703],
    1989: [5.4324, 5.7696, 6.1212, 5.8363, 5.0438, 4.8984, 4.8941, 5.0717, 5.125, 5.2246, 5.034, 5.623],
    1990: [4.9934, 5.5457, 5.2142, 5.3366, 4.8979, 4.6454, 5.0189, 5.1101, 5.2757, 5.6323, 5.0806, 5.2634],
    1991: [5.5418, 6.0859, 6.078, 5.465, 5.3923, 4.7993, 4.7998, 4.6224, 4.9565, 5.2258, 5.4079, 5.2078],
    1992: [5.7955, 6.2172, 6.024, 5.6155, 4.7808, 4.6358, 3.9804, 4.8533, 5.2963, 5.3328, 4.8362, 5.4727],
    1993: [5.5066, 5.3669, 5.6743, 4.987, 4.6138, 4.6781, 5.0494, 5.1067, 5.2042, 5.7394, 5.3614, 5.64],
    1994: [5.8975, 6.0581, 5.808, 5.3266, 4.8043, 4.7165, 4.5778, 4.8547, 5.1336, 5.6093, 5.1175, 5.5882],
    1995: [5.5872, 5.8757, 5.6551, 5.3047, 5.0453, 4.4611, 4.7976, 4.9831, 5.3779, 5.3616, 5.3866, 5.4036],
    1996: [5.9148, 5.8699, 6.2412, 5.6837, 4.9937, 4.4196, 4.7758, 5.1358, 5.0182, 5.3484, 5.2538, 5.3122],
    1997: [5.6671, 5.4473, 6.5153, 5.4946, 4.7472, 5.1912, 4.6044, 4.9032, 5.4425, 5.6892, 5.5435, 5.5402],
    1998: [6.1344, 5.8282, 6.078, 5.2651, 4.5725, 4.5398, 4.8926, 5.2567, 5.3762, 5.3854, 5.461, 5.4202],
    1999: [5.3366, 5.5452, 6.3427, 5.1842, 5.4826, 4.878, 4.8002, 4.7354, 5.0866, 5.2884, 5.1996, 5.5603],
    2000: [5.7156, 6.024, 6.0996, 5.7554, 4.7911, 4.8677, 5.1427, 4.9853, 5.0328, 4.9694, 5.3122, 5.3983],
    2001: [6.1615, 6.5285, 6.1783, 5.7739, 4.8466, 4.691, 4.997, 4.5482, 5.3957, 5.5598, 5.6057, 4.9325],
    2002: [5.7713, 6.2122, 5.8519, 5.4833, 5.1266, 4.3426, 5.045, 4.8233, 5.3278, 5.4439, 5.2562, 5.7029],
    2003: [6.1978, 6.4702, 5.8944, 4.9507, 4.7659, 4.5773, 4.1875, 4.9586, 4.9855, 5.2056, 5.1881, 5.5591],
    2004: [5.9678, 6.3826, 6.2854, 5.2042, 4.6116, 4.7292, 4.8446, 4.8302, 5.0666, 5.3083, 5.1734, 5.5322],
    2005: [5.5877, 6.0194, 6.5278, 4.8535, 4.65, 4.577, 4.7465, 4.6786, 5.1562, 5.4396, 5.1398, 5.4919],
    2006: [5.1607, 6.3281, 5.7622, 5.8162, 4.501, 4.5223, 4.2734, 4.8706, 5.467, 5.2178, 5.2637, 5.4029],
    2007: [5.7398, 6.6737, 5.6561, 5.2438, 4.6469, 4.7604, 4.9474, 4.715, 5.154, 5.0033, 5.3225, 5.155],
    2008: [5.801, 6.0389, 6.3917, 5.7641, 4.903, 4.981, 4.6682, 5.1319, 5.2795, 5.3875, 4.9346, 5.2646],
    2009: [5.4607, 6.0569, 5.6537, 5.9786, 5.297, 4.7405, 4.7117, 5.1713, 5.4598, 5.4264, 5.7564, 5.7264],
    2010: [6.2443, 5.7084, 5.5142, 4.3385, 4.8274, 4.6603, 4.8019, 4.7153, 5.291, 5.5442, 5.0071, 5.2166],
    2011: [5.9285, 6.1368, 5.5397, 5.1845, 4.6397, 4.8113, 4.5998, 5.0285, 5.1228, 5.1689, 4.7767, 5.1924],
    2012: [5.5925, 5.9652, 5.2572, 4.8718, 4.879, 4.7863, 4.2742, 4.6483, 5.22, 5.1101, 5.5704, 5.3539],
    2013: [6.0931, 5.8325, 5.8548, 5.3249, 5.0213, 4.9229, 4.8958, 4.5629, 5.0774, 5.2339, 5.3962, 5.1643],
    2014: [6.0691, 6.1229, 6.3269, 5.2913, 5.3592, 4.6286, 4.877, 5.1026, 5.3249, 4.944, 5.2721, 5.6734],
    2015: [5.7144, 6.001, 6.301, 5.5315, 5.0201, 4.6166, 4.5773, 4.59, 5.3657, 5.2188, 5.2548, 5.3832],
    2016: [6.3202, 6.1397, 5.9971, 4.4909, 4.4582, 4.8017, 4.6776, 5.033, 4.9342, 5.2968, 4.8125, 5.207],
    2017: [5.5637, 6.1433, 5.6148, 5.6088, 5.2426, 4.703, 4.2991, 5.1958, 5.1739, 5.0155, 5.4902, 5.7106],
    2018: [5.8416, 6.383, 6.0175, 5.0357, 4.7064, 4.5146, 4.4842, 4.7381, 5.1535, 5.2692, 5.3796, 5.831],
    2019: [5.9897, 6.1882, 5.9633, 5.2289, 4.7767, 4.4885, 4.7654, 4.7453, 5.1144, 5.5668, 5.3995, 5.4247],
    2020: [6.1411, 6.3478, 6.3874, 5.3292, 4.8833, 4.8564, 4.6159, 4.734, 5.3114, 5.5783, 4.9097, 5.4982],
    2021: [5.5982, 6.115, 5.7713, 5.4274, 4.925, 4.9834, 4.5509, 4.6956, 5.2406, 5.4622, 5.5766, 5.219],
    2022: [6.0955, 5.8339, 5.9635, 5.3998, 5.0712, 4.3906, 4.901, 4.9886, 5.2711, 5.3902, 4.6774, 5.6582],
    2023: [5.6009, 5.9777, 6.1985, 5.227, 5.0162, 4.2672, 4.4542, 5.3323, 5.3678, 5.4934, 5.5106, 5.5044],
    2024: [6.1308, 5.8562, 5.7096, 5.2214, 4.3286, 4.1083, 4.3906, 5.0647, 5.2219, 5.6693, 5.0743, 5.5368]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")

# =============================================================================
# CONJUNTO 5 - ORGANIZADO Location: Latitude  5.8267   Longitude -69.4985
# =============================================================================
datos_1 = {
    1984: [5.2874, 5.9215, 6.0161, 4.9594, 4.8922, 4.1585, 4.3706, 4.7414, 5.0158, 5.137, 5.047, 5.0849],
    1985: [5.6933, 5.6616, 5.6359, 5.1679, 4.757, 4.3142, 4.7899, 5.0647, 4.9819, 5.082, 4.643, 5.0417],
    1986: [5.0009, 5.0033, 5.3518, 4.2274, 4.3361, 4.1794, 4.5998, 4.5242, 4.6956, 4.6008, 4.8065, 4.8504],
    1987: [5.2848, 5.2913, 5.8831, 4.955, 4.7942, 4.5444, 4.2907, 4.5862, 5.1199, 4.8984, 5.2666, 5.1994],
    1988: [5.495, 5.9573, 6.0934, 5.1912, 5.0304, 4.8509, 4.2122, 4.6339, 4.8895, 5.0311, 4.6793, 5.256],
    1989: [5.1247, 5.6635, 5.5735, 5.1163, 4.3279, 4.5245, 4.6795, 5.0856, 4.8962, 4.7335, 4.9351, 5.4706],
    1990: [4.7906, 5.5514, 4.9032, 4.4827, 4.3608, 4.2763, 4.577, 4.8845, 5.0671, 5.0762, 4.8612, 5.2397],
    1991: [5.5694, 5.4826, 5.6184, 4.9747, 4.735, 4.5422, 4.2653, 4.2396, 4.7426, 4.7969, 5.0146, 5.1576],
    1992: [5.617, 5.8546, 5.5356, 5.1737, 4.8485, 4.453, 4.3673, 4.7381, 4.8545, 4.7426, 4.8859, 5.363],
    1993: [5.1655, 5.1811, 5.2142, 4.439, 4.5115, 4.205, 4.7218, 4.9176, 4.3819, 4.7467, 4.8696, 5.5738],
    1994: [5.5654, 5.5027, 5.0676, 4.7273, 4.3627, 4.4006, 4.4172, 4.7707, 4.6807, 4.8857, 4.9826, 5.3635],
    1995: [5.2747, 5.6018, 5.1739, 4.7539, 4.4321, 3.9696, 4.4172, 4.7914, 5.1605, 5.0753, 4.9927, 5.1497],
    1996: [5.8865, 5.3698, 5.6174, 4.9267, 4.2569, 4.0522, 4.4302, 4.6373, 4.9711, 4.8715, 5.0407, 4.938],
    1997: [5.6758, 5.0177, 6.0943, 4.9298, 4.2658, 4.6918, 4.2871, 4.6786, 5.0323, 5.4223, 5.2258, 5.4578],
    1998: [5.8798, 5.4353, 5.2944, 4.5269, 4.4597, 4.2317, 4.5418, 4.8065, 5.3074, 5.0026, 5.2874, 5.2946],
    1999: [5.1998, 5.1557, 5.7948, 4.41, 4.9536, 4.7141, 4.5005, 4.5506, 4.8461, 4.9186, 5.2272, 5.1766],
    2000: [5.724, 5.6808, 5.6304, 5.0633, 4.3082, 4.1088, 4.535, 4.5682, 4.8118, 4.6723, 5.2334, 5.1002],
    2001: [6.0334, 5.9544, 5.5862, 5.243, 4.6915, 4.4765, 4.7899, 4.4429, 4.7964, 5.1115, 5.1302, 4.5787],
    2002: [5.6446, 5.843, 5.3155, 5.0002, 4.2838, 4.147, 4.2924, 4.5259, 4.8209, 5.0983, 4.8924, 5.4602],
    2003: [5.9875, 5.9333, 4.9846, 4.529, 4.1009, 4.416, 4.0574, 5.034, 4.6498, 4.5674, 5.0232, 5.045],
    2004: [5.8433, 5.9114, 5.6381, 4.297, 3.9504, 4.3848, 4.5283, 4.5756, 4.9608, 4.8614, 4.7206, 5.4014],
    2005: [5.5082, 5.509, 5.8229, 4.3656, 4.2802, 4.331, 4.4472, 4.5878, 4.6226, 5.0198, 4.6968, 5.3933],
    2006: [4.8862, 5.8661, 5.0782, 4.8576, 4.4518, 4.3282, 4.1179, 4.5012, 5.2327, 4.7359, 4.7378, 5.166],
    2007: [5.5999, 6.3122, 5.2879, 4.8324, 4.3342, 4.1086, 4.645, 4.3906, 4.7806, 4.4926, 5.0986, 4.9824],
    2008: [5.6453, 5.5217, 5.9318, 5.2548, 4.434, 4.5264, 4.4506, 4.8334, 4.8658, 4.9658, 4.5024, 5.3947],
    2009: [4.9894, 5.7494, 5.2807, 5.1204, 4.9963, 4.1242, 4.5422, 4.7165, 5.053, 4.871, 5.3345, 5.4742],
    2010: [5.9414, 5.1461, 4.9958, 4.1412, 4.1213, 4.2062, 4.3486, 4.3663, 5.2762, 5.2908, 4.7496, 4.9673],
    2011: [5.7398, 5.6878, 5.1917, 4.4959, 3.9804, 4.44, 4.2362, 4.9486, 4.8247, 4.7854, 4.6442, 4.6639],
    2012: [5.4367, 5.5853, 4.705, 4.4616, 4.3051, 4.3968, 4.1146, 4.2636, 4.6032, 5.0294, 5.2169, 5.3141],
    2013: [5.9446, 5.1487, 5.1034, 4.8826, 4.2202, 4.17, 4.5281, 4.183, 4.6958, 5.0388, 5.0462, 5.208],
    2014: [5.8867, 5.5454, 5.5781, 4.4467, 4.704, 4.074, 4.4604, 4.6385, 4.6133, 4.4767, 4.9306, 5.359],
    2015: [5.4886, 5.6554, 5.7146, 4.6061, 4.7105, 4.3862, 4.3174, 4.3488, 4.9085, 4.9121, 4.8, 5.118],
    2016: [6.1781, 5.622, 5.3256, 3.9698, 4.0034, 4.3126, 4.1558, 4.7222, 5.1125, 4.662, 4.6553, 4.9164],
    2017: [5.2524, 5.9338, 4.8643, 5.2414, 4.6063, 4.2509, 4.1136, 4.8869, 4.9829, 4.789, 5.0182, 5.651],
    2018: [5.587, 6.1841, 5.447, 4.2677, 4.1268, 3.9564, 4.0613, 4.6982, 4.7686, 4.4102, 5.1218, 5.7758],
    2019: [5.599, 5.7101, 5.1432, 4.6118, 4.4453, 4.23, 4.2965, 4.4635, 4.9824, 5.0066, 5.0839, 5.1355],
    2020: [6.0182, 6.1591, 5.6544, 4.9658, 4.477, 4.3759, 4.4666, 4.3402, 4.8209, 4.9718, 4.717, 5.3261],
    2021: [5.3983, 5.8015, 5.2255, 4.9687, 4.3548, 4.3202, 4.1885, 4.3375, 5.0455, 4.9718, 5.383, 5.3129],
    2022: [5.9364, 5.4593, 5.2567, 5.0114, 4.3769, 4.1959, 4.4918, 4.3951, 4.8763, 4.8775, 4.6618, 5.6722],
    2023: [5.4622, 5.7218, 5.6302, 5.0172, 4.5158, 4.0903, 4.4738, 4.9642, 5.3822, 5.177, 4.9966, 5.225],
    2024: [5.9522, 5.447, 4.9788, 4.7172, 3.8542, 4.1894, 4.1112, 4.9102, 4.8082, 5.2267, 4.6963, 5.4019]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")


# =============================================================================
# CONJUNTO 6 y 7 - ORGANIZADO  Latitude  4.9571   Longitude -70.8334 y Latitude  4.0919   Longitude -70.8938
# =============================================================================
datos_1 = {
    1984: [5.5459, 5.7432, 6.0122, 4.6054, 4.7033, 4.2497, 4.2053, 4.3327, 4.6301, 4.6704, 4.5149, 4.8346],
    1985: [5.9796, 5.9878, 5.5884, 5.2627, 4.4506, 4.2113, 4.5934, 4.1844, 4.9159, 4.7618, 4.5883, 5.4682],
    1986: [5.3141, 5.4331, 5.3364, 4.5569, 4.1338, 3.9079, 4.2526, 4.7292, 4.6174, 4.5223, 4.7861, 4.8598],
    1987: [5.3491, 5.2286, 6.0127, 5.1043, 4.8187, 4.4434, 4.3154, 4.5353, 5.4223, 4.9346, 5.161, 4.9807],
    1988: [5.4869, 5.8474, 6.0202, 4.817, 4.573, 4.829, 4.2941, 4.5353, 4.8014, 4.5386, 4.6735, 5.0935],
    1989: [5.131, 5.6369, 5.1746, 4.8125, 4.4066, 4.2358, 4.643, 5.0849, 5.1931, 4.7112, 4.7916, 5.4151],
    1990: [4.6778, 5.4271, 4.9174, 4.5377, 4.3891, 4.14, 4.6042, 4.8451, 5.2121, 5.1336, 4.6099, 5.0491],
    1991: [5.5786, 5.2577, 5.2284, 4.793, 4.41, 4.4254, 4.4537, 4.1923, 4.7566, 5.1691, 4.8554, 5.2488],
    1992: [5.587, 5.7062, 5.3086, 4.9867, 4.7146, 4.2751, 4.2761, 4.5734, 4.7544, 4.7671, 4.4035, 5.1898],
    1993: [5.0107, 5.2462, 4.8624, 4.7035, 4.4726, 4.0884, 4.6114, 4.6322, 4.7282, 4.2962, 4.7206, 5.5517],
    1994: [5.6417, 5.3981, 4.661, 4.6022, 4.1978, 4.3145, 4.2391, 4.613, 4.717, 4.9039, 4.848, 5.2702],
    1995: [5.5142, 5.5618, 5.1629, 4.5012, 4.5372, 4.0862, 4.3368, 4.8605, 5.2378, 5.1643, 5.0208, 5.0141],
    1996: [5.9618, 5.0261, 5.2742, 4.8977, 4.4688, 4.2593, 4.3889, 4.56, 4.9279, 4.7218, 4.783, 4.7417],
    1997: [5.8044, 4.9481, 6.0182, 4.7894, 4.1354, 4.697, 4.3896, 4.6517, 5.0242, 5.1919, 4.9001, 5.4271],
    1998: [5.6326, 5.3414, 5.1151, 4.4551, 4.4846, 4.2922, 4.481, 4.6978, 5.065, 5.0402, 4.8761, 5.0938],
    1999: [5.1725, 5.0417, 5.7449, 4.3226, 4.7885, 4.3975, 4.5228, 4.4654, 4.8242, 5.0088, 5.1691, 5.0268],
    2000: [5.725, 5.5949, 5.4624, 4.9226, 4.3925, 4.1383, 4.6063, 4.6879, 4.7875, 4.584, 4.9186, 4.7772],
    2001: [6.1078, 5.7708, 5.016, 4.8878, 4.3762, 4.3171, 4.6416, 4.3606, 4.9649, 5.0822, 4.8955, 4.2984],
    2002: [5.4986, 5.6652, 5.0299, 4.6418, 3.9571, 4.0632, 4.2372, 4.6274, 4.9886, 4.9373, 4.872, 5.3189],
    2003: [6.0598, 5.6822, 4.5823, 4.3783, 4.1369, 4.3702, 3.9907, 4.6176, 4.879, 4.583, 4.8022, 4.8415],
    2004: [5.7694, 5.886, 5.3911, 4.4081, 4.0958, 4.4626, 4.4794, 4.7174, 5.1312, 4.883, 4.6865, 5.2579],
    2005: [5.3568, 5.4034, 5.5042, 4.2427, 4.3039, 4.2331, 4.3975, 4.4921, 4.7866, 4.9207, 4.7563, 5.3635],
    2006: [4.6795, 5.5819, 4.867, 4.763, 4.4419, 4.2276, 4.0769, 4.4563, 4.9759, 4.8497, 4.6452, 5.0777],
    2007: [5.4982, 6.3634, 4.8742, 4.8295, 4.4371, 4.1906, 4.4849, 4.3094, 4.9562, 4.6181, 4.9649, 4.8816],
    2008: [5.5673, 5.2735, 5.6707, 5.0472, 4.2982, 4.2857, 4.3092, 4.7842, 4.973, 4.8326, 4.3296, 5.5519],
    2009: [4.6639, 5.5735, 5.0801, 4.6841, 4.7582, 4.1126, 4.4172, 4.5504, 4.8941, 4.8936, 5.0285, 5.4535],
    2010: [5.8366, 5.0482, 5.1065, 4.2929, 4.0267, 4.3303, 4.2734, 4.2732, 4.8672, 5.0976, 4.6855, 4.8715],
    2011: [5.6153, 5.4761, 4.9728, 4.4952, 3.9218, 4.2144, 4.3164, 4.9543, 4.9843, 4.4652, 4.4314, 4.6123],
    2012: [5.4473, 5.5548, 4.5034, 4.3135, 4.3073, 4.2643, 4.2055, 4.453, 4.8295, 4.9889, 4.961, 5.3083],
    2013: [5.7804, 4.909, 4.8038, 4.8252, 4.4652, 4.3073, 4.4182, 4.2929, 4.8646, 5.0028, 4.8031, 5.0904],
    2014: [5.8118, 5.3273, 5.4132, 4.6181, 4.4892, 3.7754, 4.1926, 4.3814, 4.8701, 4.5317, 4.8852, 5.0446],
    2015: [5.3731, 5.605, 5.365, 4.4522, 4.5173, 4.291, 4.3282, 4.2838, 5.3923, 4.8331, 4.5574, 4.8142],
    2016: [6.2275, 5.3018, 5.2056, 4.1544, 4.0601, 4.3382, 4.2379, 4.7347, 5.2654, 4.8696, 4.6039, 4.6157],
    2017: [5.1936, 5.8318, 4.7794, 5.0676, 4.613, 4.0378, 3.9329, 4.9829, 5.2879, 4.8574, 4.8295, 5.5992],
    2018: [5.3868, 6.0734, 5.0964, 4.321, 4.1738, 3.8678, 4.0054, 4.9102, 4.9178, 4.5938, 4.8302, 5.717],
    2019: [5.3074, 5.4566, 4.6039, 4.5247, 4.2288, 4.1978, 4.3332, 4.4755, 4.8283, 4.9603, 4.9615, 4.9992],
    2020: [5.8798, 6.0041, 5.5894, 4.8048, 4.337, 4.3891, 4.3447, 4.1935, 4.9325, 5.0237, 4.5125, 5.0544],
    2021: [5.2884, 5.6074, 4.9579, 4.9037, 4.187, 4.2883, 4.1506, 4.2427, 4.9176, 4.848, 5.1677, 5.2433],
    2022: [5.7857, 5.3359, 4.89, 4.9999, 4.399, 3.9907, 4.2895, 4.7323, 4.9056, 4.7213, 4.5283, 5.5831],
    2023: [5.3537, 5.5594, 5.3196, 4.6097, 4.5446, 3.9818, 4.4527, 5.1161, 5.5488, 5.2114, 4.8146, 4.8218],
    2024: [5.863, 5.4197, 4.7858, 4.7549, 4.1093, 4.3478, 4.1302, 4.8338, 4.704, 5.1869, 4.4815, 5.0794]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")

# =============================================================================
# CONJUNTO 8 - ORGANIZADO Latitude  3.0503   Longitude -70.9322
# =============================================================================
datos_1 = {
    1984: [5.3554, 5.1161, 5.5802, 4.6896, 4.5804, 4.0438, 4.2206, 4.453, 4.6318, 4.5259, 4.398, 4.8206],
    1985: [6.0689, 5.9266, 5.6582, 4.8461, 4.4465, 4.0649, 4.405, 4.2019, 4.872, 4.6092, 4.5631, 5.3681],
    1986: [5.1451, 5.1149, 5.0844, 4.5149, 4.0282, 3.9408, 4.008, 4.7633, 4.6111, 4.4117, 4.6241, 4.5684],
    1987: [5.1444, 5.0095, 5.9446, 4.5302, 4.9922, 4.4119, 4.5437, 4.5475, 5.1319, 4.9073, 4.7729, 4.961],
    1988: [5.3038, 5.7326, 6.0425, 5.1566, 4.4122, 4.3478, 3.9578, 4.5898, 4.8077, 4.4935, 4.693, 5.0875],
    1989: [4.9334, 5.381, 5.1998, 4.6702, 4.4592, 4.2564, 4.3618, 4.8734, 5.0114, 4.9224, 4.7638, 5.4298],
    1990: [4.5912, 5.2406, 4.7158, 4.386, 4.2787, 4.2917, 4.4297, 4.7026, 5.1134, 5.1977, 4.6265, 4.7179],
    1991: [5.5819, 5.1271, 5.1744, 4.7054, 4.3512, 4.4678, 4.2521, 4.1419, 4.8252, 4.9805, 4.7436, 5.2834],
    1992: [5.5591, 5.4617, 5.0818, 4.6999, 4.4707, 4.1904, 4.0877, 4.5286, 4.6584, 4.7743, 4.3327, 5.0642],
    1993: [4.8725, 5.1226, 4.6346, 4.5134, 4.5394, 4.0298, 4.6891, 4.4386, 4.6538, 4.357, 4.8434, 5.3957],
    1994: [5.4898, 5.2704, 4.8708, 4.5444, 4.2782, 4.3018, 4.2732, 4.6548, 4.603, 4.7297, 4.7215, 5.0436],
    1995: [5.3251, 5.5735, 5.137, 4.3865, 4.7275, 4.0358, 4.427, 4.867, 5.1288, 5.0875, 4.8113, 4.9495],
    1996: [5.7307, 4.644, 5.2634, 5.2382, 4.3685, 4.1537, 4.2324, 4.7033, 4.7275, 4.7402, 4.5802, 4.7026],
    1997: [5.7329, 4.8574, 5.9609, 4.6507, 4.1095, 4.5293, 4.4429, 4.6447, 5.1526, 4.8842, 4.8982, 5.3479],
    1998: [5.5951, 5.2555, 5.1576, 4.3142, 4.4261, 4.2677, 4.386, 4.7033, 4.9526, 4.9114, 4.777, 4.949],
    1999: [4.9104, 5.028, 5.4854, 4.2732, 4.8074, 4.4018, 4.6154, 4.2713, 4.783, 4.8046, 5.1353, 5.0856],
    2000: [5.6186, 5.6172, 5.279, 4.674, 4.2898, 4.2862, 4.3008, 4.6526, 4.7023, 4.4518, 4.8998, 4.7304],
    2001: [5.8867, 5.5666, 4.938, 4.8156, 4.4621, 4.3123, 4.5161, 4.3114, 4.9392, 5.0515, 4.7119, 4.3109],
    2002: [5.4406, 5.603, 4.8816, 4.4918, 3.9041, 4.0397, 4.1808, 4.5454, 5.1634, 4.859, 4.751, 5.1806],
    2003: [6.042, 5.4778, 4.4335, 4.3265, 3.9914, 4.3375, 3.7838, 4.4328, 4.7515, 4.7599, 4.5955, 4.627],
    2004: [5.7233, 5.6681, 5.0016, 4.5773, 4.1227, 4.2732, 4.5946, 4.7335, 4.951, 4.789, 4.6428, 5.1226],
    2005: [5.136, 5.3177, 5.1298, 4.5528, 4.3944, 4.3817, 4.1218, 4.511, 4.7585, 4.9001, 4.8468, 5.0873],
    2006: [4.4071, 5.4583, 4.7184, 4.7741, 4.3027, 4.1714, 3.9934, 4.476, 4.8679, 4.6805, 4.4364, 4.9786],
    2007: [5.3285, 6.2554, 4.7988, 4.7878, 4.3668, 3.9622, 4.4033, 4.1498, 4.7978, 4.488, 4.925, 4.8869],
    2008: [5.5591, 5.2318, 5.58, 4.9459, 4.3327, 4.0262, 4.2101, 4.8074, 4.9596, 4.7184, 4.2734, 5.436],
    2009: [4.4383, 5.5082, 4.8394, 4.6246, 4.7652, 4.289, 4.3277, 4.5046, 4.8482, 4.8996, 4.9438, 5.2642],
    2010: [5.568, 4.8773, 5.094, 4.3939, 4.1573, 4.3094, 4.3445, 3.9977, 5.0196, 5.153, 4.5725, 4.7861],
    2011: [5.5241, 5.2946, 4.9939, 4.4906, 3.876, 4.2744, 4.1196, 4.8343, 5.0846, 4.5094, 4.2574, 4.4287],
    2012: [5.2224, 5.269, 4.3608, 4.4033, 4.3517, 4.2305, 4.2595, 4.2638, 5.1641, 4.9363, 4.848, 5.1576],
    2013: [5.6974, 4.8218, 4.7189, 4.7141, 4.5269, 4.4563, 4.4926, 4.1858, 5.0011, 5.0561, 4.8828, 5.0316],
    2014: [5.6165, 5.1122, 5.1125, 4.667, 4.578, 3.8652, 4.1124, 4.3567, 4.9603, 4.7026, 4.7626, 4.9313],
    2015: [4.9202, 5.3462, 5.1346, 4.4914, 4.4539, 4.2094, 4.3939, 4.283, 5.4228, 4.9056, 4.7275, 4.8785],
    2016: [6.2633, 4.933, 5.0225, 4.338, 4.2062, 4.3718, 4.079, 4.7794, 5.2553, 4.8996, 4.5144, 4.4724],
    2017: [5.0052, 5.7574, 4.8266, 4.9745, 4.5391, 4.1405, 3.8774, 5.1166, 5.0088, 4.7638, 4.631, 5.3753],
    2018: [5.1874, 6.0888, 4.8041, 4.2216, 4.254, 3.9113, 3.9691, 4.8211, 5.0299, 4.7237, 4.6778, 5.4391],
    2019: [5.0846, 5.2925, 4.4563, 4.7076, 4.194, 4.3111, 4.1969, 4.4078, 5.0318, 4.8326, 4.8276, 4.7434],
    2020: [5.8908, 5.9923, 5.3707, 4.6788, 4.3253, 4.3922, 4.4762, 3.8633, 5.0119, 4.9272, 4.3788, 4.861],
    2021: [5.1218, 5.3232, 4.8118, 4.8264, 4.1155, 4.3289, 3.9557, 4.2974, 5.1749, 4.8072, 5.1175, 5.099],
    2022: [5.7955, 5.2944, 4.529, 4.963, 4.3594, 3.8683, 4.2314, 4.7419, 5.0674, 4.7482, 4.597, 5.6467],
    2023: [5.2812, 5.5322, 5.2853, 4.5228, 4.3841, 4.0711, 4.4273, 5.1305, 5.6081, 5.2992, 4.8478, 4.8115],
    2024: [5.7022, 5.3302, 4.5871, 4.8821, 4.26, 4.3795, 3.9811, 4.8192, 4.7539, 5.2471, 4.5982, 4.8523]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")

# =============================================================================
# CONJUNTO 9 y 10 - ORGANIZADO  Latitude  4.0043   Longitude -69.9435 y  Latitude  4.7272   Longitude -69.4161
# =============================================================================
datos_1 = {
    1984: [5.2498, 5.429, 6.0067, 5.0237, 4.6637, 4.273, 4.2746, 4.8175, 5.1775, 4.7419, 4.9843, 4.7458],
    1985: [5.6446, 5.6316, 5.544, 4.9166, 4.4335, 4.205, 4.6118, 5.0369, 5.0203, 4.6973, 4.6682, 4.9642],
    1986: [4.9999, 5.0266, 5.2435, 4.0416, 4.4158, 4.4539, 4.5487, 4.9709, 5.0165, 4.7366, 4.7496, 4.7328],
    1987: [5.147, 4.9469, 5.9155, 5.0364, 4.6574, 4.3745, 4.5187, 4.3939, 5.3328, 4.7424, 4.9733, 4.8754],
    1988: [5.3268, 5.8025, 6.0403, 5.1792, 4.6682, 4.6639, 4.1486, 4.8564, 4.9704, 4.7796, 4.6169, 5.1058],
    1989: [5.0832, 5.4391, 5.2591, 4.7878, 4.2545, 4.4261, 4.5557, 4.9572, 4.9279, 5.0033, 4.8734, 5.3664],
    1990: [4.4705, 5.383, 4.7693, 4.6546, 4.3524, 4.2566, 4.4736, 4.9219, 5.0002, 5.0978, 4.6015, 4.813],
    1991: [5.4799, 5.2824, 5.4062, 4.7724, 4.5192, 4.5026, 4.5154, 4.1606, 4.7894, 5.0045, 4.9313, 5.1439],
    1992: [5.5423, 5.603, 5.2932, 4.932, 4.7011, 4.3284, 4.2886, 4.861, 5.1194, 4.5749, 4.536, 5.117],
    1993: [5.0849, 5.1578, 4.8557, 4.3032, 4.477, 4.0723, 4.6313, 4.8118, 4.6123, 4.6325, 4.8062, 5.4288],
    1994: [5.3479, 5.3131, 4.9392, 4.5242, 4.2672, 4.3385, 4.5048, 4.9188, 4.6826, 4.9354, 4.8221, 5.3311],
    1995: [5.363, 5.4089, 5.214, 4.6327, 4.4842, 4.0891, 4.4273, 4.9296, 5.0222, 5.0129, 4.8936, 5.0506],
    1996: [5.6155, 4.9632, 5.4934, 5.0988, 4.3416, 4.1081, 4.494, 4.6747, 4.9169, 4.735, 4.7093, 4.8828],
    1997: [5.6777, 4.7657, 6.0588, 4.7402, 4.1803, 4.5139, 4.4378, 4.7306, 5.1391, 5.1182, 5.0383, 5.4127],
    1998: [5.6808, 5.328, 5.1262, 4.5226, 4.465, 4.1933, 4.465, 4.7712, 5.2711, 5.0873, 4.9543, 5.0909],
    1999: [5.0666, 4.8394, 5.6594, 4.3913, 4.686, 4.3006, 4.5905, 4.5278, 4.9464, 4.9858, 5.0414, 5.0959],
    2000: [5.6986, 5.5963, 5.581, 4.7366, 4.403, 4.0963, 4.3949, 4.7287, 4.6958, 4.5653, 4.8413, 4.8233],
    2001: [5.7631, 5.645, 5.0539, 5.0458, 4.585, 4.338, 4.6272, 4.2991, 5.1137, 5.0239, 5.0623, 4.2818],
    2002: [5.4578, 5.5308, 5.125, 4.8113, 4.0769, 4.0606, 4.2072, 4.482, 4.9627, 4.9656, 4.8211, 5.2116],
    2003: [5.8277, 5.7298, 4.7285, 4.403, 3.9826, 4.4285, 4.0642, 4.8605, 4.7395, 4.5048, 4.7532, 4.8475],
    2004: [5.7415, 5.6662, 5.2493, 4.4057, 4.0752, 4.4407, 4.4695, 4.7647, 5.1091, 4.8384, 4.6178, 5.2853],
    2005: [5.3287, 5.3887, 5.4859, 4.3673, 4.3366, 4.2542, 4.3997, 4.6567, 4.734, 5.0633, 4.6063, 5.2541],
    2006: [4.417, 5.5752, 4.6973, 4.7002, 4.2619, 4.2348, 4.1782, 4.5562, 5.1852, 4.7321, 4.6795, 5.0923],
    2007: [5.3705, 6.2191, 4.9654, 4.7606, 4.259, 4.2365, 4.481, 4.4237, 4.9944, 4.5818, 5.015, 4.8533],
    2008: [5.5841, 5.2807, 5.6066, 5.2087, 4.4383, 4.3082, 4.441, 4.7304, 5.0366, 5.0095, 4.3978, 5.268],
    2009: [4.6524, 5.562, 5.0184, 4.7575, 4.8778, 4.1846, 4.6483, 4.6279, 5.0333, 4.8583, 5.1247, 5.257],
    2010: [5.6885, 5.2447, 5.0916, 4.3351, 3.9617, 4.4088, 4.4304, 4.4882, 5.1382, 5.1826, 4.7501, 4.8247],
    2011: [5.5322, 5.4353, 5.0753, 4.405, 4.0298, 4.217, 4.2086, 5.0513, 5.1619, 4.4496, 4.5737, 4.6034],
    2012: [5.1998, 5.4401, 4.4666, 4.4198, 4.4134, 4.1897, 4.1177, 4.6488, 4.9234, 5.0551, 4.9654, 5.167],
    2013: [5.7125, 4.7431, 4.8329, 4.8334, 4.4878, 4.3483, 4.5384, 4.3214, 4.9462, 5.2178, 4.8425, 5.1211],
    2014: [5.7022, 5.2814, 5.3508, 4.621, 4.6704, 3.792, 4.3447, 4.5221, 4.8415, 4.5048, 4.8134, 5.077],
    2015: [5.2666, 5.4773, 5.3558, 4.4143, 4.6003, 4.3433, 4.4398, 4.4112, 5.1818, 4.7642, 4.8516, 4.9154],
    2016: [6.143, 5.2097, 5.183, 4.3195, 3.983, 4.4398, 4.368, 4.854, 5.1607, 4.7705, 4.5504, 4.6255],
    2017: [5.0916, 5.9052, 4.8958, 5.0858, 4.668, 4.2151, 3.9478, 5.0412, 5.1293, 4.8821, 4.8598, 5.5747],
    2018: [5.411, 6.1044, 5.1629, 4.393, 3.9826, 3.9442, 4.0627, 4.9397, 5.0174, 4.5653, 4.8799, 5.5788],
    2019: [5.3282, 5.2488, 4.7366, 4.6531, 4.1916, 4.3519, 4.2919, 4.5017, 4.9824, 5.0218, 5.0762, 4.9063],
    2020: [5.9546, 5.9923, 5.447, 4.7592, 4.3536, 4.4753, 4.5641, 4.0966, 5.0196, 4.967, 4.6798, 4.8629],
    2021: [5.2226, 5.5634, 4.9886, 4.6694, 4.3502, 4.3135, 4.1314, 4.4441, 5.1338, 4.9354, 5.041, 5.1106],
    2022: [5.7984, 5.4122, 4.9294, 4.8989, 4.374, 4.2605, 4.421, 4.5696, 4.9764, 4.7846, 4.6162, 5.5118],
    2023: [5.2447, 5.419, 5.3904, 4.6778, 4.3774, 3.9082, 4.4028, 5.1617, 5.6004, 5.3268, 4.9202, 4.8098],
    2024: [5.6959, 5.4259, 4.6848, 4.5847, 3.931, 4.3973, 4.0694, 4.8763, 5.0232, 5.293, 4.5922, 4.9373]
}


# Crear DataFrame
months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
df = pd.DataFrame(datos_1, index=months).T

print("═" * 70)
print("ANÁLISIS - PRIMER CONJUNTO DE DATOS")
print("═" * 70)
print(f"Período: {df.index.min()}-{df.index.max()}")
print(f"Dimensión: {df.shape[0]} años × {df.shape[1]} meses")
print(f"Rango global: {df.values.min():.2f} - {df.values.max():.2f} kWh/m²/day")

# Configuración de estilo para gráficas
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Monthly Time Series - ALLSKY_SFC_SW_DWN\nConjunto 1 - Lat=4.7218, Lon=-69.46',
             fontsize=16, fontweight='bold')

# 1. SERIE TEMPORAL MENSUAL
ax1 = axes[0, 0]
colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
for i, month in enumerate(months):
    ax1.plot(df.index, df[month], label=month, linewidth=1, alpha=0.7, color=colors[i])

ax1.set_title('a) Monthly Time Series', fontweight='bold', loc='left')
ax1.set_xlabel('Year')
ax1.set_ylabel('Irradiance (kWh/m²/day)')
ax1.grid(True, alpha=0.3)
ax1.legend(ncol=4, fontsize=8, loc='upper center', bbox_to_anchor=(0.5, -0.15))
ax1.set_xlim(1984, 2024)
ax1.set_ylim(3.0, 6.5)

# 2. MEDIA ANUAL
ax2 = axes[0, 1]
annual_mean = df.mean(axis=1)
ax2.plot(annual_mean.index, annual_mean.values, linewidth=2.5, color='red', marker='o', markersize=3)
ax2.set_title('b) Annual Mean Irradiance (from monthly values)', fontweight='bold', loc='left')
ax2.set_xlabel('Year')
ax2.set_ylabel('Mean Annual Irradiance (kWh/m²/day)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1984, 2024)
ax2.set_ylim(4.2, 5.2)

# Tendencia lineal
z = np.polyfit(annual_mean.index, annual_mean.values, 1)
p = np.poly1d(z)
ax2.plot(annual_mean.index, p(annual_mean.index), "r--", alpha=0.8, linewidth=1.5,
         label=f'Tendencia: {z[0]:.4f} kWh/m²/año')
ax2.legend()

# 3. CLIMATOLOGÍA MENSUAL
ax3 = axes[1, 0]
climatology = df.mean(axis=0)
ax3.plot(months, climatology.values, marker='o', linewidth=2.5, color='green',
         markerfacecolor='darkgreen', markersize=6)
ax3.set_title('c) Climatology: Mean Monthly Irradiance (kWh/m²/day) - 1984-2024',
              fontweight='bold', loc='left')
ax3.set_xlabel('Month')
ax3.set_ylabel('Mean Irradiance (kWh/m²/day)')
ax3.grid(True, alpha=0.3)
ax3.set_ylim(4.0, 5.4)
ax3.fill_between(months, climatology.values, alpha=0.2, color='green')

# 4. ANOMALÍAS MENSUALES
ax4 = axes[1, 1]
anomalies = df - climatology

# Anomalías mensuales
for i, month in enumerate(months):
    ax4.plot(anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i])

# Media anual de anomalías
annual_anomalies = anomalies.mean(axis=1)
ax4.plot(annual_anomalies.index, annual_anomalies.values, linewidth=2.5, color='black',
         label='Media anual', marker='o', markersize=3)

# Media móvil de 5 años
rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
ax4.plot(rolling_mean.index, rolling_mean.values, linewidth=2, color='blue',
         label='Media móvil (5 años)')

ax4.set_title('d) Monthly Anomalies Relative to Climatology', fontweight='bold', loc='left')
ax4.set_xlabel('Year')
ax4.set_ylabel('Anomaly (kWh/m²/day)')
ax4.grid(True, alpha=0.3)
ax4.axhline(y=0, color='black', linestyle='-', alpha=0.7)
ax4.set_xlim(1984, 2024)
ax4.set_ylim(-1.0, 1.0)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.93)
plt.show()

# ANÁLISIS ESTADÍSTICO COMPLETO
print("\n" + "═" * 70)
print("ESTADÍSTICAS DETALLADAS - CONJUNTO 1")
print("═" * 70)

# Estadísticas básicas
print(f"\n1. ESTADÍSTICAS GLOBALES:")
print(f"   • Período: {df.index.min()}-{df.index.max()} ({len(df)} años)")
print(f"   • Media global: {df.values.mean():.4f} kWh/m²/day")
print(f"   • Desviación estándar: {df.values.std():.4f} kWh/m²/day")
print(f"   • Rango total: {df.values.min():.4f} - {df.values.max():.4f} kWh/m²/day")

print(f"\n2. ESTADÍSTICAS ANUALES:")
print(f"   • Media anual promedio: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} kWh/m²/day")
print(f"   • Año con mayor irradiancia: {annual_mean.idxmax()} ({annual_mean.max():.4f})")
print(f"   • Año con menor irradiancia: {annual_mean.idxmin()} ({annual_mean.min():.4f})")
print(f"   • Tendencia lineal: {z[0]:.6f} kWh/m²/day/año")

print(f"\n3. CLIMATOLOGÍA MENSUAL (1984-2024):")
print("   Mes    Promedio   Máximo    Mínimo     Std")
print("   " + "-" * 45)
for i, month in enumerate(months):
    month_data = df[month]
    print(f"   {month}     {climatology[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}")

print(f"\n4. ANÁLISIS DE ANOMALÍAS:")
print(f"   • Año con mayor anomalía positiva: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})")
print(f"   • Año con mayor anomalía negativa: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})")
print(f"   • Años con anomalía positiva: {sum(annual_anomalies > 0)}")
print(f"   • Años con anomalía negativa: {sum(annual_anomalies < 0)}")
print(f"   • Desviación estándar de anomalías: {annual_anomalies.std():.4f}")

# Estacionalidad
print(f"\n5. ESTACIONALIDAD:")
max_month = months[np.argmax(climatology)]
min_month = months[np.argmin(climatology)]
seasonal_amplitude = climatology.max() - climatology.min()
print(f"   • Mes más irradiante: {max_month} ({climatology.max():.4f} kWh/m²/day)")
print(f"   • Mes menos irradiante: {min_month} ({climatology.min():.4f} kWh/m²/day)")
print(f"   • Amplitud estacional: {seasonal_amplitude:.4f} kWh/m²/day")

# Variabilidad interanual
print(f"\n6. VARIABILIDAD INTERANUAL:")
cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
print(f"   • Coeficiente de variación anual: {cv_annual:.2f}%")
print(f"   • Rango interanual: {annual_mean.max() - annual_mean.min():.4f} kWh/m²/day")

# Gráfica adicional: Evolución por décadas
plt.figure(figsize=(12, 6))
decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
decade_colors = ['blue', 'green', 'orange', 'red']

for i, (start, end) in enumerate(decades):
    dec_data = annual_mean[(annual_mean.index >= start) & (annual_mean.index <= end)]
    if len(dec_data) > 0:
        plt.plot(dec_data.index, dec_data.values, 'o-', color=decade_colors[i],
                label=f'{start}-{end}', alpha=0.7, markersize=4)

plt.plot(annual_mean.index, p(annual_mean.index), 'k--', linewidth=2,
         label=f'Tendencia general ({z[0]:.4f}/año)')
plt.title('Evolución de la Irradiancia Media Anual por Décadas\nConjunto 1 (1984-2024)')
plt.xlabel('Año')
plt.ylabel('Irradiancia Media Anual (kWh/m²/day)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\n7. RESUMEN FINAL - CONJUNTO 1:")
print(f"   • Tendencia general: {'POSITIVA' if z[0] > 0 else 'NEGATIVA' if z[0] < 0 else 'ESTABLE'}")
print(f"   • Variabilidad estacional: {seasonal_amplitude:.4f} kWh/m²/day")
print(f"   • Estabilidad interanual: {cv_annual:.2f}% de variación")
