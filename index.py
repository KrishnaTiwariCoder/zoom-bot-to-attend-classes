import subprocess
import pandas as pd
import time 
import pyautogui
from datetime import datetime

def sign_in (meetingid  , password):
    
    subprocess.run('C:\\Users\\KRISHNA TIWARI\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
    time.sleep(2)
    
    join_button = pyautogui.locateCenterOnScreen("join-btn.png")
    pyautogui.moveTo(join_button)
    pyautogui.click()
    
    meeting_id_button = pyautogui.locateCenterOnScreen("enter-meeting-id.png")
    pyautogui.moveTo(meeting_id_button)
    pyautogui.click()
    pyautogui.write(meetingid)
    
    media_buttons = pyautogui.locateAllOnScreen("media.png")
    
    for btn in media_buttons:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)
    
    
    join_button_2 = pyautogui.locateCenterOnScreen("join-btn-2.png")
    pyautogui.moveTo(join_button_2)
    pyautogui.click()
    
    time.sleep(3)
        
    passcode_input = pyautogui.locateCenterOnScreen("passcode-input.png")
    pyautogui.moveTo(passcode_input)
    pyautogui.write(password)
    # pyautogui.click()
    
    pyautogui.press("enter")
    
    print("joined")
    
    
df = pd.read_csv("timings.csv")

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

       row = df.loc[df['timings'] == now]
       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])

       sign_in(m_id, m_pswd)
       time.sleep(40)

