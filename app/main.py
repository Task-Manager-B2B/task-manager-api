from fastapi import FastAPI

app = FastAPI(
    title='Task B2B',
    description='Task Manager B2B',
    version='1.0.0'
)

@app.get('/Health')
async def health():
    return {'status': 'OK'}
