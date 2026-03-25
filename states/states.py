from aiogram.fsm.state import StatesGroup, State


class ApplicationFormStates(StatesGroup):
    marka_model = State()
    engine = State()
    drive = State()
    fuel = State()
    mileage = State()
    year = State()
    budget = State()
    repairs = State()
    url_or_image = State()
    phone = State()
