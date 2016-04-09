import random

class Randomize:
   def __init__( self, test_mode = False ):
      self.test_mode = test_mode
      random.seed()

   def value( self, lower, upper ):
      if self.test_mode:
         return upper
      return random.randrange(lower, upper + 1)


# Not in test mode
#rand = Randomize()
#print rand.value(20, 40)

# Test mode
#rand = Randomize(True)
#print rand.value(20, 40)
