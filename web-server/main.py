import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def getList():
    return '''
    <h1>Welcome</h1>
    <p>This is a test</p>
    '''


@app.get('/numbers')
def getList():
    return [1, 2, 3, 4, 5, 6]


@app.get('/abc')
def getList():
    return ['a', 'b', 'c', 'd', 'e', 'f']


@app.get('/categories')
def getList():
    return [{'id': 1, 'name': 'cars'}, {'id': 2, 'name': 'motorcycles'}, {'id': 3, 'name': 'Boats'}]


def run():
    store.getCategories()


if __name__ == '__main__':
    run()
