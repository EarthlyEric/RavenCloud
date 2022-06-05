import random


def easter_egg():
    style = """
        <style>
            html{
                background-image: url("/img/easter_egg.gif");
                background-repeat: no-repeat, repeat;
                background-position:bottom left;
                background-size: 134px 187px;
                }
        </style>
        """
    choice = random.choice([True, False])
    if choice == True:
        return style
    elif choice == False:
        None