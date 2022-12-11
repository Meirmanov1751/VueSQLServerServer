from pydantic import BaseModel


class Student(BaseModel):
  name: str = None
  kurs: int = None
  vazrast: int = None
  gpa: int = None


class Urok(BaseModel):
  urok: str = None
  kredity: int = None
  prerodavatel: str = None


class Ekzamen(BaseModel):
  ekzamen: str = None
  data: str = None
  urok: str = None
  prepod: str = None


class Prepodavatel(BaseModel):
  prepodavatel: str = None
  name: str = None
  urok: str = None
  kredity: int = None
  prerodavatel: str = None


class News(BaseModel):
  image: str = None
  text: str = None
  link: str = None
