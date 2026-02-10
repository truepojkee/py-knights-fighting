from app.knights.knight import Knight


def battle(knight_config: dict) -> dict:

    # create new king from Class Knight
    lancelot = Knight(knight_config["lancelot"])
    arthur = Knight(knight_config["arthur"])
    mordred = Knight(knight_config["mordred"])
    red_knight = Knight(knight_config["red_knight"])

    # battle Lancelot vs Mordred
    apply_battle_result(lancelot, mordred)
    # Athur vs Red Knight
    apply_battle_result(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def apply_battle_result(hero1: Knight, hero2: Knight) -> None:
    dmg_to_hero1 = max(0, hero2.power - hero1.protection)
    dmg_to_hero2 = max(0, hero1.power - hero2.protection)

    hero1.take_damage(dmg_to_hero1)
    hero2.take_damage(dmg_to_hero2)
