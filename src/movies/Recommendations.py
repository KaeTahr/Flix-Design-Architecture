import models as m
from sqlalchemy.orm import sessionmaker

class StrategyRecommendation(): #interfaz
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.engine = m.engine
        self.db = m.Base
        self.Session = sessionmaker(self.engine)
    def run_algorithm(self): # abstracto
        pass

class StrategyRecommendationAsc(StrategyRecommendation): # BOT 10
    def __init__(self, p1, p2, p3):
        StrategyRecommendation.__init__(self, p1, p2, p3)
    def run_algorithm(self):
        pref_key = ((self.p1 * self.p2 * self.p3) % 5) + 1
        result = None
        with self.Session() as session:
            result = session.query(m.Movie).filter_by(preference_key = pref_key).order_by(m.Movie.rating.asc()).limit(10).all()

    ## query select from movies where pref_key = pref_key order_by rating asc limit 10
        return result

class StrategyRecommendationDesc(StrategyRecommendation): # TOP 10
    def __init__(self, p1, p2, p3):
        StrategyRecommendation.__init__(self, p1, p2, p3)
    def run_algorithm(self):
        pref_key = ((self.p1 * self.p2 * self.p3) % 5) + 1
        ## query select from movies where pref_key = pref_key order_by rating desc limit 10
        result = None
        with self.Session() as session:
            result = session.query(m.Movie).filter_by(preference_key = pref_key).order_by(m.Movie.rating.desc()).limit(10).all()
        return result

    