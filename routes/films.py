from flask import Blueprint, jsonify, request
from models.films import FilmInfo
import logging  # 使用日志记录相关信息


logging.basicConfig(filename='films_api.log', level=logging.DEBUG)
films_bp = Blueprint('films', __name__)


@films_bp.route('/', methods=['GET'])
def get_films():
    # 返回所有的电影信息
    try:  # 在所有的路由中，都要进行错误处理
        films = FilmInfo.query.all()
        # 疑似有错↓
        # results = [films.to_dict() for film in films]
        results = [film.to_dict() for film in films]
        logging.info('All films were successfully retrieved from the database.')  # 用logging模块记录日志
        return jsonify(results)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})


@films_bp.route('/count_by_year', methods=['GET'])
def count_by_year():
    try:
        result = FilmInfo.count_by_year()  # 直接调用FilmInfo类中构建的静态方法count_by_year()
        logging.info('获得各年份电影数量序列')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})
# 返回按年统计的每年电影的数量信息，返回的json数据格式如下所示
# {
#   "1900": 1,
#   "1913": 1,
#   "1916": 1,
#   "1923": 1,
#   "1925": 4,
#   "1926": 3,
#   "1927": 1,
#   "1928": 3,
#   "1929": 5,
#   "1930": 5,
#   "1931": 6,
#   "1932": 2,
#   "1933": 9,
#   "1934": 10,
#   "1935": 6,
#   "1936": 8,
#   "1937": 12,
# ……
# }


@films_bp.route('/avg_rate_by_region', methods=['GET'])
def avg_rate_by_region():
    try:
        result = FilmInfo.avg_rate_by_region()
        logging.info('获得各地区电影平均得分')
        return jsonify(result)
    except Exception as e:
        logging.error('Error occurred while retrieving students from the database. Error message: {}'.format(str(e)))
        return jsonify({"error": str(e)})
# 返回按年统计的中国大陆、中国香港、中国台湾每年电影的平均得分，,返回的json数据格式如下所示
# {
#   "cn": {
#     "1916": null,
#     "1923": 8.3,
#     "1925": null,
#     "1926": 7.199999999999999,
#     "1927": 7.0,
#     "1928": 7.1,
#     "1929": 6.26,
#     "1930": 7.5,
#     "1931": 7.85,
#     "1932": 7.5,
#     "1933": 7.359999999999999,
#     "1934": 7.642857142857144,
#     "1935": 7.6,
#     "1936": 7.7,
#     "1937": 7.58,
#     "1938": 6.933333333333334,
#     "1939": 6.75,
#     "1940": 6.6,
# ……
# }
#  "hk": {
#     "1913": null,
#     "1925": null,
#     "1928": null,
#     "1931": null,
#     "1933": null,
#     "1934": null,
#     "1935": 6.6,
#     "1936": null,
#     "1937": null,
#     "1938": 6.8,
#     "1939": 6.5,
#     "1940": null,
#     "1941": null,
#      ……
# }
# "tw": {
#     "1916": null,
#     "1923": 8.3,
#     "1925": null,
#     "1926": 7.199999999999999,
#     "1927": 7.0,
#     "1928": 7.1,
#     "1929": 6.26,
#     "1930": 7.5,
#     "1931": 7.85,
#     "1932": 7.5,
#     "1933": 7.359999999999999,
#     "1934": 7.642857142857144,
#     "1935": 7.6,
#     "1936": 7.7,
#     "1937": 7.58,
#     "1938": 6.933333333333334,
#     "1939": 6.75,
#      ……
# }
# }



