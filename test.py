
import options,strutils,strformat,times

type xy = tuple
  x,y: int

type path = tuple
  xy0,xy1: xy

type wire = seq[path]

type move = proc (start: xy, d: int): xy {.nimcall.}

proc right(start: xy, d: int) : xy = (start.x + d, start.y)
proc left(start: xy, d: int) : xy = (start.x - d, start.y)
proc up(start: xy, d: int) : xy = (start.x, start.y + d)
proc down(start: xy, d: int) : xy = (start.x, start.y - d)

proc parseCmd(cmd: string) : (move,int) =
  case cmd[0]
  of 'R': return (right, parseInt(cmd[1..^1]))
  of 'L': return (left, parseInt(cmd[1..^1]))
  of 'U': return (up, parseInt(cmd[1..^1]))
  of 'D': return (down, parseInt(cmd[1..^1]))
  else: raise newException(ValueError,&"Invalid Cmd: {cmd}")

proc routeWire(cmds: seq[string]) : wire =
  var
    c0,c1 : xy = (0,0)
    p : path
    f : move
    v : int
  for cmd in cmds:
    (f,v) = parseCmd(cmd)
    c1 = f(c0,v)
    p = (c0,c1)
    result.add(p)
    c0 = c1

proc horizontal(p: path) : bool = p.xy0.y == p.xy1.y
proc vertical(p: path) : bool = p.xy0.x == p.xy1.x
proc min_x(p: path) : int = min(p.xy0.x,p.xy1.x)
proc max_x(p: path) : int = max(p.xy0.x,p.xy1.x)
proc min_y(p: path) : int = min(p.xy0.y,p.xy1.y)
proc max_y(p: path) : int = max(p.xy0.y,p.xy1.y)

proc length(p: path) : int =
  case p.horizontal
  of true: p.max_x - p.min_x
  of false: p.max_y - p.min_y

proc distance(p0,p1: xy) : int =
  case horizontal((p0,p1))
  of true: abs(p1.x - p0.x)
  of false: abs(p1.y - p0.y)

proc manhattan(p: xy) : int = abs(p.x) + abs(p.y)

proc intersects(p0,p1: path) : Option[xy] =
  if horizontal(p0):
    if vertical(p1) and (p1.min_y < p0.xy0.y and p1.max_y > p0.xy0.y) and (p0.min_x < p1.xy0.x and p0.max_x > p1.xy1.x):
        return some((p1.xy0.x,p0.xy0.y))
  else:
    if horizontal(p1) and (p0.min_y < p1.xy0.y and p0.max_y > p1.xy0.y) and (p1.min_x < p0.xy0.x and p1.max_x > p0.xy1.x):
        return some((p0.xy0.x,p1.xy0.y))
  return none(xy)

proc part1(line0,line1: string) : int =
  let w0 = routeWire(line0.split(','))
  let w1 = routeWire(line1.split(','))
  for p0 in w0:
    for p1 in w1:
      let i = p0.intersects(p1)
      if i.isSome:
        if result == 0:
          result = i.get.manhattan
        else:
          result = min(result,i.get.manhattan)

proc part2(line0,line1: string) : int =
  let w0 = routeWire(line0.split(','))
  let w1 = routeWire(line1.split(','))
  var l0,l1 : int
  for p0 in w0:
    l1 = 0
    for p1 in w1:
      let i = p0.intersects(p1)
      if i.isSome:
        let 
          x = i.get
          d0 = l0 + distance(p0.xy0,x)
          d1 = l1 + distance(p1.xy0,x)
        if result == 0:
          result = d0 + d1
        else:
          result = min(result,d0 + d1)
      l1 += p1.length
    l0 += p0.length

assert part1("R8,U5,L5,D3","U7,R6,D4,L4") == 6
assert part1("R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83") == 159
assert part1("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135

assert part2("R8,U5,L5,D3","U7,R6,D4,L4") == 30
assert part2("R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83") == 610
assert part2("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410

let
  line0 = stdin.readLine()
  line1 = stdin.readLine()

let t1 = cpuTime()
echo &"Part 1 : {part1(line0,line1)} :: {cpuTime()-t1:0.6f} secs"

let t2 = cpuTime()
echo &"Part 2 : {part2(line0,line1)} :: {cpuTime()-t2:0.6f} secs"

