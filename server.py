import uvicorn
from route import *

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, host='127.0.0.1', port=8000)
