from fastapi import APIRouter
from app.forms import Student, News, Prepodavatel, Ekzamen, Urok
from app.db.database import cursor

router = APIRouter()


@router.get("/students")
async def root():
  cursor.execute('SELECT * FROM student')
  json = []
  while 1:
    i = +1
    row = cursor.fetchone()
    if not row:
      break
    student_json = {"name": row.name.strip(), "kurs": row.kurs, "vazrast": row.vazrast, "gpa": row.gpa}
    json.append(Student(**student_json))

  print(json)
  return json


@router.post("/students")
async def root(items: Student):
  print(items)
  cursor.execute(f"INSERT INTO student VALUES ('{items.name}',{items.kurs},{items.vazrast},{items.gpa});")
  return items


@router.get("/urok")
async def root():
  cursor.execute("SELECT *\
    FROM prepodavatel\
    INNER JOIN urok\
    ON prepodavatel.prepodavatel = urok.prerodavatel")
  json = []
  while 1:
    i = +1
    row = cursor.fetchone()
    if not row:
      break
    prepodavatel_json = {"prepodavatel": row.prepodavatel.strip(), "name": row.name.strip(), "urok": row.urok.strip(),
                         "kredity": row.kredity, "prerodavatel": row.prerodavatel.strip()}
    json.append(Prepodavatel(**prepodavatel_json))
    print(row.name)

  print(json)
  return json


@router.post("/urok")
async def root(items: Urok):
  print(items)
  cursor.execute(f"INSERT INTO urok VALUES ('{items.urok}',{items.kredity},'{items.prerodavatel}');")
  return items


@router.get("/ekzamen")
async def root():
  cursor.execute("SELECT * FROM ekzamen")
  json = []
  while 1:
    i = +1
    row = cursor.fetchone()
    if not row:
      break
    prepodavatel_json = {"ekzamen": row.ekzamen.strip(), "data": row.data.strip(), "urok": row.urok.strip(),
                         "prepod": row.prepod.strip()}
    json.append(Ekzamen(**prepodavatel_json))
    print(row.ekzamen)

  print(json)
  return json


@router.post("/ekzamen")
async def root(items: Ekzamen):
  print(items)
  cursor.execute(f"INSERT INTO ekzamen VALUES ('{items.ekzamen}','{items.data}','{items.urok}','{items.prepod}');")
  return items


@router.get("/news")
async def root():
  cursor.execute("SELECT * FROM news")
  json = []
  while 1:
    i = +1
    row = cursor.fetchone()
    if not row:
      break
    prepodavatel_json = {"image": row.image.strip(), "text": row.text.strip(), "link": row.link.strip()}
    json.append(News(**prepodavatel_json))
    print(row.link)

  print(json)
  return json


# @app.delete('/students')
# async def delete_student():
#   cursor.execute("")

@router.get("/hello/{name}")
async def say_hello(name: str):
  return {"message": f"Hello {name}"}
