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
    twelvehour_format = datetime.strptime(time_str, "%I:%M:%S %p").strftime(
        "%I:%M:%S %p"
    )
    return twelvehour_format


def check_alarm(alarm_time):
    current_time = get_CT()
    if current_time == hour12_format(alarm_time):
        return True
    return False


# Main function to play audio using Pyaudio
def main(audio_file):
    size = 1024
    wf = wave.open(audio_file, "rb")
    p = pyaudio.PyAudio()

    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
    )

    data = wf.readframes(size)

    while data:
        stream.write(data)
        data = wf.readframes(size)

    stream.stop_stream()
    stream.close()
    p.terminate()


print("***== Alarm clock ==***")
print("Date: ", get_date())
print("Time: ", get_CT())
print("-" * 30)
alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
while True:
    print(f"Current time is.. {get_CT()}", end="\r")
    if check_alarm(alarm_time):
        print("\nWake up!")
        source = main("audio/alarm-995.wav")
        break
    time.sleep(1)
