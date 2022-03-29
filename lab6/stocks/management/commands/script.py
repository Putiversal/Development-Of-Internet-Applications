import sqlite3
from django.core.management.base import BaseCommand

donuts_values = [
  ('Порше', 'Вам нравиться наблюдать за красотой, скоростью и грацией? За звездами на \
лобовом стекле. Тогда вам обязательно стоит попробовать ее.', 3000000, 'car-1.jpg'),
  ('Ламбаргини', 'Итальянцы делали тракторы и вдруг взялись за спорткары. ', 8000000, 'car-2.jpeg'),
  ('Роллс Ройс"', 'Видели Мерседес? Так вот, это в разы лучше.', 11000000, 'car-3.jpg'),
  ('Ягуар', 'Обязательно обьездите наше скоростное чудо', 5000000, 'car-4.jpg'),
  ('Тайота', 'Надежный японец, вытянет из любой грязи', 800000, 'car-5.jpeg'),
  ('Мерседес', 'С иголочки, почти вычурно, но ослепительно!', 1000000, 'car-6.jpg'),
  ('БМВ', 'Агрессивная немецкая машина.', 900000, 'car-7.jpg'),
  ('Ситроен', 'Спокойный и качественный француз', 700000, 'car-8.jpg'),
  ('Лада', 'Хорошо, первая машина!', 250000, 'car-9.jpg'),
  ('Киа', 'Уже лучше, чем Лада.', 400000, 'car-10.jpg'),
  ('Лошадь', 'По-старому, только старее.', 50000, 'car-11.jpg'),
  ('Лошадь с повозкой', 'По-старому.', 100000, 'car-12.jpg'),
]

sets_values = [
  ('Сет "Дорого-богато"', 'Здесь собраны машины на любой вкус. Вам обязательно понравится!', 'set-1.jpg'),
  ('Стандартный сет', 'Наш фирменный набор машин для обеспеченных', 'set-2.jpg'),
  ('Сет "Бюджет"', 'В селе вас не засмеют', 'set-3.jpg'),
]

fk_values = [ # Один ко многим
  ('1', '1'),
  ('1', '2'),
  ('1', '3'),
  ('1', '4'),
  ('2', '5'),
  ('2', '6'),
  ('2', '7'),
  ('2', '8'),
  ('3', '9'),
  ('3', '10'),
  ('3', '11'),
  ('3', '12'),
]

fill_sets_query = "INSERT INTO donutssets (name, info, picture) VALUES (?, ?, ?);"
fill_donuts_query = "INSERT INTO donuts (name, info, cost, picture) VALUES (?, ?, ?, ?);"
fill_donutssets_fk_donuts_query = "INSERT INTO donutssets_fk_donuts (donutsset_id, donut_id) VALUES (?, ?);"

class Command(BaseCommand):
  help = "filling db donuts"

  def handle(self, *args, **options):
    self.fillDonuts()
    self.fillDonutsSets()
    self.fillDonutsFkSets()

  def fillDonuts(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for donut in donuts_values:
      c.execute(fill_donuts_query, donut)

    db.commit()
    c.close()
    db.close()

  def fillDonutsSets(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for set in sets_values:
      c.execute(fill_sets_query, set)

    db.commit()
    c.close()
    db.close()

  def fillDonutsFkSets(self):
    db = sqlite3.connect("donuts.sqlite3")
    c=db.cursor()

    for fk in fk_values:
      c.execute(fill_donutssets_fk_donuts_query, fk)

    db.commit()
    c.close()
    db.close()