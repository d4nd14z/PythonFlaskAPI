import traceback
from flask import Blueprint, request, jsonify
from src.utils.Logger import Logger
from src.utils.Security import Security
from src.services.LanguageService import LanguageService

main = Blueprint('language_blueprint', __name__)

@main.route('/')
def get_languages():
    has_acess = Security.verify_token(request.headers)
    if has_access: 
        try: 
            languages = LanguageService.get_languages()
            if (len(languages) > 0): 
                return jsonify({'languages': languages, 'message': 'SUCCESS', 'success': True})
            else: 
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex: 
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return jsonify({'message': 'ERROR', 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401