from PySumo import *
import math

def printPoint(p):
	print(f"({p.x}, {p.y}, {p.z})")
	
def printList(List):
	for p in List:
		printPoint(p)
		
MaterialDB = SoMaterialDB()
MaterialDB.Read()
Steel = MaterialDB.Search( "S355JR", SoMaterial.eType.Steel )
if( Steel!=None ):
	Model.AddUndoably(Steel, None, None)
	
