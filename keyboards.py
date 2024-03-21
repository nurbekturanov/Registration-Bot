from data import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
import math

def send_contact():
    keyboard = [[KeyboardButton('Send Contact', request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)

def generate_region_keyboard():
    button = []
    for i in range(0, len(REGIONS), 2):
        k_button = REGIONS[i : i + 2]
        button.append(k_button)
    return button


def generate_region_inline_keyboard():
    button = []
    for i in range(0, len(REGIONS), 2):
        k_button = REGIONS[i : i + 2]
        if len(k_button) == 2:
            i_b = [
                InlineKeyboardButton(f"{k_button[0]}", callback_data=f"{k_button[0]}"),
                InlineKeyboardButton(f"{k_button[1]}", callback_data=f"{k_button[1]}"),
            ]
        else:
            i_b = [
                InlineKeyboardButton(f"{k_button[0]}", callback_data=f"{k_button[0]}")
            ]

        button.append(i_b)
    return button


def lang_array(context, current_p):

    arr = []
    start_index = (current_p - 1) * LANGUAGES_PER_PAGE
    end_index = min(start_index + LANGUAGES_PER_PAGE, len(leng_list))

    for i, lang in enumerate(leng_list[start_index:end_index]):
        key = lang[0]
        value = lang[1]
        if (
            key is not None
            and "languages" in context.user_data
            and key in context.user_data["languages"]
        ):
            arr.append(
                [
                    InlineKeyboardButton(
                        f"✅ {value}", callback_data=f"for|{key}|{current_p}"
                    )
                ]
            )
        else:
            arr.append(
                [InlineKeyboardButton(value, callback_data=f"for|{key}|{current_p}")]
            )
    return arr


def generate_language_keyboard(
    context: ContextTypes.DEFAULT_TYPE, key=None, current_p=None
):
    keyboard = []
    if current_p is None:
        current_p = 1
    prev_p = current_p - 1
    next_p = current_p + 1
    current_p = int((prev_p + next_p) / 2)

    langs = lang_array(context, current_p)

    for row in langs:
        temp = []
        for user in row:
            temp.append(user)
        keyboard.append(temp)

    page_count = math.ceil(len(leng_list)/LANGUAGES_PER_PAGE)
    visible_pages = 5
    visible_pages = min(visible_pages, page_count)
    pagination_buttons = []
    if page_count > 1:
        if current_p + 2 <= page_count:
            start_page = max(1, current_p - math.ceil((visible_pages-1) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)
        elif current_p + 1 == page_count:
            start_page = max(1, current_p - math.ceil((visible_pages) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)
        else:
            start_page = max(1, current_p - math.ceil((visible_pages+2) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)

        for i in range(start_page, end_page +1):
            button_text = str(i)
            callback_data = f'lang|{i}'

            if i == current_p:
                button = InlineKeyboardButton(f"*{button_text}*", callback_data=callback_data)
            else:
                button = InlineKeyboardButton(button_text, callback_data=callback_data)
            pagination_buttons.append(button)
        keyboard.append(pagination_buttons)

    k = [
        InlineKeyboardButton("⬅️", callback_data=f"lang|{prev_p}"),
        InlineKeyboardButton("✔️Done", callback_data="Done"),
        InlineKeyboardButton("➡️", callback_data=f"lang|{next_p}"),
    ]
    keyboard.append(k)
    return InlineKeyboardMarkup(keyboard)


def user_array(current_p):
    arr = []
    start_index = (current_p - 1) * USERS_PER_PAGE
    end_index = min(start_index + USERS_PER_PAGE, len(REGISTERED_USERS))

    for i, user in enumerate(REGISTERED_USERS[start_index:end_index]):
        arr.append(
            [
                InlineKeyboardButton(
                    f'{user['id']}. {user["full_name"]}', callback_data=f"info|{user['id']}|{current_p}"
                )
            ]
        )
    return arr

def generate_user_keyboard(current_p):
    if current_p is None:
        current_p = 1
    prev_p = current_p - 1
    next_p = current_p + 1
    current_p = int((prev_p+next_p)/2)

    data = user_array(current_p)
    keyboard = []
    for row in data:
        temp = []
        for user in row:
            temp.append(user)
        keyboard.append(temp)

    page_count = math.ceil(len(REGISTERED_USERS)/USERS_PER_PAGE)
    visible_pages = 5
    visible_pages = min(visible_pages, page_count)
    pagination_buttons = []
    if page_count > 1:
        if current_p + 2 <= page_count:
            start_page = max(1, current_p - math.ceil((visible_pages-1) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)
        elif current_p + 1 == page_count:
            start_page = max(1, current_p - math.ceil((visible_pages) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)
        else:
            start_page = max(1, current_p - math.ceil((visible_pages+2) / 2))
            end_page = min(page_count, start_page + visible_pages - 1)

        for i in range(start_page, end_page +1):
            button_text = str(i)
            callback_data = f'users|{i}'

            if i == current_p:
                button = InlineKeyboardButton(f"*{button_text}*", callback_data=callback_data)
            else:
                button = InlineKeyboardButton(button_text, callback_data=callback_data)
            pagination_buttons.append(button)
        keyboard.append(pagination_buttons)

    k = [
            InlineKeyboardButton('⬅️', callback_data=f'users|{prev_p}'),
            InlineKeyboardButton('❌', callback_data=f'cross'),
            InlineKeyboardButton('➡️', callback_data=f'users|{next_p}')
        ]
    
    keyboard.append(k)
    return InlineKeyboardMarkup(keyboard)
