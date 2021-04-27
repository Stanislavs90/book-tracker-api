from rest_framework import serializers
from .models import Book, Character, Author

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        read_only_fields = ('book',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('book',)


class BookSerializer(serializers.ModelSerializer):
    # nested serializer to connect to different models 
    # characters = CharacterSerializer(many=True, read_only=True) 
    # authors = AuthorSerializer(many=True, read_only=True) 

    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True) 

    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'published','characters','authors']


    # look up create function and set() in docs 
    def create(self, validated_data):
        characters = validated_data.pop('characters')
        authors = validated_data.pop('authors')

        book = Book.objects.create(**validated_data)

        for character in characters:
            Character.objects.create(**character,book=book )

        
        for author in authors:
            Author.objects.create(**author, book=book)

        return book

"""
            # example_relationship = validated_data.pop('example_relationship')
            # instance = ExampleModel.objects.create(**validated_data)
            # instance.example_relationship = example_relationship
            # return instance

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name','amount','measurement']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validate_data):
        ingredients = validate_data.pop('ingredients')
        recipe = Recipe.objects.create(**validate_data)
        for ingredient in ingredients:
            Ingredient.objects.create(**ingredient, recipe=recipe)
        return recipe



"""