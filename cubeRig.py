from maya import cmds

cube = cmds.polyCube()
cubeShape = cube[0]

print cubeShape, cube

circle = cmds.circle()
circleShape = circle[0]

print circleShape, circle

cmds.parent(cubeShape, circleShape)

cmds.setAttr(cubeShape+".translate", lock=True)
cmds.setAttr(cubeShape+".rotate", lock=True)
cmds.setAttr(cubeShape+".scale", lock=True)

cmds.select(circleShape)