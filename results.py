class Result:
    def __init__(self, result_id, params, result):
        self.result_id = result_id
        self.params = params
        self.result = result

def select_all_results(db):
    c = db.cursor()
    string = 'SELECT * FROM results'
    c.execute(string)
    results = [Result(r[0], r[1], r[2]) for r in c.fetchall()]
    return results
