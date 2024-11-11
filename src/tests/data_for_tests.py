
temp = [
    {
        'id': 1, 'recipe_name': 'Test recipe 1', 'cooking_time': 25,
        'recipe_description': 'Test recipe description 1', 'views': 1, 'ingredients':
        [
            {'name': 'Test ingredient 1', 'description': 'Test ingredient description 1', 'quantity': 'i1 test r1'},
            {'name': 'Test ingredient 2', 'description': 'Test ingredient description 2', 'quantity': 'i2 test r1'},
            {'name': 'Test ingredient 3', 'description': 'Test ingredient description 3', 'quantity': 'i3 test r1'}
        ]
    }
]
print(len(temp[0]['ingredients']))
