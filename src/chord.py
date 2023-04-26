from src.scale import Scale


class Chord:
    def __init__(self):
        self.__scale = Scale()

    def get_chord(self, note, type, seventh=False):
        _scale = self.__scale.get_scale(note, type)
        chord = [_scale[0], _scale[2], _scale[4]]
        if seventh:
            chord.append(_scale[6])
        return chord
