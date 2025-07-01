import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()


home_directory = Jinja2Templates(directory="home")
@app.exception_handler(404)
async def _(request: Request, _):
    path = request.url.path
    if path.endswith("/") and os.path.exists(f"home{path}index.html") and os.path.isfile(f"home{path}index.html"):
        return home_directory.TemplateResponse(
            name="root.html",
            context={
                "request": request
            },
        )
    elif not path.endswith(".html") and os.path.exists(f"home{path}") and os.path.isfile(f"home{path}"):
        return FileResponse(
            f"home{path}"
        )
    else:
        return Response(
            content="404",
            status_code=404,
            media_type="text/plain"
        )
