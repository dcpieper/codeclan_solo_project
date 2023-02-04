import pdb
from models.game import Game
from models.publisher import Publisher

import repositories.game_repository as game_repository
import repositories.publisher_repository as publisher_repository

game_repository.delete_all()
publisher_repository.delete_all()

game1 = Game("Dawn of War", "Relic", "THQ", "RTS", 15, 35, 50)
game_repository.save(game1)
game2 = Game("Star Wars: Battlefront", "Pandemic Studios", "EA", "FPS", 15, 35, 22)
game_repository.save(game2)
game3 = Game("World of Warcaft", "Blizzard", "Activision", "MMORPG", 10, 30, 9)
game_repository.save(game3)
game4 = Game("Knight's of the Old Republic", "Bioware", "Lucasarts", "RPG", 18, 35, 4)
game_repository.save(game4)

game_repository.select_all()

publisher1 = Publisher("THQ", "actuallyok@thq.com")
publisher_repository.save(publisher1)
publisher2 = Publisher("EA", "wastedstarwarsexclusivity@ea.com")
publisher_repository.save(publisher2)
publisher3 = Publisher("Activision", "bobbykoticksyachtfund@activision.com")
publisher_repository.save(publisher3)
publisher4 = Publisher("Lucasarts", "soldouttodisney@lucasarts.com")
publisher_repository.save(publisher4)

pdb.set_trace()

