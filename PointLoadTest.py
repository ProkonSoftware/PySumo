from PySumo import *

Objects = []
LC = SoLoadCase.Create("Any","Test description")
Objects.append(LC)

Load = SoPointLoad.Create(IwVector3d(0,5,5))
Load.SetLoad(1,2,3)
Load.SetMoment(4,5,6)
Load.SetLoadCase(LC)
Objects.append(Load)

Model.AddUndoably( Objects, None )
