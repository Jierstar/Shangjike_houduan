from app import db
from statistics import mean




class FilmInfo(db.Model):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    director = db.Column(db.Text)
    language = db.Column(db.Text)
    rate = db.Column(db.Double)
    rating_num = db.Column(db.Integer)
    region = db.Column(db.Text)
    runtime = db.Column(db.Integer)
    title = db.Column(db.Text)
    type = db.Column(db.Text)
    year = db.Column(db.Integer)
    is_cn = db.Column(db.Integer)
    is_hk = db.Column(db.Integer)
    is_tw = db.Column(db.Integer)

    # 将返回的记录转化为字典格式
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'director': self.director,
            'language': self.language,
            'rate': self.rate,
            'rating_num': self.rating_num,
            'region': self.region,
            'runtime': self.runtime,
            'title': self.title,
            'type': self.type,
            'year': self.year,
        }

    # 按年统计每年电影的数量
    @staticmethod
    def count_by_year():
        ret = {}
        years = db.session.query(FilmInfo.year.distinct()).all()
        for year in years:
            res = db.session.query(FilmInfo).filter(FilmInfo.year == year[0]).all()
            ret[year[0]] = len(res)

        return ret

    # 分别按年统计中国大陆、中国香港、中国台湾每年电影的平均得分
    @staticmethod
    def avg_rate_by_region():
        hk, cn, tw = {}, {}, {}
        years = db.session.query(FilmInfo.year.distinct()).all()
        for year in years:
            hkRate = db.session.query(FilmInfo).filter(FilmInfo.year == year[0]).filter(FilmInfo.is_hk == 1).all()
            cnRate = db.session.query(FilmInfo).filter(FilmInfo.year == year[0]).filter(FilmInfo.is_cn == 1).all()
            twRate = db.session.query(FilmInfo).filter(FilmInfo.year == year[0]).filter(FilmInfo.is_tw == 1).all()

            hkRate = list(filter(None, map(lambda a: a.rate, hkRate)))
            cnRate = list(filter(None, map(lambda a: a.rate, cnRate)))
            twRate = list(filter(None, map(lambda a: a.rate, twRate)))

            hk[year[0]] = mean(hkRate) if hkRate else None
            cn[year[0]] = mean(cnRate) if cnRate else None
            tw[year[0]] = mean(twRate) if twRate else None
            ret = {"hk": hk, "cn": cn, "tw": tw}

        return ret
