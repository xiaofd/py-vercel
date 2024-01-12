import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.responses import HTMLResponse  
from fastapi.staticfiles import StaticFiles
# 加载.env文件中的环境变量（如果存在）
load_dotenv()


# 使用环境变量或系统环境变量的默认值
api_key = os.getenv('PYTHON', 'default_api_key')
db_port = os.getenv('DB_PORT', '5432')

print(api_key)
print(db_port)

app = FastAPI()
app.mount("/dist", StaticFiles(directory="dist"), name="static")

@app.get('/one')
def getroot():
    return {'key':api_key,'num':db_port}

@app.get('/',response_class=HTMLResponse)
def getone():
    with open('dist/index.html','rb') as f:
        data = f.read()
        return data
