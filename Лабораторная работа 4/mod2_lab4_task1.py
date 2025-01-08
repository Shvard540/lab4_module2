class Games:
    '''класс "игры" '''

    def __init__(self, quality: str, price: float):
        self.quality = quality
        self.price = price

    def __str__(self) -> str:
        return f"Данные об игре: цена {self.price}, качество {self.quality}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(price={self.price!r}, quality={self.quality!r})"

    def show_shop_price(self) -> str:
        '''показывает цену с магазинной накидкой'''
        return f"Цена в магазинах (при 3%): {self.price * 1.03}"

    def characteristics(self, extra=None) -> str:
        '''
        выводит список значений класса.
        ---
        перегрузил так как классы имеют свои
        частные параметры
        '''
        if extra != None:
            print (f'{self.quality}' + " " + f'{self.price}' + " " + f'{extra}')
        else:
            print(f'{self.quality}' + " " + f'{self.price}')


class Boardgames(Games):
    '''подкласс "настольные игры"'''

    def __init__(self, quality: str, price: float, material: str):
        super().__init__(quality, price)
        self.quality = quality
        self.price = price
        self.material = material

    def __str__(self) -> str:
        return f"{super.__str__()}" + f", материал {self.material}"

    def __repr__(self) -> str:
        return super.__repr__() + f", material={self.material!r}"


class Computergames(Games):
    '''подкласс "компьютерные игры"'''

    def __init__(self, quality: str, price: float, data_size: int):
        super().__init__(quality, price)
        self.quality = quality
        self.price = price
        self.data_size = data_size

    def __str__(self) -> str:
        return f"{super.__str__()}" + f", объем данных {self.data_size}"

    def __repr__(self) -> str:
        return super.__repr__() + f", data_size={self.data_size!r}"


# ПОЛЕ ПРОВЕРОК

# создаем экземпляры
g = Games("normal", 10000)
bg = Boardgames("good", 1000, "paper")
cg = Computergames("good", 1000, 100)

# проверка наследования
print(cg.show_shop_price())

# проверка перегрузки
g.characteristics()
bg.characteristics("material")
cg.characteristics(123)
g.characteristics()
