# Useful python emacs mode commands:
# C-M-a or e: Go to beginning or end of block
# C-M-h: Mark function/class
# C-c C-k: Mark block
# C-c TAB: Indent region
# C-c #: Comment region

# C-M-x: execute block
# C-c C-c: Execute buffer

from util import *

TileTypes = enum('Wall', 'Cannon', 'Mine', 'Empty')

class Player:
   def __init__(s):
      s.wallCash = 0
      s.cannonCash = 0

   def canBuyWall(s):
      return s.wallCash > 0

   def canBuyCannon(s):
      return s.cannonCash > 0

   def buyWall(s):
      s.wallCash -= 1

   def buyCannon(s):
      s.cannonCash -= 1

P1 = Player()
P2 = Player()

class Tile:
   def __init__(s, owner=None, typ=TileTypes.Empty):
      s.owner = owner
      s.type = typ

# Playing field
class Field:
   def __init__(s):
      s.w = 20
      s.h = 20
      s.tiles = []
      for x in range(s.w * s.h):
         # New empty tile with no owner
         s.tiles.append(Tile())

   # XXX: Bounds checking...
   def get(s, x, y):
      return s.tiles[x + (y*s.h)]

   def set(s, x, y, tile):
      s.tiles[x + (y*s.h)] = tile

   def isWall(s, x, y):
      return s.get(x, y).type == TileTypes.Wall

   def isCannon(s, x, y):
      return s.get(x, y).type == TileTypes.Cannon

   def isMine(s, x, y):
      return s.get(x, y).type == TileTypes.Mine

   def isEmpty(s, x, y):
      return s.get(x, y).type == TileTypes.Empty

   def isAdjacentToOwnedWall(s, player):
      pass
   
   # If you are in an owned space or
   # adjacent to an owned wall...
   def buildWall(s, player,  x, y):
      if not s.isEmpty(x, y):
         return
      else:
         t = s.get(x, y)
         if t.owner == player or isAdjacentToOwnedWall(player):
            if player.canBuildWall():
               player.buyWall()
               s.set(x, y, Tile(player, TileTypes.Wall))

   def buildCannon(s, player, x, y):
      pass


class Drawer:
   def drawField(s, field):
      for i in range(field.w):
         for j in range(field.h):
            s.drawTile(field.get(i,j), i, j)

   def drawTile(s, tile, x, y):
      if tile.type == TileTypes.Wall:
         s.drawWall(tile, x, y)
      elif tile.type == TileTypes.Cannon:
         s.drawCannon(tile, x, y)
      elif tile.type == TileTypes.Mine:
         s.drawMine(tile, x, y)
      elif tile.type == TileTypes.Empty:
         s.drawEmpty(tile, x, y)
      else:
         raise Exception("Impossible tile type!")

   def drawWall(s, tile, x, y):
      pass

   def drawCannon(s, tile, x, y):
      pass

   def drawMine(s, tile, x, y):
      pass

   def drawEmpty(s, tile, x, y):
      pass

def main():
   field = Field()
   draw = Drawer()
   draw.drawField(field)
   print field
   print field.tiles

if __name__ == '__main__':
   main()
