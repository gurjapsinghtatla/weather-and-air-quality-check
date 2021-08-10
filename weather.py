import json
import requests


def conversion_to_coordinates(state):
    file = open("indian_states", 'r')
    data = file.readlines()
    length = len(data)
    index=0
    target_state = None
    while index < length :
        if state in data[index]:
            target_state=data[index]
            print(target_state)
            break
        else:
            index+=1
    if target_state == None:
        print("not found")
        return
    new_target_state = target_state.split(" ")
    use_key={
        'city':new_target_state[0],
        'latitude' : new_target_state[2] ,
        'longitude' : new_target_state[3] ,
        'api_key' : "0f42410c8cd84d2d9b9006afabf52e11"}


    choices(use_key=use_key)
    air_quality(use_key=use_key)
    weather(use_key=use_key)

def choices(use_key):
    decesion=int(input("ENTER [1] TO CHECK AIR QUALITY \nENTER [2] TO CHECK WEATHER FORECAST \nENTER [3] TO CHECK BOTH\n  "))
    if decesion==1:
        air_quality(use_key=use_key)
    elif decesion==2:
        weather(use_key=use_key)
    elif decesion == 3:
        air_quality(use_key=use_key)
        weather(use_key=use_key)
    else:
        print("enter a valid choice")
        choices(use_key)


def air_quality(use_key):

    url = "https://api.weatherbit.io/v2.0/current/airquality?lat={latitude}&lon={longitude}&key={api_key}".format_map(use_key)

    print(url)
    response = requests.get(url)
    data = json.loads(response.text)
    print("_"*100)
    print("AIR QUALITY CHECK")

    state_data={
       'air_quality': data['data'][0]['aqi'],
        'small_particles': data['data'][0]['pm10'],
        'Ozone': data['data'][0]['o3'],
        'Sulphur dioxide ':data['data'][0]['so2'],
        'Nitrogen dioxide ': data['data'][0]['no2'],
        'Carbon Monoxide ': data['data'][0]['co'],

    }
    print(state_data)

def weather(use_key):
    url="https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key={api_key}".format_map(use_key)
    response=requests.get(url)
    data = json.loads(response.text)
    print("WEATHER CHECK")


    state_data = {
        'Highest temperature': data['data'][0]['high_temp'],
        'Highest feels like': data['data'][0]['app_max_temp'],

        'Lowest temperature': data['data'][0]['min_temp'],
        'Lowest feels like': data['data'][0]['app_min_temp'],

        'Average temperature': data['data'][0]['temp'],

        'Total Rainfall': data['data'][0]['precip'],
        'Probabilty of rainfall in future': data['data'][0]['pop'] ,
        'Cloud Coverage': data['data'][0]['clouds'],
        'Visibilty': data['data'][0]['vis'],

        'Realtive Humidity': data['data'][0]['rh'],

        'Wind speed': data['data'][0]['wind_spd'],
        'Wind Direction': data['data'][0]['wind_dir'],

    }
    print(state_data)



def main():
    state=input("enter your state")
    conversion_to_coordinates(state=state)


if __name__ == '__main__':
    main()



