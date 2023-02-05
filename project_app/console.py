import pdb
from models.game import Game
from models.publisher import Publisher

import repositories.game_repository as game_repository
import repositories.publisher_repository as publisher_repository

game_repository.delete_all()
publisher_repository.delete_all()

publisher_1 = Publisher("THQ", "actuallyok@thq.com")
publisher_repository.save(publisher_1)

publisher_2 = Publisher("EA", "wastedstarwarsexclusivity@ea.com")
publisher_repository.save(publisher_2)

publisher_3 = Publisher("Activision", "bobbykoticksyachtfund@activision.com")
publisher_repository.save(publisher_3)

publisher_4 = Publisher("Lucasarts", "soldouttodisney@lucasarts.com")
publisher_repository.save(publisher_4)

game_1 = Game("Dawn of War", "Relic", publisher_1, "RTS", 15, 35, 50)
game_repository.save(game_1)

game_2 = Game("Star Wars: Battlefront", "Pandemic Studios", publisher_2, "FPS", 15, 35, 22)
game_repository.save(game_2)

game_3 = Game("World of Warcaft", "Blizzard", publisher_3, "MMORPG", 10, 30, 9)
game_repository.save(game_3)

game_4 = Game("Knight's of the Old Republic", "Bioware", publisher_4, "RPG", 18, 35, 4)
game_repository.save(game_4)

pdb.set_trace()

