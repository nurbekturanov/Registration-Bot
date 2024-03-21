NAME, SURNAME, AGE, PHONE_NUMBER, REGION, LANGUAGE = range(6)

USERS_PER_PAGE = 10
MAX_BUTTONS_PER_PAGE = 5
LANGUAGES_PER_PAGE = 3

REGIONS = [
    "Toshkent",
    "Sirdaryo",
    "Namangan",
    "Termiz",
    "Farg'ona",
    "Andijon",
    "Surxandaryo",
    "Jizzah",
    "Navoiy",
    "Qashqadaryo",
    "Buxoro",
    "Samarqand",
    "Qoraqalpog'iston",
]

LANGUAGES = {
    "english": "Ingliz tili",
    "russian": "Rus tili",
    "german": "Nemis tili",
    "turkish": "Turk tili",
    "korean": "Karis tili",
    "arabic": "Arab tili",
    "hindi": "Hind tili",
    "japan": "Yapon tili",
    "kazak": "Qozoq tili",
    "tajik": "Tojik tili",
    "eron": "Eron tili",
    "china": "Xitoy tili",
    "norway": "Norveg tili",
    "brazil": "Brazil tili",
    "mongol": "Mongol tili",
    "spain": "Ispan tili",
    "french": "Fransuz tili",
    "italian": "Italian tili",
    "sweden": "Shvetsaria tili",
}

leng_list = []
for key, value in LANGUAGES.items():
    leng_list.append([key, value])

REGISTERED_USERS = [
    {
        "id": 1,
        "full_name": "Olim Bek",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Ingliz",
    },
    {
        "id": 2,
        "full_name": "Jasur Misandifov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Ingliz, Turk",
    },
    {
        "id": 3,
        "full_name": "Shox Ble",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Xorazm",
        "selected_languages_str": "Ingliz, Turk, Arab",
    },
    {
        "id": 4,
        "full_name": "Bek Jon",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 5,
        "full_name": "Anvar Narz",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 6,
        "full_name": "Salim Boy",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 7,
        "full_name": "O'tkir Ergashev",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 8,
        "full_name": "Jeck Lee",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 9,
        "full_name": "Laylo Mahkamova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 10,
        "full_name": "Malika Karimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 11,
        "full_name": "Axror Murodov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 12,
        "full_name": "Shahzod Suvonqulov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Ingliz",
    },
    {
        "id": 13,
        "full_name": "Dilshod Abdullayev",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Ingliz, Turk",
    },
    {
        "id": 14,
        "full_name": "Javlon Pirimqulov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Xorazm",
        "selected_languages_str": "Ingliz, Turk, Arab",
    },
    {
        "id": 15,
        "full_name": "Islom Mo'minov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 16,
        "full_name": "Rasul Karimov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 17,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 18,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 19,
        "region": "Tashkent",
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 20,
        "region": "Tashkent",
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 21,
        "region": "Tashkent",
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 22,
        "region": "Tashkent",
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 23,
        "region": "Tashkent",
        "full_name": "Olim Bek",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Ingliz",
    },
    {
        "id": 24,
        "region": "Jizzakh",
        "full_name": "Jasur Misandifov",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Ingliz, Turk",
    },
    {
        "id": 25,
        "region": "Xorazm",
        "full_name": "Shox Ble",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Ingliz, Turk, Arab",
    },
    {
        "id": 26,
        "region": "Fergana",
        "full_name": "Bek Jon",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 27,
        "region": "Tashkent",
        "full_name": "Anvar Narz",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 28,
        "region": "Jizzakh",
        "full_name": "Salim Boy",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 29,
        "region": "Jizzakh",
        "full_name": "O'tkir Ergashev",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 30,
        "region": "Fergana",
        "full_name": "Jeck Lee",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 31,
        "region": "Fergana",
        "full_name": "Laylo Mahkamova",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 32,
        "region": "Fergana",
        "full_name": "Malika Karimova",
        "age": 26,
        "phone_number": "+998901234567",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 33,
        "full_name": "Axror Murodov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 34,
        "full_name": "Shahzod Suvonqulov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Ingliz",
    },
    {
        "id": 35,
        "full_name": "Dilshod Abdullayev",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Ingliz, Turk",
    },
    {
        "id": 36,
        "full_name": "Javlon Pirimqulov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Xorazm",
        "selected_languages_str": "Ingliz, Turk, Arab",
    },
    {
        "id": 37,
        "full_name": "Islom Mo'minov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 38,
        "full_name": "Rasul Karimov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 39,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 40,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 41,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 42,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 43,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 44,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 45,
        "full_name": "Islom Mo'minov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 46,
        "full_name": "Rasul Karimov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 47,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 48,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 49,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 50,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 51,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 52,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 53,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 54,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 55,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 56,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 57,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 58,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 59,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 60,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 61,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 62,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 63,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 64,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 65,
        "full_name": "Islom Mo'minov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Fergana",
        "selected_languages_str": "Ingliz, Turk, Arab, Rus",
    },
    {
        "id": 66,
        "full_name": "Rasul Karimov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Turk, Arab, Rus",
    },
    {
        "id": 67,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 68,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 69,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 70,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 71,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 72,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 73,
        "full_name": "Ahmad Faruhov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus",
    },
    {
        "id": 74,
        "full_name": "Donyor Odilov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Jizzakh",
        "selected_languages_str": "Arab, Rus, Turk",
    },
    {
        "id": 75,
        "full_name": "Aziz Aminov",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Turk, Ingliz",
    },
    {
        "id": 76,
        "full_name": "Shahlo Ahmedova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
    {
        "id": 77,
        "full_name": "Sevinch Mo'minova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz, Turk",
    },
    {
        "id": 78,
        "full_name": "Sevara Azimova",
        "age": 26,
        "phone_number": "+998901234567",
        "region": "Tashkent",
        "selected_languages_str": "Arab, Rus, Ingliz",
    },
]
