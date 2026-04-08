import streamlit as st
about_me=st.Page(
    page='views/about.py',
    title='About us',
    icon=':material/home:',
    default=True
)
contact_me=st.Page(
    page='views/contact.py',
    title='Contact us',
    icon=':material/contact_mail:',
)
service_me=st.Page(
    page='views/services.py',
    title='Services',
    icon=':material/engineering:',
)
pg=st.navigation(pages=[about_me,contact_me,service_me])
# st.logo('apply')
pg.run()