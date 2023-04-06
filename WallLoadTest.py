from PySumo import *

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

LC = SoLoadCase.Create("Test","Test description")
Objects.append(LC)

Load = SoWallDistributedLoad.Create();
Load.SetBottomLoad(-5)
Load.SetTopLoad(-3)
Load.SetLoadCase(LC)
Load.SetDirection(SoWallDistributedLoad.eLoadDir.DIR_L)
Load.SetHost(Wall)
Objects.append(Load)

Model.AddUndoably( Objects, None )
