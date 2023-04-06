from PySumo import *

Objects = []
LC = SoLoadCase.Create("Any","Test description")
Objects.append(LC)

LC = SoLoadCase.Create("SW","Self-weight description")
LC.SetSelfWeightCase(True)
Objects.append(LC)

Model.AddUndoably( Objects, None )
