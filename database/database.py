from datetime import datetime

from fastapi import FastAPI
from sqlalchemy import text
from engine import engine


def create_tables():
    conn = engine.connect()
    print(engine)
    try:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS Visits (
                id SERIAL PRIMARY KEY,
                link VARCHAR(255),
                visit_time TIMESTAMP
            )
        """))
        conn.commit()
    finally:
        conn.close()


def close_database_connection():
    engine.dispose()


def insert_links(links):
    conn = engine.connect()
    try:
        for link in links:
            conn.execute(text("INSERT INTO Visits (link, visit_time) VALUES (:link, :visit_time)"),
                         {"link": link, "visit_time": datetime.utcnow()})
    finally:
        conn.close()


def get_visited_domains(from_time: int, to_time: int):
    conn = engine.connect()
    try:
        result = conn.execute(text("""
            SELECT DISTINCT SUBSTRING(link FROM 'https?://([^/]+)') as domain
            FROM Visits WHERE visit_time BETWEEN to_timestamp(:from_time) AND to_timestamp(:to_time)
            ORDER BY domain
        """), {"from_time": from_time, "to_time": to_time})
        domains = [row[0] for row in result.fetchall()]
        return domains
    finally:
        conn.close()


def insert_sample_data():
    conn = engine.connect()
    try:
        links = [
            "https://ya.ru/",
            "https://ya.ru/search/?text=мемы+с+котиками",
            "https://sber.ru",
            "https://stackoverflow.com/questions/65724760/how-it-is"
        ]
        for link in links:
            conn.execute(
                text("INSERT INTO Visits (link, visit_time) VALUES (:link, to_timestamp(:visit_time))"),
                {"link": link, "visit_time": 1545222222}
            )

    finally:
        conn.commit()
        conn.close()


def setup_db(app: FastAPI):
    @app.on_event("startup")
    def startup():
        create_tables()
        insert_sample_data()

    @app.on_event("shutdown")
    def shutdown_event():
        close_database_connection()
