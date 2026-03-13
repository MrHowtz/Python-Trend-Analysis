import tkinter as tk
from tkinter import filedialog, ttk, messagebox

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.impute import SimpleImputer


df3 = None
countries = []

def load_file():
    global df3, countries

    file_path = filedialog.askopenfilename(
        title="Select COVID Dataset",
        filetypes=[("CSV files", "*.csv")]
    )

    if not file_path:
        return

    df = pd.read_csv(file_path)

    df.drop(columns=["SNo", "Last Update"], inplace=True, errors="ignore")

    df.rename(columns={
        'Province/State': 'State',
        'Country/Region': 'Country'
    }, inplace=True)

    df['Date'] = pd.to_datetime(df['Date'])

    imputer = SimpleImputer(strategy='constant')
    df2 = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    df3 = df2.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

    countries = sorted(df3['Country'].unique())

    country_dropdown["values"] = countries

    messagebox.showinfo("Success", "File loaded successfully!")


def clear_plot():
    ax.clear()


def draw_plot():
    canvas.draw()


def show_country():
    if df3 is None:
        messagebox.showerror("Error", "Load a file first")
        return

    country = country_var.get()

    if not country:
        messagebox.showerror("Error", "Select a country")
        return

    clear_plot()

    C = df3[df3['Country'] == country]

    ax.plot(C['Date'], C['Confirmed'], label='Confirmed')
    ax.plot(C['Date'], C['Deaths'], label='Deaths')
    ax.plot(C['Date'], C['Recovered'], label='Recovered')

    ax.set_title(f"COVID Trend in {country}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cases")
    ax.legend()

    draw_plot()


def show_all():
    if df3 is None:
        messagebox.showerror("Error", "Load a file first")
        return

    for country in countries:

        clear_plot()

        C = df3[df3['Country'] == country]

        ax.plot(C['Date'], C['Confirmed'], label='Confirmed')
        ax.plot(C['Date'], C['Deaths'], label='Deaths')
        ax.plot(C['Date'], C['Recovered'], label='Recovered')

        ax.set_title(f"COVID Trend in {country}")
        ax.set_xlabel("Date")
        ax.set_ylabel("Cases")
        ax.legend()

        draw_plot()

        root.update()
        root.after(800)


def global_trend():
    if df3 is None:
        messagebox.showerror("Error", "Load a file first")
        return

    clear_plot()

    df4 = df3.groupby('Date')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

    ax.scatter(np.arange(len(df4)), df4['Confirmed'], label='Confirmed')
    ax.scatter(np.arange(len(df4)), df4['Deaths'], label='Deaths')
    ax.scatter(np.arange(len(df4)), df4['Recovered'], label='Recovered')

    ax.set_title("Global COVID Trend")
    ax.set_xlabel("Days")
    ax.set_ylabel("Cases")
    ax.legend()

    draw_plot()


root = tk.Tk()
root.title("COVID Data Visualizer")
root.geometry("900x600")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)


control_frame = tk.Frame(root)
control_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

for i in range(5):
    control_frame.columnconfigure(i, weight=1)


load_btn = tk.Button(control_frame, text="Load CSV", command=load_file)
load_btn.grid(row=0, column=0, sticky="ew", padx=5)


country_var = tk.StringVar()

country_dropdown = ttk.Combobox(
    control_frame,
    textvariable=country_var,
    state="readonly"
)

country_dropdown.grid(row=0, column=1, sticky="ew", padx=5)


show_btn = tk.Button(control_frame, text="Show Country", command=show_country)
show_btn.grid(row=0, column=2, sticky="ew", padx=5)


all_btn = tk.Button(control_frame, text="Show All", command=show_all)
all_btn.grid(row=0, column=3, sticky="ew", padx=5)


global_btn = tk.Button(control_frame, text="Global Trend", command=global_trend)
global_btn.grid(row=0, column=4, sticky="ew", padx=5)


plot_frame = tk.Frame(root)
plot_frame.grid(row=1, column=0, sticky="nsew")

plot_frame.rowconfigure(0, weight=1)
plot_frame.columnconfigure(0, weight=1)


fig, ax = plt.subplots()

canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()

canvas_widget.grid(row=0, column=0, sticky="nsew")


root.mainloop()