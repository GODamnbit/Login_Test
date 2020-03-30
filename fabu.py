# coding=utf-8
from flask import render_template, request, Blueprint
import op_db
from datetime import datetime

fa = Blueprint('fabu', __name__)


@fa.route('/station', methods=['GET', 'POST'])
def station():
    now = datetime.now()
    station_id = request.values.get('station_id')
    sql = "SELECT density FROM station WHERE station_id='%s';" % station_id
    results = op_db.fabu(sql).values()  # 执行sql
    for result in results:
        print(result[0])
        if result == "R":
            context1 = {
                'msg' : str(now) + '\n该站点人群密集！不建议由此站点出行！'
            }
            return render_template('index.html', image='./static/images/R.jpg', **context1)
        elif result == "B":
            context2 = {
                'msg': str(now) + '\n该站点人群不怎么多，可考虑由此站点出行。'
            }
            return render_template('index.html', image='./static/images/B.jpg', **context2)
        elif result == "G":
            context3 = {
                'msg': str(now) + '\n该站点人很少，很建议由此站点出行哦~'
            }
            return render_template('index.html', image='./static/images/G.jpg', **context3)
