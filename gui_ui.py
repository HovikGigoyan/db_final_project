import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = "http://127.0.0.1:8001"

def fetch_data(endpoint):
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}/")
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return []

def post_data(endpoint, payload):
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}/", json=payload)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Record added successfully!")
        else:
            messagebox.showerror("Error", f"Failed to add record: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error adding data: {e}")

def display_data(title, data):
    data_window = tk.Toplevel()
    data_window.title(title)
    data_window.geometry("600x400")
    
    frame = ttk.Frame(data_window, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=("Helvetica", 10))
    scrollbar.config(command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(fill=tk.BOTH, expand=True)

    for item in data:
        text.insert(tk.END, f"{item}\n\n")
    text.config(state=tk.DISABLED)

def add_festival():
    def submit():
        payload = {
            "Name": name_var.get(),
            "Location": location_var.get(),
            "Date": date_var.get(),
            "Organizer": organizer_var.get(),
            "Format": format_var.get(),
        }
        post_data("Festivals", payload)
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add New Festival")
    add_window.geometry("400x400")
    
    ttk.Label(add_window, text="Name:").pack(pady=5)
    name_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=name_var).pack(pady=5)

    ttk.Label(add_window, text="Location:").pack(pady=5)
    location_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=location_var).pack(pady=5)

    ttk.Label(add_window, text="Date (YYYY-MM-DD):").pack(pady=5)
    date_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=date_var).pack(pady=5)

    ttk.Label(add_window, text="Organizer:").pack(pady=5)
    organizer_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=organizer_var).pack(pady=5)

    ttk.Label(add_window, text="Format (Outdoor/Indoor):").pack(pady=5)
    format_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=format_var).pack(pady=5)

    ttk.Button(add_window, text="Submit", command=submit).pack(pady=10)

def add_rockband():
    def submit():
        payload = {
            "Name": name_var.get(),
            "YearFounded": year_founded_var.get(),
            "Genre": genre_var.get(),
            "Producer": producer_var.get(),
            "Members": members_var.get(),
        }
        post_data("RockBands", payload)
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add New Rock Band")
    add_window.geometry("400x400")
    
    ttk.Label(add_window, text="Name:").pack(pady=5)
    name_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=name_var).pack(pady=5)

    ttk.Label(add_window, text="Year Founded:").pack(pady=5)
    year_founded_var = tk.IntVar()
    ttk.Entry(add_window, textvariable=year_founded_var).pack(pady=5)

    ttk.Label(add_window, text="Genre:").pack(pady=5)
    genre_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=genre_var).pack(pady=5)

    ttk.Label(add_window, text="Producer:").pack(pady=5)
    producer_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=producer_var).pack(pady=5)

    ttk.Label(add_window, text="Members (comma-separated):").pack(pady=5)
    members_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=members_var).pack(pady=5)

    ttk.Button(add_window, text="Submit", command=submit).pack(pady=10)

def add_performance():
    def submit():
        payload = {
            "FestivalID": festival_id_var.get(),
            "BandID": band_id_var.get(),
            "PerformanceType": performance_type_var.get(),
            "Number": number_var.get(),
            "Duration": duration_var.get(),
        }
        post_data("Performances", payload)
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add New Performance")
    add_window.geometry("400x400")
    
    ttk.Label(add_window, text="Festival ID:").pack(pady=5)
    festival_id_var = tk.IntVar()
    ttk.Entry(add_window, textvariable=festival_id_var).pack(pady=5)

    ttk.Label(add_window, text="Band ID:").pack(pady=5)
    band_id_var = tk.IntVar()
    ttk.Entry(add_window, textvariable=band_id_var).pack(pady=5)

    ttk.Label(add_window, text="Performance Type:").pack(pady=5)
    performance_type_var = tk.StringVar()
    ttk.Entry(add_window, textvariable=performance_type_var).pack(pady=5)

    ttk.Label(add_window, text="Number:").pack(pady=5)
    number_var = tk.IntVar()
    ttk.Entry(add_window, textvariable=number_var).pack(pady=5)

    ttk.Label(add_window, text="Duration (mins):").pack(pady=5)
    duration_var = tk.DoubleVar()
    ttk.Entry(add_window, textvariable=duration_var).pack(pady=5)

    ttk.Button(add_window, text="Submit", command=submit).pack(pady=10)

app = tk.Tk()
app.title("Rock Festival Management")
app.geometry("500x400")

notebook = ttk.Notebook(app)
notebook.pack(fill=tk.BOTH, expand=True, pady=10)

festivals_tab = ttk.Frame(notebook)
rockbands_tab = ttk.Frame(notebook)
performances_tab = ttk.Frame(notebook)

notebook.add(festivals_tab, text="Festivals")
notebook.add(rockbands_tab, text="Rock Bands")
notebook.add(performances_tab, text="Performances")

ttk.Label(festivals_tab, text="Festivals Management", font=("Helvetica", 14, "bold")).pack(pady=10)
ttk.Button(festivals_tab, text="View All Festivals", command=lambda: display_data("Festivals", fetch_data("Festivals"))).pack(pady=5)
ttk.Button(festivals_tab, text="Add New Festival", command=add_festival).pack(pady=5)

ttk.Label(rockbands_tab, text="Rock Bands Management", font=("Helvetica", 14, "bold")).pack(pady=10)
ttk.Button(rockbands_tab, text="View All Rock Bands", command=lambda: display_data("Rock Bands", fetch_data("Rockbands"))).pack(pady=5)
ttk.Button(rockbands_tab, text="Add New Rock Band", command=add_rockband).pack(pady=5)

ttk.Label(performances_tab, text="Performances Management", font=("Helvetica", 14, "bold")).pack(pady=10)
ttk.Button(performances_tab, text="View All Performances", command=lambda: display_data("Performances", fetch_data("Performances"))).pack(pady=5)
ttk.Button(performances_tab, text="Add New Performance", command=add_performance).pack(pady=5)

footer = ttk.Label(app, text="Rock Festival Management System", font=("Helvetica", 10, "italic"))
footer.pack(side=tk.BOTTOM, pady=10)

app.mainloop()