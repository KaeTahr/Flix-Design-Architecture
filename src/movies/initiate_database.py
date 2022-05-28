import models as m
from sqlalchemy.orm import sessionmaker
import csv
from datetime import datetime

def main():
    engine = m.engine
    db = m.Base
    #Se usa el Design Pattern de *Factory* en el modulo de sessionmaker al crear diferentes objetos de sesion sin tener la
    #logica de creacion en esta clase
    Session = sessionmaker(engine)
    with Session() as session:

        with open('movies/movie_results.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            i = 1
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    m_id = i
                    pk = row[0]
                    mt = row[1]
                    r = row[3]
                    y = row[4]
                    t = datetime.now()
                    movie = m.Movie(movie_id= m_id,
                        preference_key=pk,
                        movie_title = mt,
                        rating = r,
                        year = y,
                        create_time = t)
                    session.add(movie) 
                    i += 1
            session.commit()




        
        