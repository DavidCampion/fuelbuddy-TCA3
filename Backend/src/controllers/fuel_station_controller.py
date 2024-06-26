#! /usr/bin/env python3

from flask import Blueprint
from ..services import get_fuel_stations, get_past_petrol_prices, store_fuel_stations, get_favorite_fuel_stations, favorite_fuel_station, store_fuel_prices, store_ev_prices, search_fuel_stations, add_rating_to_fuel_station
fuel_station_blueprint = Blueprint('fuel_station', __name__)

# GET fuel_stations
fuel_station_blueprint.route(
    '/fuel_stations', methods=['POST'])(get_fuel_stations)
fuel_station_blueprint.route(
    '/get_favorite_fuel_stations', methods=['GET'])(get_favorite_fuel_stations)
fuel_station_blueprint.route(
    '/search_fuel_stations', methods=['GET'])(search_fuel_stations)

# POST
fuel_station_blueprint.route(
    '/store_fuel_stations', methods=['POST'])(store_fuel_stations)
fuel_station_blueprint.route(
    '/store_ev_prices', methods=['POST'])(store_ev_prices)
fuel_station_blueprint.route(
    '/manage_favorite_fuel_station', methods=['POST'])(favorite_fuel_station)
fuel_station_blueprint.route(
    '/store_fuel_prices', methods=['POST'])(store_fuel_prices)
fuel_station_blueprint.route(
    '/get_past_petrol_prices', methods=['POST'])(get_past_petrol_prices)
fuel_station_blueprint.route(
    '/add_rating_to_fuel_station', methods=['POST'])(add_rating_to_fuel_station)
