from PySumo import *
import math
  
Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.SetFileName("c:/prokon/user/defaults.mtl")
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )
Objects.append(Concrete)

r1 = 1.0
r2 = 3.0

x1 = r1
y1 = 0.0
z1 = 0.0
x2 = r2
y2 = 0.0
z2 = 0.0

for thetad in range(10,365,10):
	Curves = []
	Loops = []
	
	theta = thetad/180.0*math.pi
	
	x3 = r1*math.cos(theta)
	y3 = theta/math.pi 
	z3 = -r1*math.sin(theta)
	x4 = r2*math.cos(theta)
	y4 = y3
	z4 = -r2*math.sin(theta)
	
	Curves.append( SoLine.Create( IwVector3d(x1,y1,z1),IwVector3d(x2,y2,z2) ) )
	Curves.append( SoLine.Create( IwVector3d(x2,y2,z2),IwVector3d(x4,y4,z4) ) )
	Curves.append( SoLine.Create( IwVector3d(x4,y4,z4),IwVector3d(x1,y1,z1) ) )
		
	Loop = sLoop()
	Loop.orient = IW_OT_SAME
	Loop.num = 3
	Loop.closed = False
	Loops.append(Loop)

	Shell = SoPlaneShell.Create()
	Shell.SetCurves(Curves,Loops)
	Shell.SetMaterial(Concrete)
	Shell.SetThickness(0.1)
	Shell.SetMeshSize(0.1)
	Objects.append(Shell)
	
	Curves = []
	Loops = []
	
	Curves.append( SoLine.Create( IwVector3d(x1,y1,z1),IwVector3d(x4,y4,z4) ) )
	Curves.append( SoLine.Create( IwVector3d(x4,y4,z4),IwVector3d(x3,y3,z3) ) )
	Curves.append( SoLine.Create( IwVector3d(x3,y3,z3),IwVector3d(x1,y1,z1) ) )
		
	Loop = sLoop()
	Loop.orient = IW_OT_SAME
	Loop.num = 3
	Loop.closed = False
	Loops.append(Loop)
	
	Shell = SoPlaneShell.Create()
	Shell.SetCurves(Curves,Loops)
	Shell.SetMaterial(Concrete)
	Shell.SetThickness(0.1)
	Shell.SetMeshSize(0.1)
	Objects.append(Shell)
	
	x1 = x3
	y1 = y3
	z1 = z3
	x2 = x4
	y2 = y4
	z2 = z4
	
Model.AddUndoably( Objects, None )

