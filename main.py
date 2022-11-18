from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """     
     <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.btn {
  border: 2px solid black;
  border-radius: 5px;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  width: 150px;
}

/* Зеленый */
.success {
  border-color: #4CAF50;
  color: green;
}
div.section {
    counter-reset: headings 0;
}
h2:before {
    counter-increment: headings 1;
    content: "Амперметр
    +" counter(headings, decimal) ": ";
}

.success:hover {
  background-color: #4CAF50;
  color: white;
}

/* Синий */
.info {
  border-color: #2196F3;
  color: dodgerblue
}

.info:hover {
  background: #2196F3;
  color: white;
}

/* Оранжевый */
.warning {
  border-color: #ff9800;
  color: orange;
}

.warning:hover {
  background: #ff9800;
  color: white;
}

/* Красный */
.danger {
  border-color: #f44336;
  color: red
}

.danger:hover {
  background: #f44336;
  color: white;
}

/* Серый */
.default {
  border-color: #e7e7e7;
  color: black;
}

.default:hover {
  background: #e7e7e7;
}
</style>
</head>
<body>
<h1>Мультиметр</h1>

<button class="btn success">Амперметр</button>
<button class="btn info">Вольтметр</button>
<button class="btn warning">Ваттметр</button>
<button class="btn danger">Омметр</button>

<br>
<button class="btn default">104.43 A</button>
<button class="btn default">230.76 В</button>
<button class="btn default">150.00 Вт</button>
<button class="btn default">100 Ом</button>



</body>
</html>
"""