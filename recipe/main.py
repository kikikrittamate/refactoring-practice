from recipe import Recipe


# replace redundant code with creational method
def create_recipe(name, chocolate=0, coffee =0, sugar=0, milk=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    return recipe



if __name__ == '__main__':

    recipe1 = create_recipe("Coffee with sugar")
    recipe1.coffee = 4
    recipe1.sugar = 2
    recipe1.milk = 0
    recipe1.price = 30.0
    print(recipe1)

    recipe2 = create_recipe("Latte")
    recipe2.coffee = 3
    recipe2.sugar = 2
    recipe2.milk = 1
    recipe2.price = 40.0
    print(recipe2)


    recipe3 = create_recipe("Hot Chocolate")
    recipe3.coffee = 0
    recipe3.chocolate = 3
    recipe3.sugar = 2
    recipe3.milk = 4
    recipe3.price = 30.0
    print(recipe3)
    
