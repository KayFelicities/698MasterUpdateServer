# -*- coding: utf-8 -*-
from flask import send_file, Flask, render_template, flash, redirect, url_for, make_response, request
import re
import pathlib

APP_DIR = pathlib.Path('/698master/')
# APP_DIR = pathlib.Path('g:\\')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

def calc_ver(ver: str) -> float:
    ver = ver.lower()
    v1a = re.search(r'v([0-9\.]*)', ver)[1]
    v1b = re.search(r'beta([0-9]*)', ver)[1] if 'beta' in ver else '0'
    v1a, v1b = int(float(v1a)*10), int(float(v1b)*10)
    ver_calc = float('{}.{}'.format(v1a, v1b))
    return ver_calc

def get_newest_exe():
    apps = [x.name for x in APP_DIR.glob('*.exe')]
    if not apps:
        return 'V0'
    newest_exe = max(apps, key = lambda x: calc_ver(x))
    print('newest_exe:{}'.format(newest_exe))
    return newest_exe


@app.route('/')
def index():
    return redirect(url_for('infol'))

def get_last_698master():
    # return send_file('static/698master.exe', as_attachment=True, attachment_filename='698master.exe')
    return send_file(str(APP_DIR/get_newest_exe()), as_attachment=True)

@app.route('/last_ver')
def last_ver():
    return get_last_698master()

@app.route('/infol')
def infol():
    return '<a href="/last_ver">请点击升级</a>'

@app.route('/infol/<ver>')
def infol_ver(ver):
    need_update = False
    try:
        newest_ver = calc_ver(get_newest_exe())
        ver = calc_ver(ver)
        print(newest_ver, ver)
        if newest_ver > ver:
            need_update = True
    except Exception as e:
        print('get ver error', e)
        need_update = True
    if need_update:
        return '<a href="/last_ver">请点击升级(不点不是中国人)</a>'
    return '<p>:)<p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
