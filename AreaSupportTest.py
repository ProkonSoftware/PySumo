from PySumo import *

Objects = []
Curves = []

Support = SoPlaneAreaSupport.Create()
Curves.append(SoLine.Create(IwVector3d(0,0,0),IwVector3d(10,0,0)))
Curves.append(SoLine.Create(IwVector3d(10,0,0),IwVector3d(10,0,10)))
Curves.append(SoLine.Create(IwVector3d(10,0,10),IwVector3d(0,0,10)))
Curves.append(SoLine.Create(IwVector3d(0,0,10),IwVector3d(0,0,0)))
Support.SetCurves(Curves)
Support.SetModulus(20233)
Support.SetAllowTension(False)
Objects.append(Support)

Model.AddUndoably( Objects, None )
