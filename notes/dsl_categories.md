# ARC DSL Function Categorization

Functions are grouped by input signature and then by output type in a single table.

| Input Signature | Output Type | Functions |
|---|---|---|
| `(a: Any, b: Any)` | `Boolean` | `equality` |
| `(a: Boolean, b: Boolean)` | `Boolean` | `both`, `either` |
| `(a: Container, b: Container)` | `Container` | `combine` |
| `` | `FrozenSet` | `product` |
| `(a: FrozenSet, b: FrozenSet)` | `FrozenSet` | `difference`, `intersection` |
| `(a: Grid, b: Grid)` | `Grid` | `hconcat`, `vconcat` |
| `(a: Grid, b: Grid, fallback: Integer)` | `Grid` | `cellwise` |
| `(a: Integer, b: Integer)` | `Boolean` | `greater` |
| `` | `IntegerTuple` | `astuple` |
| `(a: IntegerTuple, b: IntegerTuple)` | `Indices` | `connect` |
| `(a: Numerical, b: Numerical)` | `Numerical` | `add`, `divide`, `multiply`, `subtract` |
| `(a: Patch, b: Patch)` | `Boolean` | `adjacent`, `hmatching`, `vmatching` |
| `` | `Integer` | `manhattan` |
| `` | `IntegerTuple` | `position` |
| `(a: Tuple, b: Tuple)` | `TupleTuple` | `pair` |
| `(b: Boolean)` | `Boolean` | `flip` |
| `(condition: Boolean, a: Any, b: Any)` | `Any` | `branch` |
| `(container: Container)` | `Any` | `first`, `last`, `leastcommon`, `mostcommon` |
| `` | `Integer` | `size` |
| `(container: Container, compfunc: Callable)` | `Any` | `argmax`, `argmin` |
| `` | `Integer` | `valmax`, `valmin` |
| `` | `Tuple` | `order` |
| `(container: Container, condition: Callable)` | `Any` | `extract` |
| `` | `Container` | `sfilter` |
| `(container: Container, function: Callable)` | `FrozenSet` | `mfilter` |
| `(container: Container, n: Integer)` | `FrozenSet` | `sizefilter` |
| `(container: Container, value: Any)` | `Any` | `other` |
| `(container: FrozenSet)` | `Tuple` | `totuple` |
| `(container: IntegerSet)` | `Integer` | `maximum`, `minimum` |
| `(containers: ContainerContainer)` | `Container` | `merge` |
| `(element: Element)` | `Integer` | `leastcolor`, `mostcolor` |
| `` | `IntegerSet` | `numcolors`, `palette` |
| `(element: Element, factor: Integer)` | `Element` | `upscale` |
| `(element: Element, value: Integer)` | `Integer` | `colorcount` |
| `(function: Callable, a: Tuple, b: Tuple)` | `Tuple` | `mpapply`, `papply` |
| `(function: Callable, container: Container)` | `Container` | `apply` |
| `(function: Callable, container: ContainerContainer)` | `FrozenSet` | `mapply` |
| `(function: Callable, fixed: Any)` | `Callable` | `lbind`, `rbind` |
| `(function: Callable, n: Integer)` | `Callable` | `power` |
| `(function: Callable, target: Any)` | `Callable` | `matcher` |
| `(function: Unknown, a: Container, b: Container)` | `FrozenSet` | `prapply` |
| `(functions: Container, value: Any)` | `Container` | `rapply` |
| `(grid: Grid)` | `Grid` | `bottomhalf`, `compress`, `lefthalf`, `righthalf`, `rot180`, `rot270`, `rot90`, `tophalf`, `trim` |
| `` | `Indices` | `asindices` |
| `` | `Object` | `asobject` |
| `` | `Objects` | `fgpartition`, `frontiers`, `partition` |
| `(grid: Grid, a: Integer, b: Integer)` | `Grid` | `switch` |
| `(grid: Grid, factor: Integer)` | `Grid` | `downscale`, `hupscale`, `vupscale` |
| `(grid: Grid, loc: IntegerTuple)` | `Integer` | `index` |
| `(grid: Grid, n: Integer)` | `Tuple` | `hsplit`, `vsplit` |
| `(grid: Grid, obj: Object)` | `Grid` | `paint`, `underpaint` |
| `` | `Indices` | `occurrences` |
| `(grid: Grid, obj: Object, offset: IntegerTuple)` | `Grid` | `move` |
| `(grid: Grid, patch: Patch)` | `Grid` | `cover` |
| `(grid: Grid, replacee: Integer, replacer: Integer)` | `Grid` | `replace` |
| `(grid: Grid, start: IntegerTuple, dims: IntegerTuple)` | `Grid` | `crop` |
| `(grid: Grid, univalued: Boolean, diagonal: Boolean, without_bg: Boolean)` | `Objects` | `objects` |
| `(grid: Grid, value: Integer)` | `Indices` | `ofcolor` |
| `(grid: Grid, value: Integer, patch: Patch)` | `Grid` | `fill`, `underfill` |
| `(h: Callable, g: Callable, f: Callable)` | `Callable` | `chain` |
| `(i: Integer)` | `IntegerTuple` | `toivec` |
| `(item: Any, num: Integer)` | `Tuple` | `repeat` |
| `(j: Integer)` | `IntegerTuple` | `tojvec` |
| `(loc: IntegerTuple)` | `Indices` | `dneighbors`, `ineighbors`, `neighbors` |
| `(location: IntegerTuple)` | `Indices` | `hfrontier`, `vfrontier` |
| `(n: Integer)` | `Boolean` | `even` |
| `(n: Numerical)` | `Numerical` | `double`, `halve`, `invert` |
| `(obj: Object)` | `Integer` | `color`, `hperiod`, `vperiod` |
| `(objs: Objects, value: Integer)` | `Objects` | `colorfilter` |
| `(outer: Callable, a: Callable, b: Callable)` | `Callable` | `fork` |
| `(outer: Callable, inner: Callable)` | `Callable` | `compose` |
| `(patch: Patch)` | `Boolean` | `hline`, `vline` |
| `` | `Indices` | `backdrop`, `box`, `corners`, `delta`, `inbox`, `outbox`, `toindices` |
| `` | `Integer` | `leftmost`, `lowermost`, `rightmost`, `uppermost` |
| `` | `IntegerTuple` | `center`, `centerofmass`, `llcorner`, `lrcorner`, `ulcorner`, `urcorner` |
| `` | `Patch` | `normalize` |
| `(patch: Patch, directions: IntegerTuple)` | `Patch` | `shift` |
| `(patch: Patch, grid: Grid)` | `Boolean` | `bordering` |
| `` | `Grid` | `subgrid` |
| `` | `Object` | `toobject` |
| `(piece: Piece)` | `Boolean` | `portrait`, `square` |
| `` | `Integer` | `height`, `width` |
| `` | `IntegerTuple` | `shape` |
| `` | `Piece` | `cmirror`, `dmirror`, `hmirror`, `vmirror` |
| `(source: Patch, destination: Patch)` | `IntegerTuple` | `gravitate` |
| `(start: Integer, stop: Integer, step: Integer)` | `Tuple` | `interval` |
| `(start: IntegerTuple, direction: IntegerTuple)` | `Indices` | `shoot` |
| `(tup: Tuple)` | `Tuple` | `dedupe` |
| `(value: Any)` | `FrozenSet` | `initset` |
| `(value: Any, container: Container)` | `Boolean` | `contained` |
| `` | `Container` | `remove` |
| `(value: Any, container: FrozenSet)` | `FrozenSet` | `insert` |
| `(value: Integer, dimensions: IntegerTuple)` | `Grid` | `canvas` |
| `(value: Integer, patch: Patch)` | `Object` | `recolor` |
| `(x: Any)` | `Any` | `identity` |
| `(x: Integer)` | `Boolean` | `positive` |
| `(x: Numerical)` | `Numerical` | `crement`, `decrement`, `increment`, `sign` |
