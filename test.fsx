-- ============================================================
-- AION FACTORY – AUTO BUILD FSX SCRIPT FOR FLEXSIM
-- ============================================================

function makeFolder(name)
    local f = model:find(name)
    if f then return f end
    return model:addfolder(name)
end

function makeProcessor(parent, name, x, y, z)
    local obj = parent:addobject("Processor", name)
    obj:setlocation(x, y, z)
    return obj
end

function makeRobot(parent, name, x, y, z)
    local obj = parent:addobject("Robot", name)
    obj:setlocation(x, y, z)
    return obj
end

function makeConveyor(parent, name, x, y, z, length)
    local obj = parent:addobject("Conveyor", name)
    obj:setlocation(x, y, z)
    obj.length = length or 5
    return obj
end

function makeSafety(parent, name, x, y, z, radius)
    local c = parent:addobject("Cylinder", name)
    c:setlocation(x, y, z)
    c.scale.x = radius*2
    c.scale.y = radius*2
    c.scale.z = 2
    c:setcolor(1,0,0,0.25)  -- red transparent
    return c
end

function makeNode(parent, x, y, z)
    local node = parent:addobject("NetworkNode", "")
    node:setlocation(x, y, z)
    return node
end

-- Root container
local factory = makeFolder("Guangzhou_Aion_Factory")


-- ============================================================
-- ZONE: STAMPING
-- ============================================================
local stamping = factory:addfolder("Stamping")

makeProcessor(stamping, "Press_1", 10, 20, 0)
makeProcessor(stamping, "Press_2", 30, 10, 0)

makeSafety(stamping, "Stamping_Operator_Safety", 15, 15, 0, 2)

local sp1 = makeNode(stamping, 5, 5, 0)
local sp2 = makeNode(stamping, 35, 15, 0)
sp1:connect(sp2)


-- ============================================================
-- ZONE: WELDING
-- ============================================================
local welding = factory:addfolder("Welding")

makeRobot(welding, "KUKA_KR16", 25, 25, 0)
makeRobot(welding, "ABB_IRB460", 35, 15, 0)

makeSafety(welding, "Welding_Robot_Safety", 25, 25, 0, 3)

local w1 = makeNode(welding, 20, 20, 0)
local w2 = makeNode(welding, 40, 10, 0)
w1:connect(w2)


-- ============================================================
-- ZONE: PAINTING
-- ============================================================
local painting = factory:addfolder("Painting")

makeProcessor(painting, "Paint_Booth_1", 50, 10, 0)
makeProcessor(painting, "Paint_Booth_2", 60, 20, 0)

makeSafety(painting, "Painting_Operator_Safety", 55, 15, 0, 2)
makeSafety(painting, "Painting_Spray_Safety", 55, 15, 0, 5)

local p1 = makeNode(painting, 45, 5, 0)
local p2 = makeNode(painting, 70, 25, 0)
p1:connect(p2)


-- ============================================================
-- ZONE: ASSEMBLY
-- ============================================================
local assembly = factory:addfolder("Assembly")

makeConveyor(assembly, "Conveyor_A", 80, 10, 0, 8)
makeConveyor(assembly, "Conveyor_B", 90, 20, 0, 8)

makeSafety(assembly, "Assembly_Operator_Safety", 85, 15, 0, 2)

local a1 = makeNode(assembly, 75, 5, 0)
local a2 = makeNode(assembly, 95, 25, 0)
a1:connect(a2)


-- ============================================================
-- ZONE: TESTING
-- ============================================================
local testing = factory:addfolder("Testing")

makeProcessor(testing, "Test_Stand_1", 110, 10, 0)
makeProcessor(testing, "Test_Stand_2", 120, 20, 0)

makeSafety(testing, "Testing_Operator_Safety", 115, 15, 0, 2)

local t1 = makeNode(testing, 105, 5, 0)
local t2 = makeNode(testing, 130, 25, 0)
t1:connect(t2)


-- ============================================================
-- END
-- ============================================================

msg("AION FACTORY MODEL GENERATED SUCCESSFULLY!")
