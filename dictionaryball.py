game_dictionary = { 'home': {
        'team_name': "Brooklyn Nets",
        'colors': ["Black", "White"],
        'players': {
            "Alan Anderson": {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1 },
            "Reggie Evans": {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7 },
            "Brook Lopez": {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15 },
            "Mason Plumlee": {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5 },
            "Jason Terry": {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1 }
        }
    },
    'away': {
        'team_name': "Charlotte Hornets",
        'colors': ["Turquoise", "Purple"],
        'players': {
            "Jeff Adrien": {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2 },
            "Bismak Biyombo": {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10 },
            "DeSagna Diop": {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5 },
            "Ben Gordon": {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0 },
            "Brendan Haywood": {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12 }
        }
    }}

def game_dict():
    return game_dictionary


def num_points_scored(name):
    for team, stats in game_dictionary.items():
        if name in stats['players']:
            return stats['players'][name]['points']


def shoe_size(name):
    for team, stats in game_dictionary.items():
        if name in stats['players']:
            return stats['players'][name]['shoe']

def team_points(team_name):
    for team, stats in game_dictionary.items():
        if team_name in stats['team_name']:
            return [stats['players'][name]['points'] for name in stats['players']]

def team_colors(team_name):
    for team, stats in game_dictionary.items():
        if team_name == stats['team_name']:
            return stats['colors']

def team_names():
    return [stats['team_name'] for team, stats in game_dictionary.items()]


def player_numbers(team_name):
    for team, stats in game_dictionary.items():
        if team_name in stats['team_name']:
         return [stats['players'][name]['number'] for name in stats['players']]


def player_stats(name):
    stat_dict = {}
    for team, stats in game_dictionary.items():
        if name in stats['players']:
            for key in stats['players'][name]:
                stat_dict[key] = stats['players'][name][key]

    return stat_dict

def big_shoe_rebounds():
    shoe_list = []
    for team, stats in game_dictionary.items():
        for player, details in stats['players'].items():
            shoe_list.append((player,details['shoe']))
    player_name = max(shoe_list,key = lambda x:x[1])[0]
    for team, stats in game_dictionary.items():
        if player_name in stats['players']:
            return stats['players'][player_name]['rebounds']

def most_points_scored():
    point_list = []
    for team, stats in game_dictionary.items():
        for player, details in stats['players'].items():
            point_list.append((player,details['points']))
    player_name = max(point_list,key = lambda x:x[1])[0]
    return player_name

def winning_team():
    total_points = []
    for name in team_names():
        total_points.append((name,sum(team_points(name))))
    team = max(total_points,key = lambda x:x[1])[0]
    return team

def player_with_longest_name():
    names = []
    for team, stats in game_dictionary.items():
        for key in stats['players']:
            names.append(key)
    return max(names, key = lambda x: len(x))

def player_with_most_steals():
    names = []
    for team, stats in game_dictionary.items():
        for name,stat in stats['players'].items():
            names.append((name,stat['steals']))
    return max(names, key = lambda x: x[1])[0]

def long_name_steals_a_ton():
    if player_with_longest_name() == player_with_most_steals():
        return True
    else:
        return False



def good_practices():
    for location, team_stats in game_dict().items():
    # are you ABSOLUTELY SURE what 'location' and 'team_stats' are? use pdb.set_trace() to find out!
        import pdb; pdb.set_trace()
        for stats, data in team_stats.items():
            # are you ABSOLUTELY SURE what 'stats' and 'data' are? use pdb.set_trace() to find out!
            import pdb; pdb.set_trace()
            # what is 'data' at each level of the for loop block? when will we be able to iterate through a list?
            # When would the following line of code break?
            for item in data:
                print(item)
