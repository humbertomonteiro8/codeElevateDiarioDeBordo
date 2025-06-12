# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

def oracle_connection():
    return create_engine(
        "oracle+oracledb://SYSTEM:SuperPassword@localhost:1521/?service_name=XEPDB1"
    )
