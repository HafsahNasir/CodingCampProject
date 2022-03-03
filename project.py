import collections       


# This program basically takes input from the user about what ingredients they have, and will give them some suggested recipies
# The user can then choose which recipie they want to make and then the chosen recipie will be displayed


# -------------------------------------------- Recipies Starting ------------------------------------------------------------------
# Most of the recipies are from https://www.biggerbolderbaking.com/
# Other recipies are my own or are recipies I found a long time ago and can't find the sources

cheescake = """ 
Ingredients: 
   Crust:
     • 200g Biscuits 
     • 100g Butter
    Cheescake:
     • 339 g cream cheese 
     • 75 g sugar 
     • 1/3 tsp vanilla 
     • Juice of 1 lemon
     • 1.5 large eggs 
     • 12 g flour

Method:
• Preheat the oven to 350°F (180°C).
• In a small bowl mix together the cookie crumbs and melted butter. Press into a springform tin. Place in the fridge to chill.
• Using a stand mixer or an electric hand mixer, whisk the cream cheese and sugar together on high speed until smooth and there are no lumps.
• Add in the vanilla and lemon juice.
• Slowly add in the eggs one at a time until fully blended. At this point, your mix should be nice and airy from all the mixing.
• Add in the flour and mix until combined.
• Bake for about 70-80 minutes. You will know when it is done when there will still be a slight jiggle in the middle. Set aside to cool. TIP: Place a baking pan with hot water on the shelf below the cheesecake as it bakes. This will help avoid a cracked cheesecake.
• While still in the tin place the cheesecake in the fridge to chill for a minimum of 5 hours but preferably overnight

"""

chocolate_cake = """
Makes 2, 8-inch cakes or 24 cupcakes
Ingredients
• 2 cups flour
• 1 tsp baking powder
• 1 tsp baking soda
• 2 tbsp cocoa powder
• ½ tsp salt
• 2 cups sugar
• 170g butter (softened)
• 1 ½ cups milk
• 3 large eggs
• 1 tsp vanilla extract
• 1 tsp instant coffee
• 2oz semi-sweet chocolate (melted)

Method
• Preheat oven to 180°C
• Line tins with parchment paper and grease.
• Combine the flour, baking powder, baking soda, cocoa powder, and salt together and mix well
• Add the sugar and butter and beat with a stand mixer or an electric whisk till the mixture is pale and fluffy. Roughly 7-10 min.
• Mix the milk, eggs, vanilla, and coffee (brewed in a little bit of water).
• Once the sugar and butter have creamed, add in the flour in three additions and the wet ingredients in two additions. Starting and ending with the dry ingredients.
• Once the batter has been evenly incorporated, add in the melted chocolate and give it one final mix.
• Distribute amongst the tins and bake for 25-30 min, or until a skewer inserted comes out clean.

"""
brownies = """
Ingredients:
• 225g butter (melted and cooled)
• 2 tbsp vegetable oil (coconut or canola)
• 177g brown sugar
• 227g white sugar
• 4 large eggs (room temperature)
• 2 tsp vanilla extract
• 142g flour
• 115g unsweetened cocoa powder 
• 1 teaspoon salt
• 255g roughly chopped chocolate or chocolate chips

Method
• Preheat the oven to 350°F (175°C) then line a 9x9 inch baking tray with parchment paper and set it aside. 
• In a large bowl combine melted butter, oil, and both sugars.
• Add the eggs, vanilla and salt then whisk for about one minute until evenly combined and light in colour.
• Over the same bowl sift in the flour and cocoa powder. Gently fold the dry ingredients into the wet ingredients until JUST combined (do NOT over mix). Fold in half of the chocolate chunks.
• Pour the batter into the prepared pan, then smooth the top. Generously top with the remaining chocolate chunks.
• Bake for 35-40 minutes, or until the center of the brownies no longer jiggles and is JUST set to the touch.
• Remove from the oven and allow to cool to room temperature before removing from the baking tray and slicing.

"""
shortbread_cookies = """
Ingredients:
• 2 cups (256g) all-purpose flour
• 1 cup (115g) powdered sugar
• 3/4 teaspoon salt
• 1 cup (227g) unsalted butter, room temp and cut into pieces

Method
• Preheat the oven to 325°F and line 3 baking sheets with parchment paper.
• Place the flour, powdered sugar, salt, and butter into the bowl of a food processor and pulse until all of the butter is incorporated, about 10 to 15 one-second pulses, but could be more depending upon your food processor. It’s ready when the mixture looks like wet sand and clumps together when pressed. Stop when the mixture begins to climb up the bowl. 
• Dump everything onto the counter and gently press it together into a crumbly mound. I use a flexible bowl scraper to scoop and press the mound together at first, then knead the dough a few times and form it into a square shape. 
• Roll the dough out on a well-floured surface to 1/4- to 1/2-inch thickness (depending on how thick you like your cookies) and either use a knife to cut out rectangles or use a cutter to make shapes. 
• Transfer the cookies to one of the parchment-lined baking sheets. Chill the cookies on the sheet pan in the freezer for 15 minutes or until the cookies are solid to the touch. Transfer the frozen cookies, in batches, onto the other baking sheets, leaving about 1/2 inch between each cookie. 
• Bake the cookies, one pan at a time, for 15-18 minutes, or until the cookies are dry to the touch and the bottoms just begin to turn golden. 
• Remove from the oven and cool on a rack before transferring to a container for storage. The baked and cooled cookies can be stored in an airtight container for several days.

"""
cinnamon_rolls = """
Ingredients:
  Dough: 
    • 240g flour
    • 1 tsp salt
    • 1 ½ tsp instant dried yeast
    • 89g milk
    • 45g water
    • 1 large eggs
    • 17g honey
    • 30g melted butter

  Filling:
    • 60g melted butter
    • 105g brown sugar
    • 1 ¼ tbsp ground cinnamon

Method:
• To make the dough, combine all of the dry ingredients in a very large bowl.
• In a separate jug add in the milk, water, honey, and butter. Heat it in the microwave until it is warm (at blood temperature) and the butter has melted. Whisk in the eggs quickly.
• Stir the wet into the dry to make a soft dough. You can simply mix with a spoon until there are no flour lumps yet. Scrape down the dough from the sides of the bowl. Just add sufficient liquid to bring the dough together to a soft but not wet dough. 
• Cover the bowl, and let the dough rise for 2 hours at cool room temperature. It will triple in size
• After this, refrigerate the dough for at least 8 hours, preferably overnight. It can be refrigerated for up to 3 days before use.
• When you're ready to make your cinnamon rolls, make the filling. Combine the butter, brown sugar, and cinnamon in a bowl. Stir until smooth. Set aside.
• Transfer the dough to a floured work surface and roll it into a rectangle approximately 1/4" thick. It will be long so you can always do it in 2 goes.
• Spread the filling over the dough, leaving a narrow margin around the edges uncovered.
• Starting with a long edge, gently roll the dough into a log. Don't roll it too tightly; if you do, the centers of the buns will pop up as they bake.
• Slice the rolls 2” thick and set them with their cinnamon face up
• In a deep baking pan lined with parchment space the buns in the pan.
• Cover the pan and allow the rolls to rise until they're have grown into each other and are puffed up, about 30 minutes to an hour. (Depending on how hot your kitchen is.)
• (Towards the end of the rising time, preheat the oven to 375°F/ 190°C)
• Uncover the pan, and bake the buns for 40 to 45 minutes, till they're a deep golden brown. Rotate the tray during baking so they can get golden brown all over.
• Remove the pan from the oven and let it rest for 20 minutes. Once cooled remove from the pan and onto a cooling rack.

"""

churros = """
Ingredients:
• 1 cup water
• 85g butter
• 2 tbsp sugar
• 1 tsp vanilla
• 1 cup flour
• 1 tsp salt
• 2 large eggs
• Cinnamon Sugar ( ¼ cup sugar + ½ tbsp cinnamon)
• Oil (for frying)

Method:
• In a large saucepan over medium heat, add water, butter, and sugar. Bring to a boil, then add vanilla. Turn off heat and add flour and salt. Stir with a wooden spoon until thickened, 30 seconds. Let mixture cool for 10 minutes. 
• To cooled mixture, using a hand mixer, beat in eggs one at a time until combined. Transfer mixture to a piping bag fitted with a large open star tip. 
• In a large pot over medium heat, add enough oil to come halfway up the sides and heat to 375°F. Holding the piping bag a few inches above the oil, carefully pipe churros into long ropes. Use kitchen scissors to cut off dough from piping bag. 
• Fry until golden, 4 to 5 minutes, turning, as necessary. Fry 3 to 4 churros at a time and let oil come back to 375°F before each batch. 
• Remove churros with a slotted spoon or tongs and immediately roll churros in cinnamon sugar, then place on a cooling rack. 

"""
donuts = """
Ingredients
• 454g all-purpose flour
• 57g granulated sugar
• 2 ¼ tsp active dried yeast
• 1 tsp salt
• 1 cup + 1 tbsp (8floz/225ml) whole milk
• 57g butter
• 1 tsp vanilla extract
Method
• Mix the flour, sugar, yeast, and salt together in a standing mixer fitted with a dough hook.
• In a measuring jug, heat together the milk and butter until the butter has melted. Stir in the vanilla.
• Turn the machine on low and slowly add the milk mixture until your dough comes together to form a ball. If your dough is a little dry add a splash more milk.
• Increase the speed to medium and mix until the dough is shiny and smooth, 6-8 minutes. The dough is supposed to be saggy.
• Rub your mixing bowl with vegetable oil. Place the dough in the bowl and turn to coat lightly.
• Cover the bowl with plastic wrap tightly and let the dough rise until doubled, roughly 2 hours.
• Once it has risen, turn out the fluffy dough onto a floured work surface. Roll out to ½ inch thick
• Using a 3 inch round cutter, cut off your circles. Then cut out the donut holes with a much smaller cutter. You will get 12-14 donuts. TIP: You can prepare the donuts to this stage and put them in the refrigerator until the next day. When needed, take out and let me come to room temp and rise a little (roughly 30 minutes) and then fry off as instructed below.
• Cover your donuts with cling film and let them rise at room temperature for 20-30 minutes. Then fry in 180 C oil, for 2-3 minutes per side



Chocolate Donut Glaze
Ingredients
• 86g powdered sugar
• 2 tbsp unsweetened cocoa powder
• 1 ½ tbsp milk
• ½ tsp pure vanilla extract

Methods
• In a medium bowl, whisk together powdered sugar and cocoa powder. Slowly stir in milk and vanilla extract. Whisk until silky and smooth. If you need a touch more milk to make this a dippable glaze, add a bit more.
• Dip doughnuts in chocolate glaze and let rest to harden slightly.
"""
# -------------------------------------------- Recipies Over ------------------------------------------------------------------

# writing out ingredients needed for each recipie
recipie_ingredients = {
"cheescake":['biscuits','butter', 'cream cheese', 'sugar', 'vanilla extract', 'eggs', 'flour'],
"chocolate cake": ['flour', 'baking powder', 'baking soda', 'cocoa powder','sugar', 'butter', 'milk', 'eggs', 'vanilla extract', 'instant coffee', 'chocolate'],
"brownies": ['butter', 'oil', 'brown sugar', 'sugar', 'eggs', 'vanilla extract', 'flour', 'cocoa powder', 'chocolate'],
"classic shortbread cookies": ['flour', 'icing sugar', 'butter'],
"cinnamon rolls":['flour', 'yeast', 'milk', 'eggs', 'honey', 'butter', 'cinnamon'],
"churros":['butter', 'sugar', 'vanilla extract', 'flour', 'eggs', 'cinammon', 'oil - for frying'],
"donuts": ['flour','sugar', 'yeast', 'milk', 'butter', 'vanilla extract', 'icing sugar', 'cocoa powder', 'milk'],
}

#initialising a few lists and dictionaries
possible_recipies = []
dict_missing_ingredients = collections.defaultdict(list)
missing_ingredients = {}
availible_ingredients = []

#list of possible ingredients the user can choose from
ingredients = ['flour','baking soda', 'baking powder', 'yeast','sugar','brown sugar', 'icing sugar','butter', 'eggs', 'milk', 'vanilla extract','chocolate', 'cream cheese', 'biscuits', 'cocoa powder']
print("These are all the ingredients you can chose from: ")
print(ingredients)


#taking input from user
print("Please enter the names of the items you have and press 'x' when done")
counter = len(ingredients)
while counter > 0:
    chosen = input()
    chosen = chosen.lower()
    if chosen == 'x':
        break
    if chosen in ingredients and chosen not in availible_ingredients:
        availible_ingredients.append(chosen)
        counter = counter - 1
    else:
        print("incorrect input")


#deciding which recipies are possible, using the criteria that if the recipie has less than 3 missing ingredients its possible
for recipie in recipie_ingredients:
    missing_ingredients_count = 0
    for ingredient in recipie_ingredients[recipie]:
        if ingredient not in availible_ingredients:
            missing_ingredients_count += 1
    if missing_ingredients_count <= 3:
        possible_recipies.append(recipie)

#making a dictionary that goes {"recipie name", [list of recipie's missing ingredients]}
for recipie in possible_recipies:
     for ingredient in recipie_ingredients[recipie]:
        if ingredient not in availible_ingredients:
             dict_missing_ingredients[recipie].append(ingredient)

missing_ingredients = dict(dict_missing_ingredients)

# Making a dictionary that goes {1, 'possible recipie 1': 2, 'possible recipie 2'...}
dict_possible_recipies = {}
keys_possible_recipies = []

for x in range(len(possible_recipies)):
    keys_possible_recipies.append(x+1)
    dict_possible_recipies[keys_possible_recipies[x]] = possible_recipies[x]

#print statement showning possible recipie options and missing ingredients for each recipie
print("The possible recipies you can make are:")
print("")
for recipie_no in dict_possible_recipies:
    print("Option",str(recipie_no) + ".", dict_possible_recipies[recipie_no])
    print("If you have the following ingredients:")
    recipie = dict_possible_recipies[recipie_no]
    for ingredient in range(len(missing_ingredients[recipie])):
        print(missing_ingredients[recipie][ingredient])
    print("")

#taking in input for which recipie they want to make and valiating input
chosen_recipie_no = int(input("Please enter the recipie number you want to make: "))
user_input = False
while user_input == False:
    if chosen_recipie_no > (len(possible_recipies)+1):
        print("incorrect input, please input again")
        chosen_recipie_no = int(input("Please enter the recipie number you want to make: "))
    else:
        user_input = True
        break


#printing recipie string corresponding to user input
chosen_recipe = dict_possible_recipies[chosen_recipie_no]
if chosen_recipe == "cheescake":
    print(cheescake)
elif chosen_recipe == "chocolate cake":
    print(chocolate_cake)
elif chosen_recipe == "brownies":
    print(brownies)
elif chosen_recipe == "classic shortbread cookies":
    print(shortbread_cookies)
elif chosen_recipe == "cinnamon rolls":
    print(cinnamon_rolls)
elif chosen_recipe == "churros":
    print(churros)
elif chosen_recipe == "donuts":
    print(donuts)
else:
    print("error")

