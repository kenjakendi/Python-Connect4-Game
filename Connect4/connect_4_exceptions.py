class WrongBoardDimensionsValueError(ValueError):
    def __str__(self):
        return "The height and width values must be in range <4,9>"


class FullColumnError(Exception):
    def __str__(self):
        return 'Chosen column is full, choose another one.'


class ColumnOutOfRangeError(ValueError):
    def __str__(self):
        return "Column number is out of range, choose another one."


class NoIntColumnError(ValueError):
    def __str__(self):
        return "Chosen column must be an integer, choose another one."


class WrongSaveGameFileError(Exception):
    def __str__(self):
        return 'There is no suitable "saved_game" file.'


class WrongBestScoresFileError(Exception):
    def __str__(self):
        return 'There is no suitable "best_scores" file.'


class EmptyBestScoresFileError(Exception):
    def __str__(self):
        return 'There is no best score yet'
