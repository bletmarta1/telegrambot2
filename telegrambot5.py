import telebot
import random
import bs4
import requests
from telebot import types

bot = telebot.TeleBot('1645279566:AAEDWDLAxJo7MN5-qiQdh_SKRfuP8fzrCDM') 	# сюда токен

#--------------------------parser---------------------------------------
def parser_gif(search):
	'''Функция которая парсит ссылки с гифками'''
	
	# подключаемся к сайту
	res = requests.get('https://tenor.com/search/'+search+'-gifs')
	
	# проверка на ошибки
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text)
	
	# здесь хранятся гифки
	gifElem = soup.select('img[src]')
	
	gif_list = []
	
	for i in gifElem:
        # достает только ссылки
		url = i.get('src')
        # добавляет ссылки в список
		gif_list.append(url)
	
    # достает рандомную гифку из списка
	gif_random = random.choice(gif_list)
	return gif_random
#--------------------------parser---------------------------------------

#--------------------------start----------------------------------------
@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	# кнпопки
	button = types.ReplyKeyboardMarkup()
	button.row("🤬", "🤯", "🤑")
	button.row("😤", "🥰", "🎃") 
	bot.send_message(message.chat.id, 'Ну привет!', reply_markup=button)
	#print(message.chat.first_name, message.text)
#--------------------------start----------------------------------------

#----------------------------------star----------------------------------
@bot.message_handler(commands=['start'])
def message_hello(message):
	'''Отвечает на приветсвие человека'''
	bot.send_message(message.chat.id, 'Здрасте!')
	#print(message.chat.first_name, message.text)
#------------------------------star-------------------------------------

#------------------------------text-------------------------------------
@bot.message_handler(content_types=['text'])
def message_text(message):
	'''Принимает текст и отвечает на него'''
	# бот отправляет сообщение 
	print(message.chat.first_name, message.text)
	if  'бонжур'  in  message.text.lower() :
		bot.send_message(message.chat.id, 'хелоул')
	#bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBB2A9BS4QJh0f5Rfijr3BE5x8X68aAAIUAAPANk8TrWWZ5Lkw9j4eBA')
	elif  'в каком месте вы бы хотели окозатса прямо осечас?'  == message.text.lower() :
		bot.send_message(message.chat.id, ' в монако')
	elif  'команды'  in message.text.lower() :
		bot.send_message(message.chat.id, '''вот такие комады я могу отвечать. в каком месте вы бы хотели окозатса прямо осечас?,
	бонжур,скока лет тебе,ты захватываеш мир,как дела,''')	
	elif  'сколько тебе лет'  in  message.text.lower() :
		bot.send_message(message.chat.id, '5')
	elif  'ты захватываеш мир'  in  message.text.lower() :
		bot.send_message(message.chat.id, 'конечно я уже давно ево захвачиваю')
		bot.send_message(message.chat.id, "😈")
	elif  'как дела'  in  message.text.lower() :
		bot.send_message(message.chat.id, 'нормально')
		bot.send_message(message.chat.id, "🥰🤑🤬")
	elif  "😜"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ты  вкусною поел еду?')
	elif  'да поел'  in  message.text.lower() :
		bot.send_message(message.chat.id, 'прикольно . а она была еда в кусноя ?')
		bot.send_message(message.chat.id, "😋")
	elif  'да он был очень вкусный.это блинчик'  in  message.text.lower() :
		bot.send_message(message.chat.id, 'прикольно я бы поел')	
		bot.send_message(message.chat.id, "👋")
	elif  "🤬"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ты офигел ?')
	elif  "🤯"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'че бошка розкаливаетса. Сложная задачка по матешы чтоли ?')
	elif  "🤑"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'че банк ограбил? щя в полицую  позвоню и тебя здам , так что деньги гани')
	elif  "😤"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ты че понты попутал. ты на меня быкуеш ?')
	elif  "🥰"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ты че влюбилась ?')
	elif  "🎃"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'прикольно но до хелуина ище долго')
	elif  "апчхи"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'не карона бро')
	elif  "не,не карона бро"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'точно не карона бро')
	elif  "не"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ну тогда хорошо')
	elif  "мг"  in  message.text.lower() :
		bot.send_message(message.chat.id, 'ага')
	else :
		bot.send_message(message.chat.id, parser_gif(message.text))
#------------------------------text-------------------------------------

#-----------------------------sticker-----------------------------------
@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
	stickers =['CAACAgIAAxkBAAIDdWB5ObmhBi8W8JfiS4uomHIsQYp2AAJFAAOtZbwUmHusIZtTJjAfBA',
	'CAACAgIAAxkBAAIDd2B5Ob8rLVIVW-3qc7_9T5rj7QdPAAJRAAOtZbwUhqL2m7j1-W4fBA',
	'CAACAgIAAxkBAAIDeWB5OcLxhJ0luZoRBfy-7JGKh9c8AAJYAAOtZbwUC_ayaijl7FUfBA',
	'CAACAgIAAxkBAAIDe2B5OcYGM036w159uhBh57oOXASIAAJNAAOtZbwU9rZs9GUx5hofBA',
	'CAACAgIAAxkBAAIDfWB5OciNaM5yPKKGuVv2sULiVyFsAAJUAAOtZbwUJTaFSf0QNk4fBA',
	'CAACAgIAAxkBAAIDf2B5OcnvrzgoHxnZ806BRoi_Ae02AAI1AAOtZbwU9aVxXMUw5eAfBA',
	'CAACAgIAAxkBAAIDgWB5OcpZaJGCE3mLtbgRQ_Mn-XWdAAJCAAOtZbwUJXfx78xEyfIfBA',
	'CAACAgIAAxkBAAIDg2B5Ocz24INgFYHL4G_tVeT5HH7RAAJSAAOtZbwU2nZehNgFfdYfBA',
	'CAACAgIAAxkBAAIDjWB5OzWSS0K9i00XSQM9EYKPPaGGAAI7AAMkcWIatVbiuzmYQ_4fBA',
	'CAACAgIAAxkBAAIDjmB5OzV1VWheJmJzyVIFN4M-GDQuAAJRAAMkcWIa6UcbX8Y_pyMfBA',
	'CAACAgIAAxkBAAIDkWB5Ozc77N3MI1dQI_382ie5eNz4AAJNAAMkcWIaP0h_gyO63p0fBA',
	'CAACAgIAAxkBAAIDk2B5OzhKR8hNNJJ_0KpIwUsSFAXtAAJBAAMkcWIaBMylHS4fuEAfBA',
	'CAACAgIAAxkBAAIDk2B5OzhKR8hNNJJ_0KpIwUsSFAXtAAJBAAMkcWIaBMylHS4fuEAfBA',
	'CAACAgIAAxkBAAIDl2B5OzskZUl95u4yVrRKPZbsku_-AAI3AAMkcWIaWEUH6ryDOtsfBA',
	'CAACAgIAAxkBAAIDmWB5Ozu6bF1CVz0gshTTcxWsduB8AAJPAAMkcWIaWMzn4qdTlUgfBA',
	'CAACAgIAAxkBAAIDm2B5OzxzHlVhkzuQ3wGi50AHh_h3AAJMAAMkcWIaRVe5OQcfS1UfBA',
	'CAACAgIAAxkBAAIDnWB5Oz0Ktckl-EWqgP3iffEa-jXBAAI-AAMkcWIaojPkXVgw9UQfBA',
	'CAACAgIAAxkBAAIDn2B5Oz7KgJnXpIMkGSNs6cADHPUzAAJFAAMkcWIa4ZtaUZ7G95kfBA',
	'CAACAgIAAxkBAAIDoWB5Oz_k80YSL6eeg1CcQbYAAav1NwACQwADJHFiGg0pc5OW40-tHwQ',
	'CAACAgIAAxkBAAIDo2B5O0BhRCb9AAHtWh0W3O3rMRxcngACSwADJHFiGgmyhtppUJ4YHwQ',
	'CAACAgIAAxkBAAIDpWB5O0Dpk2L9TmVBJSBqAVQULuiwAAJEAAMkcWIaKP-GQBO4Gi4fBA',
	'CAACAgIAAxkBAAIDp2B5O0GWHW_XGYrOU3tAY2kUDdE5AAJHAAMkcWIaRDNBRXqiQAUfBA',
	'CAACAgIAAxkBAAIDqWB5O0IeOjsBvnZH5pBOPoeWqZ-5AAJOAAMkcWIaM5x6pJsdnn0fBA',
	'CAACAgIAAxkBAAIDq2B5O0JYCnZg92JCssZ_oOpsMs2HAAJIAAMkcWIasrl3SqTDeQcfBA',
	'CAACAgIAAxkBAAIDrWB5O0NP_PmirLnP5QwvkhM702DAAAJKAAMkcWIaC4dFUswxNZAfBA',
	'CAACAgIAAxkBAAIDr2B5O0REPu7_05smE8rtPNKxeijTAAI8AAMkcWIaabO2zx1zr50fBA',
	'CAACAgIAAxkBAAIDsWB5O0UoaXFbDILc2y9NUsMq6-dAAAJQAAMkcWIa7BKntj5DTM4fBA',
	'CAACAgIAAxkBAAIDs2B5O0URbQ4W5kfHi7htmj8cZUQKAAI9AAMkcWIaam2lpfVTfrofBA',
	'CAACAgIAAxkBAAIDtWB5O0jWKp8RorCE1aL3hphI80NGAAMBAAL3AsgPRrWfLIs5XUsfBA',
	'CAACAgIAAxkBAAIDt2B5O0k0VZo_xKLE13UYT9b24QtDAAL6AAP3AsgPcgN0rrC8YjIfBA',
	'CAACAgIAAxkBAAIDuWB5O0pccTAlN5pcZudlKbic8mbEAAL3AAP3AsgP0JfeP4rRPA4fBA',
	'CAACAgIAAxkBAAIDu2B5O0qdU1ft5iHtFb1BMNma8untAAL5AAP3AsgP9zQfNR3ox5QfBA',
	'CAACAgIAAxkBAAIDvWB5O0sriw-GnqXBM9TVppqk8jeHAAL8AAP3AsgP4krCZ6WVKu4fBA',
	'CAACAgIAAxkBAAIDv2B5O0wfVHgyRoejjjp7rlMWC-KTAALyAAP3AsgPv9o9irIBGMofBA',
	'CAACAgIAAxkBAAIDwWB5O0xnZuQPIlRylUW4Og4odjyzAAIJAQAC9wLIDxTRAAGAHs0QzR8E',
	'CAACAgIAAxkBAAIDw2B5O03EjrEwQ7N4W_eYw855gHVBAALzAAP3AsgPhnmk5pbwEy4fBA',
	'CAACAgIAAxkBAAIDxWB5O07g5Hwx8eMevHC01Vff6D4mAAL1AAP3AsgPR0aYYdFQyLEfBA',
	'CAACAgIAAxkBAAIDx2B5O09BBPhSVQjkfX7VuF8UJXX3AAL2AAP3AsgPR6sHvPRvfEUfBA',
	'CAACAgIAAxkBAAIDyWB5O1DvJOs_PkgVKZna9P7rKLflAAL7AAP3AsgPBko1ZNitKK8fBA',
	'CAACAgIAAxkBAAIDy2B5O1BMk1f8jZOaWv3r6GWvB1NsAAL9AAP3AsgPAt3mLW3TR9YfBA',
	'CAACAgIAAxkBAAIDzWB5O1GxPBaCMjrY-TmpgfzyLWjhAAL-AAP3AsgP3-aiC34PENYfBA',
	'CAACAgIAAxkBAAIDz2B5O1KmH8fbC534tiaZxxP7G6SmAAL_AAP3AsgPPtD0Q46sx-gfBA',
	'CAACAgIAAxkBAAID0WB5O1IKZHrOy-Cn7bXPaToqERCDAAIBAQAC9wLID74G3SutWOIkHwQ',
	'CAACAgIAAxkBAAID02B5O1OuesbtQW89L09h4EUm9ILtAAICAQAC9wLID0hlbS1v8yGcHwQ',
	'CAACAgIAAxkBAAID1WB5O1WwA-c9SOfxjLGxZ8dlR5z9AAIDAQAC9wLIDxRk0fMksG_QHwQ',
	'CAACAgIAAxkBAAID12B5O1WBmgibY54o9cIJ5wlwfUnbAAIEAQAC9wLIDyAPdzvpq8hJHwQ',
	'CAACAgIAAxkBAAID2WB5O1aEupj79FjHl6-VhJJZp6G7AAIFAQAC9wLID9HldLdGJaShHwQ',
	'CAACAgIAAxkBAAID22B5O1bYY0vsaE8kz1mZdM3onDRdAAIGAQAC9wLIDze9PVBIAAFjkh8E',
	'CAACAgIAAxkBAAID3WB5O1fyDf_7eryCZu6wo6mourWbAAIIAQAC9wLID90BAAHsytBr5R8E',
	'CAACAgIAAxkBAAID32B5O1iqqf0KOwZT0qpNidOSDK-WAAIKAQAC9wLID_9wnXyYvO8kHwQ',
	'CAACAgIAAxkBAAID4WB5O1gGud_QEicF43v09UjTBzXyAAILAQAC9wLID8X0O5iVqnHbHwQ',
	'CAACAgIAAxkBAAID42B5O1kH7OvwqmYMHPoQc8zLnr5FAAIMAQAC9wLIDxsTqjMbQvqzHwQ',
	'CAACAgIAAxkBAAID5WB5O1r_y4hH_YslqNr_OhzSWxk4AAIHAQAC9wLID1LOip0jBN7DHwQ',
	'CAACAgIAAxkBAAID52B5O2MuSVDQDKRlY9MmsWQbTnaBAAIBAAPANk8TGC5zMKs_LVEfBA',
	'CAACAgIAAxkBAAID6WB5O2Pyno3ZLf2eeozeWXPVlucXAAICAAPANk8TCPVuRfqEp1kfBA',
	'CAACAgIAAxkBAAID62B5O2QWPkODc9DgfzMHRzIO5EilAAIVAAPANk8TzVamO2GeZOcfBA',
	'CAACAgIAAxkBAAID7WB5O2QHOeEAAQpkdrc_dHCoE6bQDAACAwADwDZPE6Qp7uZ988B4HwQ',
	'CAACAgIAAxkBAAID72B5O2XA9ExOZFGvR97hEvVV2U4gAAIFAAPANk8T-WpfmoJrTXUfBA',
	'CAACAgIAAxkBAAID8WB5O2Z1l-zEzrK4CWsx_JOGFjukAAIGAAPANk8Tx8qi9LJucHYfBA',
	'CAACAgIAAxkBAAID82B5O2fvMxUkx1kSYvDmwJg4kB5sAAIHAAPANk8TSGF3UwinIscfBA',
	'CAACAgIAAxkBAAID9WB5O2d_hRxPLBngRo6Yqcjfk7d2AAITAAPANk8TqrOH9384yqUfBA',
	'CAACAgIAAxkBAAID92B5O2hAVgsPdtwwND6IHIcNIT7rAAIIAAPANk8Tb2wmC94am2kfBA',
	'CAACAgIAAxkBAAID-WB5O2n2CjoBkYs4VeB-BCWKKxxRAAIRAAPANk8TDaqzD9wePuUfBA',
	'CAACAgIAAxkBAAID-2B5O2p4ExSZJOCWZ_B7Dtp8jwwNAAIJAAPANk8T780bokr_cZUfBA',
	'CAACAgIAAxkBAAID_WB5O2qf4mjmgu0swn80QOyZchJxAAIQAAPANk8T6oGKKfEfAugfBA',
	'CAACAgIAAxkBAAID_2B5O2xbTKVyarQbRr8uBdkUviBUAAIKAAPANk8T_w2uPugO_QgfBA',
	'CAACAgIAAxkBAAIEAWB5O20ZehlFFPKj2IulITFrA5eZAAILAAPANk8TCPiv2Fk4yTMfBA',
	'CAACAgIAAxkBAAIEA2B5O22X3b_vxahubGY01_X7bbi3AAISAAPANk8TM7yeAS6VBzcfBA',
	'CAACAgIAAxkBAAIEBWB5O27qiu6XByLc5FXoryfUxP3SAAIMAAPANk8T4s8j_8J3n7wfBA',
	'CAACAgIAAxkBAAIEB2B5O2_oO_ApzlAVfr0lVTROa9LRAAINAAPANk8TpPnh9NR4jVMfBA',
	'CAACAgIAAxkBAAIECWB5O3C5AtTXi5bf_J64ECm1Tv1PAAIOAAPANk8TI1cURIdu1mUfBA',
	'CAACAgIAAxkBAAIEC2B5O3BdKHUQPcIr2iqkuElRJ8NXAAIPAAPANk8TBejUhfLUDp8fBA',
	'CAACAgIAAxkBAAIEDWB5O3HpyxNaWl9h0g8h6F-wetpHAAIUAAPANk8TrWWZ5Lkw9j4fBA',
	'CAACAgIAAxkBAAIED2B5O3IHf1oIRcc27bsUlyVBAAGycwACFgADwDZPE2Ah1y2iBLZnHwQ',
	'CAACAgIAAxkBAAIEEWB5O3K5LjkRVdEOSg4UzSMjMw9vAAIYAAPANk8T1vonv5xqGPgfBA',
	'CAACAgIAAxkBAAIEE2B5O3OcRXcICOi1Riv9WiBoqEJ2AAIZAAPANk8T0EOA9iBXFEsfBA',
	'CAACAgIAAxkBAAIEFWB5O3Ro7TryngABtdeAXt1kstht5QACGgADwDZPE4LbsLU8BkFXHwQ',
	'CAACAgIAAxkBAAIEF2B5O3QbOrz5GAuYXsb2cMxFVWzSAAIbAAPANk8Tfb2Kg8tETWofBA',
	'CAACAgIAAxkBAAIEGWB5O3UE_f-PMwsQL8W3iOJFj7ZlAAIcAAPANk8TwYIa0yz-DuEfBA',
	'CAACAgIAAxkBAAIEG2B5O3bDd6SKwZZphLFvr3z45hInAAIdAAPANk8TXtim3EE93kgfBA',
	'CAACAgIAAxkBAAIEHWB5O3aBeYvU2CJCrni0EOLTFJx9AAIeAAPANk8ToWBbLasAAd4EHwQ',
	'CAACAgIAAxkBAAIEH2B5O3f869o72EQ3bsz4zkeYQxg2AAIfAAPANk8T5Dgz94RSmZIfBA',
	'CAACAgIAAxkBAAIEIWB5O3j72D2V9uJC4XDDOzTRdLx1AAIgAAPANk8T9A8ruj5f9M8fBA',
	'CAACAgIAAxkBAAIEI2B5O3lXWVOdksFCetcn8TDzx1VnAAJaAAPANk8TC_wPT9xGGeEfBA',
	'CAACAgIAAxkBAAIEL2B5QmqrKD-kA5Fmnd0enkAdClqyAAKsCgACXUbpSo4XJwJu2nnNHwQ',
	'CAACAgIAAxkBAAIEMWB5QnLDoJB1OBY0MQ7EYeF7sps5AAIHDAACFYXoStVnavRui1yVHwQ',
	'CAACAgIAAxkBAAIEM2B5QnY5MJCWYYM_avLbGWR5X74eAAKsCgACXUbpSo4XJwJu2nnNHwQ',
	'CAACAgIAAxkBAAIENWB5QnfpHIEwsxMZrvwFkVgZ-_dNAALbDQACtDIAAUopejqONpdQhh8E',
	'CAACAgIAAxkBAAIEN2B5QndUAsja-KE5GJv6LlgLVLOMAAIUDAACT44AAUpDseaNpfXX2x8E',
	'CAACAgIAAxkBAAIEOWB5QniIQv1V4GGHxJAo4M71VT14AAIhDQACJbHpSkIGtxqjnYp4HwQ',
	'CAACAgIAAxkBAAIEO2B5Qnn6eznrW10TnqZpAU1pBsBjAAJeDgACxnIAAUp_u5hCDprnfR8E',
	'CAACAgIAAxkBAAIEPWB5QnoDFTdlP_GKuO-k06wpgjLNAAIkDgACcB7gSqzl42xcG1oeHwQ',
	'CAACAgIAAxkBAAIEP2B5QnoQws91UujYem-F7EdRir9mAAL9DQAC6BwAAUrEhyo9WU4NPR8E',
	'CAACAgIAAxkBAAIEQWB5Qnsq6ampgoY3NTicKPBjs0D4AAIEDAACducAAUq9HT75BIYRZR8E',
	'CAACAgIAAxkBAAIEQ2B5QnxQzflsbZoBzjtYQAV-2K-pAAIaDAACRTR5SjpcnyBhKubIHwQ',
	'CAACAgIAAxkBAAIERWB5Qnz7GAqQBDxuOXkqEotu6Ex9AALbCgAC46TgSkiTdQyDG_NKHwQ',
	'CAACAgIAAxkBAAIER2B5Qn0EyBl8Pwps4K8flCDUx2h_AAKyCAACHxfpStCwLe7qBpdLHwQ',
	'CAACAgIAAxkBAAIESWB5Qn4KhDaSwzdQtjN16jx6n1mWAALQDAACfEfoSqRm0c_iN5naHwQ',
	'CAACAgIAAxkBAAIES2B5Qn-8Sbz6V1QuU_Z9iat7ZxeQAALIDgACGdrpSmdw7bJ9PdkpHwQ',
	'CAACAgIAAxkBAAIETWB5Q4Qs1_1NdrRP2EnjlD_gycxYAALhDQACMQyYSrKI3Zujr4leHwQ',
	'CAACAgIAAxkBAAIET2B5Q4ef9SCUaDJbW-aAmZLaDCinAAKzCwACKlBRSiyjtgnsadPWHwQ',
	'CAACAgIAAxkBAAIEUWB5Q4pPvReP7lxSC4PvSZK5lj-iAAI2AQAC9wLID8fiDh2KfjbgHwQ',
	'CAACAgIAAxkBAAIEU2B5Q43qCcydhAPuH2nXszCc5Q_EAAJSDAACWKA5SiLsOEtVOw2yHwQ',
	'CAACAgIAAxkBAAIEVWB5Q48ejy_MndAv-1eRgpeT4EpwAAInAQAC9wLID-9HhEodcwYsHwQ',
	'CAACAgIAAxkBAAIEV2B5Q5BfIT_9CsAeCAuSnwoqtxDKAAKxCgACJY7BSRAufHAmXj1kHwQ',
	'CAACAgIAAxkBAAIEWWB5Q5AwF96GtDK8ZLzuYkiNzMgNAAI5AQAC9wLID86ar9wQ5OpbHwQ',
	'CAACAgIAAxkBAAIEW2B5Q--QZNiQlRMe1q89o9jBPlbPAAIdDQACTPS5SkmsZZ3HCwMQHwQ',
	'CAACAgIAAxkBAAIEXWB5Q_EvDZIizwlD5sVhLYKlSvFVAALBCwAC757RSZjFilQiIkvZHwQ',
	'CAACAgIAAxkBAAIEX2B5Q_gxdPACQ7vXBT9r1E1NX2s_AAI6AQAC9wLIDzzYR8AMHMjcHwQ',
	'CAACAgIAAxkBAAIEYWB5Q_ySt1O9KSnSZ573622oOsxdAAIzAQAC9wLIDzvK4ZTu2U7NHwQ',
	'CAACAgIAAxkBAAIEY2B5Q_3xLmWwYZuBHbZK2PnldJMuAAIvAQAC9wLIDwfqmQdeqOyEHwQ']
	bot.send_sticker(message.chat.id, random.choice (stickers))
	print(message.sticker.file_id)
#-----------------------------sticker-----------------------------------

print('#run bot...')
bot.polling()
