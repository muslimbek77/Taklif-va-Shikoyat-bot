from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()

class ChannelState(StatesGroup):
    kanal_qoshish = State()


class DelChannelState(StatesGroup):
    delete_channel = State()

class OfferState(StatesGroup):
    offer = State()

from aiogram.fsm.state import State, StatesGroup

class ApplyCourseState(StatesGroup):
    full_name = State()
    age = State()
    phone = State()
    schedule = State()
    time_preference = State()
    level = State()
