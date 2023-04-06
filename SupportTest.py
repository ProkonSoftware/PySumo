from PySumo import *

Objects = []

Support = SoPointSupport.Create(IwVector3d(3,4,5))
Support.SetFixity(SoSupport.DOF.X, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Y, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.Z, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.x, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.y, SoSupport.Type.Fixed)
Support.SetFixity(SoSupport.DOF.z, SoSupport.Type.Fixed)
Objects.append(Support)

Support = Support.MakeACopy()
Support.SetFixity(SoSupport.DOF.x, SoSupport.Type.Free)
Support.SetFixity(SoSupport.DOF.y, SoSupport.Type.Free)
Support.SetFixity(SoSupport.DOF.z, SoSupport.Type.Free)
Support.SetPoint(IwVector3d(0,0,0))
Objects.append(Support)

Model.AddUndoably( Objects, None )
