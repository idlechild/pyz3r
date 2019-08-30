import math


class customizer:
    def convert2settings(
            customizer_save,
            tournament=False,
            spoilers_ongen=False):
        """Converts a customizer-settings.json file from alttpr.com to a settings dictionary that can be used for generating a game.

        Arguments:
            customizer_save {dict} -- A dictionary of the customizer-settings.json file (needs to already be converted to a dict)

        Keyword Arguments:
            tournament {bool} -- Setting to True generates a race rom, which excludes the spoiler log. (default: {False})

        Returns:
            dict -- a dictionary of settings that can be used with pyz3r.alttpr()
        """
        # the settings defaults, hopefully this is accurate
        settings = {
            "item_placement": "advanced",
            "dungeon_items": "standard",
            "accessibility": "items",
            "goal": "ganon",
            "crystals": {
                "ganon": "7",
                "tower": "7"},
            "mode": "standard",
            "weapons": "randomized",
            "item": {
                "pool": "normal",
                "functionality": "normal"},
            "tournament": tournament,
            "spoilers_ongen": spoilers_ongen,
            "lang": "en",
            "name": "",
            "notes": "",
            "l": {},
            "eq": [
                "BossHeartContainer",
                "BossHeartContainer",
                "BossHeartContainer"],
            "drops": {
                "0": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "1": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "2": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "3": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "4": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "5": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "6": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "pull": [
                    "auto_fill",
                    "auto_fill",
                    "auto_fill"],
                "crab": [
                    "auto_fill",
                    "auto_fill"],
                "stun": ["auto_fill"],
                "fish": ["auto_fill"]},
            "custom": {
                "item.Goal.Required": "",
                "item.require.Lamp": False,
                "item.value.BlueClock": "",
                "item.value.GreenClock": "",
                "item.value.RedClock": "",
                "item.value.Rupoor": "",
                "prize.crossWorld": True,
                "prize.shuffleCrystals": True,
                "prize.shufflePendants": True,
                "region.bossNormalLocation": True,
                "region.wildBigKeys": False,
                "region.wildCompasses": False,
                "region.wildKeys": False,
                "region.wildMaps": False,
                "rom.dungeonCount": "off",
                "rom.freeItemMenu": False,
                "rom.freeItemText": False,
                "rom.mapOnPickup": False,
                "rom.timerMode": "off",
                "rom.timerStart": "",
                "rom.rupeeBow": False,
                "rom.genericKeys": False,
                "spoil.BootsLocation": False,
                "spoil.Hints": True,
                "canBombJump": False,
                "canBootsClip": False,
                "canBunnyRevive": False,
                "canBunnySurf": False,
                "canDungeonRevive": False,
                "canFakeFlipper": False,
                "canMirrorClip": False,
                "canMirrorWrap": False,
                "canOneFrameClipOW": False,
                "canOWYBA": False,
                "canSuperBunny": False,
                "canSuperSpeed": False,
                "canWaterFairyRevive": False,
                "canWaterWalk": False,
                "item": {
                    "count": {
                        "BottleWithRandom": 4,
                        "Nothing": 0,
                        "L1Sword": 0,
                        "L1SwordAndShield": 0,
                        "MasterSword": 0,
                        "L3Sword": 0,
                        "L4Sword": 0,
                        "BlueShield": 0,
                        "RedShield": 0,
                        "MirrorShield": 0,
                        "FireRod": 1,
                        "IceRod": 1,
                        "Hammer": 1,
                        "Hookshot": 1,
                        "Bow": 0,
                        "Boomerang": 1,
                        "Powder": 1,
                        "Bombos": 1,
                        "Ether": 1,
                        "Quake": 1,
                        "Lamp": 1,
                        "Shovel": 1,
                        "OcarinaInactive": 1,
                        "CaneOfSomaria": 1,
                        "Bottle": 0,
                        "PieceOfHeart": 24,
                        "CaneOfByrna": 1,
                        "Cape": 1,
                        "MagicMirror": 1,
                        "PowerGlove": 0,
                        "TitansMitt": 0,
                        "BookOfMudora": 1,
                        "Flippers": 1,
                        "MoonPearl": 1,
                        "BugCatchingNet": 1,
                        "BlueMail": 0,
                        "RedMail": 0,
                        "Bomb": 0,
                        "ThreeBombs": 16,
                        "Mushroom": 1,
                        "RedBoomerang": 1,
                        "BottleWithRedPotion": 0,
                        "BottleWithGreenPotion": 0,
                        "BottleWithBluePotion": 0,
                        "TenBombs": 1,
                        "OneRupee": 2,
                        "FiveRupees": 4,
                        "TwentyRupees": 28,
                        "BowAndArrows": 0,
                        "BowAndSilverArrows": 0,
                        "BottleWithBee": 0,
                        "BottleWithFairy": 0,
                        "BossHeartContainer": 10,
                        "HeartContainer": 1,
                        "OneHundredRupees": 1,
                        "FiftyRupees": 7,
                        "Heart": 0,
                        "Arrow": 1,
                        "TenArrows": 12,
                        "SmallMagic": 0,
                        "ThreeHundredRupees": 5,
                        "BottleWithGoldBee": 0,
                        "OcarinaActive": 0,
                        "PegasusBoots": 1,
                        "BombUpgrade5": 0,
                        "BombUpgrade10": 0,
                        "ArrowUpgrade5": 0,
                        "ArrowUpgrade10": 0,
                        "HalfMagic": 1,
                        "QuarterMagic": 0,
                        "SilverArrowUpgrade": 0,
                        "Rupoor": 0,
                        "RedClock": 0,
                        "BlueClock": 0,
                        "GreenClock": 0,
                        "ProgressiveSword": 4,
                        "ProgressiveShield": 3,
                        "ProgressiveArmor": 1,
                        "ProgressiveGlove": 2,
                        "ProgressiveBow": 2,
                        "Triforce": 0,
                        "TriforcePiece": 0,
                        "MapA2": 1,
                        "MapD7": 1,
                        "MapD4": 1,
                        "MapP3": 1,
                        "MapD5": 1,
                        "MapD3": 1,
                        "MapD6": 1,
                        "MapD1": 1,
                        "MapD2": 1,
                        "MapA1": 0,
                        "MapP2": 1,
                        "MapP1": 1,
                        "MapH1": 0,
                        "MapH2": 1,
                        "CompassA2": 1,
                        "CompassD7": 1,
                        "CompassD4": 1,
                        "CompassP3": 1,
                        "CompassD5": 1,
                        "CompassD3": 1,
                        "CompassD6": 1,
                        "CompassD1": 1,
                        "CompassD2": 1,
                        "CompassA1": 0,
                        "CompassP2": 1,
                        "CompassP1": 1,
                        "CompassH1": 0,
                        "CompassH2": 0,
                        "BigKeyA2": 1,
                        "BigKeyD7": 1,
                        "BigKeyD4": 1,
                        "BigKeyP3": 1,
                        "BigKeyD5": 1,
                        "BigKeyD3": 1,
                        "BigKeyD6": 1,
                        "BigKeyD1": 1,
                        "BigKeyD2": 1,
                        "BigKeyA1": 0,
                        "BigKeyP2": 1,
                        "BigKeyP1": 1,
                        "BigKeyH1": 0,
                        "BigKeyH2": 0,
                        "KeyH2": 1,
                        "KeyH1": 0,
                        "KeyP1": 0,
                        "KeyP2": 1,
                        "KeyA1": 2,
                        "KeyD2": 1,
                        "KeyD1": 6,
                        "KeyD6": 3,
                        "KeyD3": 4,
                        "KeyD5": 2,
                        "KeyP3": 1,
                        "KeyD4": 1,
                        "KeyD7": 4,
                        "KeyA2": 4}},
                "drop": {
                    "count": {
                        "Bee": 0,
                        "BeeGood": 0,
                        "Heart": 13,
                        "RupeeGreen": 9,
                        "RupeeBlue": 7,
                        "RupeeRed": 6,
                        "BombRefill1": 7,
                        "BombRefill4": 1,
                        "BombRefill8": 2,
                        "MagicRefillSmall": 6,
                        "MagicRefillFull": 3,
                        "ArrowRefill5": 5,
                        "ArrowRefill10": 3,
                        "Fairy": 1}}}}

        # vt.custom.prizepacks
        try:
            if not customizer_save['vt.custom.prizepacks'] is None:
                settings['drops'] = customizer_save['vt.custom.prizepacks']
        except KeyError:
            pass

        # vt.custom.drops
        try:
            if not customizer_save['vt.custom.drops'] is None:
                settings['data']['alttp']['custom']['drop']['count'] = customizer_save['vt.custom.drops']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.settings'] is None:
                for key, value in customizer_save['vt.custom.settings'].items(
                ):
                    settings['data']['alttp']['custom'][key] = value
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.items'] is None:
                settings['data']['alttp']['custom']['item']['count'] = customizer_save['vt.custom.items']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.locations'] is None:
                settings['l'] = customizer_save['vt.custom.locations']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.rom-logic'] is None:
                settings['data']['alttp']['custom']['rom']['logicMode'] = customizer_save['vt.custom.rom-logic']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.HardMode'] is None:
                settings['data']['alttp']['custom']['rom']['HardMode'] = customizer_save['vt.custom.HardMode']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.logic'] is None:
                settings['logic'] = customizer_save['vt.custom.logic']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.weapons'] is None:
                settings['weapons'] = customizer_save['vt.custom.weapons']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.goal'] is None:
                settings['goal'] = customizer_save['vt.custom.goal']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.state'] is None:
                settings['mode'] = customizer_save['vt.custom.state']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.notes'] is None:
                settings['notes'] = customizer_save['vt.custom.notes']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.name'] is None:
                settings['name'] = customizer_save['vt.custom.name']
        except KeyError:
            pass

        try:
            if not customizer_save['vt.custom.equipment'] is None:
                eq = []
                for key, value in customizer_save['vt.custom.equipment'].items(
                ):
                    if key in ['Bottle1', 'Bottle2', 'Bottle3', 'Bottle4']:
                        if value == 1:
                            eq += ['Bottle']
                        elif value == 2:
                            eq += ['BottleWithRedPotion']
                        elif value == 3:
                            eq += ['BottleWithGreenPotion']
                        elif value == 4:
                            eq += ['BottleWithBluePotion']
                        elif value == 5:
                            eq += ['BottleWithBee']
                        elif value == 6:
                            eq += ['BottleWithGoldBee']
                        elif value == 7:
                            eq += ['BottleWithFairy']
                    elif key == 'ProgressiveBow':
                        if value == 1:
                            eq += ['SilverArrowUpgrade']
                        elif value == 2:
                            eq += ['Bow']
                        elif value == 3:
                            eq += ['BowAndSilverArrows']
                    elif key == 'Boomerang':
                        if value == 1:
                            eq += ['Boomerang']
                        elif value == 2:
                            eq += ['RedBoomerang']
                        elif value == 3:
                            eq += ['Boomerang', 'RedBoomerang']
                    elif key == 'Ocarina':
                        if value == 1:
                            eq += ['OcarinaInactive']
                        elif value == 2:
                            eq += ['OcarinaActive']
                    elif key == "Rupees":
                        value = int(
                            customizer_save['vt.custom.equipment']['Rupees'])

                        eq += math.floor(value / 300) * ['ThreeHundredRupees']
                        value %= 300

                        eq += math.floor(value / 100) * ['OneHundredRupees']
                        value %= 100

                        eq += math.floor(value / 50) * ['FiftyRupees']
                        value %= 50

                        eq += math.floor(value / 20) * ['TwentyRupees']
                        value %= 20

                        eq += math.floor(value / 5) * ['FiveRupees']
                        value %= 5

                        eq += math.floor(value / 1) * ['OneRupee']
                    else:
                        eq += int(value) * [key]

                settings['eq'] = eq

        except KeyError:
            pass

        return settings
