from flask import Blueprint, request, send_from_directory, jsonify
from models import User, Picture
from extension import db
from urllib.parse import urlparse
import os

bp = Blueprint("picture",
               __name__,
               url_prefix="/api/picture",
               static_folder="",
               static_url_path=".."
               )


@bp.route("/tableData", methods=['GET', 'POST'])
def tableData():
    if request.method == 'GET':
        # 获取参数
        pageNum = request.args.get('pageNum')
        pageSize = request.args.get('pageSize')
        userId = request.args.get('userId')
        result = []
        # 从数据库获取分页数据
        paginate = Picture.query.filter(Picture.userId == userId).order_by(Picture.id).paginate(int(pageNum),
                                                                                                int(pageSize),
                                                                                                error_out=False)
        pag = paginate.items
        # 数据组织称dict形式
        for item in pag:
            all_info = {"id": item.id,
                        "filename": item.fileName,
                        "time": item.time,
                        "state": item.state,
                        "origin": item.origin_path,
                        "target": item.target_path,
                        }
            result.append(all_info)
        page_total = paginate.total
        return jsonify({
            'result': result,
            'total': page_total})
    else:
        pass
        return "success"


@bp.route("/delete", methods=['DELETE'])
def deletePicture():
    # 获取参数
    id = request.args.get('picId')
    print(id)
    # 从数据库读取图片地址
    picture = Picture.query.filter_by(id=id).first()
    origin_url = picture.origin_path
    target_url = picture.target_path
    # 删除图片
    if origin_url:
        origin_path = urlparse(origin_url)
        if os.path.exists(origin_path.path[1:]):
            os.remove(origin_path.path[1:])
    if target_url:
        target_path = urlparse(target_url)
        os.remove('..' + target_path.path)
    # 删除数据库条目
    db.session.delete(picture)
    db.session.commit()
    res = {
        'code': '0',
        'msg': '删除成功',
    }
    return res


