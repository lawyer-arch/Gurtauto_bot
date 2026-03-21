from aiogram.fsm.state import StatesGroup, State


class ApplicationFormStates(StatesGroup):
    WAITING_FOR_DESCRIPTION = State()
    WAITING_FOR_CONTACTS = State()
    
    marka = State()                # Вопрос 1: Марка автомобиля
    model = State()                # Вопрос 2: Модель автомобиля
    year = State()                 # Вопрос 3: Год выпуска
    budget = State()               # Вопрос 4: Бюджет покупки
    contact = State()              # Вопрос 5: Контактные данные