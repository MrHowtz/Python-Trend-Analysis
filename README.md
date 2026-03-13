
# COVID-19 Data Visualizer

A Python-based desktop application built with Tkinter and Matplotlib that allows users to load, process, and visualize COVID-19 dataset trends. 

## Features

* **Interactive GUI:** Easy-to-use interface built with Tkinter.
* **Custom Data Loading:** Load your own COVID-19 CSV datasets locally via a file dialog.
* **Data Cleaning:** Automatically handles missing values using `scikit-learn`'s `SimpleImputer` and standardizes column names for processing.
* **Country-Specific Analysis:** Select a specific country from the dropdown to view its confirmed cases, deaths, and recoveries over time.
* **Animated 'Show All' Mode:** Automatically cycles through all available countries, rendering their trends sequentially.
* **Global Aggregation:** View the overall global trend across all days via a scatter plot.

## Prerequisites

Ensure you have Python 3.x installed on your machine. You will also need to install the required external libraries.

### Dependencies

* `pandas`
* `numpy`
* `matplotlib`
* `scikit-learn`

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/covid-data-visualizer.git](https://github.com/yourusername/covid-data-visualizer.git)
   cd covid-data-visualizer

```

2. **Install the required packages:**
You can install the dependencies using `pip`:
```bash
pip install pandas numpy matplotlib scikit-learn

```


3. **Run the application:**
```bash
python main.py

```



## Usage

1. Launch the application.
2. Click the **Load CSV** button and select your COVID-19 dataset.
3. Once the success message appears, use the dropdown menu to select a country.
4. Click **Show Country** to plot the data for the selected region.
5. Click **Show All** to iterate through and visualize every country in the dataset automatically.
6. Click **Global Trend** to view the aggregated worldwide data plotted over time.

## Expected Dataset Format

For the application to parse your data correctly, the imported CSV should ideally be in a standard daily COVID-19 reporting format containing the following columns (though it handles minor variations):

* `Date`
* `Province/State` (Will be renamed to `State`)
* `Country/Region` (Will be renamed to `Country`)
* `Confirmed`
* `Deaths`
* `Recovered`

*(Note: Columns like `SNo` and `Last Update` are automatically dropped by the application to streamline data processing.)*
