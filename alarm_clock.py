from datetime import datetime
import time
import pytz
import wave
import pyaudio


def get_CT():
    current_time = datetime.now(pytz.timezone("Asia/Makassar")).strftime("%I:%M:%S %p")
    return current_time


def get_date():
    current_date = datetime.now().strftime("%d-%m-%Y")
    return current_date


def hour12_format(time_str):
    return datetime.strptime(time_str, "%I:%M:%S %p").strftime("%I:%M:%S %p")


def check_alarm(alarm_time):
    current_time = get_CT()
    if current_time == hour12_format(alarm_time):
        return True
    return False


# Function to play audio using PyAudio
def play_audio(file):
    chunk = 1024
    wf = wave.open(file, "rb")
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()


print("***== Alarm clock ==***")
print("Date: ", get_date())
print("Time: ", get_CT())
print("-" * 30)
alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
while True:
    print(f"Current time-- {get_CT()}", end="\r")
    if check_alarm(alarm_time):
        print("\nWake up!")
        source = play_audio("audio/mixkit-classic-alarm-995.wav")
        break
    time.sleep(1)
