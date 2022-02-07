
from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation, UndefinedTable

def series():
    try:
        Series.read_series()
        
    except UndefinedTable:
        Series.create()
        return jsonify({"data": []}), HTTPStatus.OK    
    
    except TypeError:
        return jsonify({"data": []}), HTTPStatus.OK    
    
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    series_list = [dict(zip(serie_keys, serie)) for serie in Series.read_series()]
    
    return jsonify({'data': series_list}), HTTPStatus.OK

def select_by_id(serie_id):
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    series_list = [dict(zip(serie_keys, serie)) for serie in Series.read_series_by_id(serie_id)]
    
    if series_list == []:
        return jsonify({"error": "Not Found"}), HTTPStatus.NOT_FOUND

    return jsonify({'data': series_list[0]}), HTTPStatus.OK

def create():
    
    Series.create()
    
    data = request.get_json()
    
    serie = Series(**data)
    
    try:
        inserted_serie = serie.create_serie()
    
    except UniqueViolation as error:
        return (
            jsonify({"msg": error.args}), HTTPStatus.UNPROCESSABLE_ENTITY
        )
        
    serie_keys = ['id', 'serie', 'seasons', 'released_date', 'genre', 'imdb_rating']
    
    inserted_serie = dict(zip(serie_keys, inserted_serie))
    
    return jsonify(inserted_serie), HTTPStatus.CREATED