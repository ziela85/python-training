from flask.ext.jsonpify import jsonify

class RestController:
    def query(self):

        j = jsonify({'name': 'alice',
                 'email': 'alice@outlook.com'})
        return j