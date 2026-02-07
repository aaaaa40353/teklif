import streamlit as st
import time


st.set_page_config(page_title="Soru")


st.write("baska sekil olmicak gibi")
time.sleep(1)
st.write("seni cok seviyorum")
time.sleep(1)
st.subheader("benim citlembigim olcan?")

time.sleep(1)
col1, col2 = st.columns(2)

with col1:
    if st.button("evet"):
        st.success("YAASSSS!! ")
        st.balloons()
        st.image("https://media1.tenor.com/m/RFvdfYRDt3cAAAAC/cat-flop.gif", width=300)

with col2:
    if st.button("hayir"):
        st.info("ok")
        st.image("https://media1.tenor.com/m/EGOH7ESHBtwAAAAd/sad-seal-seal.gif",width=300)