class Notes:
    def __init__(self):
        self._notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        self._positions = {}
        self.__cache_positions()

    def __cache_positions(self):
        for _idx, _note in enumerate(self._notes):
            self._positions[_note] = _idx

    def pos(self, note):
        return self._positions[note]
