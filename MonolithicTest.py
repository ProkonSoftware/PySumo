from PySumo import *
import math

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )
Objects.append(Concrete)
	
Line = SoLine.Create(IwVector3d(0,0,0),IwVector3d(10,0,10))

Beam = SoMonolithicBeam.Create()
Beam.SetWidth(0.3)
Beam.SetDepth(0.6)
Beam.SetOffset(0.35)
Beam.SetCurve(Line)

Objects.append(Beam)
Model.AddUndoably( Objects, None )