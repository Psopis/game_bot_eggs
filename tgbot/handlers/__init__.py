"""Import all routers and add them to routers_list."""

from tgbot.handlers.inline.check_subscribe_handler import sub_router
from tgbot.handlers.inline.user_start_handler import user_router
from tgbot.handlers.reply import neuroseti_handler
from tgbot.handlers.reply import start_dialog_handler
from tgbot.handlers.reply import main_profile_handlers
from tgbot.handlers.inline.neuro import remake_video_handler, remake_photo_handler
from tgbot.handlers.inline.neuro.generation_photos_choose import SD_generation_photo_handler, Dalle_g_photo_handler, \
    Midjourny_g_photo_handler
from tgbot.handlers.inline.main_profile_dop import subscribes_handler, help_handler, partner_programm_handler
from tgbot.handlers.inline.main_profile_dop.promoSet_and_moneyGet import enter_promo, prom_Set

routers_list = [
    user_router,
    sub_router,
    start_dialog_handler.router,
    neuroseti_handler.router,
    main_profile_handlers.router,
    SD_generation_photo_handler.gen_router,
    Dalle_g_photo_handler.gen_router,
    Midjourny_g_photo_handler.gen_router,
    remake_photo_handler.gen_router,
    remake_video_handler.gen_router,
    subscribes_handler.dop_router,
    help_handler.dop_router,
    partner_programm_handler.dop_router,
    enter_promo.dop_router,
    prom_Set.dop_router
    # echo_router must be last
]

__all__ = [
    "routers_list",
]
