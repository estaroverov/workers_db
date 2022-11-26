import streamlit as st
def print_all_data(data):
    if data == None:
        st.text("No such file!")
        return None
    if len(data) > 0:
        print_data(data)
    else:
        st.text("База пуста!")

def print_data(data):
    st.text("Фамилия".center(20)+ "Имя".center(20)+"Отчество".center(20)+ "Дата рождения".center(20)+ "Телефон".center(15)+ "Должность".center(30))
    st.text("-"*130)
    for item in data:
        st.text(item[0].center(20)+ item[1].center(20)+ item[2].center(20)+ item[3].center(20)+ item[4].center(15)+ item[5].center(30))

def print_found_rows(found):
    if found == None:
        st.text("No such file!")
        return None
    if found != None or found != []:
        print_data(found)
    else:
        st.text("Данные не обнаружены")


