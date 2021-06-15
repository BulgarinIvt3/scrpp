import unittest
from wbscrp import Find_Cars


class TestCars(unittest.TestCase):

    def test_model(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(1478).models)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!bmw').models)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('qs').models)
    def test_volume(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_value(str, []).volumes)
        self.assertRaises(ValueError, Find_Cars.Find_by_value(14.78, 12).volumes)
    def test_power(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_value(11.1, str).powers)
        self.assertRaises(ValueError, Find_Cars.Find_by_value(-1, 8).powers)
    def test_type_engine(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(11).type_engines)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('выц').type_engines)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!дизель').type_engines)
    def test_box(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line([]).boxes)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!коробка').boxes)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('ав').boxes)
    def test_body(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(11).bodes)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!qqw').bodes)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('ав').bodes)
    def test_drive(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(11).drives)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!полный').drives)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('ав').drives)
    def test_color(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(00).colors)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!желтый').colors)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('ав').colors)
    def test_km(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_value('kilometer', 222).kms)
        self.assertRaises(ValueError, Find_Cars.Find_by_value(100, 11111111111).kms)
    def test_price(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_value([],'222').prices)
        self.assertRaises(ValueError, Find_Cars.Find_by_value(100, 11111111111).prices)
    def test_year(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_value('year', 33.2).years)
        self.assertRaises(ValueError, Find_Cars.Find_by_value(1, 4444).years)
    def test_place(self):
        self.assertRaises(TypeError, Find_Cars.Find_by_line(777).places)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('!москва').places)
        self.assertRaises(ValueError, Find_Cars.Find_by_line('Мос').places)
    def test_all_cars(self):
        self.assertRaises(TypeError, Find_Cars.all_cars('file', 221))


if __name__ == '__main__':
    unittest.main()
