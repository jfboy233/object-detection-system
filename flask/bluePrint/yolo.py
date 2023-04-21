from flask import Blueprint, request, send_from_directory, jsonify
from models import User, Picture
from extension import db
import os

bp = Blueprint("yolo",
               __name__,
               url_prefix="/api/yolo",
               static_folder="",
               static_url_path=".."
               )


@bp.route("/", methods=['POST'])
def yolo():
    pass
