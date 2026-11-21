import streamlit as st

from supabase import create_client,Client

from urllib.parse import urlparse
print("Active Supabase host:", urlparse(st.secrets["SUPABASE_URL"]).hostname)

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)

supabase_admin: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_SECRET_KEY"]
)