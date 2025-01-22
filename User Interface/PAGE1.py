from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import math
import random

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="weather app")
    location = geolocator.geocode(city)
    
    if location is not None:
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        
        # Display the timezone and city
        timezone.config(text=f"{result}")## in place of city we can use result also
        long_lat.config(text=f"{round(location.longitude,4)}°N {round(location.latitude,4)}°E")
        
        
        # Get the local time in the timezone
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        ## Weather api
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=79065bfbcd894f8fd45f962278dfaa88"
        data = requests.get(api_url).json()
    temperature = round(data['main']['temp'] - 273.15, 2)  # Convert Kelvin to Celsius
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description'].capitalize()
        
    ## Update labels
    temp_label.config(text=f"Temperature: {temperature} °C")
    humidity_label.config(text=f"Humidity: {humidity} %")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    wind_label.config(text=f"Wind: {wind_speed} m/s")
    description_label.config(text=f"Description: {description}")
   
    temperK = data['main']['temp']
    temperC = int(temperK - 273.15)
    icon = data['weather'][0]['icon']    
   
    # Simulate weather icons based on a predefined pattern or random selection
    weather_conditions = [
    {"icon": "01d", "description": "clear sky"},
    {"icon": "02d", "description": "few clouds"},
    {"icon": "03d", "description": "scattered clouds"},
    {"icon": "09d", "description": "shower rain"},
    {"icon": "10d", "description": "rain"},
    {"icon": "13d", "description": "snow"},
    {"icon": "50d", "description": "mist"},
    ]
    
    ##display temperature
    Temperature_deg=Label(root, text=f"{temperC}°", font=("Helvetica", 120, "bold"), fg="white", bg="#57adff")
    Temperature_deg.place(x=100, y=300)
    Feeltemp = data['main']['feels_like']
    Feeltemp = int(Feeltemp - 273.15)
    feel_temps=Label(root, text=f"Feels like : {Feeltemp}°C", font=("Helvetica", 15, "bold"), fg="white", bg="#57adff")
    feel_temps.place(x=100, y=500)

    #first cell
    firstdayimage = f"{temperC},{icon}"
    firsticon = f"{icon}"
    file_path1 = rf"User Interface\DayImages\{firsticon}.png" 
    photo1 = ImageTk.PhotoImage(file=file_path1)
    firstimage.config(image=photo1)
    firstimage.image = photo1
    firstimage.place(x=24, y=40)
    tempday1 =int(data['main']['temp_max'] - 273.15)
    tempnig1 =int(data['main']['temp_max'] - 273.15)
    tempday1 = f"{tempday1}°C"
    tempnig1 = f"{tempnig1}°C"
    day1temp.config(text=f"Day:{tempday1}")
    nig1temp.config(text=f"Night:{tempnig1}")
         
    #second cell
    if firstdayimage != "":
     days_ahead2 = 6
    temps2 = [round(temperC + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
    weather2 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
    seconddayimage = f"{temps2[0]},{weather2[0]['icon']}"
    secondicon = f"{weather2[0]['icon']}"
    file_path2 = rf"User Interface\DayImages\{secondicon}.png"
    photo2 = ImageTk.PhotoImage(file=file_path2)
    secondimage.config(image=photo2)
    secondimage.image = photo2
    secondimage.place(x=24, y=40)
    day2temp.config(text=f"{temps2[0]}°C")
    day2weather.config(text=f"{weather2[0]['description']}")
    
    #Third cell
    if seconddayimage != "":
       temps3 = [round(temps2[0] + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
       weather3 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
       thirddayimage = f"{temps3[0]},{weather3[0]['icon']}"
    thirdicon = f"{weather3[0]['icon']}"
    file_path3 = rf"User Interface\DayImages\{thirdicon}.png"
    photo3 = ImageTk.PhotoImage(file=file_path3)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3
    thirdimage.place(x=24, y=40)
    day3temp.config(text=f"{temps3[0]}°C")
    day3weather.config(text=f"{weather3[0]['description']}")
    
    #Fourth cell
    if thirddayimage != "":
      temps4 = [round(temps3[0] + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
      weather4 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
      fourthdayimage = f"{temps4[0]},{weather4[0]['icon']}"
    fourthicon = f"{weather4[0]['icon']}"
    file_path4 = rf"User Interface\DayImages\{fourthicon}.png"
    photo4 = ImageTk.PhotoImage(file=file_path4)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4
    fourthimage.place(x=24, y=40)
    day4temp.config(text=f"{temps4[0]}°C")
    day4weather.config(text=f"{weather4[0]['description']}")
    
    #Fifth cell
    if fourthdayimage != "":
      temps5 = [round(temps4[0] + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
      weather5 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
      fifthdayimage = f"{temps5[0]},{weather5[0]['icon']}"
      fifthicon = f"{weather5[0]['icon']}"
      filepath5 = rf"User Interface\DayImages\{fifthicon}.png"
      photo5 = ImageTk.PhotoImage(file=filepath5)
      fifthimage.config(image=photo5)
      fifthimage.image= photo5
      fifthimage.place(x=24, y=40)
      day5temp.config(text=f"{temps5[0]}°C")
      day5weather.config(text=f"{weather5[0]['description']}")
    
    
    #Sixth cell
    if fifthdayimage != "":
      temps6 = [round(temps5[0] + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
      weather6 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
      sixthdayimage = f"{temps6[0]},{weather6[0]['icon']}"
    sixthimage = f"{weather6[0]['icon']}"
    sixthicon=f"{weather6[0]['icon']}"
    sixthimage = Label(root, bg="#282829")
    filepath6 = rf"User Interface\DayImages\{sixthicon}.png"
    photo6 = ImageTk.PhotoImage(file=filepath6)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6 
    sixthimage.place(x=1180, y=670)
    day6temp.config(text=f"{temps6[0]}°C")
    day6weather.config(text=f"{weather6[0]['description']}")
    
    
    
    #Seventh cell
    if sixthdayimage != "":
      temps7 = [round(temps6[0] + 2 * math.sin(i), 2) for i in range(1, days_ahead2 + 1)]
      weather7 = [random.choice(weather_conditions) for _ in range(days_ahead2)]
      seventhdayimage = f"{temps7[0]},{weather7[0]['icon']}"
    seventhicon = f"{weather7[0]['icon']}"
    filepath7 = rf"User Interface\DayImages\{seventhicon}.png"
    photo7 = ImageTk.PhotoImage(file=filepath7)
    seventhimage.config(image=photo7)
    seventhimage.image= photo7
    seventhimage.place(x=24, y=40)
    day7temp.config(text=f"{temps7[0]}°C")
    day7weather.config(text=f"{weather7[0]['description']}")
    
    
    
    #days
    first=datetime.now()
    day1.config(text=first.strftime('%A'))
    
    second = first + timedelta(days=1)
    day2.config(text=second.strftime('%A'))
    
    third = first + timedelta(days=2)
    day3.config(text=third.strftime('%A'))
    
    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime('%A'))
    
    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime('%A'))
    
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime('%A'))
    
    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime('%A'))
    
    
    
    
   




root = Tk()
root.title("Weather Application")
# Make the window full screen
root.attributes("-fullscreen", True)

# Optional: Exit full screen with the "Escape" key
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

root.configure(bg="#57adff")
root.resizable(False, False)

# Add icon
image_icon = Image.open("User Interface\DayImages\image.png")
image_iconresize = image_icon.resize((60, 60), Image.Resampling.LANCZOS)
image_icon1 = ImageTk.PhotoImage(image_iconresize)
root.iconphoto(False, image_icon1)

image_label=Label(root, image=image_icon1, bg="#57adff")
image_label.place(x=440, y=20)
# Heading for the weather application
heading = Label(root, text="Weather Application", font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
heading.place(x=500, y=20)  # Adjust x and y for positioning



# Search box                 
Search_image = Image.open("User Interface/Otherimages/image2.png")
search_resized_image = Search_image.resize((690, 530), Image.Resampling.LANCZOS) 
myimage = ImageTk.PhotoImage(search_resized_image)
mysearchbar = Label(image=myimage, bg="#57adff")
mysearchbar.place(x=885, y=-45)

# Load the image and resize it
file_path = r"User Interface\DayImages\04d.png"
original_image = Image.open(file_path )
resized_image = original_image.resize((60, 60), Image.Resampling.LANCZOS)  # Replace ANTIALIAS with LANCZOS
weat_image = ImageTk.PhotoImage(resized_image)

# Display the resized image
weatherimage = Label(root, image=weat_image, bg="#000000")
weatherimage.place(x=960, y=188)

textfield = tk.Entry(root, justify='center', width=25, font=('poppins', 20, 'bold'), bg="#131010", border=0, fg="white")
textfield.place(x=1025, y=206, height=42)
textfield.focus()

Search_icon = Image.open("User Interface/Otherimages/Searchicon.png")
resize_Searchicon = Search_icon.resize((50, 50), Image.Resampling.LANCZOS)
Searchicon = ImageTk.PhotoImage(resize_Searchicon)

myimage_icon = Button(image=Searchicon, borderwidth=0, cursor="hand2", bg="#000000", command=getWeather)
myimage_icon.place(x=1420, y=206)

frame1 = Frame(root, width=1600, height=300, bg="#212120")
frame1.place(x=0, y=600)  # Use place to position the larger frame

# Smaller box
# Constants for frame dimensions and spacing
large_frame_width = 320  # Width of frame2
frame_width = 178        # Width of other frames
frame_height = 225       # Height of all frames
gap = 20                 # Gap between frames
start_x = 10             # Starting x position
y_position = 620         # Fixed y position for all frames

# Frame 2 (larger width)
frame2 = Frame(root, width=large_frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame2.place(x=start_x, y=y_position)

# Frame 3
frame3 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame3.place(x=start_x + large_frame_width + gap, y=y_position)

# Frame 4
frame4 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame4.place(x=start_x + large_frame_width + gap + frame_width + gap, y=y_position)

# Frame 5
frame5 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame5.place(x=start_x + large_frame_width + gap + 2 * (frame_width + gap), y=y_position)

# Frame 6
frame6 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame6.place(x=start_x + large_frame_width + gap + 3 * (frame_width + gap), y=y_position)

# Frame 7
frame7 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame7.place(x=start_x + large_frame_width + gap + 4 * (frame_width + gap), y=y_position)

# Frame 8
frame8 = Frame(root, width=frame_width, height=frame_height, bd=4, relief="solid", bg='white',
               highlightbackground="white", highlightcolor="white")
frame8.place(x=start_x + large_frame_width + gap + 5 * (frame_width + gap), y=y_position)


# Clock
clock = Label(root, font=("helvetica", 25, 'bold'), fg='white', bg='#57adff')
clock.place(x=100, y=30)

# TimeZone
timezone = Label(root, font=("helvetica", 25, 'bold'), fg='white', bg='#57adff')
timezone.place(x=100, y=100)

long_lat = Label(root, font=("helvertica", 18), fg='#000000', bg='#57adff')
long_lat.place(x=100, y=140)

## Data frame
frame = Frame(root, width=350, height=260, bd=4,  bg='#282829',
               highlightbackground="white", highlightcolor="white")
frame.place(x=1100, y=290)

#Data Display
# Temperature Label
temp_label = Label(frame, text="Temperature: ", font=('Helvetica', 12), fg="white", bg="#282829")
temp_label.place(x=50, y=20)

# Humidity Label
humidity_label = Label(frame, text="Humidity: ", font=('Helvetica', 12), fg="white", bg="#282829")
humidity_label.place(x=50, y=60)

# Pressure Label
pressure_label = Label(frame, text="Pressure: ", font=('Helvetica', 12), fg="white", bg="#282829")
pressure_label.place(x=50, y=100)

# Wind Label
wind_label = Label(frame, text="Wind: ", font=('Helvetica', 12), fg="white", bg="#282829")
wind_label.place(x=50, y=140)

# Description Label
description_label = Label(frame, text="Weather: ", font=('Helvetica', 12), fg="white", bg="#282829")
description_label.place(x=50, y=180)

#first cell
firstframe=Frame(root,width=294,height=200,bg='#282829')
firstframe.place(x=22,y=634)
day1=Label(firstframe,font='arial 20',bg="#282829",fg='#fff')
day1.place(x=24,y=10)
firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=24,y=60)

day1temp=Label(firstframe,font='arial 18',bg="#282829",fg='#57adff')
day1temp.place(x=140,y=60)
nig1temp=Label(firstframe,font='arial 18',bg="#282829",fg='#57adff')
nig1temp.place(x=140,y=90)

#second cell
secondframe=Frame(root,width=156,height=200,bg='#282829')
secondframe.place(x=360,y=634)

day2=Label(secondframe,font='arial 10',bg="#282829",fg='#fff')
day2.place(x=29,y=10)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=24,y=30)
day2temp=Label(secondframe,font='arial 10',bg="#282829",fg='#57adff')
day2temp.place(x=24,y=160)
day2weather=Label(secondframe,font='arial 10',bg="#282829",fg='#57adff')
day2weather.place(x=24,y=140)


#Third cell
Thirdframe=Frame(root,width=156,height=200,bg='#282829')
Thirdframe.place(x=559,y=634)
day3=Label(Thirdframe,font='arial 10',bg="#282829",fg='#fff')
day3.place(x=34,y=10)
thirdimage=Label(Thirdframe,bg="#282829")
thirdimage.place(x=24,y=30)
day3temp=Label(Thirdframe,font='arial 10',bg="#282829",fg='#57adff')
day3temp.place(x=24,y=160)
day3weather=Label(Thirdframe,font='arial 10',bg="#282829",fg='#57adff')
day3weather.place(x=24,y=140)



#Fourth cell
Fourthframe=Frame(root,width=156,height=200,bg='#282829')
Fourthframe.place(x=758,y=634)
day4=Label(Fourthframe,font='arial 10',bg="#282829",fg='#fff')
day4.place(x=39,y=10)
fourthimage=Label(Fourthframe,bg="#282829")
fourthimage.place(x=39,y=30)
day4temp=Label(Fourthframe,font='arial 10',bg="#282829",fg='#57adff')
day4temp.place(x=24,y=160)
day4weather=Label(Fourthframe,font='arial 10',bg="#282829",fg='#57adff')
day4weather.place(x=24,y=140)


#Fifth cell
Fifthframe=Frame(root,width=156,height=200,bg='#282829')
Fifthframe.place(x=955,y=634)
day5=Label(Fifthframe,font='arial 10',bg="#282829",fg='#fff')
day5.place(x=44,y=10)
fifthimage=Label(Fifthframe,bg="#282829")
fifthimage.place(x=44,y=30)
day5temp=Label(Fifthframe,font='arial 10',bg="#282829",fg='#57adff')
day5temp.place(x=24,y=160)
day5weather=Label(Fifthframe,font='arial 10',bg="#282829",fg='#57adff')
day5weather.place(x=24,y=140)

#Sixth cell
Sixthframe=Frame(root,width=156,height=200,bg='#282829')
Sixthframe.place(x=1154,y=634)
day6=Label(Sixthframe,font='arial 10',bg="#282829",fg='#fff')
day6.place(x=49,y=10)
sixthimage=Label(Sixthframe,bg="#282829")
sixthimage.place(x=49,y=30)
day6temp=Label(Sixthframe,font='arial 10',bg="#282829",fg='#57adff')
day6temp.place(x=24,y=160)
day6weather=Label(Sixthframe,font='arial 10',bg="#282829",fg='#57adff')
day6weather.place(x=24,y=140)

#Seventh cell
seventhframe=Frame(root,width=156,height=200,bg='#282829')
seventhframe.place(x=1350,y=634)
day7=Label(seventhframe,font='arial 10',bg="#282829",fg='#fff')
day7.place(x=54,y=10)
seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=54,y=30)
day7temp=Label(seventhframe,font='arial 10',bg="#282829",fg='#57adff')
day7temp.place(x=24,y=160)
day7weather=Label(seventhframe,font='arial 10',bg="#282829",fg='#57adff')
day7weather.place(x=24,y=140)


root.mainloop()

