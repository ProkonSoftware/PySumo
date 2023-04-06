from PySumo import *

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.SetFileName("c:/prokon/user/defaults.mtl")
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )
Objects.append(Concrete)
	
Slab = SoSlab.Create()

Curves = []
Curves.append( SoLine.Create( IwVector3d(-5,0,5),IwVector3d(5,0,5) ) )
Curves.append( SoLine.Create( IwVector3d(5,0,5),IwVector3d(5,0,-5) ) )
Curves.append( SoLine.Create( IwVector3d(5,0,-5),IwVector3d(-5,0,-5) ) )
Curves.append( SoLine.Create( IwVector3d(-5,0,-5),IwVector3d(-5,0,5) ) )

p1 = IwVector3d(0, 0.0, 0.0)
p2 = IwVector3d(2, 0.0, 0.0)
Circle = SoCircle.Create()
Circle.SetCenterPoint(p1)
Circle.SetRadiusPoint(p2)
Curves.append(Circle)

Loops = []
Loop = sLoop()
Loop.orient = IW_OT_SAME
Loop.num = 4
Loop.closed = False
Loops.append(Loop)

Loop = sLoop()
Loop.num = 1
Loop.orient = IW_OT_SAME
Loop.closed = True
Loops.append(Loop)

Slab.SetCurves(Curves,Loops)
Slab.SetMaterial(Concrete)
Slab.SetThickness(0.5)
Slab.SetMeshSize(0.5)

Objects.append(Slab)

LC = SoLoadCase.Create("Test","Test description")
Objects.append(LC)

Load = SoSlabDistributedLoad.Create();
Load.SetLoad(-5)
Load.SetLoadCase(LC)
Load.SetDirection(SoSlabDistributedLoad.eLoadDir.DIR_Y)
Load.SetHost(Slab)
Objects.append(Load)

Model.AddUndoably( Objects, None )
