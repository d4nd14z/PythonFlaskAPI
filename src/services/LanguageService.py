import traceback
from src.database.db_mysql import get_connection
from src.utils.Logger import Logger
from src.models.LanguageModel import Language

class LanguageService():

    @classmethod
    def get_languages(cls): 
        try: 
            connection = get_connection()
            languages = []
            with connection.cursor() as cursor:
                cursor.execute('CALL sp_listLanguages()')
                resultset = cursor.fetchall()
                for row in resultset: 
                    language = Language(int(row[0]), row[1])
                    languages.append(language.to_json())
            connection.close()
            return languages
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
