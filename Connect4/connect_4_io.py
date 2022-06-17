import json
from connect_4_exceptions import (
    WrongSaveGameFileError,
    WrongBestScoresFileError,
    EmptyBestScoresFileError
    )


def save_game(game, bot, tour, last_player=2):
    gameboard = game.board().gameboard()
    data = {
        'gameboard': gameboard,
        'bot': bot,
        'last_player': last_player,
        'tour': tour
    }
    with open('saved_game', 'w') as file_handle:
        json.dump(data, file_handle)


def load_game():
    try:
        with open('saved_game', 'r') as file_handle:
            data = json.load(file_handle)
            gameboard = data['gameboard']
            bot = data['bot']
            last_player = data['last_player']
            tour = data['tour']
        return (gameboard, bot, last_player, tour)
    except FileNotFoundError or PermissionError:
        raise WrongSaveGameFileError
    except json.JSONDecodeError:
        raise WrongSaveGameFileError


def save_score(name, bot, tour):
    score = {
        'name': name,
        'number of tours': tour,
        'played with bot': bot
    }
    try:
        with open('best_scores', 'r') as file_handle:
            data = json.load(file_handle)
        data.append(score)
        data.sort(key=lambda score: score['number of tours'])
        with open('best_scores', 'w') as file_handle:
            json.dump(data, file_handle, indent=3, ensure_ascii=False)
    except FileNotFoundError:
        save_score_one_score(score)
    except json.JSONDecodeError:
        save_score_one_score(score)


def save_score_one_score(score):
    data = []
    data.append(score)
    with open('best_scores', 'w') as file_handle:
        json.dump(data, file_handle, indent=3, ensure_ascii=False)


def load_scores():
    scores_list = []
    try:
        with open('best_scores', 'r') as file_handle:
            data = json.load(file_handle)
        for score in data:
            name = score['name']
            tour = score['number of tours']
            bot = score['played with bot']
            score_tuple = (name, tour, bot)
            scores_list.append(score_tuple)
        if len(scores_list) > 10:
            scores_list = scores_list[:10]
        return scores_list
    except FileNotFoundError or PermissionError:
        raise WrongBestScoresFileError
    except json.JSONDecodeError:
        raise EmptyBestScoresFileError


def save_score_player(name, tour):
    save_score(name, False, tour)


def save_score_bot(name, tour):
    save_score(name, True, tour)
