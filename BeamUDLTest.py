from PySumo import *

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

LC = SoLoadCase.Create("Test","Test description")
Objects.append(LC)

Load = SoBeamDistributedLoad.Create();
Load.SetStartLoad(-5)
Load.SetEndLoad(-2)
Load.SetLoadCase(LC)
Load.SetDirection(eLoadDirection.DIR_L)
Load.SetHost(Beam)
Load.SetOffset(1)
Load.SetLength(3)
Objects.append(Load)

Model.AddUndoably( Objects, None )
