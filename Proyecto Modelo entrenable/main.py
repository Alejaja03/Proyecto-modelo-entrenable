import discord 
from discord.ext import commands
from model import predict_image
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
@bot.command()
async def predict(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image to predict.")
        return

    attachment = ctx.message.attachments[0]
    image_path = f"temp_{attachment.filename}"
    await attachment.save(image_path)

    model_path = "keras_model.h5"
    labels_path = "labels.txt"

    class_name, confidence_score = predict_image(model_path, image_path, labels_path)

    await ctx.send(f"Prediction: {class_name}\nConfidence Score: {confidence_score:.2f}")
bot.run('YOUR_DISCORD_BOT_TOKEN')