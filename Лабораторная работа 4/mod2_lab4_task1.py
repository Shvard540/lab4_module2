class Games:
    '''
    класс "игры"
    '''

    def __init__(self, quality: str, price: float):
        '''
        инициализация экземпляра класса

        :param quality: качество игры
        :param price: цена игры
        '''
        self.quality = quality
        self.price = price

        if not isinstance(quality, str):
            raise TypeErrror("Качество может быть только строкой str")
        elif not isinstance(price, float):
            raise TypeErrror("Цена может быть только числом типа float")
        elif price < 0:
            raise ValueErrror("Цена не может быть отрицательной")
            

    def __str__(self) -> str:
        return f"Данные об игре: цена {self.price}, качество {self.quality}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(price={self.price!r}, quality={self.quality!r})"

    def show_shop_price(self) -> str:
        '''
        показывает цену с магазинной накидкой
        '''
        return f"Цена в магазинах (при 3%): {self.price * 1.03}"

    def characteristics(self, extra=None) -> str:
        '''
        выводит список значений класса.
        :param extra: доп параметр (для подклассов)
        ---
        перегрузил так как подклассы имеют свои
        частные параметры
        '''
        if extra != None:
            print (f'{self.quality}' + " " + f'{self.price}' + " " + f'{extra}')
        else:
            print(f'{self.quality}' + " " + f'{self.price}')


class Boardgames(Games):
    '''
    подкласс "настольные игры"
    '''

    def __init__(self, quality: str, price: float, material: str):
        '''
        инициализация экземпляра подкласса

        :param quality: качество игры
        :param price: цена игры
        :param material: материал, из чего изготовлен
        '''
        super().__init__(quality, price)
        self.quality = quality
        self.price = price
        self.material = material

        if not isinstance(quality, str):
            raise TypeErrror("Качество может быть только строкой str")
        elif not isinstance(price, float):
            raise TypeErrror("Цена может быть только числом типа float")
        elif price < 0:
            raise ValueErrror("Цена не может быть отрицательной")
        elif not isinstance(material, str):
            raise TypeErrror("Материал может быть только строкой str")

    def __str__(self) -> str:
        return f"{super.__str__()}" + f", материал {self.material}"

    def __repr__(self) -> str:
        return super.__repr__() + f", material={self.material!r}"


class Computergames(Games):
    '''
    подкласс "компьютерные игры"
    '''

    def __init__(self, quality: str, price: float, data_size: int):
        '''
        инициализация экземпляра подкласса

        :param quality: качество игры
        :param price: цена игры
        :param data_size: объем данных игры
        '''
        super().__init__(quality, price)
        self.quality = quality
        self.price = price
        self.data_size = data_size

        if not isinstance(quality, str):
            raise TypeErrror("Качество может быть только строкой str")
        elif not isinstance(price, float):
            raise TypeErrror("Цена может быть только числом типа float")
        elif price < 0:
            raise ValueErrror("Цена не может быть отрицательной")
        elif not isinstance(data_size, int):
            raise TypeErrror("Объем данных может быть только числом типа int")
        elif data_size < 0:
            raise ValueErrror("Объем данных не может быть отрицательным")

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
