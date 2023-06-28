from IPython.core.getipython import get_ipython
from IPython.display import display, Markdown, Latex
import pandas as pd
from time import time, sleep
from tqdm.notebook import tqdm
from tqdm import trange
import datetime
import requests
import json

# from tqdm.contrib.telegram import tqdm, trange
from configparser import ConfigParser


def create_new_cell(contents):
    shell = get_ipython()

    payload = dict(
        source='set_next_input',
        text=contents,
        replace=False,
    )
    shell.payload_manager.write_payload(payload, single=False)
    
def calculate_seconds(timestring):
    time_obj = datetime.datetime.strptime(timestring, "%H:%M:%S")
    hours = time_obj.hour
    minutes = time_obj.minute
    seconds = time_obj.second

    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    

    return total_seconds

def step_commands(df, index_num):
    line1 = f"print('**{df.Combined.iloc[index_num]}**')"
    total_seconds = calculate_seconds(df.Duration.iloc[index_num])

    line2 = f"print('Duration is {round(total_seconds/60, 3)} minutes')"

    line3 = f"countdown(df.Duration.iloc[{index_num}], df.Combined.iloc[{index_num}])"

    combined_lines = line1 + " \n" + line2 + " \n" + line3 

    return combined_lines


def countdown(timestring, step_text):
    time_obj = datetime.datetime.strptime(timestring, "%H:%M:%S")

    hours = time_obj.hour
    minutes = time_obj.minute
    seconds = time_obj.second

    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    total_seconds_original = total_seconds

    pbar = tqdm(
        # total=100,
        total=total_seconds,
        bar_format="{desc}   {percentage:3.0f}% [Elapsed: {elapsed} -- Remaining: {remaining}]",
        
    )
    while total_seconds > 0:
        # # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)


        # print(timer, sep='\r')


        # Update the tqdm progress bar
        # pbar.update(100 / total_seconds_original)

        sleep(1)

        total_seconds -= 1
        pbar.update(1)



    pbar.refresh()
    display(f"COMPLETED {step_text}")
    send_discord_message(f"COMPLETED {step_text} in {step_text}")
    
def send_discord_message(content):
    payload = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 204:
        print("Discord notification successful!")
    else:
        print(f"Failed to notify on discord. Status code: {response.status_code}")


def current_datetime():
    current_datetime = datetime.datetime.now()

    # Format the datetime as "Day, mm/dd/yy at hh:mm:ss AM/PM"
    formatted_datetime = current_datetime.strftime("%A, %m/%d/%y at %I:%M:%S %p")

    return formatted_datetime
