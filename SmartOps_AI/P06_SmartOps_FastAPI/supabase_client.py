"""
This file is used to make connection with supabase
"""
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

def get_supabase_client():
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )

    return supabase