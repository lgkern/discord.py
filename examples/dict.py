import json
 
class DictionaryReader:
	
	def __init__(self):
		self.file = 'dictEntries.txt'
		self.dictionary = {}
		self.loadDict()
		self.loop = 0
		
	def loadDict(self):
		try:
			with open(self.file, 'r') as f:
				s = f.read()
				self.dictionary = json.loads(s)
		except Exception:
			return
	
	def readEntry(self, entry):
		self.loop = self.loop + 1
		if self.loop > 10
			return "Loop error!\nLikely an issue with my dictionary database.\n*pokes* @Anshlun#1497 Fix me! "
		fixed = self.fixEntry(entry)
		print(fixed)
		if fixed in self.dictionary:
			while fixed in self.dictionary:
				fixed = self.dictionary[fixed]
			return fixed
		else:
			print(entry.split('.')[0]+".invalid")
			return self.readEntry(entry.split('.')[0]+".invalid")
            
            
			
	def fixEntry(self, entry):
		result = entry.lower()
		#Head
		result = result.replace("helm","head",1)
		#Neck
		result = result.replace("amulet","neck",1)
		result = result.replace("necklace","neck",1)
		#Shoulder
		result = result.replace("shoulders","shoulder",1)
		#Cloak
		result = result.replace("cloak","back",1)
		#Chest
		result = result.replace("robe","chest",1)
		#Wrist
		result = result.replace("wrists","wrist",1)
		result = result.replace("bracer","wrist",1)
		result = result.replace("bracers","wrist",1)
		#Gloves
		result = result.replace("hands","gloves",1)
		#Waist
		result = result.replace("belt","waist",1)
		#Legs
		result = result.replace("leggings","legs",1)
		#Feet
		result = result.replace("boots","feet",1)
		result = result.replace("foot","neck",1)
		#Ring
		result = result.replace("finger","ring",1)
		#Trinket
		#Weapon
		#Off-hand
		
		#Specs
		if "ord" not in result:
			if "discipline" not in result:
				result = result.replace("disc","discipline",1)
		return result
		
	def commandReader(self, params):
		return self.readEntry('.'.join(params))
    
	def itemReader(self, params):
		result = self.commandReader(params)
		if 'Invalid' in result:
			if params[1].isdigit():
				return 'https://legion.wowhead.com/item='+params[1]
		return result