from src.notes import Notes


class Scale:
    def __init__(self):
        self.__nt = Notes()
        self._major_shifts = [2, 2, 1, 2, 2, 2, 1]
        self._minor_shifts = [2, 1, 2, 2, 1, 2, 2]

    def get_scale(self, note, type):
        scale = [note]
        num_notes = len(self.__nt._notes)
        pos = self.__nt.pos(note)
        __shifts = []
        if type == "major":
            __shifts = self._major_shifts
        else:
            __shifts = self._minor_shifts

        for _shft in __shifts:
            pos = (pos + _shft) % num_notes
            scale.append(self.__nt._notes[pos])

        return scale
