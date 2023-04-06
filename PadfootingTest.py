from PySumo import *

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )

Objects.append(Concrete)

Pad = SoPadFooting.Create(IwVector3d(3,4,5))
Pad.SetFixity(SoSupport.DOF.X, SoSupport.Type.Fixed)
Pad.SetFixity(SoSupport.DOF.Y, SoSupport.Type.Fixed)
Pad.SetFixity(SoSupport.DOF.Z, SoSupport.Type.Fixed)
Pad.SetFixity(SoSupport.DOF.x, SoSupport.Type.Fixed)
Pad.SetFixity(SoSupport.DOF.y, SoSupport.Type.Fixed)
Pad.SetFixity(SoSupport.DOF.z, SoSupport.Type.Fixed)
Pad.SetWidth(3.0)
Pad.SetHeight(3.0)
Pad.SetDepth(0.7)
Pad.SetStubWidth(0.7)
Pad.SetStubHeight(0.7)
Pad.SetStubDepth(1.0)
Pad.SetMaterial(Concrete)

Objects.append(Pad)
Model.AddUndoably( Objects, None )