import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from windows import set_dpi_awareness
from math import *
from datetime import *
set_dpi_awareness()


class main_frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Age Calculator')
        self.geometry('600x800');
        self.zodiac_signs = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio',
                             'Sagittarius','Capricorn','Aquaris','Pisces']
        self.personality_traits = ['Bold and ambitious, Aries dives headfirst into even the most challenging situations.',
                                   'Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors.',
                                   'Have you ever been so busy that you wished you could clone yourself just to get everything done? That’s the Gemini experience in a nutshell. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself.',
                                   'Cancer is a cardinal water sign. Represented by the crab, this crustacean seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces: For instance, Cancers can effortlessly pick up the energies in a room',
                                   'Roll out the red carpet because Leo has arrived. Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They’re delighted to embrace their royal status: Vivacious, theatrical, and passionate, Leos love to bask in the spotlight and celebrate themselves.',
                                   'Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo’s deep-rooted presence in the material world. Virgos are logical, practical, and systematic in their approach to life. This earth sign is a perfectionist at heart and isn’t afraid to improve skills through diligent and consistent practice.',
                                   'Libra is an air sign represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libras fixation on balance and harmony. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life.',
                                   'Scorpio is one of the most misunderstood signs of the zodiac. Because of its incredible passion and power, Scorpio is often mistaken for a fire sign. In fact, Scorpio is a water sign that derives its strength from the psychic, emotional realm.',
                                   'Represented by the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual adventures.',
                                   'The last earth sign of the zodiac, Capricorn is represented by the sea goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.',
                                   'Despite the “aqua” in its name, Aquarius is actually the last air sign of the zodiac. Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign.',
                                   'Pisces, a water sign, is the last constellation of the zodiac. Its symbolized by two fish swimming in opposite directions, representing the constant division of Pisces attention between fantasy and reality. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs.']
        self.days_list = []
        self.months_list = []
        self.hours_list = []
        self.years_list = []

        for i in range (1,32):
            self.days_list.append(i)
        for i in range(0,24):
            self.hours_list.append(i)
        for i in range(1900,2022):
            self.years_list.append(i)
        for month in ['January','February','March','April',
                      'May','June','July','August','September','October',
                      'November','December']:
            self.months_list.append(month)

        self.age = tk.StringVar()
        self.zodiacSign = tk.StringVar()
        self.Personality = tk.StringVar()
        self.name = tk.StringVar()
        self.year = tk.IntVar()
        self.day = tk.IntVar()
        self.month = tk.StringVar()
        self.hour = tk.IntVar()

        label_name = ttk.Label(self,text='Name')
        entry_name = ttk.Entry(self,textvariable=self.name)
        label_year = ttk.Label(self,text='Year')
        label_month = ttk.Label(self,text='Month')
        label_day = ttk.Label(self,text='Day')
        label_hour = ttk.Label(self,text='Hour')
        combo_year=ttk.Combobox(self,values=self.years_list,textvariable=self.year)
        combo_month=ttk.Combobox(self,values=self.months_list,textvariable=self.month)
        combo_day=ttk.Combobox(self,values=self.days_list,textvariable=self.day)
        combo_hour=ttk.Combobox(self,values=self.hours_list,textvariable=self.hour)
        combo_year.set(self.years_list[-1])
        combo_month.set(self.months_list[0])
        combo_day.set(self.days_list[0])
        combo_hour.set(self.hours_list[0])

        label_name.grid(row=1,column=0,padx=(30,0),pady=(30,30))
        entry_name.grid(row=1,column=1,padx=(0,30),pady=(30,30),ipadx=20,ipady=10)
        label_year.grid(row=2, column=0, padx=(30, 0), pady=(0, 30))
        combo_year.grid(row=2,column=1,padx=(0,30),pady=(0,30))
        label_month.grid(row=3, column=0, padx=(30, 0), pady=(0, 30))
        combo_month.grid(row=3,column=1,padx=(0,30),pady=(0,30))
        label_day.grid(row=4, column=0, padx=(30, 0), pady=(0, 30))
        combo_day.grid(row=4,column=1,padx=(0,30),pady=(0,30))
        label_hour.grid(row=5, column=0, padx=(30, 0), pady=(0, 30))
        combo_hour.grid(row=5,column=1,padx=(0,30),pady=(0,30))
        submit = ttk.Button(self,text='Calculate',command=self.calculate_fn)
        submit.grid(row=6,column=0,columnspan=2,padx=(100,0),pady=(10,30))
        label_age = ttk.Label(self,text='Your age:')
        label_zodiac = ttk.Label(self,text='Your Zodiac sign')
        label_personality = ttk.Label(self,text='Personality')
        label_age.grid(row=7,column=0,padx=(30,0),pady=(10,30))
        label_zodiac.grid(row=8, column=0, padx=(60, 0), pady=(10, 30))
        label_personality.grid(row=9, column=0, padx=(30, 0), pady=(10, 30))
        zodiac_output=ttk.Entry(self,textvariable=self.zodiacSign)
        age_output=ttk.Label(self,textvariable=self.age,wraplength=250)
        personality_output=ttk.Label(self,textvariable=self.Personality,wraplength=250)
        age_output.grid(row=7,column=1,padx=(0,30),pady=(10,30),ipadx=20,ipady=10)
        zodiac_output.grid(row=8,column=1,padx=(0,30),pady=(10,30),ipadx=20,ipady=10)
        personality_output.grid(row=9,column=1,padx=(0,30),pady=(10,30),ipadx=40,ipady=10)
        self.bind('<Return>', self.calculate_fn)




    def calculate_fn(self,*args):
        name = self.name.get()
        year = self.year.get()
        month = self.month.get()
        day = self.day.get()
        hour = self.hour.get()

        if name == '':
            self.wrong_input_name()
        else:
            if self.isLeap() == True and month == 'February' and day > 29:
                self.wrong_input_leap()
            elif self.isLeap() == False and month == 'February' and day > 28:
                self.wrong_input_noLeap()
            elif month in ['April','June','September','November'] and day > 30:
                self.wrong_input_excess()

            elif self.year.get() not in self.years_list:
                self.wrong_input_Year()
            elif self.month.get() not in self.months_list:
                self.wrong_input_Month()
            elif self.day.get() not in self.days_list:
                self.wrong_input_Day()
            elif self.hour.get() not in self.hours_list:
                self.wrong_input_Hour()
            else:
                self.calculate_zodiac()
                self.calculate_age()



    def isLeap(self):
        year=self.year.get()
        value=False
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    value=True
                else:
                    value=False
            else:
                value=True
        else:
            value=False
        return value

    def wrong_input_name(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label=ttk.Label(window,text='Enter Name BC!',wraplength=100)
        label.pack()

    def wrong_input_leap(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text=f"Number of days can't exceed 29 for {self.month.get()} for a Leap year",wraplength=100)
        label.pack()

    def wrong_inputnoLeap(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text=f"Number of days can't exceed 28 for {self.month.get()} for a non Leap year",wraplength=100)
        label.pack()

    def wrong_input_excess(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text=f"Number of days can't exceed 30 for {self.month.get()}",wraplength=100)
        label.pack()
    def wrong_input_Year(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text="The year you entered was invaid",wraplength=100)
        label.pack()
    def wrong_input_Month(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text="The month you entered was invaid",wraplength=100)
        label.pack()
    def wrong_input_Day(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text="The day you entered was invaid",wraplength=100)
        label.pack()
    def wrong_input_Hour(self):
        window = tk.Toplevel()
        window.geometry('150x150')
        window.title("Error!")
        label = ttk.Label(window, text="The hour you entered was invaid",wraplength=100)
        label.pack()


    def calculate_zodiac(self):
        month = self.month.get()
        day = self.day.get()
        index=0

        if (month=='March' and day >=21 ) or (month=='April' and day<=19):
            index=0
        elif (month=='April' and day >=20) or (month=='May' and day <=20):
            index=1
        elif (month=='May' and day >=21) or (month=='June' and day <=20):
            index=2
        elif (month=='June' and day >=21) or (month=='July' and day <=22):
            index=3
        elif (month=='July' and day >= 23) or (month=='August' and day <=22):
            index=4
        elif (month=='August'and day >=23) or (month=='September'and day <=22):
            index=5
        elif (month=='September' and day >=23) or (month=='October' and day <= 22):
            index=6
        elif (month=='October' and day >=23) or (month=='November' and day <= 21):
            index=7
        elif (month =='November' and day >= 22) or (month=='December' and day <= 21):
            index=8
        elif (month =='December' and day >= 22) or (month =='January' and day <= 19):
            index=9
        elif (month=='January' and day >=20) or (month=='February' and day <= 18):
            index=10
        elif (month=='February' and day >=19) or (month=='March' and day <= 20):
            index=11

        self.zodiacSign.set(self.zodiac_signs[index])
        self.Personality.set(self.personality_traits[index])



    def calculate_age(self):
        year = self.year.get()
        month = self.month.get()
        month = self.months_list.index(month)+1
        day = self.day.get()
        hour = self.hour.get()
        date = datetime.now()
        curr_year = date.year
        curr_month = date.month
        curr_day = date.day
        curr_hour = date.hour
        year_diff = abs(curr_year-year)
        month_diff= abs(curr_month-month)
        day_diff = abs(curr_day-day)
        hour_diff=abs(curr_hour-hour)
        if month > curr_month:
            year_diff=year_diff-1
            month_diff=12-month_diff

        name=self.name.get()

        result=f'Hey {name} you are: \n {year_diff} Years \n {month_diff} Months \n {day_diff} days \n {hour_diff} hours old'
        self.age.set(result)
        print(result)


root=main_frame()
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("vista"))
root.mainloop()