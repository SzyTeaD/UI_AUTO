from config.pathes import PROJECTINFO
from utils.FileReader import YamlReader

c = YamlReader(PROJECTINFO).get('OA').get('mail')['senduser']
print(c)

