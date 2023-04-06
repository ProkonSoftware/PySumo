from PySumo import *

Objects = []
LC = SoLoadCase.Create("Test","Test description")
Objects.append(LC)

Load = SoLineLoad.Create();
Curve = SoLine.Create(IwVector3d(0,0,0), IwVector3d(5,0,0))
Load.SetCurve(Curve)
Load.SetLoad(1,2)
Load.SetLoadCase(LC)
Load.SetDirection(IwVector3d(0,0,1))
Objects.append(Load)

Load = SoLineLoad.Create();
Curve = SoLine.Create(IwVector3d(5,0,0), IwVector3d(10,0,0))
Load.SetCurve(Curve)
Load.SetLoad(2,3)
Load.SetLoadCase(LC)
Load.SetDirection(eLoadDirection.DIR_Z)
Objects.append(Load)

Model.AddUndoably( Objects, None )
