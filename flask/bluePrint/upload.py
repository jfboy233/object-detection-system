from flask import Blueprint, request, send_from_directory
from urllib.parse import urljoin
from models import User
from extension import db
import string
import os

bp = Blueprint("upload",
               __name__,
               url_prefix="/api/upload",
               static_folder="static",
               static_url_path="../static"
               )

################################################
# 配置参数
################################################
AVATAR_FOLDER = "static/avatar"
if not os.path.isdir(AVATAR_FOLDER):
    os.mkdir(AVATAR_FOLDER)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# 检查后缀名是否为允许的文件
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route("/avatar", methods=['POST'])
def avatar():
    file = request.files.get('file')
    username = request.form.get('username')
    # 验证文件格式是否符合要求
    if file and allowed_file(file.filename):
        # 生成文件路径
        filePath = os.path.join(AVATAR_FOLDER, file.filename)
        file_url = urljoin(request.host_url, filePath)
        # 将url插入数据库，存储文件
        user = User.query.filter_by(username=username).first()
        user.head = file_url
        db.session.commit()
        file.save(filePath)
        res = {
            'head': file_url
        }
    return res


@bp.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(AVATAR_FOLDER, filename)
