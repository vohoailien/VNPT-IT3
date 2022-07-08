
import telepot


token = '5442022731:AAH8_LbPeOMiO-6aCGxb786ZuaNUOSeph9g' 
receiver_id = -745194194 


bot = telepot.Bot(token)

bot.sendMessage(receiver_id, 'Hihi ') # send a activation message to telegram receiver id

bot.sendPhoto(receiver_id, photo=open('test_img.jpg', 'rb')) # send message to telegram
