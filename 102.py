import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "It's Water Time...",
            message = "Getting enough water every day is important for your health.\n Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change,\n cause your body to overheat, and lead to constipation and kidney stones.\n Water helps your body: Keep a normal temperature.",
            app_icon = "C:\Users\Cvi\Downloads\Python\Projects\Project 102\water_glass.ico",
            timeout = 10
        )

        time.sleep(60*60) 


