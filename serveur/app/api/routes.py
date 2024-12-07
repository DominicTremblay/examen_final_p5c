from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import db
from app.modeles import Film, Utilisateur, Commentaire
from app.api import api_bp


@api_bp.route("/", methods=["GET"])
def accueil():
    return jsonify({"message": "Bienvenue sur l'API de Films"})


