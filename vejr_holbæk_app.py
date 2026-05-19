import requests, ttkbootstrap
from datetime import datetime, timedelta

# Henter data fra Open-Meteo API for Holbæk, Danmark
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.7175&longitude=11.717578&hourly=temperature_2m,wind_speed_10m,visibility,rain,precipitation&wind_speed_unit=ms&models=dmi_harmonie_arome_europe")

# Konverterer API responsen til JSON format
data = response.json()

# Henter for de forskellige tidspunker og enheder
hourly = data["hourly"]
units = data["hourly_units"]

# Den nuværende tid, som er sat til hele timer, og konverteret til en integer for at kunne bruges.
now = int(datetime.now().strftime("%H"))

# Opsætter et GUI vindue ved hjælp af ttkbootstrap
root = ttkbootstrap.Window(title="Vejr i Holbæk")

# Den nuværrende tid + bruger format strings
current_time = ttkbootstrap.Label(root, text=f"Klokken er nu: {datetime.now().strftime('%H:%M, %d-%m-%Y')} i Holbæk", bootstyle="inverse-success")
current_time.grid(row=0, column=0, padx=10, pady=10)

line = ttkbootstrap.Separator()
line.grid(row=1, column=0, padx=10, pady=10)

# Tilføjet nootbook til intiaktivitet.
notebook = ttkbootstrap.Notebook(root)
notebook.grid(row=2, column=0)

# Tilføjer tabs
tab1 = ttkbootstrap.Frame(notebook)
tab2 = ttkbootstrap.Frame(notebook)
tab3 = ttkbootstrap.Frame(notebook)

# Tekst box til vejret og vindhastighed lige nu
# Border
you_frame = ttkbootstrap.Frame(tab1 ,bootstyle="default", borderwidth=5, relief="solid")
you_frame.grid(row=2, column=0, padx=10, pady=10)

current_weather = ttkbootstrap.Label(you_frame, text="Vejret på nuværrende tidspunkt: ", bootstyle="inverse-default")
current_weather.grid(row=2, column=0)

temp = ttkbootstrap.Label(you_frame, text=f"Temperatur: {hourly['temperature_2m'][now]} {units['temperature_2m']}")
temp.grid(row=3, column=0, padx=5, pady=5)

wind = ttkbootstrap.Label(you_frame, text=f"Vindhastighed: {hourly['wind_speed_10m'][now]} {units['wind_speed_10m']}")
wind.grid(row=4, column=0, padx=5, pady=5)

# Vejret dagen efter den nuværrende dag, hvor der er brugt max og min, og slicing til at få de forskellige temperature.
die_frame=ttkbootstrap.Frame(tab1, bootstyle="default",borderwidth=5, relief="solid")
die_frame.grid(row=2, column=1, padx=10, pady=10)

current_wind = ttkbootstrap.Label(die_frame, text="Vejret om et døgn: ", bootstyle="inverse-default")
current_wind.grid(row=2, column=1)

temp_tomorrow = ttkbootstrap.Label(die_frame, text=f"Temp -> Max: {max(hourly['temperature_2m'][24:49])} {units['temperature_2m']} | Min: {min(hourly['temperature_2m'][24:49])} {units['temperature_2m']}")
temp_tomorrow.grid(row=3, column=1, padx=5, pady=5)

wind_tomorrow = ttkbootstrap.Label(die_frame, text=f"Vind -> Max: {max(hourly['wind_speed_10m'][24:49])} {units['wind_speed_10m']} | Min: {min(hourly['wind_speed_10m'][24:49])} {units['wind_speed_10m']}")
wind_tomorrow.grid(row=4, column=1, padx=5, pady=5)

# Tilføjer, tekst box til fremtidigt vejr
I_frame=ttkbootstrap.Frame(tab1, bootstyle="default", borderwidth=5, relief="solid")
I_frame.grid(row=5, columnspan=2, padx=10, pady=10)

future_weather = ttkbootstrap.Label(I_frame, text="Vejret i dag og 12 timer frem: ", bootstyle="inverse-default")
future_weather.grid(row=5, column=0, padx=10, pady=10)

# Max & min temp og vind i dag
temp_today = ttkbootstrap.Label(I_frame, text=f"Temp -> Max: {max(hourly['temperature_2m'][0:25])} {units['temperature_2m']} | Min: {min(hourly['temperature_2m'][0:25])} {units['temperature_2m']}")
temp_today.grid(row=6, column=0, padx=1, pady=1)

wind_today = ttkbootstrap.Label(I_frame, text=f"Vind -> Max: {max(hourly['wind_speed_10m'][0:25])} {units['wind_speed_10m']} | Min: {min(hourly['wind_speed_10m'][0:25])} {units['wind_speed_10m']}")
wind_today.grid(row=7, column=0, padx=1, pady=1)

# Vejret 12 timer fremad
future_1 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=1)).strftime('%H:%M')}: {hourly['temperature_2m'][now+1]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=7)).strftime('%H:%M')}: {hourly['temperature_2m'][now+7]} {units['temperature_2m']}")
future_1.grid(row=6, column=1, padx=1, pady=1)

future_2 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=2)).strftime('%H:%M')}: {hourly['temperature_2m'][now+2]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=8)).strftime('%H:%M')}: {hourly['temperature_2m'][now+8]} {units['temperature_2m']}")
future_2.grid(row=7, column=1, padx=1, pady=1)

future_3 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=3)).strftime('%H:%M')}: {hourly['temperature_2m'][now+3]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=9)).strftime('%H:%M')}: {hourly['temperature_2m'][now+9]} {units['temperature_2m']}")
future_3.grid(row=8, column=1, padx=1, pady=1)

future_4 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=4)).strftime('%H:%M')}: {hourly['temperature_2m'][now+4]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=10)).strftime('%H:%M')}: {hourly['temperature_2m'][now+10]} {units['temperature_2m']}")
future_4.grid(row=9, column=1, padx=1, pady=1)

future_5 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=5)).strftime('%H:%M')}: {hourly['temperature_2m'][now+5]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=11)).strftime('%H:%M')}: {hourly['temperature_2m'][now+11]} {units['temperature_2m']}")
future_5.grid(row=10, column=1, padx=1, pady=1)

future_6 = ttkbootstrap.Label(I_frame, text=f"{(datetime.now() + timedelta(hours=6)).strftime('%H:%M')}: {hourly['temperature_2m'][now+6]} {units['temperature_2m']}\t{(datetime.now() + timedelta(hours=12)).strftime('%H:%M')}: {hourly['temperature_2m'][now+12]} {units['temperature_2m']}")
future_6.grid(row=11, column=1, padx=1, pady=1)

# Tab2 med regn-information
# Regn lige nu
regnnu_frame = ttkbootstrap.Frame(tab2, bootstyle="default", borderwidth=5, relief="solid")
regnnu_frame.grid(row=2, column=0, padx=10, pady=10)

current_rain = ttkbootstrap.Label(regnnu_frame, text="Regn på nuværrende tidspunkt: ", bootstyle="inverse-default")
current_rain.grid(row=2, column=0)

rain = ttkbootstrap.Label(regnnu_frame, text=f"Regn: {hourly['rain'][now]} {units['rain']}")
rain.grid(row=3, column=0, padx=5, pady=10)

# Tab 2 -> Regn indenfor de næste 2 døgn
regnto_frame = ttkbootstrap.Frame(tab2, bootstyle="default", borderwidth=5, relief="solid")
regnto_frame.grid(row=2, column=1, padx=10, pady=10)

twoday_rain = ttkbootstrap.Label(regnto_frame, text="Regn næste 2 døgn?", bootstyle="inverse-default")
twoday_rain.grid(row=3, column=1)

regnudsigt2døgn = max(hourly['rain'][0:49])

if regnudsigt2døgn == 0:
    nejtilregn = ttkbootstrap.Label(regnto_frame, text="Ingen regn forkommer indenfor \nde næste 2 døgn.")
    nejtilregn.grid(row=4, column=1)
else:
    jatilregn = ttkbootstrap.Label(regnto_frame, text="Det VIL regne indenfor de næste 2 døgn, \nkig på skemaet under for mere information")
    jatilregn.grid(row=4, column=1)

# Tab 2 -> Liste over regn de næste 2 døgn
liste1frame = ttkbootstrap.Frame(tab2, bootstyle="default", borderwidth=5, relief="solid")
liste1frame.grid(row=4, column=0, padx=10, pady=10)

overskriftliste1 = ttkbootstrap.Label(liste1frame, text="Nuværende døgn:", bootstyle="inverse-default")
overskriftliste1.grid(row=4, column=0)

regn_1 = ttkbootstrap.Label(liste1frame, text=f"00:00: {hourly['rain'][0]} {units['rain']}\t13:00: {hourly['rain'][now+13]} {units['rain']}")
regn_1.grid(row=5, column=0, padx=1, pady=1)

regn_2 = ttkbootstrap.Label(liste1frame, text=f"01:00: {hourly['rain'][1]} {units['rain']}\t14:00: {hourly['rain'][now+14]} {units['rain']}")
regn_2.grid(row=6, column=0, padx=1, pady=1)

regn_3 = ttkbootstrap.Label(liste1frame, text=f"02:00: {hourly['rain'][2]} {units['rain']}\t15:00: {hourly['rain'][now+15]} {units['rain']}")
regn_3.grid(row=7, column=0, padx=1, pady=1)

regn_4 = ttkbootstrap.Label(liste1frame, text=f"03:00: {hourly['rain'][3]} {units['rain']}\t16:00: {hourly['rain'][now+16]} {units['rain']}")
regn_4.grid(row=8, column=0, padx=1, pady=1)

regn_5 = ttkbootstrap.Label(liste1frame, text=f"04:00: {hourly['rain'][4]} {units['rain']}\t17:00: {hourly['rain'][now+17]} {units['rain']}")
regn_5.grid(row=9, column=0, padx=1, pady=1)

regn_6 = ttkbootstrap.Label(liste1frame, text=f"05:00: {hourly['rain'][5]} {units['rain']}\t18:00: {hourly['rain'][now+18]} {units['rain']}")
regn_6.grid(row=10, column=0, padx=1, pady=1)

regn_7 = ttkbootstrap.Label(liste1frame, text=f"06:00: {hourly['rain'][6]} {units['rain']}\t19:00: {hourly['rain'][now+19]} {units['rain']}")
regn_7.grid(row=11, column=0, padx=1, pady=1)

regn_8 = ttkbootstrap.Label(liste1frame, text=f"07:00: {hourly['rain'][7]} {units['rain']}\t20:00: {hourly['rain'][now+20]} {units['rain']}")
regn_8.grid(row=12, column=0, padx=1, pady=1)

regn_9 = ttkbootstrap.Label(liste1frame, text=f"08:00: {hourly['rain'][8]} {units['rain']}\t21:00: {hourly['rain'][now+21]} {units['rain']}")
regn_9.grid(row=13, column=0, padx=1, pady=1)

regn_10 = ttkbootstrap.Label(liste1frame, text=f"09:00: {hourly['rain'][9]} {units['rain']}\t22:00: {hourly['rain'][now+22]} {units['rain']}")
regn_10.grid(row=14, column=0, padx=1, pady=1)

regn_11 = ttkbootstrap.Label(liste1frame, text=f"10:00: {hourly['rain'][10]} {units['rain']}\t23:00: {hourly['rain'][now+23]} {units['rain']}")
regn_11.grid(row=15, column=0, padx=1, pady=1)

regn_12 = ttkbootstrap.Label(liste1frame, text=f"11:00: {hourly['rain'][11]} {units['rain']}\t24:00: {hourly['rain'][now+24]} {units['rain']}")
regn_12.grid(row=16, column=0, padx=1, pady=1)

regn_13 = ttkbootstrap.Label(liste1frame, text=f"12:00: {hourly['rain'][12]} {units['rain']}")
regn_13.grid(row=17, column=0, padx=1, pady=1, sticky="nw")

liste2frame = ttkbootstrap.Frame(tab2, bootstyle="default", borderwidth=5, relief="solid")
liste2frame.grid(row=4, column=1, padx=10, pady=10)

overskriftliste1 = ttkbootstrap.Label(liste2frame, text="Kommende døgn:", bootstyle="inverse-default")
overskriftliste1.grid(row=4, column=1)

regn_1 = ttkbootstrap.Label(liste2frame, text=f"00:00: {hourly['rain'][25]} {units['rain']}\t13:00: {hourly['rain'][now+38]} {units['rain']}")
regn_1.grid(row=5, column=1, padx=1, pady=1)

regn_2 = ttkbootstrap.Label(liste2frame, text=f"01:00: {hourly['rain'][26]} {units['rain']}\t14:00: {hourly['rain'][now+39]} {units['rain']}")
regn_2.grid(row=6, column=1, padx=1, pady=1)

regn_3 = ttkbootstrap.Label(liste2frame, text=f"02:00: {hourly['rain'][27]} {units['rain']}\t15:00: {hourly['rain'][now+40]} {units['rain']}")
regn_3.grid(row=7, column=1, padx=1, pady=1)

regn_4 = ttkbootstrap.Label(liste2frame, text=f"03:00: {hourly['rain'][28]} {units['rain']}\t16:00: {hourly['rain'][now+41]} {units['rain']}")
regn_4.grid(row=8, column=1, padx=1, pady=1)

regn_5 = ttkbootstrap.Label(liste2frame, text=f"04:00: {hourly['rain'][29]} {units['rain']}\t17:00: {hourly['rain'][now+42]} {units['rain']}")
regn_5.grid(row=9, column=1, padx=1, pady=1)

regn_6 = ttkbootstrap.Label(liste2frame, text=f"05:00: {hourly['rain'][30]} {units['rain']}\t18:00: {hourly['rain'][now+43]} {units['rain']}")
regn_6.grid(row=10, column=1, padx=1, pady=1)

regn_7 = ttkbootstrap.Label(liste2frame, text=f"06:00: {hourly['rain'][31]} {units['rain']}\t19:00: {hourly['rain'][now+44]} {units['rain']}")
regn_7.grid(row=11, column=1, padx=1, pady=1)

regn_8 = ttkbootstrap.Label(liste2frame, text=f"07:00: {hourly['rain'][32]} {units['rain']}\t20:00: {hourly['rain'][now+45]} {units['rain']}")
regn_8.grid(row=12, column=1, padx=1, pady=1)

regn_9 = ttkbootstrap.Label(liste2frame, text=f"08:00: {hourly['rain'][33]} {units['rain']}\t21:00: {hourly['rain'][now+46]} {units['rain']}")
regn_9.grid(row=13, column=1, padx=1, pady=1)

regn_10 = ttkbootstrap.Label(liste2frame, text=f"09:00: {hourly['rain'][34]} {units['rain']}\t22:00: {hourly['rain'][now+47]} {units['rain']}")
regn_10.grid(row=14, column=1, padx=1, pady=1)

regn_11 = ttkbootstrap.Label(liste2frame, text=f"10:00: {hourly['rain'][35]} {units['rain']}\t23:00: {hourly['rain'][now+48]} {units['rain']}")
regn_11.grid(row=15, column=1, padx=1, pady=1)

regn_12 = ttkbootstrap.Label(liste2frame, text=f"11:00: {hourly['rain'][36]} {units['rain']}\t24:00: {hourly['rain'][now+49]} {units['rain']}")
regn_12.grid(row=16, column=1, padx=1, pady=1)

regn_13 = ttkbootstrap.Label(liste2frame, text=f"12:00: {hourly['rain'][37]} {units['rain']}")
regn_13.grid(row=17, column=1, padx=1, pady=1, sticky="nw")

# Tab3 med ekstra information omkring Holbæk
lokalinformation = ttkbootstrap.Label(tab3, text="Områdebeskrivelse", bootstyle="inverse-default")
lokalinformation.grid(row=2, column=0, padx=10, pady=10)

latitude = ttkbootstrap.Label(tab3, text=f"Latitude: {data['latitude']}")
latitude.grid(row=3, column=0, padx=5, pady=5, sticky="nw")

longitude = ttkbootstrap.Label(tab3, text=f"Longitude: {data['longitude']}")
longitude.grid(row=4, column=0, padx=5, pady=5, sticky="nw")

elevation = ttkbootstrap.Label(tab3, text="Elevation: 11 m")
elevation.grid(row=5, column=0, padx=5, pady=5, sticky="nw")


# Tilføjer frames til vores notebook
notebook.add(tab1, text="Vejr")
notebook.add(tab2, text="Regn")
notebook.add(tab3, text="Lokalinformation")

root.mainloop()