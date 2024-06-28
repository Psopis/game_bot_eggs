"""Import all routers and add them to routers_list."""

from tgbot.handlers.inline.user_handler import user_router

from tgbot.handlers.reply import start_dialog_handler

routers_list = [
    user_router,

    start_dialog_handler.router,

    # echo_router must be last
]

__all__ = [
    "routers_list",
]
