# DietApp

DietApp is a recipe recommendation system to easily meet fitness goals or plan restrictive diets.

## Structure

- dietapp/: Python source code
- Data/: Users, recipes and rating data, as well a script used to generate some extra ratings
- Media/: Video with a example of use

## Usage

To use DietApp, import dietapp/dietapp.py and use the following functions:
- register_user(age, height, weight, sex, exercise_level, goal): to register a new user
- recommend_recipe(uid): to ask for a recommendation
- rate_recipe(uid, title, rating): to rate a recipe

## Authors

- **Alejandro León Fernández** - [@AlejandroLF](https://github.com/AlejandroLF)
- **Javier Esteban Pérez Rivas** - [@alu0100946499](https://github.com/alu0100946499)
- **Sara Revilla Báez** - [@mizsrb](https://github.com/mizsrb)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
