from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "8892569006:AAHGV_bSk8iqDw6KgXQRbkAbAeKnX-Ifu1M"
CHAT_ID = 8892569006


async def reminder(app):
    await app.bot.send_message(
        chat_id=CHAT_ID,
        text="Напоминание: зайди в мсм"
    )


async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "бот запущен, я буду напоминать тебе о заходе в игру"
    )


async def post_init(app):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    scheduler.add_job(reminder, "cron", hour=9, minute=0, args=[app])
    scheduler.add_job(reminder, "cron", hour=14, minute=0, args=[app])
    scheduler.add_job(reminder, "cron", hour=19, minute=0, args=[app])

    scheduler.start()


app = (
    Application.builder()
    .token(TOKEN)
    .post_init(post_init)
    .build()
)

app.add_handler(MessageHandler(filters.ALL, reply_message))

app.run_polling()