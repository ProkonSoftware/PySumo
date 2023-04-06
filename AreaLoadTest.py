from PySumo import *

Objects = []
LC = SoLoadCase.Create("Test","Test description")
Objects.append(LC)

Curves = []
Load = SoPlaneAreaLoad.Create();
Curves.append(SoLine.Create(IwVector3d(0,5,0), IwVector3d(5,0,0)))
Curves.append(SoLine.Create(IwVector3d(5,0,0), IwVector3d(0,0,5)))
Curves.append(SoLine.Create(IwVector3d(0,0,5), IwVector3d(0,5,0)))
Load.SetCurves(Curves)
Load.SetLoad(-5)
Load.SetLoadCase(LC)
Load.SetDirection(SoPlaneAreaLoad.eLoadDir.DIR_Y)
Objects.append(Load)

Model.AddUndoably( Objects, None )
