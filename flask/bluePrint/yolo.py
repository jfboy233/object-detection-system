from flask import Blueprint, request, send_from_directory, jsonify
from urllib.parse import urlparse, urljoin
from yolov5.detect import run
from model import User, Picture
from extension import db
import os

bp = Blueprint("yolo",
               __name__,
               url_prefix="/api/yolo",
               static_folder="",
               static_url_path=".."
               )


@bp.route("/picture", methods=['POST'])
def yolo():
    # 接收参数 分离源文件路径
    data = request.get_json(silent=True)
    sourceUrl = data.get('source')
    picId = data.get('picId')
    sourcePath = urlparse(sourceUrl).path[1:]
    # picture表中查找id 修改state=2 读出userid，确定用户名，生成存储位置路径
    picture = Picture.query.filter_by(id=picId).first()
    picture.state = 2
    db.session.commit()
    userId = picture.userId
    username = User.query.filter_by(id=userId).first().username
    project = 'static/picture/' + username + '/target'
    # 运行detect过程，将储存位置存入数据库
    picture = Picture.query.filter_by(id=picId).first()
    if picture.state == 2:
        picture.target_path = urljoin(request.host_url, run(weights='yolov5/train2023.3.5/exp/weights/best.pt',
                                                            source=sourcePath,
                                                            project=project))
    picture.state = 3
    db.session.commit()
    # 返回操作成功
    return {'code': '1',
            'msg': "success"}
