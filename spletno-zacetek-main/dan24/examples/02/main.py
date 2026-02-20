from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/html", response_class=HTMLResponse)
def return_html():
    return """
    <html>
        <head>
            <title>Moja stran</title>
        </head>
        <body>
            <h1>Pozdrav iz HTML!</h1>
            <p>To je HTML vsebina iz FastAPI.</p>
        </body>
    </html>
    """