# Mobile Number Tracker & Wi-Fi Scanner (Python Tkinter)

A **Python GUI application** that can:

* Track basic information about an **Indian mobile number**
* Scan and list **available Wi-Fi networks**
* Provide **voice feedback using text-to-speech**
* Maintain **search history**

The application is built using **Python Tkinter** with a **dark terminal-style interface**.

---

# Features

### Mobile Number Tracking

Fetch information about a mobile number using an API.

Information displayed:

* Mobile Number
* Local Format
* International Format
* Country Prefix
* Country Code
* Country Name
* Location
* Carrier
* Line Type

---

### Wi-Fi Network Scanner

Type **wifi** to scan available Wi-Fi networks.

The program will:

* Detect nearby Wi-Fi SSIDs
* Display them inside the GUI
* Save results to a file

Output file:

```
wifi_networks.txt
```

---

### Voice Assistant

The application includes **text-to-speech** functionality using **pyttsx3**.

The system speaks:

* Mobile number information
* Wi-Fi scan results
* Error messages
* History information

---

### Search History

Type:

```
history
```

to display previously searched mobile numbers.

Stored information includes:

* Number searched
* Country name
* Carrier

History can be saved to:

```
search_history.json
```

---

# Commands

| Command       | Function                      |
| ------------- | ----------------------------- |
| Mobile number | Track number information      |
| history       | Show previous searches        |
| wifi          | Scan available Wi-Fi networks |

Example:

```
9876543210
```

```
wifi
```

```
history
```

---

# Requirements

Python **3.x**

Required libraries:

```
requests
pyttsx3
tkinter
```

Install dependencies:

```
pip install requests pyttsx3
```

(Tkinter usually comes pre-installed with Python.)

---

# How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/mobile-number-tracker.git
```

2. Open the project folder

```
cd mobile-number-tracker
```

3. Run the program

```
python tracker.py
```

---

# Project Structure

```
mobile-number-tracker/
│
├── tracker.py
├── wifi_networks.txt
├── search_history.json
└── README.md
```

---

# Technologies Used

* Python
* Tkinter GUI
* Requests API
* Pyttsx3 (Text-to-Speech)
* Subprocess
* Regex
* JSON

---

# API Used

This project uses the **Numverify API** to validate and retrieve mobile number information.

Website:

```
https://numverify.com
```

Note:
You must provide your **API key** in the code.

Example:

```
api_key = "YOUR_API_KEY"
```

---

# Educational Purpose

This project helps beginners learn:

* Python GUI programming
* API integration
* Text-to-Speech systems
* File handling
* Wi-Fi scanning using system commands

---

# Author

**Sayan**

BCA Student
Python GUI Project

---

# Disclaimer

This tool is created for **educational purposes only**.
Mobile number data depends on the **API service accuracy**.

---

# License

Free to use for **learning and educational projects**.
