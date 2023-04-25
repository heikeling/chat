from flask import *
from loguru import logger
s = ""
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'], endpoint='test01')
def index():
    global a,ip,s
    ip = request.remote_addr
    data = request.form
    a = str(data.get("ky"))
    s += ip+":"+a+"\n"
    return render_template("index.html",texts = s)
app.run(host='0.0.0.0',port="80")