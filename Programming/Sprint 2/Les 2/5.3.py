def lang_genoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de attractie!"
    else:
        return "Sorry, je bent te klein!"

user_length = int(input("Hoelang ben je in cm?: "))
print(lang_genoeg(user_length))