from app import app
from models.films import FilmInfo
from flask import jsonify
from flask_cors import CORS

CORS(app)


@app.route('/', methods=['GET'])
def get_films():
    # 返回所有的电影信息
    try:  # 在所有的路由中，都要进行错误处理
        films = FilmInfo.query.all()
        results = [film.to_dict() for film in films]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/count_by_year', methods=['GET'])
def count_by_year():
    try:
        result = FilmInfo.count_by_year()  # 直接调用FilmInfo类中构建的静态方法count_by_year()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/avg_rate_by_region', methods=['GET'])
def avg_rate_by_region():
    try:
        result = FilmInfo.avg_rate_by_region()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/count_by_region', methods=['GET'])
def count_by_region():
    try:
        res = FilmInfo.count_by_region()
        return jsonify(res)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/count_by_type', methods=['GET'])
def count_by_type():
    try:
        res = FilmInfo.count_by_type()
        return jsonify(res)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    # Json中的中文显示为unicode
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
