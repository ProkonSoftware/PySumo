from PySumo import *
import math

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )
Objects.append(Concrete)
	
Curve = SoLine.Create( IwVector3d(0,0,0), IwVector3d(5,0,4) )
Wall = SoWall.Create(3,0.23)
Wall.SetCurve(Curve)
Wall.SetMaterial(Concrete)

Objects.append(Wall)
Model.AddUndoably( Objects, None )