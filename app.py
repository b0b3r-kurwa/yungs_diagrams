import pandas as pd
import streamlit as st
from alhorithms.amount_algorithm import nf
from alhorithms.yung_algorithm import create_pictures

st.set_page_config(layout="wide")
amount, diagram = st.columns(2)


def get_data(n):
    p_n = []
    for i in range(n + 1):
        p_n.append(nf(i, i))
    data = pd.DataFrame({
        "p(n)": p_n
    })
    return data


@st.fragment
def show_lines():
    n = st.slider("Select n: ", 2, 100, 2)
    data = get_data(n)
    st.bar_chart(data)
    with st.container(height=630):
        st.table(data)


def show_diagram():
    n = st.slider("Select n ", 4, 20, 4)
    images = create_pictures(n)
    with st.container(height=1020):
        left, right = st.columns(2)
        j = 1
        for i in images:
            if j % 2:
                with left:
                    st.image(i)
            else:
                with right:
                    st.image(i)
            j += 1


with amount:
    st.title('🏁 Calculating the number of partitions')
    st.write("when selecting numbers > 60, it takes considerable time to calculate")
    show_lines()
with diagram:
    st.title("🏁 Constructing Young diagrams of order N")
    st.write("when selecting numbers > 10, it takes considerable time to calculate")
    show_diagram()
