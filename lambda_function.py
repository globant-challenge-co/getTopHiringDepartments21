import sys
import logging
import json
import pandas as pd
import os
import psycopg2
logging.getLogger().setLevel(logging.DEBUG)

def handler(event, context):
    logging.warning(f"ℹ️🤖LLM Inference generator...")
    logging.warning(f'ℹ️🔔' +  sys.version + '!' )
    logging.info(f'ℹ️🔔' +  sys.version + '!' )
    queryResult = _getTopHiringDepartments21()
    return {
        'statusCode': 200,
        'body': queryResult
    }


def _getTopHiringDepartments21():
    logging.info(f'🔔Calling Query')
    conn = psycopg2.connect(
        dbname=os.environ.get("DB_NAME"), 
        user=os.environ.get("DB_USER"), 
        password=os.environ.get("DB_PASSWORD"), 
        host=os.environ.get("DB_HOST"), 
        port=os.environ.get("DB_P0RT")
    )
    cur = conn.cursor()
    cur.execute(f'{os.environ.get("TOP_DPT_HI_21_VIEW")}')
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    result = [dict(zip(colnames, row)) for row in rows]
    cur.close()
    conn.close()
    logging.info(f'🔔Finish Query')
    return result
    
    

