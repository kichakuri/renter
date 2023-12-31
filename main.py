from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app1=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

'''
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # return {"greetings": "Hello world"}
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/properties", response_class=HTMLResponse)
def load_properties(request: Request):
    return templates.TemplateResponse("properties_list.html", {"request": request,
                                                               "list": ["property1", "property2"]})
'''


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app1.get("/Kichakuri/{stuff}")
async def read_stuff(stuff):
    return {"Stuff": stuff}