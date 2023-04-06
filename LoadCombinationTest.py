from PySumo import *

Objects = []
LC1 = SoLoadCase.Create("Any","Test description")
Objects.append(LC1)

LC2 = SoLoadCase.Create("SW","Self-weight description")
LC2.SetSelfWeightCase(True)
Objects.append(LC2)

Combo = SoLoadCombination.Create()
Combo.SetName("Combination")
Combo.SetNotes("Test combination description")

Item = SoLoadCaseItem.Create()
Item.SetLoadCase(LC1)
Item.SetULSFactor(1.6)
Item.SetSLSFactor(1.1)
Combo.Add(Item,None,False)

Item = SoLoadCaseItem.Create()
Item.SetLoadCase(LC2)
Item.SetULSFactor(1.2)
Item.SetSLSFactor(0.9)
Combo.Add(Item,None,False)

Objects.append(Combo)

Model.AddUndoably( Objects, None )
