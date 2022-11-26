from import_data import import_data
from export_data import export_data
from print_data import *
from search_data import *
import streamlit as st


def greeting():
    st.write("Добро пожаловать в базу данных сотрудников!")


def input_data():
    last_name = st.text_input("Введите фамилию: ")
    first_name = st.text_input("Введите имя: ")
    middle_name = st.text_input("Введите отчество: ")
    brith_name = st.text_input("Введите дату рождения: ")
    phone_number = st.text_input("Введите номер сотрудника: ")
    note = st.text_input("Введите должность: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def choice_sep():
    sep = st.text_input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep


def choice_todo():
    st.text("Доступные операции с базой данных:\n")
    ch = st.radio("Выберите", ('Добавить сотрудника',
                  'Показать всех сотрудников', 'Поиск сотрудника', 'Поиск сотрудника по столбцу'))
    if ch:
        filename = st.text_input("Введите имя файла: ", "phone.csv")
    if ch == 'Добавить сотрудника':
        sep = choice_sep()
        input_row = input_data()
        accept = st.button("Отправить")
        if accept:
            import_data(input_row, filename, sep)
    elif ch == 'Показать всех сотрудников':
        accept = st.button("Отправить")
        if accept:
            data = export_data(filename)
            print_all_data(data)
    elif ch == 'Поиск сотрудника':
        word = st.text_input("Введите данные для поиска: ")
        search = st.button('Поиск')
        if search:
            data = export_data(filename)
            item = search_data(word, data)
            print_found_rows(item)
    elif ch == 'Поиск сотрудника по столбцу':
        word = st.text_input("Введите данные для поиска: ")
        column = st.text_input("Введите номер столбца: ")
        search = st.button('Поиск')
        if search:
            data = export_data(filename)
            item = search_val(word, data, column)
            print_found_rows(item)
