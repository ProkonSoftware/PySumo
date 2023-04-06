from PySumo import * #Sumo module to bind to Sumo methods/types/Objects
import math

p1 = IwVector3d(0.0, 0.0, 0.0)
p2 = IwVector3d(1.5, 0.0, 0.0)
p3 = IwVector3d(0.0, 0.0, 1.5)

line = SoLine.Create(p1,p2);
Model.AddUndoably(line,None,None)

line2 = line.MakeACopy()
transform = IwAxis2Placement( IwVector3d(2.0,0.0,2.0), IwVector3d(0.707,0,0.707), IwVector3d(0,1,0) )
line2.Transform(transform)
line2.Regen()
Model.AddUndoably(line2,None,None)

print(line.GetClassType())
print(line.GetObjectTypeName())
print(line.GetObjectVersion().GetString())
print(line.GetGeometryType())
print(line2.GetLength())

Points = IwPoint3dVector()
if(line.GetExtremaPoints(pos=Points)):
	for p in Points:
		print(f"({p.x}, {p.y}, {p.z})")

line.Reverse()
Model.WasModified(line)
Points = IwPoint3dVector()
if(line.GetExtremaPoints(pos=Points)):
	for p in Points:
		print(f"({p.x}, {p.y}, {p.z})")
		
Points = IwPoint3dVector()
if(line.GetMidPoints(pos=Points)):
	for p in Points:
		print(f"({p.x}, {p.y}, {p.z})")
		
line3 = line2.MakeACopy()
Model.AddUndoably(line3,None,None)
line3.Extend(line,IwVector3d(1,0,0))
Model.WasModified(line3)

line2.Offset(IwVector3d(0,1,0),5)
line2.Drop(line,IwVector3d(1,0,0))
Model.WasModified(line2)
			
line = SoLine.Create(p1,p1);
Model.AddUndoably(line,None,None)
msg = StringVector()
sev = SeverityVector()
line.Verify(msg,sev)

for i in range(len(msg)):
	if(sev[i]==eSeverity.Error):
		print(msg[i])
	
p4 = IwVector3d(6.0, 2.0, -1.5)
line = SoLine.Create(p1,p4);
line.ProjectToPlane(p1,IwVector3d(0,1,0))
line.UpdateFrom(line2,True)
color = SoObjectColor()
color.ColorRef = eColours.Red
style = SoObjectLineStyle()
style.Style = eLineStyle.Solid
line.SetLineStyle(style)
line.SetColor(color)
line.SetLineWeight(2)
line.SetStartPoint(IwVector3d(-5,0,0))
line.SetEndPoint(IwVector3d(-5,0,5))
Model.AddUndoably(line,None,None)

print(line.Equals(line2))
print(line.Equals(line3))

line = SoLine.Create(p1,p4);
print(line.GetElevation())
line.SetElevation(0.0)
Model.AddUndoably(line,None,None)
print( f"On plane: {line.InPlane(p1,IwVector3d(0,1,0))}")
print( f"On plane: {line.InPlane(p1,IwVector3d(-0.707,0.707,0))}")

print(line.ToString())



