import requests
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import subprocess
import re
import pyttsx3  # For text-to-speech

history = []

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def track_mobile_number(api_key, phone_number):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=IN&format=1"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("valid"):
            for widget in info_box.winfo_children():
                widget.destroy()
            
            info_list = [
                ("Mobile Number", data['number']),
                ("Local Format", data['local_format']),
                ("International Format", data['international_format']),
                ("Country Prefix", data['country_prefix']),
                ("Country Code", data['country_code']),
                ("Country Name", data['country_name']),
                ("Location", data['location']),
                ("Carrier", data['carrier']),
                ("Line Type", data['line_type'])
            ]
            
            output_text = ""
            for label_text, value in info_list:
                row_frame = ttk.Frame(info_box, style="Black.TFrame")
                row_frame.pack(pady=5, fill='x')
                
                label_desc = ttk.Label(row_frame, text=label_text, style="Green.TLabel")
                label_desc.pack(side='left', padx=(0, 10), anchor='center')
                
                label_value = ttk.Label(row_frame, text=value, style="Green.TLabel")
                label_value.pack(side='left', anchor='center')
                
                output_text += f"{label_text}: {value}. "
            
            # Speak the results
            speak("Here's the information for the mobile number:")
            speak(output_text)
            
            # Add this search to the history
            history.append({"number": phone_number, "data": data})
        else:
            messagebox.showerror("Error", "INVALID MOBILE NUMBER OR UNABLE TO FETCH INFORMATION")
            speak("Invalid mobile number or unable to fetch information.")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error: {e}")
        speak(f"An error occurred: {e}")

def display_history():
    for widget in info_box.winfo_children():
        widget.destroy()

    if not history:
        messagebox.showinfo("History", "No search history available.")
        speak("No search history available.")
        return

    output_text = "Search history:\n"
    for entry in history:
        row_frame = ttk.Frame(info_box, style="Black.TFrame")
        row_frame.pack(pady=5, fill='x')
        
        # Display only key information from history for clarity
        labels = [
            ("Searched Number", entry["number"]),
            ("Country Name", entry["data"]["country_name"]),
            ("Carrier", entry["data"]["carrier"])
        ]
        
        for label_text, value in labels:
            label_desc = ttk.Label(row_frame, text=label_text, style="Green.TLabel")
            label_desc.pack(side='left', padx=(0, 10), anchor='center')
            
            label_value = ttk.Label(row_frame, text=value, style="Green.TLabel")
            label_value.pack(side='left', anchor='center')
            output_text += f"{label_text}: {value}. "
        
        output_text += "\n"
    
    speak(output_text)

def on_enter(event=None):
    phone_number = entry.get().strip().lower()
    if phone_number == "history":
        display_history()
    elif phone_number == "wifi":
        # Wi-Fi Scanning Functionality
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        networks = result.stdout

        # Use regex to find all SSIDs
        ssid_pattern = re.compile(r'SSID \d+ : (.+)')
        ssids = ssid_pattern.findall(networks)

        # Clear previous content in info_box
        for widget in info_box.winfo_children():
            widget.destroy()

        output_text = "Available Wi-Fi networks:\n"
        for index, ssid in enumerate(ssids, start=1):
            row_frame = ttk.Frame(info_box, style="Black.TFrame")
            row_frame.pack(pady=5, fill='x')
            
            label_desc = ttk.Label(row_frame, text=f"Network {index}", style="Green.TLabel")
            label_desc.pack(side='left', padx=(0, 10), anchor='center')
            
            label_value = ttk.Label(row_frame, text=ssid, style="Green.TLabel")
            label_value.pack(side='left', anchor='center')
            
            output_text += f"Network {index}: {ssid}. "

        # Speak the Wi-Fi networks
        speak(output_text)

        # Optionally save to file if needed
        with open('wifi_networks.txt', 'w') as file:
            file.write("NO\tNAME\n")
            for index, ssid in enumerate(ssids, start=1):
                file.write(f"{index}\t{ssid.upper()}\n")

        messagebox.showinfo("Wi-Fi Scan", "Wi-Fi networks have been displayed.")
    else:
        if phone_number:
            track_mobile_number(api_key, phone_number)
        else:
            messagebox.showwarning("Input Error", "Please enter a mobile number, 'history', or 'wifi'")
            speak("Please enter a mobile number, type 'history', or 'wifi'.")

def save_history():
    """Save the search history to a JSON file."""
    history_file = "search_history.json"
    try:
        with open(history_file, 'w') as f:
            json.dump(history, f)
        speak("Search history has been saved.")
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save history: {e}")
        speak(f"Failed to save history: {e}")

def exit_app():
    save_history()  # Save history before exiting
    root.destroy()

api_key = "f98b8d297dfe98415eba65f5ecccb9f2"

root = tk.Tk()
root.title("Mobile Number Tracker / Wi-Fi Scanner")
root.attributes('-fullscreen', True)
root.configure(bg='black')

style = ttk.Style()
style.theme_use('clam')
style.configure("Black.TFrame", background="black")
style.configure("Green.TLabel", foreground="green", background="black", font=('Arial', 14))
style.configure("TButton", foreground="green", background="black", font=('Arial', 14))
style.configure("TRed.TButton", foreground="red", background="black", font=('Arial', 14))

main_frame = ttk.Frame(root, style="Black.TFrame")
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

upper_frame = ttk.Frame(main_frame, style="Black.TFrame")
upper_frame.pack(fill='both', expand=True, pady=(20, 10))

info_box = ttk.Frame(upper_frame, style="Black.TFrame", borderwidth=2, relief="solid")
info_box.pack(fill='both', expand=True, padx=20, pady=20)

lower_frame = ttk.Frame(main_frame, style="Black.TFrame")
lower_frame.pack(side='bottom', fill='x', pady=(10, 20))

input_label = ttk.Label(lower_frame, text="ENTER THE INDIAN MOBILE NUMBER\n    \t HISTORY OR WIFI", style="Green.TLabel", anchor='center')
input_label.pack(pady=10)

entry = ttk.Entry(lower_frame, style="TEntry", font=('Arial', 14))
entry.pack(pady=10)
entry.bind('<Return>', on_enter)

search_button = ttk.Button(lower_frame, text="FOUND", command=on_enter)
search_button.pack(side='left', padx=10, pady=10)

exit_button = ttk.Button(lower_frame, text="EXIT", command=exit_app, style="TRed.TButton")
exit_button.pack(side='right', padx=10, pady=10)

root.mainloop()