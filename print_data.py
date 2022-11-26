import streamlit as st
import pandas as pd


def print_all_data(data):
    if data == None:
        st.text("No such file!")
        return None
    if len(data) > 0:
        st.dataframe(print_data(data))
    else:
        st.text("База пуста!")


def print_data(data):
    return pd.DataFrame(
        {
            "Фамилия": [item[0] for item in data],
            "Имя": [item[1] for item in data],
            "Отчество": [item[2] for item in data],
            "Дата рождения": [item[3] for item in data],
            "Телефон": [item[4] for item in data],
            "Должность": [item[5] for item in data]

        })
    #st.text("".center(20)+ "Имя".center(20)+"Отчество".center(20)+ "Дата рождения".center(20)+ "Телефон".center(15)+ "Должность".center(30))
    # st.text("-"*130)
    # for item in data:
    #     st.text(item[0].center(20)+ item[1].center(20)+ item[2].center(20)+ item[3].center(20)+ item[4].center(15)+ item[5].center(30))


def print_found_rows(found):
    if found == None:
        st.text("No such file!")
        return None
    if found != None or found != []:
        # st.dataframe(pd.DataFrame({"Фамилия": found[0],
        #                            "Имя": found[1],
        #                            "Отчество": found[2],
        #                            "Дата рождения": found[3],
        #                            "Телефон": found[4],
        #                            "Должность": found[5]
        #                            }))
        st.dataframe(print_data(found))
    else:
        st.text("Данные не обнаружены")
# df = load_data()
