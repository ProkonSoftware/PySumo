from PySumo import *
import math

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Steel = MaterialDB.Search( "S355JR", SoMaterial.eType.Steel )
Objects.append(Steel)
	
SectionDB = SoSectionDB()
SectionDB.Read()
Section = SectionDB.Manufacture(
	"203x133x25", 
	SectionDB.eSectionType.SteelIParallel, 
	SectionDB.eSectionSubType.Standard 
);
if( Section!=None ):
	Section.SetMaterial(Steel)
	Objects.append(Section)
	
Curve = SoLine.Create( IwVector3d(0,0,0), IwVector3d(5,0,4) )
Beam = SoBeam.Create()
Beam.SetCurve(Curve)
Beam.SetSection_1(Section)

Objects.append(Beam)
Model.AddUndoably( Objects, None )