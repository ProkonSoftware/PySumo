from PySumo import *

Objects = []

Support = SoCurveSupport.Create()
Curve = SoLine.Create(IwVector3d(0,0,0),IwVector3d(10,0,0))
Support.SetCurve(Curve)
Support.SetFixity(SoSupport.DOF.X, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Y, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Z, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.x, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.y, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.z, SoSupport.Type.Fixed)
Objects.append(Support)

Support = SoCurveSupport.Create()
Curve = SoLine.Create(IwVector3d(5,0,5),IwVector3d(10,0,5))
Support.SetCurve(Curve)
Support.SetFixity(SoSupport.DOF.X, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Y, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Z, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.x, SoSupport.Type.Free)
Support.SetFixity(SoSupport.DOF.y, SoSupport.Type.Free)
Support.SetFixity(SoSupport.DOF.z, SoSupport.Type.Free)
Objects.append(Support)

Model.AddUndoably( Objects, None )
