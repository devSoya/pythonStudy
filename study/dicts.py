player = {
  'name' : 'any',
  "age" : 12,
  'alive' : True,
  'fav_food' : ["🍔","🍕"]
}

print(player)
print(player.get('age'))
player.pop('age')
print(player['fav_food'])
print(player)
player['xp'] = 1500
print(player)
player['fav_food'].append("🍜")
print(player.get('fav_food'))
print(player['fav_food'])
