# How to Add New Datasets

This document explains how to add new datasets to the system in an easy and dynamic way.

## Steps to Add a New Dataset

### 1. Add Dataset Data

In `src/data/data_sets.py`, simply add your new dataset at the end of the file:

```python
# Example: Adding dataset_11
dataset_11 = {
    1984: [5.1, 5.3, 4.8, 4.2, 3.9, 3.7, 3.8, 4.1, 4.5, 4.7, 4.9, 5.2],
    1985: [5.0, 5.2, 4.9, 4.3, 4.0, 3.8, 3.9, 4.2, 4.6, 4.8, 4.8, 5.1],
    # ... more years
}
```

### 2. Add Metadata

In the `DATASET_METADATA` dictionary, add the information for the new dataset:

```python
DATASET_METADATA = {
    # ... existing datasets ...
    'dataset_11': {
        'name': 'Dataset 11',
        'location': 'Lat=X.XXXX, Lon=-XX.XXXX',
        'description': 'Solar irradiance data - ALLSKY_SFC_SW_DWN'
    },
}
```

### For Combined Datasets (Multiple Stations)

If your dataset has multiple stations, use this format:

```python
# Dataset with 3 stations (A, B, C)
dataset_12_13_14 = {
    1984: [5.1, 5.3, 4.8, 4.2, 3.9, 3.7, 3.8, 4.1, 4.5, 4.7, 4.9, 5.2],
    # ... more years
}

# Metadata
'dataset_12_13_14': {
    'name': 'Dataset 12-13-14',
    'name_suffix': 'combined',  # ← This will make it appear as "Combined"
    'location': 'Station A: Lat=X.XX, Lon=-XX.XX | Station B: Lat=Y.YY, Lon=-YY.YY | Station C: Lat=Z.ZZ, Lon=-ZZ.ZZ',
    'description': 'Combined solar irradiance data from three stations - ALLSKY_SFC_SW_DWN'
},
```

## That's It! 🎉

**You don't need to modify any other files.** The system automatically:

- ✅ Will detect the new dataset
- ✅ Include it in all menus
- ✅ Allow individual analysis
- ✅ Include it in complete analysis
- ✅ Allow DOCX/PDF export
- ✅ Handle translations automatically
- ✅ Format locations correctly

## Automatic Features

### Automatic Detection

The system automatically searches for all variables that:

- Start with `dataset_`
- Are dictionaries (contain data)
- Have corresponding metadata

### Natural Sorting

Datasets are sorted naturally:

- `dataset_1`, `dataset_2`, ..., `dataset_10`, `dataset_11`
- Not alphabetically: ~~`dataset_1`, `dataset_10`, `dataset_2`~~

### Dynamic Translations

- **"Dataset"** → **"Dataset"** (in both languages)
- **"Combined"** → **"Combinado"** (in Spanish)
- **"Station A/B/C/..."** → **"Estación A/B/C/..."** (in Spanish)

### Dynamic Station Handling

The system can handle any number of stations:

- Station A, Station B (current)
- Station A, Station B, Station C (future)
- Station 1, Station 2, Station 3 (also works)

## Usage Examples

```python
# Simple dataset
dataset_15 = { ... }
'dataset_15': {
    'name': 'Dataset 15',
    'location': 'Lat=1.234, Lon=-5.678',
    'description': '...'
}

# Combined dataset with 4 stations
dataset_16_17_18_19 = { ... }
'dataset_16_17_18_19': {
    'name': 'Dataset 16-17-18-19',
    'name_suffix': 'combined',
    'location': 'Station A: Lat=1.1, Lon=-1.1 | Station B: Lat=2.2, Lon=-2.2 | Station C: Lat=3.3, Lon=-3.3 | Station D: Lat=4.4, Lon=-4.4',
    'description': '...'
}
```

**The system is completely scalable and easy to use!** 🚀
