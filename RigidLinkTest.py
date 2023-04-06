from PySumo import *
import math

Objects = []

Curve = SoLine.Create( IwVector3d(0,0,0), IwVector3d(5,0,4) )
Link = SoRigidLink.Create()
Link.SetCurve(Curve)

Objects.append(Link)
Model.AddUndoably( Objects, None )