from aiogram.fsm.state import StatesGroup, State


class ApplicationFormStates(StatesGroup):
    
    WAITING_FOR_DESCRIPTION = State()
    WAITING_FOR_CONTACTS = State()
    WAITING_FOR_URL_PICTURE = State()
