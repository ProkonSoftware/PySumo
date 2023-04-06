from PySumo import *
import math

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Steel = MaterialDB.Search( "S355JR", SoMaterial.eType.Steel )
if( Steel!=None ):
	Model.AddUndoably(Steel, None, None)
	
Section = SoSection.CreateRectangular( Steel, 0.05, 0.1 )
if( Section!=None ):
	Model.AddUndoably( Section, None, None )
	
SectionDB = SoSectionDB()
SectionDB.Read()
print("Active section db country: "+SectionDB.GetActiveCountry())
Section = SectionDB.Manufacture(
	"203x133x25", 
	SectionDB.eSectionType.SteelIParallel, 
	SectionDB.eSectionSubType.Standard 
);
if( Section!=None ):
	Section.SetMaterial(Steel)
	Model.AddUndoably( Section, None, None )