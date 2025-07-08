import uvicorn
from route import *

if __name__ == '__main__':
    uvicorn.run('server:app', reload=True, host='192.168.1.95', port=8000)
