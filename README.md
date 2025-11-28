# Alarm Clock

A simple command-line alarm clock application built with Python that plays an audio alert at a specified time.

## Features

- Set alarm time in 12-hour format (HH:MM:SS AM/PM)
- Real-time display of current time
- Timezone support (Asia/Makassar)
- Audio playback using PyAudio
- Continuous time monitoring with live updates

## Requirements

- Python 3.x
- PyAudio
- PyTZ
- Wave (included in Python standard library)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd alarm-clock
```

1. Install required dependencies:

```bash
pip install pyaudio pytz
```

## Usage

Run the alarm clock:

```bash
python alarm_clock.py
```

The program will:

1. Display the current date and time
1. Prompt you to enter the alarm time in `HH:MM:SS AM/PM` format (e.g., `07:30:00 AM`)
1. Monitor the current time continuously
1. Play an alarm sound when the specified time is reached

Example:

```text
***== Alarm clock ==***
Date:  28-11-2025
Time:  08:45:30 AM
------------------------------
Enter time in 'HH:MM:SS AM/PM' format: 08:46:00 AM
Current time is.. 08:45:45 AM
```

## Project Structure

```text
alarm-clock/
├── alarm_clock.py          # Main application file
├── audio/                  # Directory containing alarm sounds
│   └── mixkit-classic-alarm-995.wav
├── LICENSE                 # License file
└── README.md              # This file
```

## License

See the [LICENSE](LICENSE) file for details.
