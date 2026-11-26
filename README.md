# Mobile Number Tracker & Wi-Fi Scanner

A Python Tkinter GUI application for retrieving mobile number information, scanning nearby Wi-Fi networks, and providing voice feedback.

## Features

### Mobile Number Information
Uses the Numverify API to retrieve available information about an Indian mobile number, including:
- Local and international number formats
- Country prefix and country code
- Country name and location
- Carrier and line type

### Wi-Fi Network Scanner
- Detects nearby Wi-Fi network names (SSIDs).
- Displays detected networks in the application.
- Saves results to `wifi_networks.txt`.

**Platform limitation:** Wi-Fi scanning currently uses the Windows `netsh` command and is therefore supported on Windows only. It does not work as-is on Fedora or other Linux distributions.

### Voice Assistant
Uses `pyttsx3` for text-to-speech feedback.

### Search History
- Displays previously searched mobile numbers using the `history` command.
- Saves history in `search_history.json`.

## Requirements

- Python 3
- Tkinter
- Requests
- pyttsx3

## Installation

Clone the repository:

```bash
git clone https://github.com/sayan08880/MOBILE-NUMBER-INFORMATION-.git
cd MOBILE-NUMBER-INFORMATION-
```

Install the Python dependencies:

```bash
python -m pip install requests pyttsx3
```

On Fedora KDE, install Tkinter if needed:

```bash
sudo dnf5 install python3-tkinter
```

## API Key Configuration

This project uses the [Numverify API](https://numverify.com/).

Set your API key as an environment variable instead of placing it directly in the source code.

**Fedora / Linux:**

```bash
export NUMVERIFY_API_KEY="YOUR_API_KEY"
```

**Windows PowerShell:**

```powershell
$env:NUMVERIFY_API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your own Numverify API key.

Keep your API key private. Never commit it to GitHub.

## Run the Application

```bash
python info.py
```

## Available Commands

| Input | Function |
|---|---|
| Mobile number | Retrieve available number information |
| `history` | Display previous searches |
| `wifi` | Scan available Wi-Fi networks (Windows only) |

## Project Structure

```text
MOBILE-NUMBER-INFORMATION-/
├── info.py
└── README.md
```

The application creates `wifi_networks.txt` and `search_history.json` when those features are used.

## Technologies Used

- Python
- Tkinter
- Requests
- pyttsx3
- Subprocess
- Regular expressions
- JSON

## Educational Purpose

This project demonstrates Python GUI development, API integration, text-to-speech, file handling, and operating-system command execution.

## Author

**Sayan**
BCA Student

## Disclaimer

This project is intended for educational purposes. Mobile number information depends on the Numverify API and its data accuracy.

## License

Free to use for learning and educational projects.
