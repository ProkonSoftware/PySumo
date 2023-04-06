from PySumo import *
import math

Added = []
Deleted = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Steel = MaterialDB.Search( "S355JR", SoMaterial.eType.Steel )
Added.append(Steel)
	
SectionDB = SoSectionDB()
SectionDB.Read()
Section = SectionDB.Manufacture(
	"203x133x25", 
	SectionDB.eSectionType.SteelIParallel, 
	SectionDB.eSectionSubType.Standard 
);
if( Section!=None ):
	Section.SetMaterial(Steel)
	Added.append(Section)
	
List = Model.GetObjectsByType(SoTypes.RigidLink)
for Link in List:
	Curve = Link.GetDefiningCurve().MakeACopy()
	Beam = SoBeam.Create()
	Beam.SetCurve(Curve)
	Beam.SetSection_1(Section)
	Added.append(Beam)
	Deleted.append(Link)
	
Model.DeleteUndoably( Deleted )
Model.AddUndoably( Added, None )