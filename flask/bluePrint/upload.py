from flask import Blueprint, request, send_from_directory
from urllib.parse import urljoin
from model import User, Picture
from extension import db
from datetime import datetime
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
# 头像
AVATAR_FOLDER = "static/avatar"
if not os.path.isdir(AVATAR_FOLDER):
    os.mkdir(AVATAR_FOLDER)

AVATAR_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# 图片
PICTURE_FOLDER = "static/picture"


def create_picture_folder(username):
    url = PICTURE_FOLDER+'/'+username
    if not os.path.isdir(url):
        os.mkdir(url)
        os.mkdir(url + '/origin')
        os.mkdir(url + '/target')


PICTURE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# 检查后缀名是否为允许的文件
def allowed_file(filename, standard):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in standard


# 更改文件名
def change_filename(originName, username):
    tail = originName.rsplit('.', 1)[1]
    targetName = username + '.' + tail
    return targetName


@bp.route("/avatar", methods=['POST'])
def avatar():
    file = request.files.get('file')
    username = request.form.get('username')
    # 验证文件格式是否符合要求
    if file and allowed_file(file.filename, AVATAR_ALLOWED_EXTENSIONS):
        # 生成文件路径
        filePath = os.path.join(AVATAR_FOLDER, change_filename(file.filename, username))
        file_url = urljoin(request.host_url, filePath)
        # 将url插入数据库，存储文件
        user = User.query.filter_by(username=username).first()
        user.head = file_url
        db.session.commit()
        file.save(filePath)
        res = {
            'code': '0',
            'message': '上传成功',
            'head': file_url
        }
    else:
        res = {
            'code': '1',
            'message': '文件格式错误',
        }
    return res


@bp.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(AVATAR_FOLDER, filename)


@bp.route("/uploadPicture", methods=['POST'])
def uploadPicture():
    file = request.files.get('file')
    username = request.form.get('username')
    userId = request.form.get('userId')
    # 验证是否需要创建文件夹
    create_picture_folder(username)
    # 验证文件格式是否正确
    if file and allowed_file(file.filename, PICTURE_ALLOWED_EXTENSIONS):
        # 生成文件路径
        filePath = os.path.join(PICTURE_FOLDER, username, 'origin', file.filename)
        fileUrl = urljoin(request.host_url, filePath)
        # 创建picture实体
        picture = Picture(userId, file.filename, datetime.now(), fileUrl)
        # 存储实体到数据库
        db.session.add(picture)
        db.session.commit()
        # 存储文件
        file.save(filePath)
        res = {
            'code': '0',
            'message': '上传成功',
        }
    else:
        res = {
            'code': '1',
            'message': '格式错误',
        }
    return res



