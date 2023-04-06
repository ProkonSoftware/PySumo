from PySumo import *
import math

Objects = []

MaterialDB = SoMaterialDB()
MaterialDB.Read()
Concrete = MaterialDB.Search( "30 MPa", SoMaterial.eType.Concrete )
Objects.append(Concrete)
	
Section = SoSection.CreateRectangular( Concrete, 0.3, 0.6 )
Section.SetMaterial(Concrete)
Objects.append(Section)
	
Column = SoColumn.Create(5.0)
Column.SetSection(Section)
Column.SetOrigin(IwVector3d(5,0,3))

Objects.append(Column)
Model.AddUndoably( Objects, None )