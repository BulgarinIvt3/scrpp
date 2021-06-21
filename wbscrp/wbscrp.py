from bs4 import BeautifulSoup
from requests import get
import time
import random


param = ('model: ', 'engine: ', 'box: ', 'body: ', 'drive: ', 'color: ', 'km: ', 'year: ', 'price: ', 'place: ', \
               'time: ', 'link: ', 'condition: ')
xxx = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()=+/,?`;:"
otstup = '=====================================================================================\n'

def ts(value):
    time.sleep(value)

def cod(value):
    value = value.encode('ISO-8859-1').decode('utf-8')
    return value

def write_console():
    for i, j in zip(param, spisok[0:13]):
        print(i + j)
    print(otstup)
    del spisok[0:13]

def write_file(filename):
    with open(filename, 'a+', encoding='utf-8') as f:
        for i, j in zip(param, spisok[0:13]):
            f.write(i + j.replace(' ', '').replace(' ', '').replace('₽', 'P') + '\n')
        f.write(otstup)
        del spisok[0:13]
    f.close()

def tru(filename):
    import os
    try:
        os.startfile(filename)
    except:
        print('The file was not opened')

def ras(arg1, arg2):
    if type(arg1) != int:
        raise TypeError('Enter the full number')
    if arg2 is not None:
        if type(arg2) != str:
            raise TypeError('Enter the string')

class Find_Cars:

    class Find_by_line:

        def __init__(self, arg, quantity=4000, filename=None):
            self.arg = arg
            self.quantity = quantity
            self.filename = filename
            ras(self.quantity, self.filename)

        def models(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx[62:]:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 3:
                raise ValueError('Need at least 3 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.upper()
                f = str(spisok[0].upper())
                if not f.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if f.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def boxes(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.upper()
                f = str(spisok[2].upper())
                if not f.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if f.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def bodes(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.upper()
                f = str(spisok[3].upper())
                if not f.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if f.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def drives(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.upper()
                f = str(spisok[4].upper())
                if not f.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if f.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def colors(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.upper()
                f = str(spisok[5].upper())
                if not f.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if f.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def type_engines(self):
            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                type_engine = spisok[1].split('/', 2)
                type_engine = type_engine[2].split()[0]
                self.arg = self.arg.capitalize()
                if not type_engine.find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if type_engine.find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def places(self):

            if type(self.arg) != str:
                raise TypeError('Enter the string')
            for i in self.arg:
                if i in xxx:
                    raise ValueError('Exclude some symbols')
            if len(self.arg) < 4:
                raise ValueError('Need at least 4 symbols')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            counter = 0
            while counter < self.quantity:
                self.arg = self.arg.capitalize()
                if not spisok[9].find(self.arg):
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if spisok[9].find(self.arg):
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

    class Find_by_value:

        def __init__(self, from_arg, to_arg, quantity=4000, filename=None):
            self.from_arg = from_arg
            self.to_arg = to_arg
            self.quantity = quantity
            self.filename = filename
            ras(self.quantity, self.filename)

        def volumes(self):
            if type(self.from_arg) != int:
                if type(self.from_arg) != float:
                    raise TypeError('Enter the number')
            if type(self.to_arg) != int:
                if type(self.to_arg) != float:
                    raise TypeError('Enter the number')
            rnd = lambda a, k: (a * (10 ** k) // 1) / 10 ** k
            self.from_arg = rnd(self.from_arg, 1)
            self.to_arg = rnd(self.to_arg, 1)
            if not 0.1 < self.from_arg < 10.1 or not 0.1 < self.to_arg < 10.1:
                raise ValueError('Enter the volume from 0.2 to 10')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            if self.from_arg > self.to_arg:
                self.from_arg, self.to_arg = self.to_arg, self.from_arg
            counter = 0
            while counter < self.quantity:
                try:
                    volume = spisok[1].split(' ')
                    volume = float(volume[0])
                    if self.from_arg <= volume <= self.to_arg:
                        if self.filename == None:
                            write_console()
                            counter += 1
                        if self.filename is not None:
                            write_file(self.filename)
                            counter += 1
                    if not self.from_arg <= volume <= self.to_arg:
                        del spisok[0:13]
                except:
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def powers(self):
            if type(self.from_arg) != int:
                raise TypeError('Enter the number')
            if type(self.to_arg) != int:
                raise TypeError('Enter the number')
            if self.from_arg not in range(1000000) or self.to_arg not in range(1000000):
                raise ValueError('Enter the power from 0 to 1100')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            if self.from_arg > self.to_arg:
                self.from_arg, self.to_arg = self.to_arg, self.from_arg
            counter = 0
            while counter < self.quantity:
                try:
                    power = spisok[1].split('/', 2)
                    if not power[0].find('с'):
                        el = power[1].split()[0]
                        el = int(el)
                        if self.from_arg <= power <= self.to_arg:
                            if self.filename == None:
                                write_console()
                                counter += 1
                            if self.filename is not None:
                                write_file(self.filename)
                                counter += 1
                        if not self.from_arg <= power <= self.to_arg:
                            del spisok[0:13]
                        del spisok[0:13]
                        power = []
                    power = power[1].split()[0]
                    power = int(power)
                    if self.from_arg <= power <= self.to_arg:
                        if self.filename == None:
                            write_console()
                            counter += 1
                        if self.filename is not None:
                            write_file(self.filename)
                            counter += 1
                    if not self.from_arg <= power <= self.to_arg:
                        del spisok[0:13]
                except:
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def kms(self):
            if type(self.from_arg) != int:
                raise TypeError('Enter the number')
            if type(self.to_arg) != int:
                raise TypeError('Enter the number')
            if self.from_arg not in range(1000000) or self.to_arg not in range(1000000):
                raise ValueError('Enter the mileage from 0 to 1000000')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            if self.from_arg > self.to_arg:
                self.from_arg, self.to_arg = self.to_arg, self.from_arg
            counter = 0
            while counter < self.quantity:
                try:
                    k = spisok[6].split()
                    k = ''.join(i for i in k if i.isdigit()).strip()
                    k = int(k)
                except:
                    k = str
                if self.from_arg != 0 and self.to_arg != 0:
                    if type(k) == int:
                        if self.from_arg <= k <= self.to_arg:
                            if self.filename == None:
                                write_console()
                                counter += 1
                            if self.filename is not None:
                                write_file(self.filename)
                                counter += 1
                        if not self.from_arg < k < self.to_arg:
                            del spisok[0:13]
                    if type(k) != int:
                        del spisok[0:13]
                if self.from_arg == 0 and self.to_arg == 0:
                    if type(k) != int:
                        if self.filename == None:
                            write_console()
                            counter += 1
                        if self.filename is not None:
                            write_file(self.filename)
                            counter += 1
                    if type(k) == int:
                        del spisok[0:13]
                if (self.from_arg == 0 and self.to_arg != 0) or (self.from_arg != 0 and self.to_arg == 0):
                    if type(k) == int:
                        if self.from_arg <= k <= self.to_arg:
                            if self.filename == None:
                                write_console()
                                counter += 1
                            if self.filename is not None:
                                write_file(self.filename)
                                counter += 1
                        if not self.from_arg < k < self.to_arg:
                            del spisok[0:13]
                    if type(k) != int:
                        if self.filename == None:
                            write_console()
                            counter += 1
                        if self.filename is not None:
                            write_file(self.filename)
                            counter += 1
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def years(self):
            if type(self.from_arg) != int:
                raise TypeError('Enter the full years number')
            if type(self.to_arg) != int:
                raise TypeError('Enter the full years number')
            if self.from_arg not in range(1879, 2022) or self.to_arg not in range(1879, 2022):
                raise ValueError('Enter the years from 1890 to 2021')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            if self.from_arg > self.to_arg:
                self.from_arg, self.to_arg = self.to_arg, self.from_arg
            counter = 0
            while counter < self.quantity:
                y = int(spisok[7])
                if self.from_arg <= y <= self.to_arg:
                    if self.filename == None:
                        write_console()
                        counter += 1
                    if self.filename is not None:
                        write_file(self.filename)
                        counter += 1
                if not self.from_arg < y < self.to_arg:
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

        def prices(self):
            if type(self.from_arg) != int:
                raise TypeError('Enter the full number')
            if type(self.to_arg) != int:
                raise TypeError('Enter the full number')
            if self.to_arg not in range(11000000) or self.from_arg not in range(11000000):
                raise ValueError('Enter the price from 0 to 110000000')
            if self.filename is not None:
                with open(self.filename, 'w') as f:
                    f.close()
            if self.from_arg > self.to_arg:
                self.from_arg, self.to_arg = self.to_arg, self.from_arg
            counter = 0
            while counter < self.quantity:
                try:
                    p = spisok[8].split()
                    p = ''.join(i for i in p if i.isdigit()).strip()
                    p = int(p)
                except:
                    p = str
                if type(p) == int:
                    if self.from_arg <= p <= self.to_arg:
                        if self.filename == None:
                            write_console()
                            counter += 1
                        if self.filename is not None:
                            write_file(self.filename)
                            counter += 1
                    if not self.from_arg <= p <= self.to_arg:
                        del spisok[0:13]
                if type(p) != int:
                    del spisok[0:13]
                if counter == self.quantity or len(spisok) == 0:
                    if self.filename is not None:
                        tru(self.filename)
                    print('Found', counter, 'cars')
                    break

    def all_cars(quantity=4000, filename=None):
        ras(quantity, filename)
        counter = 0
        if filename == None:
            p = input('Write to file?             (y/n): ')
            if p == 'y' or p == 'yes':
                filename = input('Enter the name file: ')
                with open(filename, 'w') as f:
                    f.close()
        while counter < quantity:
            if filename == None:
                write_console()
                counter += 1
            if filename is not None:
                write_file(filename)
                counter += 1
            if counter == quantity or len(spisok) == 0:
                if filename is not None:
                    tru(filename)
                print('Found', counter, 'cars')
                break

url = 'https://auto.ru/cars/all/?page='
cars = []
count = 1
page = input('Enter the number of pages: ')
try:
    page = int(page)
except:
    raise TypeError('Enter the number from 1 to 99')
if page not in range(1, 99):
    raise ValueError('Enter the number from 1 to 99')
while count <= page:
    url = url + str(count)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    cars_data = html_soup.find_all('div', class_="ListingItem-module__main")
    print('page ', count, 'of 99')
    if cars_data != []:
        cars.extend(cars_data)
        value = random.random()
        ts(value)
    else:
        print('Finish')
        break
    count += 1

count = 1
spisok = []
while count <= 4000:
    try:
        info = cars[int(count)]
    except:
        break
    try:
        model = info.find('a', {"class": "ListingItemTitle-module__link"}).text
    except:
        model = 'not info'
    try:
        condition = info.find('span', {"class": "ListingItemSoldInfo__text"}).text
    except:
        condition = 'available'
    inform = info.find_all('div', {"class": "ListingItemTechSummaryDesktop__cell"})
    try:
        engine = inform[0].text
    except:
        engine = 'not info'
    try:
        box = inform[1].text
    except:
        box = 'not info'
    try:
        body = inform[2].text
    except:
        body = 'not info'
    try:
        drive = inform[3].text
    except:
        drive = 'not info'
    try:
        color = inform[4].text
    except:
        color = 'not info'
    try:
        km = info.find('div', {"class": "ListingItem-module__kmAge"}).text
    except:
        km = 'not info'
    try:
        year = info.find('div', {"class": "ListingItem-module__year"}).text
    except:
        year = 'not info'
    try:
        price = info.find('div', {"class": "ListingItemPrice-module__content"}).text
    except:
        price = ' not info'
    try:
        place = info.find('span', {"class": "MetroListPlace__regionName MetroListPlace_nbsp"}).text
    except:
        place = 'not info'
    try:
        time = info.find('span', {"class": "MetroListPlace__content MetroListPlace_nbsp"}).text
    except:
        time = 'not info'
    link = info.find('a', {"class": "ListingItemTitle-module__link"})
    href = link.get('href')

    field = (cod(model), cod(engine), cod(box), cod(body), cod(drive), cod(color), cod(km), cod(year), cod(price), \
             cod(place), cod(time), href, cod(condition))
    spisok.extend(field)
    count += 1


if __name__ == '__main__':
    Find_Cars.all_cars()
